from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny

from apps.models import Contact
from apps.serializers import ContactModelSerializer


class ContactListCreateView(ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactModelSerializer
    permission_classes = (AllowAny,)
