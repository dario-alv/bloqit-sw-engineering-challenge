from django.apps import AppConfig


class BackendAppConfig(AppConfig):
    name = 'backend'
    verbose_name = 'Bloqit'
    label = 'backend'

    def ready(self):
        # Importing the Bearer token swagger auth scheme here.
        # So that it is generated at app startup.
        from .swagger import BearerTokenScheme  
