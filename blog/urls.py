from django.urls import path
from .views import article_list_view, article_detail_view, article_crate_view

urlpatterns = [
    path('list/', article_list_view, name='article_list'),
    path('list/<int:id>/', article_detail_view, name='article_detail'),
    path('create/', article_crate_view, name='article_create'),
]


