from django.contrib import admin

# Register your models here.
from .models import Post, Kerchnet_account

# admin.site.register(Kerchnet_account)  
admin.site.register(Post)

# @admin.register(Kerchnet2)
# class Kerchnet2(admin.ModelAdmin):
#     list_display = ('login',)

# @admin.register(Post)
# class Post(admin.ModelAdmin):
#     list_display = ('title', 'text')

  
@admin.register(Kerchnet_account)
class Kerchnet_account(admin.ModelAdmin):
    readonly_fields = ('kn_login','kn_datetime_created_formated')
    # kn_datetime_created_formated = ['']
    
