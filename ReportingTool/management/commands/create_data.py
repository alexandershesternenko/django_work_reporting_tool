# import datetime
# import random
# from django.core.management.base import BaseCommand
# from ReportingTool.models.completed_work import CompletedWork
# from users.models import CustomUser
#
# worker = [
#     'SSS',
#     'DDD',
#     'EEE',
#
# ]
#
# work_done = [
#     'first',
#     'second',
#     'third',
#
# ]
#
# checked_by_head = [
#     'True',
#     'False',
# ]
#
#
# def generate_worker_name():
#     index = random.randint(0, 2)
#     return worker[index]
#
#
# def generate_work_done():
#     index = random.randint(0, 2)
#     return work_done[index]
#
#
# def generate_checked_by_head():
#     val = random.randint(0, 1)
#     if val == 0:
#         return False
#     return True
#
# def generate_date():
#     year = 2022
#     month = 9
#     day = random.randint(1,28)
#     return datetime.date(year, month, day)
#
#
# class Command(BaseCommand):
#
#     def add_arguments(self, parser):
#         parser.add_argument(
#             'file_name', type=str, help='The txt file that  contains something')
#
#     def handle(self, *args, **kwargs):
#         file_name = kwargs['file_name']
#         with open(f'{file_name}.txt') as file:
#             for row in file:
#                 title = row
#                 date = generate_date()
#                 worker_name = generate_worker_name()
#                 work_done_name = generate_work_done()
#                 checked_by_head = generate_checked_by_head()
#
#                 worker = CustomUser.objects.get_or_create(
#                     name=worker_name
#                 )
#
#