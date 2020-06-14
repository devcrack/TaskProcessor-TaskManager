""" This kind of task are so lite """
from celery import shared_task
import main.machine.process_lite as p_lite

@shared_task
def exe_hrdsphere(frac_vol):
    p_lite.exe_hard_sphere(frac_vol)
