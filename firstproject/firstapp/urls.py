from django.urls import path 
from .views import studentlist,studentdetailview,studentupdateview,studentcreateview,studentdeleteview

urlpatterns=[
    path('',studentlist.as_view(),name='home'),
    path('details/<int:pk>',studentdetailview.as_view(),name='detail'),
    path('create',studentcreateview.as_view(),name='create'),
    path('details/edit/<int:pk>',studentupdateview.as_view(),name='edit'),
    path('details/delete/<int:pk>',studentdeleteview.as_view(),name='delete'),
    
] 