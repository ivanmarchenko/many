import django_tables2 as tables
from django_tables2.utils import A
from .models import Post, Kerchnet_account
from django.utils.html import strip_tags, format_html, mark_safe



# class MaterializeCssCheckboxColumn(tables.CheckBoxColumn):
#     def render(self, value, bound_column, record):
#         default = {"type": "checkbox", "name": bound_column.name, "value": value}
#         if self.is_checked(value, record):
#             default.update({"checked": "checked"})

#         general = self.attrs.get("input")
#         specific = self.attrs.get("td__input")
#         attrs = tables.utils.AttributeDict(default, **(specific or general or {}))
#         return mark_safe("<p><label><input %s/><span></span></label></p>" % attrs.as_html())

# class NewsTable(tables.Table):
#     created = tables.DateTimeColumn(format='d/m H\h\s')
#     check = MaterializeCssCheckboxColumn(accessor='uid')

#     class Meta:
#         model = News
#         fields = ('check', 'title', 'created


# class UsefulCheckBox(tables.CheckBoxColumn):
#     def render(self, value, bound_column, record):
#         default = {"type": "checkbox", "name": bound_column.name, "value": value}
#         if self.is_checked(value, record):
#             default.update({"checked": "checked"})
#         general = self.attrs.get("input")
#         specific = self.attrs.get("td__input")
#         attrs = tables.utils.AttributeDict(default, **(specific or general or {}))
#         return mark_safe("<p><label><input %s/><span></span></label></p>" % attrs.as_html())


# определение таблицы списка Post
class PostTable(tables.Table):
    # привязка к record.pk через accessor='pk'
    selected_action = tables.CheckBoxColumn(accessor='pk', attrs={
        'th__input': {'id': 'js-checkbox-main', 'onclick': 'checkedAll(this)'},
        'td__input': {'class': 'js-checkbox', 'onclick': 'checkboxClick()'}
        })
    # id = tables.LinkColumn('posts:post_detail', args=[A('pk')], attrs={'a': {'class': 'font-weight-bold'}})
    id = tables.RelatedLinkColumn(attrs={'a': {'class': 'font-weight-bold'}})
    title = tables.LinkColumn('posts:post_detail', args=[A('pk')])
    datetime_changed = tables.DateTimeColumn(format='d.m.Y H:i:s')
    counter = tables.TemplateColumn("{{ row_counter }}")
    
    class Meta:
        model = Post
        template_name = 'django_tables2/bootstrap4.html'
        fields = ['selected_action', 'id', 'title', 'text', 'datetime_changed']

    # способ переопределения
    # def render_selected_action(self, record):
    #     return format_html(f'<input type="checkbox" value="{record.pk}">')


    def render_text(self, value):
        return strip_tags(value)[:150]+'...'
    
    # def render_id(self, record ):
    #     return format_html(f'<a href="{record.pk}"><b>{record.pk}</b></a>')
    
    # def render_title(self, record ):
    #     return format_html(f'<a href="{record.pk}">{record.title}</a>')

# определение таблицы списка для Kerchnet_account
class KnAccountTable(tables.Table):
    class Meta:
        model = Kerchnet_account
        template_name = 'django_tables2/bootstrap4.html'
        fields = ['id', 'kn_datetime_created', 'kn_email', 'kn_login', 'kn_password']