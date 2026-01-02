from django.db.models import Model, CharField, ImageField, URLField
from django.db.models.enums import TextChoices
from django_ckeditor_5.fields import CKEditor5Field


class Team(Model):
    class TeamJob(TextChoices):
        director = 'director', 'Director'
        developer = 'developer', 'Developer'
        manager = 'manager', 'Manager'
        designer = 'designer', 'Designer'

    name = CharField(max_length=150)
    description = CKEditor5Field(null=True, blank=True)
    linkedin_link = URLField(max_length=300, blank=True)
    photo = ImageField(upload_to='team_photos/', null=True, blank=True)
    team_job = CharField(
        max_length=20,
        choices=TeamJob.choices,
        default=TeamJob.developer
    )

    def __str__(self):
        return f"{self.name} ({self.team_job})"
