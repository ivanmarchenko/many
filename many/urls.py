"""many URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, re_path
# from posts.views import user_login, kn_account, PostDetailView
from posts import views
from django.views.generic import RedirectView
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login

urlpatterns = [
    # На главной будем показываь форму авторизации
    # re_path(r'^$', admin.site.login),
    path('admin/', admin.site.urls),
    # вместо главной страницы
    path('posts/', include('posts.urls'), name='posts'),
    # редирект с главной на posts
    path('', RedirectView.as_view(url='/posts/', permanent=True)),
    # урл для авторизации с испльзованием собственной функции user_login
    # re_path(r'^login/$', user_login, name='login'),
    # урл для авторизации с испльзованием LoginView
    re_path(r'^login/$', LoginView.as_view(template_name='auth/login.html'), name='login'),
    # урл для выхода с помощью LogoutView
    re_path(r'^logout/$', LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
    # урл для выхода и входа
    re_path(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),    
    # урл для страницы аккаунтов с помощью ListView
    # path('kn_account/', views.KNaccountListView.as_view(), name='kerchnet_account_list_view'),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),

]

