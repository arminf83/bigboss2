
from django.urls import path , include
from .views import home
app_name='home'
urlpatterns = [
    # path('', Home.as_view() , name='home'),    #class base
    path('',home,name='home'),



]