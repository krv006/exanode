from rest_framework.serializers import ModelSerializer

from apps.models import Contact


class ContactModelSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
