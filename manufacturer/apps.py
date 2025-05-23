from django.apps import AppConfig


class ManufacturerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'manufacturer'

    def ready(self):
        import manufacturer.signals
