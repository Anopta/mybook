import profile
from turtle import title
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('profile-update', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class FamilyMember(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    relationship = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT)
    school = models.CharField(max_length=255, null=True )
    course = models.CharField(max_length=255, null=True)
    # admission_date = models.DateField(null=True)
    # graduation_date = models.DateField(null=True)
    # grade = models.FloatField(max_length=255, null=True)
    # graduation_type = models.FloatField(max_length=255, null=True)
    thesis = models.CharField(max_length=255, null=True )
    
    class Meta:
        verbose_name_plural = 'Education'

    def __str__(self):
        return self.school
