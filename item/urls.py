from  django.urls import path

from . import views

# not needed ?
app_name = 'item'

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
]