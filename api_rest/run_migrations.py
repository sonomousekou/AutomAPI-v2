from django.apps import apps
from django.core.management import call_command

from api_rest.settings import PROJECT_APPS

# Récupérer les applications spécifiées dans PROJECT_APPS
selected_apps = [apps.get_app_config(app_name) for app_name in PROJECT_APPS]

def run_migrations():
    # Récupérer la liste des configurations d'application
    app_configs = selected_apps
    
    # Exécuter les migrations pour chaque application
    for app_config in app_configs:
        app_name = app_config.name
        print(f"Exécution des migrations pour l'application {app_name}")
        call_command('makemigrations', app_name)
        call_command('migrate', app_name)
