from django.urls import path 
from .views import userregisterview

urlpatterns = [
    path('register',userregisterview.as_view(),name='registration'),
   

]
