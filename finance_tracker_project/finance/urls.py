from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # frontend
    path("transactions/", views.get_transactions),
    path("transactions/add/", views.add_transaction),
    path("transactions/delete/<str:id>/", views.delete_transaction),


]

