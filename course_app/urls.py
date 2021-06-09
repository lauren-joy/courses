from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add', views.add),
    path('courses/destroy/<int:course_id>', views.destroy),
    path('courses/delete/<int:course_id>', views.delete),
]