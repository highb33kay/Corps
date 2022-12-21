from django.db import models

# Create your models here.
class CompanyProfile(models.Model):

    # African countries choices
    countries = (
        ("Alg", "Algeria"),
        ("Ang", "Angola"),
        ("Ben", "Benin"),
        ("Bot", "Botswana"),
    )

    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    name_of_organization = models.CharField(max_length=255)
    number_of_employees = models.IntegerField()
    director_1 = models.CharField(max_length=255)
    director_2 = models.CharField(max_length=255)
    director_3 = models.CharField(max_length=255)
    phone_number = models.IntegerField(max_length=255)

    # country choices field
    country = models.CharField(max_length=3, choices=countries)
    organization_reg_no = models.IntegerField(max_length=255)
    cac_no = models.IntegerField(max_length=255)
    proposal_status = models.BooleanField(default=False, blank=False)

    # Bank Status
    correspondence_status = models.BooleanField(default=False, blank=False)
    receiver_status = models.BooleanField(default=False, blank=False)

    # clearance status
    clearance_status = models.BooleanField(default=False, blank=False)

    def __str__(self):
        return self.name
