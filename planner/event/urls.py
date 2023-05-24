from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('delete/<int:day_id>&<int:event_id>/', views.delete, name='delete'),
    path('update/<int:event_id>/', views.update, name='update'),
]

