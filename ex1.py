from datetime import datetime
import random
import re

def get_days_from_today(date):
    try:
        new_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
         print(f"Date format for '{date}' is incorrect. Expected format is 'YYYY-MM-DD'.function")
    finally:
        print('-'*30)
    
    today = datetime.today().date()
    return (today - new_date).days
    
def get_numbers_ticket(min, max, quantity):
    my_list = []
    if min >= 1 and max <= 1000:       
        while quantity >0:
            number = random.randint(min, max)
            if number in my_list:
                quantity = quantity
            else:
                my_list.append(number) 
                quantity -=1 
        return my_list
    else:
        return  my_list
    
