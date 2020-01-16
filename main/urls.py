from django.urls import path
from . import views
from main.views import refreshData


app_name = 'main'

urlpatterns = [
	path('authorize/', views.authorize, name='authorize'),
	path('', views.welcome, name='welcome'),
	path("downloads/", views.downloadss, name='downloads'),
	path("about/", views.about, name="about"),
	path("disclaimer/", views.disclaimer, name ="disclaimer")
	path("donated/", views.donated, name ="donated")
	path("fail-donated/", views.fail-donated, name ="fail-donated")
]