
from django.urls import path , include
from user.views import signup ,login
from .views import home
app_name='home'
urlpatterns = [
    # path('', Home.as_view() , name='home'),    #class base
    path('',home,name='home'),
    path('signup/',signup,name='signup'),
    path('login/',login,name='login')


]