from django.urls import path, re_path
from . import views

app_name = 'posts'
urlpatterns = [
    # re_path(r'^login/$', user_login, name='login'),
    path('', views.PostList.as_view(), name='posts'),
    # урл объявления
    # path('<slug:pk>/', views.PostDetailView.as_view(), name='post_detail')
    ###
    # path('<int:pk>/', views.post_detail, name='post_detail')
    path('<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
    # страница обновления объявления
    path('<int:pk>/', views.PostUpdate.as_view(), name='post_detail'),
    # страница добавления объявления
    path('add/', views.PostCreate.as_view(), name='post_add'), 
    # страница аккаунтов KerchNET
    re_path(r'^kn_account/$', views.KnAccountList.as_view(), name='kn_account_list'),
    # добавление аккаунта KerchNET
    path('kn_account/add/', views.KnAccountAdd.as_view(), name='kn_account_add'),
    # удаление аккаунта KerchNET
    path('kn_account/<int:pk>/delete/', views.KnAccountDelete.as_view(), name='kn_account_delete'),
    # страница списка Post с фильтрацией
    # path('posts_df/', views.PostTestList.as_view(), name='posts_test'),
    path('delete/', views.TestDelete, name='delete'),
]
