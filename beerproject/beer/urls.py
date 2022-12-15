from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('similarity_based', views.similartiy_based, name='similarity_based'),
    path('rating_based', views.rating_based, name='rating_based'),
    path('review_based', views.review_based, name='review_based'),
]