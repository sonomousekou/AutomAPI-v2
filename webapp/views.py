from django.apps import apps
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import path
import requests
import os
from api_rest.settings import PROJECT_APPS, AUTERS_APPS

API_BASE_URL = 'http://127.0.0.1:8000/api/'

APPS_CRUD = AUTERS_APPS + PROJECT_APPS

# Récupérer les applications spécifiées dans PROJECT_APPS
selected_apps = [apps.get_app_config(app_name) for app_name in APPS_CRUD]

# Generate CRUD views
def generate_crud_views():
    urlpatterns = []
    
    # for app_config in selected_apps:

    #     app_models = app_config.get_models()
    #     for model in app_models:
    #         model_name = model.__name__

    for app_config in selected_apps:
        if app_config.name.split('.')[-1] in PROJECT_APPS:
            app_name = app_config.name.split('.')[-1]
        for model in app_config.get_models():
            model_name = model.__name__.lower()

            model_api_url = f'{API_BASE_URL}{model_name.lower()}/'

            app_name = app_config.name
            app_template_dir = os.path.join(settings.BASE_DIR, 'templates', 'crud', app_name, model_name)
            os.makedirs(app_template_dir, exist_ok=True)

            app_models = app_config.get_models()
            if not app_models:
                continue

            create_html_files(app_template_dir)
            
            # Generate list view
            def model_list(request):
                response = requests.get(model_api_url)
                if response.status_code == 200:
                    items = response.json()
                    return render(request, f'crud/{app_config.name}/{model.__name__.lower()}/list.html', {'items': items, 'model_name': model_name})
                else:
                    return render(request, 'error.html', {'message': 'Error retrieving items'})
            
            # Generate create view
            def model_create(request):
                if request.method == 'POST':
                    # Get form data
                    data = {}
                    for field in model._meta.fields:
                        field_name = field.name
                        data[field_name] = request.POST.get(field_name)
                    response = requests.post(model_api_url, data=data)
                    if response.status_code == 201:
                        return redirect(f'{model_name}_list')
                    else:
                        return render(request, 'error.html', {'message': 'Error creating item'})
                return render(request, f'crud/{app_config.name}/{model_name.lower()}/create.html', {'model_name': model_name})
            
            # Generate detail view
            def model_detail(request, pk):
                response = requests.get(f'{model_api_url}{pk}/')
                if response.status_code == 200:
                    item = response.json()
                    return render(request, f'crud/{app_config.name}/{model_name.lower()}/detail.html', {'item': item, 'model_name': model_name})
                else:
                    return render(request, 'error.html', {'message': 'Error retrieving item'})
            
            # Generate update view
            def model_update(request, pk):
                response = requests.get(f'{model_api_url}{pk}/')
                if response.status_code == 200:
                    item = response.json()
                    if request.method == 'POST':
                        # Get form data
                        data = {}
                        for field in model._meta.fields:
                            field_name = field.name
                            data[field_name] = request.POST.get(field_name)
                        response = requests.put(f'{model_api_url}{pk}/', data=data)
                        if response.status_code == 200:
                            return redirect(f'{model_name}_detail', pk=pk)
                        else:
                            return render(request, 'error.html', {'message': 'Error updating item'})
                    return render(request, f'crud/{app_config.name}/{model_name.lower()}/update.html', {'item': item, 'model_name': model_name})
                else:
                    return render(request, 'error.html', {'message': 'Error retrieving item'})
            
            # Generate delete view
            def model_delete(request, pk):
                response = requests.get(f'{model_api_url}{pk}/')
                if response.status_code == 200:
                    item = response.json()
                    if request.method == 'POST':
                        response = requests.delete(f'{model_api_url}{pk}/')
                        if response.status_code == 204:
                            return redirect(f'{model_name}_list')
                        else:
                            return render(request, 'error.html', {'message': 'Error deleting item'})
                    return render(request, f'crud/{app_config.name}/{model_name.lower()}/delete.html', {'item': item, 'model_name': model_name})
                else:
                    return render(request, 'error.html', {'message': 'Error retrieving item'})
            
            # Register the views dynamically with unique names
            globals()[f'{model_name}_list'] = model_list
            globals()[f'{model_name}_create'] = model_create
            globals()[f'{model_name}_detail'] = model_detail
            globals()[f'{model_name}_update'] = model_update
            globals()[f'{model_name}_delete'] = model_delete
            
            # Register the URLs dynamically
            urlpatterns.append(path(f'{model_name.lower()}/', model_list, name=f'{model_name}_list'))
            urlpatterns.append(path(f'{model_name.lower()}/create/', model_create, name=f'{model_name}_create'))
            urlpatterns.append(path(f'{model_name.lower()}/<int:pk>/', model_detail, name=f'{model_name}_detail'))
            urlpatterns.append(path(f'{model_name.lower()}/<int:pk>/update/', model_update, name=f'{model_name}_update'))
            urlpatterns.append(path(f'{model_name.lower()}/<int:pk>/delete/', model_delete, name=f'{model_name}_delete'))
    
    return urlpatterns

# Create HTML files in app template folders
def create_html_files(template_dir):
    template_files = {
        'list.html': '<!-- Content for list.html --> {{model_name}}',
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


# Generate CRUD views and get the URL patterns
# urlpatterns = generate_crud_views()

# # Add other URLs of your project
# urlpatterns += [
#     # Other URLs
# ]


from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
def home(request):
    # verifi si l'utilisateur est connecté, redirige le vers la page home
    # if not request.user.is_authenticated:
    #     return redirect('login')
    return render(request,'pages/home.html')

# gestion des erreurs
def handler403(request,exception):
    return render(request,'pages/403.html')

def handler404(request, exception):
    return render(request,'pages/404.html',status=404)

def handler500(request):
    return render(request,'pages/500.html')

def handler503(request,exception):
    return render(request,'pages/503.html') 
