from django.urls import path

from Blog import views

app_name = 'Blog'

urlpatterns = [
    path('', views.post_list, name='post-list'),
    path('<slug:slug>/', views.post_detail, name='post-detail')
]