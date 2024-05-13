from payament_times.in_time import *
import config
from payament_times.nine_months import payamnet_nine
from payament_times.six_months import payamnet_six
from payament_times.three_months import payamnet_three
from payament_times.twelve_months import payamnet_twelve


def credit_payament(desired_car, time_option):
    if(time_option == 1):
        return (in_time(desired_car))
    elif(time_option == 2):
        return (payamnet_three(desired_car))
    elif(time_option == 3):
        return (payamnet_six(desired_car))
    elif(time_option == 2):
        return (payamnet_nine(desired_car))
    elif(time_option == 2):
        return (payamnet_twelve(desired_car))
    
