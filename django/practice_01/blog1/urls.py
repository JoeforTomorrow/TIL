from django.urls import path
from . import views

urlpatterns = [
    path('',views.index1),
    path('<int:pk>/',views.index1_pages)
]