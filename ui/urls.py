from django.urls import path
from . import views
app_name = 'ui'
urlpatterns = [
    path('', views.home_page,  name='home'),
    path('signup/', views.sign_up, name='signup'),
]
