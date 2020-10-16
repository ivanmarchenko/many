# import ckeditor.widgets
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from .models import Post, Kerchnet_account
from django.utils.translation import gettext_lazy as _

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# форма добавления аккаунта KerchNET
class KnAccountCreateForm(forms.ModelForm):
    """
    Форма KnAccountCreateForm
    """
    # kn_email = forms.EmailField()
    # kn_password = CharField()
    class Meta:
        model = Kerchnet_account
        fields = ['kn_email', 'kn_password']
        
    def __init__(self, *args, **kwargs):
        super(KnAccountCreateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

# форма обновления объявления
class PostUpdateForm(forms.ModelForm):
    """
    Форма PostUpdate
    """
    title = forms.CharField(label='Заголовок', widget=forms.TextInput)
    text = forms.CharField(label='Содержимое', widget=CKEditorUploadingWidget())
    datetime_changed = forms.DateTimeField(label='Дата-время изменения', disabled=True, required=False)

    class Meta:
        model = Post
        fields = ['title', 'text', 'category', 'datetime_changed']
   
    def __init__(self, *args, **kwargs):
        super(PostUpdateForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['size'] = 60
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

# форма добавления объявления
class PostCreateForm(PostUpdateForm):
    """
    Форма PostCreate
    """
    datetime_changed = None
    class Meta:
        model = Post
        fields = ['title', 'text', 'category']