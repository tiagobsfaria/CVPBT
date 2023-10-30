from django.urls import path
from .views import (
        home,
        CategorieListView,
        AdminPanelView,
        get_localizacoes,
        CampoCreateView,
    )
urlpatterns = [
    path("", home, name="home"),
    path('get_localizacoes/<int:category_id>/', get_localizacoes, name='get_localizacoes'),
    path('categories/', CategorieListView.as_view(), name="list-categories"),
    path("adminpanel", AdminPanelView.as_view(),  name="admin_panel"),
    path("campo_create", CampoCreateView.as_view(), name="campo_create"),

]