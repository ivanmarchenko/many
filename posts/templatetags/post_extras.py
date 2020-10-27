from django import template
register = template.Library()

@register.simple_tag
def get_model_verbose_name(model):
    """
    Возвращает имя модели
    """
    return model._meta.verbose_name
    # return instance._meta.get_field(field_name).verbose_name.title()

@register.simple_tag
def get_field_verbose_name(model, field):
    """
    Возвращает имя поля модели
    """
    return model._meta.get_field(field).verbose_name

@register.filter
def table_model_verbose_name_plural(table):
    """
    Получение названия модели через Tables
    """
    return table._meta.model._meta.verbose_name_plural

@register.simple_tag
def table_record_per_page(view):
    """
    Получение количество записей на странице
    """
    return view.paginate_by

@register.simple_tag
def get_bootstrap_alert_msg_css_name(tags):
  return 'danger' if tags == 'error' else tags