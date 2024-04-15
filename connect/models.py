from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password

class Specialization(models.Model):
    specialization_id = models.AutoField(primary_key=True)
    specialization_name = models.CharField(max_length=255, unique=True, help_text="Enter a valid Specialization Name")

    def __str__(self):
        return self.specialization_name

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200, help_text="Enter a valid first name")
    last_name = models.CharField(max_length=200, help_text="Enter a valid last name")
    specialization_id = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    email_address = models.EmailField(max_length=200, unique=True, help_text="Enter a valid email address")
    password_hash = models.CharField(max_length=128, help_text="Enter a valid password")  # Store hashed password

    def set_password(self, raw_password):
        self.password_hash = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password_hash)

    def clean(self):
        # Custom validation for password field
        if len(self.password_hash) < 8:
            raise ValidationError("Password must be at least 8 characters long.")

    def __str__(self):
        return self.email_address

class County(models.Model):
    county_id = models.AutoField(primary_key=True)
    county_name = models.CharField(max_length=255, unique=True, help_text="Enter a valid County Name")

    def __str__(self):
        return self.county_name

class Constituency(models.Model):
    constituency_id = models.AutoField(primary_key=True)
    county_id = models.ForeignKey(County, on_delete=models.CASCADE)
    constituency_name = models.CharField(max_length=255, unique=True, help_text="Enter a valid Constituency Name")

    def __str__(self):
        return self.constituency_name

class Ward(models.Model):
    ward_id = models.AutoField(primary_key=True)
    constituency_id = models.ForeignKey(Constituency, on_delete=models.CASCADE)
    ward_name = models.CharField(max_length=255, unique=True, help_text="Enter a valid Ward Name")

    def __str__(self):
        return self.ward_name

class TechCompany(models.Model):
    tech_company_id = models.AutoField(primary_key=True)
    tech_company_name = models.CharField(max_length=255, unique=True, help_text="Enter a valid Company Name")

    def __str__(self):
        return self.tech_company_name

class SlotsAvailable(models.Model):
    slots_available_id = models.AutoField(primary_key=True)
    tech_company_id = models.ForeignKey(TechCompany, on_delete=models.CASCADE)
    specialization_id = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    ward_id = models.ForeignKey(Ward, on_delete=models.CASCADE)
    slot_count = models.PositiveIntegerField(help_text="Enter a valid Slot Number")
    application_deadline = models.DateTimeField(help_text="Enter application deadline")
    application_instructions = models.TextField(help_text="Enter application instructions", blank=True)
    slots_filled = models.PositiveIntegerField(default=0)

    def clean(self):
        # Custom validation for slot_count field
        if self.slot_count <= 0:
            raise ValidationError("Slot count must be a positive number.")

        # Custom validation for application_deadline field
        if self.application_deadline <= timezone.now():
            raise ValidationError("Application deadline must be in the future.")

    def is_application_closed(self):
        """Check if the application deadline has passed."""
        return self.application_deadline < timezone.now()

    def remaining_slots(self):
        """Calculate remaining slots."""
        return self.slot_count - self.slots_filled

    def has_expired(self):
        """Check if the slot availability has expired."""
        return self.remaining_slots() <= 0

    def update_slots_filled(self):
        """Update the number of slots filled."""
        filled_slots = self.slot_count - self.remaining_slots()
        if filled_slots < 0:
            raise ValidationError("Filled slots cannot be negative.")
        self.slots_filled = filled_slots
        self.save()
    
    def __str__(self):
        return f"{self.tech_company_id}-{self.specialization_id}-{self.ward_id}"