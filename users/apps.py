from django.apps import AppConfig

#opens setting.py file and used to configure the application.
class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import users.signals
