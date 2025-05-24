from datetime import timedelta
from django.db import models

from django.dispatch import receiver
from dateutil.relativedelta import relativedelta
from requests import request
from django.contrib.auth.models import User

departments=[('Gynecologist','Gynecologist'),('Dermatologist','Dermatologist'),('Endocrinologist','Endocrinologist'),
             ('Allergist','Allergist'),('Ophthalmologist','Ophthalmologist'),
(' Pediatrician',' Pediatrician')
]
bloodGroups=[('Select bloodGroup','Select bloodGroup'),
('A+','A+'),
('A-','A-'),
('B+','B+'),
('B-','B-'),
('AB+','AB+'),
('AB-','AB-'),
('O+','O+'),
('O-',' O-')
]
CHILD_GENDER_CHOICES = [
        ('Select Gender','Select Gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
]
class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    department= models.CharField(max_length=50,choices=departments,default='Gynecologist')
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.department)

    
class Appointment(models.Model): 
    user = models.OneToOneField(User ,null=True,on_delete=models.CASCADE) 
    patientId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40,null=True)
    doctorName=models.CharField(max_length=40,null=True)
    appointmentDate=models.DateField(null=True)
    appointmentTime = models.TimeField(null=True)
    description=models.TextField(max_length=500)
    status=models.BooleanField(default=False)
    completed = models.BooleanField(default=False)


class PatientDischargeDetails(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40)
    assignedDoctorName=models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    symptoms = models.CharField(max_length=100,null=True)

    admitDate=models.DateField(null=False)
    releaseDate=models.DateField(null=False)
    daySpent=models.PositiveIntegerField(null=False)

    roomCharge=models.PositiveIntegerField(null=False)
    medicineCost=models.PositiveIntegerField(null=False)
    doctorFee=models.PositiveIntegerField(null=False)
    OtherCharge=models.PositiveIntegerField(null=False)
    total=models.PositiveIntegerField(null=False)


    

class VaccineInfo(models.Model):
    vaccine_names = models.CharField(max_length=100)
    vaccine_details = models.CharField(max_length=300)
    protect_against= models.CharField(max_length=100)
    to_be_given = models.CharField(max_length=100)

    def __str__(self):
        return self.vaccine_names
    

class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    # email = models.EmailField(max_length=254,unique=True,blank=True,null=True,validators=[EmailValidator])
    profile_pic= models.ImageField(upload_to='profile_pic/PatientProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    age = models.PositiveIntegerField(null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    bloodGroup= models.CharField(max_length=20,choices=bloodGroups, default="Select bloodGroup")
    child_gender = models.CharField(max_length=20, choices=CHILD_GENDER_CHOICES,default="Select Gender")
    mobile = models.CharField(max_length=20,null=False) 
    symptoms = models.CharField(max_length=100,null=False,default="No Symptoms") 
    assignedDoctorId = models.PositiveIntegerField(null=True)
    admitDate=models.DateField(auto_now=True)
    status=models.BooleanField(default=False) 

    def save_vaccine_schedule(self,user):
        
        # Calculate the date of birth for the Vaccine Schedule based on the Patient's date_of_birth
        
        birth_date = self.date_of_birth
        six_weeks = birth_date + timedelta(weeks=6)
        ten_weeks = birth_date + timedelta(weeks=10)
        fourteen_weeks = birth_date + timedelta(weeks=14)
        six_months = birth_date + relativedelta(months=6)
        nine_months = birth_date + relativedelta(months=9)
        nine_to_twelve_months = birth_date + relativedelta(months=11)
        twelve_months = birth_date + relativedelta(months=12)
        fifteen_months = birth_date + relativedelta(months=15)
        sixteen_to_eighteen_months = birth_date + relativedelta(months=16)
        eighteen_months = birth_date + relativedelta(months=18)
        two_years = birth_date + relativedelta(years=2)
        four_to_six_years = birth_date + relativedelta(years=4)
        ten_to_twelve_years = birth_date + relativedelta(years=10)

        # Create a VaccineSchedule object with the calculated dates
        vaccine_schedule = VaccineSchedule(
            patientId = user,
            date_of_birth=birth_date,
            birth=birth_date,
            six_weeks=six_weeks,
            ten_weeks=ten_weeks,
            fourteen_weeks=fourteen_weeks,
            six_months=six_months,
            nine_months=nine_months,
            nineTotwelve_months=nine_to_twelve_months,
            twelve_months=twelve_months,
            fivteen_months=fifteen_months,
            sixteenToEighteen_months=sixteen_to_eighteen_months,
            Eighteen_months=eighteen_months,
            two_years=two_years,
            fourToSIx_years=four_to_six_years,
            tenToTwelve_years=ten_to_twelve_years
        )

        return vaccine_schedule


    
    def save_vaccine_schedule_reminder(self,user):
        # Calculate the date of birth for the Vaccine Schedule based on the Patient's date_of_birth
        birth_date = self.date_of_birth
        six_weeks = (birth_date + timedelta(weeks=6)) - timedelta(days=2)
        ten_weeks = (birth_date + timedelta(weeks=10))- timedelta(days=2)
        fourteen_weeks = (birth_date + timedelta(weeks=14))- timedelta(days=2)
        six_months = (birth_date + relativedelta(months=6))- timedelta(days=2)
        nine_months = (birth_date + relativedelta(months=9))- timedelta(days=2)
        nine_to_twelve_months = (birth_date + relativedelta(months=11))- timedelta(days=2)
        twelve_months = (birth_date + relativedelta(months=12))- timedelta(days=2)
        fifteen_months = (birth_date + relativedelta(months=15))- timedelta(days=2)
        sixteen_to_eighteen_months = (birth_date + relativedelta(months=16))- timedelta(days=2)
        eighteen_months = (birth_date + relativedelta(months=18))- timedelta(days=2)
        two_years = (birth_date + relativedelta(years=2))- timedelta(days=2)
        four_to_six_years = (birth_date + relativedelta(years=4))- timedelta(days=2)
        ten_to_twelve_years = (birth_date + relativedelta(years=10))- timedelta(days=2)

        # Create a VaccineSchedule object with the calculated dates
        vaccine_schedule_reminder = VaccineScheduleReminder(
            patientId = user,
            date_of_birth=birth_date,
            birth=birth_date,
            six_weeks=six_weeks,
            ten_weeks=ten_weeks,
            fourteen_weeks=fourteen_weeks,
            six_months=six_months,
            nine_months=nine_months,
            nineTotwelve_months=nine_to_twelve_months,
            twelve_months=twelve_months,
            fivteen_months=fifteen_months,
            sixteenToEighteen_months=sixteen_to_eighteen_months,
            Eighteen_months=eighteen_months,
            two_years=two_years,
            fourToSIx_years=four_to_six_years,
            tenToTwelve_years=ten_to_twelve_years
        )

        return vaccine_schedule_reminder

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name
		
		
class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username		
		
class VaccineSchedule(models.Model):
    patientId=models.OneToOneField(User,on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    birth = models.DateField()
    six_weeks = models.DateField()
    ten_weeks = models.DateField()
    fourteen_weeks = models.DateField()
    six_months = models.DateField()
    nine_months = models.DateField()
    nineTotwelve_months = models.DateField()
    twelve_months = models.DateField()
    fivteen_months = models.DateField()
    sixteenToEighteen_months= models.DateField()
    Eighteen_months = models.DateField()
    two_years= models.DateField()
    fourToSIx_years= models.DateField()
    tenToTwelve_years= models.DateField()

    def __str__(self):       
        return str(self.date_of_birth)
    

class VaccineScheduleReminder(models.Model):
    patientId=models.OneToOneField(User,on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    birth = models.DateField()
    six_weeks = models.DateField()
    ten_weeks = models.DateField()
    fourteen_weeks = models.DateField()
    six_months = models.DateField()
    nine_months = models.DateField()
    nineTotwelve_months = models.DateField()
    twelve_months = models.DateField()
    fivteen_months = models.DateField()
    sixteenToEighteen_months= models.DateField()
    Eighteen_months = models.DateField()
    two_years= models.DateField()
    fourToSIx_years= models.DateField()
    tenToTwelve_years= models.DateField()

    def __str__(self):       
        return str(self.date_of_birth)


