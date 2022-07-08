from django.contrib import admin
from django.urls import path
from . import views

app_name = 'arprojsys'

urlpatterns = [
    path('',views.Mainpage, name="Mainpage"),
    path('Payment/',views.Payment, name="Payment"),
    path('Summary/',views.Summary, name="Summary"),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('pdelete/<int:id>', views.pdelete, name='pdelete'),
    path('pedit/<int:id>', views.pedit, name='pedit'),
    ]