from datetime import datetime
import random


def get_days_from_today(date):
    try:
        new_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
         print(f"Date format for '{date}' is incorrect. Expected format is 'YYYY-MM-DD'")
         return
    finally:
        print('-'*30)
    
    today = datetime.today().date()
    return (today - new_date).days
    
def get_numbers_ticket(min, max, quantity):
    my_list = []
    difference = max - min
    if max < min or difference < quantity:
        return my_list
    else:
        if min >= 1 and max <= 1000:       
            while quantity >0:
                number = random.randint(min, max)
                if number not in my_list:
                    my_list.append(number) 
                    quantity -=1  
                
            my_list.sort()
            return my_list
        else:
            return  my_list
    
