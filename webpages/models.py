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

    status = (
        ("Pending", "Pending"),
        ("Completed", "Completed"),
    )

    Name = models.CharField(max_length=255, unique=True)
    Address = models.CharField(max_length=255)
    Name_of_Organization = models.CharField(max_length=255, unique=True)
    Number_of_Employees = models.IntegerField()
    First_Director = models.CharField(max_length=255)
    Second_Director = models.CharField(max_length=255)
    Third_Director = models.CharField(max_length=255)
    Phone_Number = models.IntegerField(max_length=255)

    # country choices field
    Country = models.CharField(max_length=3, choices=countries)
    Organization_Registration_No = models.IntegerField()
    CAC_No = models.CharField(max_length=255)
    Proposal_Status = models.CharField(
        max_length=255, choices=status, default="Pending"
    )

    # Bank Status
    Correspondence_Status = models.CharField(
        max_length=255, choices=status, default="Pending"
    )
    Receiver_Status = models.CharField(
        max_length=255, choices=status, default="Pending"
    )

    # clearance status
    Clearance_Status = models.CharField(
        max_length=255, choices=status, default="Pending"
    )

    def __str__(self):
        return self.name
