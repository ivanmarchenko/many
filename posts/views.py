from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import LoginForm, PostUpdateForm, PostCreateForm, KnAccountCreateForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseForbidden
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Post, Kerchnet_account
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class UserCheckMixin:
    """
    Миксин проверка на авторизацию и собственника объекта
    """
    def dispatch(self, request, *args, **kwargs):
        user_r = request.user
        if not user_r.is_authenticated or user_r != self.get_object().user:
            raise Http404('Ошибка 404.')
        return super().dispatch(request, *args, **kwargs)

def user_login(request):
    """
    Функция авторизации login
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Dissabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# заменил это представление на PostList с помощью django_tables2 
# @login_required
# def index(request):
#     """
#     Функция отображения для домашней страницы
#     """
#     # user = request.user
#     # Привязываемся к классу Post
#     post = Post
#     posts = Post.objects.filter(user=request.user)
#     return render(request, 'post_list.html', context={'user': request.user, 'post': post, 'posts': posts})


# @login_required
# def kn_account(request):
#     """
#     Функция отображения аккаунтов пользователя
#     """
#     # Привязываемся к Kerchnet_account для получения имён полей модели
#     account = Kerchnet_account
#     # Получаем список аккаунтво KerchNet пользователя
#     kerchnet_accounts = Kerchnet_account.objects.filter(user=request.user)
#     return render(request, 'kn_account/kn_account_list.html', context={'account': account, 'kerchnet_accounts': kerchnet_accounts})

class KnAccountAdd(LoginRequiredMixin, CreateView):
    """
    Класс отображения детальной информации аккаунта KerchNET
    """
    model = Kerchnet_account
    form_class = KnAccountCreateForm
    template_name = 'kn_account/kn_account_add.html'
    success_url = reverse_lazy('posts:kn_account_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(KnAccountAdd, self).form_valid(form)

class KnAccountDelete(UserCheckMixin, DeleteView):
    """
    View удаления аккаунта KerchNET
    """
    model = Kerchnet_account
    template_name = 'kn_account/kn_account_delete.html'
    success_url = reverse_lazy('posts:kn_account_list')

class PostCreate(LoginRequiredMixin, CreateView):
    """
    View добавления объявления
    """
    model = Post
    form_class = PostCreateForm
    template_name = 'post_detail.html'
    success_url = reverse_lazy('posts:posts')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostUpdate(UserCheckMixin, UpdateView):
    """
    View обновления объявления
    """
    model = Post
    form_class = PostUpdateForm
    template_name = 'post_detail.html'
    success_url = reverse_lazy('posts:posts')

class PostDelete(UserCheckMixin, DeleteView):
    """
    View удаление объявления
    """
    model = Post
    template_name = 'form_post_delete.html'
    # Вместо reverse здесь используется reverse_lazy, 
    # таким образом пользователь не будет перенаправлен до тех пор, 
    # пока представление не завершит удаление записи из базы данных.
    success_url = reverse_lazy('posts:posts')


class test(DeleteView):
    pass

def TestDelete(request):
    """
    Групповое удаление
    """
    # model = Post
    # template_name = 'test.html'
    # success_url = reverse_lazy('posts:posts')
    pks = request.POST.getlist('selected_action')
    print(pks)
    return render(request, 'test.html', context={'pks': pks})




# ------------------------------------------------
from django_tables2 import SingleTableView
from .tables import PostTable, KnAccountTable
# теперь это представления основное для отображения главной и использованиеим django_tables2
class PostList(LoginRequiredMixin, SingleTableView):
    # model = Post
    table_class = PostTable
    template_name = 'post_list.html'
    paginate_by = 5

    # переопределили метод get_queryset фильтром по владельцу Post    
    def get_queryset(self):
        user_r = self.request.user
        queryset = Post.objects.filter(user=user_r.id).order_by('-pk')
        return queryset

# представление для аккаунтов KerchNet на базе django_tables2
class KnAccountList(LoginRequiredMixin, SingleTableView):
    # model = Kerchnet_account
    table_class = KnAccountTable
    template_name = 'kn_account/kn_account_list.html'
    paginate_by = 10

    # переопределили метод get_queryset фильтром по владельцу Post    
    def get_queryset(self):
        user_r = self.request.user
        queryset = Kerchnet_account.objects.filter(user=user_r.id).order_by('-pk')
        return queryset


# # тест
# # Использую django_filters для селективной формы 
# from django_filters import FilterSet

# # тест
# class PostFilter(FilterSet):
#     """
#     Класс фильтра Post на базе FilterSet
#     """
#     class Meta:
#         model = Post
#         fields = ['title', 'text', 'category', 'datetime_changed']
# # тест
# def post_list(request):
#     """
#     Метод отображения Post списком с фильтром
#     """
#     filter = PostFilter(request.GET, queryset=Post.objects.all())
#     return render(request, 'post_list_df.html', context={'filter': filter})
# ------------------------------------------------

    
# Не удобно работать с классом, проще использовать пользовательские функции??
# class KNaccountListView(LoginRequiredMixin, ListView):
#     """
#     Список аккаунтов керчьнет с помощью ListView
#     """
#     model = Kerchnet_account
#     template_name = 'kn_account.html'


# Реализовал проверку если пост не существует, если пользователь неавторизован, если пост не принадлежит
# пользователю, то raise Http404.
# Иначе возвращаем context.
# Позже надо этот метод проверки переделать в mixin.
# def post_detail(request, pk):
#     """
#     Объявление по pk
#     """
#     user = request.user
#     try:
#         post = Post.objects.get(pk=pk)
#     except Post.DoesNotExist:
#         raise Http404("Ошибка 404.")
#     if not user.is_authenticated or user.id != post.user.id:
#         raise Http404("Ошибка 404.")
#     else:
#         return render(request, 'post_detail.html', {'post': post})


