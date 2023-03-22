from django.urls import path

from netbox.views.generic import ObjectChangeLogView
from . import models, views


urlpatterns = (

    path('application-lists/', views.ApplicationListListView.as_view(), name='applicationlist_list'),
    path('application-lists/add/', views.ApplicationListEditView.as_view(), name='applicationlist_add'),
    path('application-lists/<int:pk>/', views.ApplicationListView.as_view(), name='applicationlist'),
    path('application-lists/<int:pk>/edit/', views.ApplicationListEditView.as_view(), name='applicationlist_edit'),
    path('application-lists/<int:pk>/delete/', views.ApplicationListDeleteView.as_view(), name='applicationlist_delete'),
    path('application-lists/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='applicationlist_changelog', kwargs={
        'model': models.ApplicationList
    }),

)
