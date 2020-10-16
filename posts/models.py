from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# from datetime import datetime
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    """
    Модель для объявлений
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, verbose_name = 'Юзер')
    title = models.CharField('Заголовок', max_length=300)
    text = models.TextField('Содержимое')
    CATEGORY_TYPES = (
        ('1', 'Автомобили (покупка)'),
        ('2', 'Автомобили (продажа)'),
        ('3', 'Автомобили (сервис)'),
        ('4', 'Бытовая техника (услуги)'),
    )
    category = models.CharField('Категория', max_length=1, choices=CATEGORY_TYPES)
    # datetime_created = models.DateTimeField('Дата-время создания')
    datetime_changed = models.DateTimeField('Дата-время изменения')

    # абсолютный урл объявления
    def get_absolute_url(self):
        return reverse('posts:post_detail', kwargs={'pk': self.pk})
        # return reverse('posts:posts')
    
    # изменить значение после изменения объекта datetime_created
    def save(self, *args, **kwargs):
        self.datetime_changed = timezone.now()
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.pk}. {self.title}'
       
    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

class Kerchnet_account(models.Model):
    """
    Модель аккаунтов керчьнет
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Юзер')
    kn_datetime_created = models.DateTimeField('Дата-время создания', default=timezone.now)
    kn_email = models.EmailField('E-mail')
    kn_login = models.CharField('Логин', max_length=50, null=True)
    kn_password = models.CharField('Пароль', max_length=50)
   
    # для форматирования даты и времени для вывода 
    @property
    def kn_datetime_created_formated(self):
        # verbose_name_plural ='s'
        return self.kn_datetime_created.strftime('%d.%m.%Y %H:%M:%S')
        
    
    def __str__(self):
        return f'{self.pk}. {self.kn_email}'
    
    class Meta:
        verbose_name = 'Аккаунт керчьнет'
        verbose_name_plural = 'Аккаунты керчьнета'