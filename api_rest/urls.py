from django.apps import apps
from rest_framework import serializers, viewsets, routers
from rest_framework import permissions
from django.urls import path, include
from .settings import PROJECT_APPS, AUTERS_APPS
from pathlib import Path
import os

from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _ 
import debug_toolbar
from ckeditor_uploader import views as ckeditor_views
from django.conf.urls import handler400,handler403,handler404,handler500

# Create a generic serializer for all tables
class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = None
        fields = '__all__'

# Create generic viewsets for all tables
class ModelViewSet(viewsets.ModelViewSet):
    queryset = None
    serializer_class = None
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Register specific views for each model in the app
def create_views_and_urls():
    router = routers.DefaultRouter()

    for app_config in apps.get_app_configs():
        if app_config.name.split('.')[-1] in PROJECT_APPS:
            app_name = app_config.name.split('.')[-1]
            for model in app_config.get_models():
                model_name = model.__name__.lower()
                model_serializer = type(f'{model_name}Serializer', (ModelSerializer,), {'Meta': type('Meta', (object,), {'model': model, 'fields': '__all__'})})
                model_viewset = type(f'{model_name}ViewSet', (ModelViewSet,), {'queryset': model.objects.all(), 'serializer_class': model_serializer})
                
                router.register(model_name, model_viewset)

    APPS_URLS = AUTERS_APPS + PROJECT_APPS
    urlpatterns = [
        path('api/', include(router.urls)),
        # ... other URLs in your application ...

        # Inclure les URLs des applications spécifiques du projet
        *[
            path('', include(app_config.name + '.urls'))
            for app_config in apps.get_app_configs()
            if app_config.name.split('.')[-1] in APPS_URLS and os.path.exists(os.path.join(app_config.path, 'urls.py'))
        ],

        ############ Authentification #######################
        path('api-auth/', include('rest_framework.urls')), #rest
        path('', include('django.contrib.auth.urls')), #django
        ############ End Authentification #######################

        # URL de l'interface d'administration
        path('admin/', admin.site.urls),

        path('__debug__/', include(debug_toolbar.urls)),

        ##################### rosetta pour la traduction ####################
        path('rosetta/', include('rosetta.urls')),
        ##################### End rosetta  ####################

        path('i18n/', include('django.conf.urls.i18n')),

        ####################### CKEditor ################################
        # CKEditor urls, don' user include to remove @staff_user_required!
        # path('upload/', ckeditor_views.upload, name='ckeditor_upload'),
        # path('browse/', ckeditor_views.browse, name='ckeditor_browse'),
        # path('ckeditor/', include('ckeditor_uploader.urls')),
        path("ckeditor5/", include('django_ckeditor_5.urls')),
        ####################### End CKEditor ################################


    ]

    return urlpatterns

urlpatterns = create_views_and_urls()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# handler403="webapp.views.handler403"
# handler404="webapp.views.handler404"
# handler500="webapp.views.handler500"
# handler503="webapp.views.handler503"

