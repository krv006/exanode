from django.urls import path

from apps.views import ContactUsListCreateView, ContactListCreateAPIView

urlpatterns = [
    path('contact-us/', ContactUsListCreateView.as_view(), name='contact-us'),
    # todo contact location phone number and others
    path('contact/', ContactListCreateAPIView.as_view(), name='contact'),
]
