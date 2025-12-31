from django.db.models import Model, CharField, TextField


class Contact(Model):
    full_name = CharField(max_length=500)
    email = CharField(max_length=500)
    subject = CharField(max_length=250)
    phone_number = CharField(max_length=250)
    company = CharField(max_length=100, null=True, blank=True)
    message = TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.full_name}--{self.email}--{self.subject}'
