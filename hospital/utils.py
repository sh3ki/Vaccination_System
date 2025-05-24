from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from celery.schedules import crontab

reminder_dates = []
dynamic_schedule = {}
def generate_reminder_dates():
    from hospital.models import Patient
    
   
    today = datetime.now().date()
    patient = Patient.objects.all()
    for i in patient:
        reminder_dates = []
        email = i.user.email
        name = i.get_name
        birth_date = i.date_of_birth
        six_weeks = (birth_date + timedelta(weeks=6)) - timedelta(days=2)
        ten_weeks = (birth_date + timedelta(weeks=10))- timedelta(days=2)
        fourteen_weeks = (birth_date + timedelta(weeks=14))- timedelta(days=2)
        six_months = (birth_date + relativedelta(months=6))- timedelta(days=2)
        nine_months = (birth_date + relativedelta(months=9))- timedelta(days=2)
        nine_to_twelve_months = (birth_date + relativedelta(months=12))- timedelta(days=2)
        twelve_months = (birth_date + relativedelta(months=12))- timedelta(days=2)
        fifteen_months = (birth_date + relativedelta(months=15))- timedelta(days=2)
        sixteen_to_eighteen_months = (birth_date + relativedelta(months=16))- timedelta(days=2)
        eighteen_months = (birth_date + relativedelta(months=18))- timedelta(days=2)
        two_years = (birth_date + relativedelta(years=2))- timedelta(days=2)
        four_to_six_years = (birth_date + relativedelta(years=4))- timedelta(days=2)
        ten_to_twelve_years = (birth_date + relativedelta(years=10))- timedelta(days=2)
        reminder_dates = [birth_date,six_weeks,ten_weeks,fourteen_weeks,six_months,nine_months,nine_to_twelve_months,
                          twelve_months,fifteen_months,sixteen_to_eighteen_months,eighteen_months,two_years,four_to_six_years,ten_to_twelve_years]
        
        for j in reminder_dates:
           
            task_name = f'my_periodic_task_{j}'

            years = j.year
            month = j.month
            day = j.day
            current_year = datetime.now().year

            if years == current_year:
                 dynamic_schedule[task_name] = {
                        'task': 'celery_task_mail.tasks.send_mail_func',
                        'schedule': crontab(hour=23, minute=5,day_of_month=day,month_of_year=month),
                        'one_off':True,
                        'args': (email,name),
                        'kwargs': {},
                        
                }                
                           
    return dynamic_schedule
        