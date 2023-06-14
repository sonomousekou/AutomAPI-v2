# project/scripts/create_templates.py
import os
from django.apps import apps
from django.conf import settings
from backoffice.settings import PROJECT_APPS

# Récupérer les applications spécifiées dans PROJECT_APPS
selected_apps = [apps.get_app_config(app_name) for app_name in PROJECT_APPS]

def create_app_template_folders():
    for app_config in selected_apps:
        app_name = app_config.name
        # app_template_dir = os.path.join(settings.BASE_DIR, app_name, 'templates', app_name)
        app_template_dir = os.path.join(settings.BASE_DIR, 'templates', 'crud', app_name)
        os.makedirs(app_template_dir, exist_ok=True)
        create_html_files(app_template_dir)

def create_html_files(template_dir):
    template_files = {
        'list.html': '<!-- Content for list.html -->',
        'create.html': '<!-- Content for create.html -->',
        'detail.html': '<!-- Content for detail.html -->',
        'update.html': '<!-- Content for update.html -->',
        'delete.html': '<!-- Content for delete.html -->',
    }

    for filename, content in template_files.items():
        file_path = os.path.join(template_dir, filename)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                file.write(content)

if __name__ == '__main__':
    create_app_template_folders()
