
from django.urls import path, include
import remaind.views
from django.conf.urls import url, include



urlpatterns = [

    path('view',remaind.views.viewremainder,name='view'),
    path('addevents',remaind.views.addevents,name='addevents'),
    path('viewaddevents', remaind.views.viewaddevent, name='viewaddevents'),
    path('editevents<int:id>', remaind.views.editevents, name='editevents'),
    path('allevents', remaind.views.allevents, name='allevents'),
    path('', remaind.views.viewhome, name='viewhome'),
    path('viewsignup', remaind.views.viewsignup, name='viewsignup'),
    path('login', remaind.views.login, name='login'),
    path('signup', remaind.views.signup, name='signup'),
    path('find', remaind.views.find, name='find'),
    path('delete<int:id>', remaind.views.delete, name='delete'),





]
