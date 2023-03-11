from  django.urls import path

from . import views

# not needed ?
app_name = 'item'

urlpatterns = [
    path('', views.item, name='items'),
    path('<int:pk>/', views.detail, name='detail'),
    path('new/', views.newItem, name='new'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.EditItem, name='edit'),
    
]