from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Student(models.Model):
    YEAR_IN_SCHOOL_FRESHMAN = 'FR'
    YEAR_IN_SCHOOL_SOPHPOMORE = 'SO'
    YEAR_IN_SCHOOL_JUNIOR = 'JR'
    YEAR_IN_SCHOOL_SENIOR = 'SR'
    YEAR_IN_SCHOOL_GRADUATE = 'GR'
    YEAR_IN_SCHOOL_CHOICES = [
        (YEAR_IN_SCHOOL_FRESHMAN, 'Freshman'),
        (YEAR_IN_SCHOOL_SOPHPOMORE, 'Sophomore'),
        (YEAR_IN_SCHOOL_JUNIOR, 'Junior'),
        (YEAR_IN_SCHOOL_SENIOR, 'Senior'),
        (YEAR_IN_SCHOOL_GRADUATE, 'Graduate'),
    ]
    id = models.BigAutoField(
    auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True)
    phone = models.IntegerField()
    city = models.CharField(blank=True, null=True, max_length=255)
    zip = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=255)
    graduation = models.IntegerField(blank=True, null=True)
    email = models.EmailField(unique=True)
    year = models.CharField(
        max_length=255, choices=YEAR_IN_SCHOOL_CHOICES, default=YEAR_IN_SCHOOL_FRESHMAN)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"