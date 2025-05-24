# Child Vaccination Monitoring and Notification System Using Django
Web Portal for Child Vaccination Monitoring and Notification System Using Django and Celery

Use the above command to run the application:
   python manage.py makemigration
   python manage.py migrate
   python manage.py runserver

To start the celery use the below command:
   celery -A hospitalmanagement.celery worker --pool=solo -l INFO
   celery -A hospitalmangement beat -l INFO


