from django.apps import apps
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import path
import requests

API_BASE_URL = 'https://api.example.com/'

def generate_crud_views():
    for app_config in apps.get_app_configs():
        app_models = app_config.get_models()
        for model in app_models:
            model_name = model.__name__
            model_api_url = f'{API_BASE_URL}{model_name.lower()}/'
            
            # Generate list view
            def model_list(request):
                response = requests.get(model_api_url)
                if response.status_code == 200:
                    items = response.json()
                    return render(request, 'list.html', {'items': items, 'model_name': model_name})
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
                return render(request, 'create.html', {'model_name': model_name})
            
            # Generate detail view
            def model_detail(request, pk):
                response = requests.get(f'{model_api_url}{pk}/')
                if response.status_code == 200:
                    item = response.json()
                    return render(request, 'detail.html', {'item': item, 'model_name': model_name})
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
                    return render(request, 'update.html', {'item': item, 'model_name': model_name})
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
                    return render(request, 'delete.html', {'item': item, 'model_name': model_name})
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

# Liste vide pour enregistrer les URL
urlpatterns = []

# Appelle la fonction pour générer les vues et les routes CRUD
generate_crud_views()

# Ajoute les autres routes de votre projet
urlpatterns += [
    # Autres routes
]
