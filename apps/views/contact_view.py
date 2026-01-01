from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny

from apps.models import Contact
from apps.serializers import ContactModelSerializer
from apps.utils import send_telegram_message


class ContactListCreateView(ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactModelSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        contact = serializer.save()

        message = (
            "📩 <b>Yangi Contact xabari</b>\n\n"
            f"👤 <b>Ism:</b> {contact.full_name}\n"
            f"📧 <b>Email:</b> {contact.email}\n"
            f"📞 <b>Telefon:</b> {contact.phone_number}\n"
            f"🏢 <b>Company:</b> {contact.company or '-'}\n"
            f"📝 <b>Subject:</b> {contact.subject}\n\n"
            f"💬 <b>Xabar:</b>\n{contact.message or '-'}"
        )

        send_telegram_message(message)