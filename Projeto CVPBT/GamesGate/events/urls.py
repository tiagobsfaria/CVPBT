from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
        home,
        CategorieListView,
        AdminPanelView,
        get_localizacoes,
        CampoCreateView,
        ContactosView,
        QuemSomosView,
        ParceriasView,
        search_campos,
    )
urlpatterns = [
    path("", home, name="home"),
    path('get_localizacoes/<int:category_id>/', get_localizacoes, name='get_localizacoes'),
    path('categories/', CategorieListView.as_view(), name="list-categories"),
    path("adminpanel", AdminPanelView.as_view(),  name="admin_panel"),
    path("campo_create", CampoCreateView.as_view(), name="campo_create"),
    path("contactos", ContactosView.as_view(), name='contactos'),
    path("quemsomos",  QuemSomosView.as_view(), name='quemsomos'),
    path("parcerias",  ParceriasView.as_view(), name='parcerias'),
    path("search_campos/", search_campos, name='search_campos'),
]