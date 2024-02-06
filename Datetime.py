#1-Create Datetime
from datetime import datetime
my_time = datetime(1992, 1, 1, 12, 30, 0)
#2-Check your date and time
year = my_time.year
month = my_time.month
day = my_time.day
second = my_time.second
print(f"The date is {year}-{month}-{day}")


#3-Doing math with datetime (adding 7 days)
from datetime import timedelta
future_datetime = my_time + timedelta(days=7)
print(f"The future date is {future_datetime}")

#4-Comparing dates
if future_datetime > my_time:
    print("The future is really good!")

#Making a birthday countdown
birthday = datetime(1992, 3, 10)
today = datetime.now()
print(f"{today}")
days_left = (birthday - today).days #
print(f"Days left until your birthday is: {days_left} days!")

#UUID
import uuid
class SpecificAnimal:
    def __init__(self, name):
        self.name = name
        self.id = str(uuid.uuid4())
cat = SpecificAnimal("Miouw")
dog = SpecificAnimal("bark")
print("f{cat.name}'s ID: {cat.id}") 

 