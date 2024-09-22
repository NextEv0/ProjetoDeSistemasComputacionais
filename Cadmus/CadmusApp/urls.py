from django.contrib.auth import views as auth_views
from django.urls import path
from .views import *

urlpatterns = [
    path('', form_continent, name="Cadmus Menu"),
    path('<int:id>', form_continent, name="continent_update"),
    path('delete/<int:id>/', delete_continent, name="continent_delete"),
    path('table/', view_continent, name="Tabelas"),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('base_generic/', base),
    
    # URLs para o CRUD geral
    path('tables/', choose_table, name='choose_table'),
    path('tables/<str:table_name>/', view_table_data, name='view_table_data'),
    path('tables/<str:table_name>/create/', create_record, name='create_record'),
]
