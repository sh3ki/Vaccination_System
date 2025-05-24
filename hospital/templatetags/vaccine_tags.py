from datetime import datetime
from django import template
from twilio.rest import Client
from dateutil.relativedelta import relativedelta

register = template.Library()

@register.filter
def get_due_on(schedule, to_be_given):
    if to_be_given == "BIRTH":
        return schedule.birth
    elif to_be_given == "6 WEEKS":
        return schedule.six_weeks
    elif to_be_given == "10 WEEKS":
        return schedule.ten_weeks
    elif to_be_given == "14 WEEKS":
        return schedule.fourteen_weeks
    elif to_be_given == "6 MONTHS":
        return schedule.six_months
    elif to_be_given == "9 MONTHS":
        return schedule.nine_months
    elif to_be_given == "9-12 MONTHS":
        return schedule.nineTotwelve_months
    elif to_be_given == "12 MONTHS":
        return schedule.twelve_months
    elif to_be_given == "15 MONTHS":
        return schedule.fivteen_months
    elif to_be_given == "16-18 MONTHS":
        return schedule.sixteenToEighteen_months
    elif to_be_given == "18 MONTHS":
        return schedule. Eighteen_months
    elif to_be_given == "2 YEARS":
        return schedule.two_years
    elif to_be_given == "4-6 YEARS":
        return schedule.fourToSIx_years
    elif to_be_given == "10-12 YEARS":
        return schedule.tenToTwelve_years
    # Add more conditions for other values of to_be_given

    return None  # Default return value if the condition is not met

reminder_date =[]
@register.filter
def reminder_set_on(schedule, to_be_given):
    if to_be_given == "BIRTH":
        reminder_date.append(schedule.birth - relativedelta(days=2))
        return schedule.birth - relativedelta(days=2)
    elif to_be_given == "6 WEEKS":
        reminder_date.append(schedule.six_weeks - relativedelta(days=2))
        return schedule.six_weeks - relativedelta(days=2)
    elif to_be_given == "10 WEEKS":
        reminder_date.append(schedule.ten_weeks - relativedelta(days=2))
        return schedule.ten_weeks - relativedelta(days=2)
    elif to_be_given == "14 WEEKS":
        return schedule.fourteen_weeks- relativedelta(days=2)
    elif to_be_given == "6 MONTHS":
        return schedule.six_months- relativedelta(days=2)
    elif to_be_given == "9 MONTHS":
        return schedule.nine_months- relativedelta(days=2)
    elif to_be_given == "9-12 MONTHS":
        return schedule.nineTotwelve_months- relativedelta(days=2)
    elif to_be_given == "12 MONTHS":
        return schedule.twelve_months- relativedelta(days=2)
    elif to_be_given == "15 MONTHS":
        return schedule.fivteen_months- relativedelta(days=2)
    elif to_be_given == "16-18 MONTHS":
        return schedule.sixteenToEighteen_months- relativedelta(days=2)
    elif to_be_given == "18 MONTHS":
        return schedule. Eighteen_months- relativedelta(days=2)
    elif to_be_given == "2 YEARS":
        return schedule.two_years- relativedelta(days=2)
    elif to_be_given == "4-6 YEARS":
        return schedule.fourToSIx_years- relativedelta(days=2)
    elif to_be_given == "10-12 YEARS":
        return schedule.tenToTwelve_years- relativedelta(days=2)
    return None   
