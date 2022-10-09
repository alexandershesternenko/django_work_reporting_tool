import datetime

from django.core.management import BaseCommand
from ReportingTool.models.directory import Period

''' Adds the number of days until the first of the next month (inclusive)'''


class Command(BaseCommand):

    def handle(self, *args, **options):

        today = datetime.datetime.today()
        next_month_first_day = (today.replace(day=1) + datetime.timedelta(days=32)).replace(day=1)
        last_date = datetime.datetime.strptime(str(Period.objects.latest('date')), '%Y-%m-%d')
        delta = next_month_first_day - last_date
        try:
            for i in range(0, int(delta.days)):
                last_date_updated = datetime.datetime.strptime(str(Period.objects.latest('date')), '%Y-%m-%d')
                new_date = last_date_updated + datetime.timedelta(days=1)
                add_instance = Period(date=new_date)
                add_instance.save()
            print(f'{i+1} dates added successfully')

        except Exception as err:
            print(err)



