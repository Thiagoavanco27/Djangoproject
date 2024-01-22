from django.apps import AppConfig


class PhilosofiaConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "philosofia"

class TemplateConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "base_template"