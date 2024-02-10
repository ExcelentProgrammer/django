from time import sleep

from celery import shared_task


@shared_task
def my_task():
    for i in range(1000):
        sleep(0.3)
        print(i)
