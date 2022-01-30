from django.apps import AppConfig


class CrmConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crm'


class AccountsConfig(AppConfig):
    name = 'customer'

    def ready(self):
        import customer.signals