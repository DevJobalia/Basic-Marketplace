from django.urls import path

from . import views 

app_name = 'conversationApp'

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('new/<int:item_pk>/', views.new_conversation, name='newUrl'),
    path('<int:pk>/', views.detail, name='detail')
]

