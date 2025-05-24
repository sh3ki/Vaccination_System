from django.contrib.auth import get_user_model

from celery import shared_task
from django.core.mail import send_mail
from hospital import models
from hospitalmanagement import settings
from django.utils import timezone
from datetime import datetime, timedelta
from django.shortcuts import render, HttpResponse
from twilio.rest import Client
from hospitalmanagement.celery import app


@shared_task(bind=True)
def send_mail_func(self,mail,name):
    # current_year = datetime.now().year
    # users = get_user_model().objects.all()
    # #timezone.localtime(users.date_time) + timedelta(days=2)
    # for user in users:
    mail_subject = f"Vaccine Reminder for {name}"
    message = f"Dear {name},\n\nThis is a friendly reminder for the vaccine.\n\nPlease ensure that you schedule an appointment with your doctor.\n\nThank you!"
    to_email = mail
    send_mail(
            subject = mail_subject,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[to_email],
                fail_silently=True,
            )
    return "Task Scehdule Done"


# tasks.py



# @shared_task(bind=True)
# def send_vaccine_reminder_email(patient_id, vaccine_name):
#     try:
#         patient = Patient.objects.get(id=patient_id)
#         email_subject = f"Vaccine Reminder for {patient.get_name}"
#         email_body = f"Dear {patient.get_name},\n\nThis is a friendly reminder for the {vaccine_name} vaccine.\n\nPlease ensure that you schedule an appointment with your doctor.\n\nThank you!"
#         sender_email = settings.EMAIL_HOST_USER  # Replace with your sender email
#         recipient_email = patient.user.email

#         send_mail(email_subject, email_body, sender_email, [recipient_email], fail_silently=False)
#         print(f"Reminder email sent to {recipient_email} for {vaccine_name} vaccine.")
#     except Patient.DoesNotExist:
#         print(f"Patient with ID {patient_id} does not exist.")
