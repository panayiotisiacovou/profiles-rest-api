from django.urls import path
from profiles_app import views

urlpatterns= [
    path('hello-view/',views.HelloAPiView.as_view())
]
