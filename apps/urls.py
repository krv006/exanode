from django.urls import path

from apps.views import ContactListCreateView

urlpatterns = [
    path('contact-us/', ContactListCreateView.as_view(), name='contact-us'),
]
