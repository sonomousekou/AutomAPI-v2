from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.apps import apps
from api_rest.settings import PROJECT_APPS, AUTERS_APPS

APPS_ADMIN = AUTERS_APPS + PROJECT_APPS
# Récupérer les applications spécifiées dans PROJECT_APPS
selected_apps = [apps.get_app_config(app_name) for app_name in APPS_ADMIN]

# Parcourir chaque application
for app_config in selected_apps:
    # Parcourir chaque modèle de l'application
    for model in app_config.get_models():
        # Personnaliser l'administration pour chaque modèle
        @admin.register(model)
        class CustomAdmin(ImportExportModelAdmin, admin.ModelAdmin):
            list_display = [field.name for field in model._meta.fields if field.name != "id"]
