from django.urls import path
from .views import (
        home,
        CategorieListView,
        CategorieEditView,
        CategorieCreateView,
        CategorieDeleteView,
    )
urlpatterns = [
    path("", home.as_view(), name="home"),
    path('categories/', CategorieListView.as_view(), name="list-categories"),
    path("categories/<int:pk>/edit/", CategorieEditView.as_view(), name="category_edit"),
    path("categories/<int:pk>/delete/", CategorieDeleteView.as_view(), name="category_delete"),
    path("categories/new/", CategorieCreateView.as_view(), name="category_create"),

]