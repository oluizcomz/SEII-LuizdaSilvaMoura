#import my_module
from my_module import find_index, test as texto
import sys
import random
import math
import datetime
import calendar
import os
courses =['History','Math','Phisics','compSci']

index = find_index(courses,'Math')
print(index)
print(texto)
print(sys.path)
print(f'random: {random.choice(courses) }')
print(f'rad p/ graus: { math.radians(180)} seno: {math.sin(3.14)}')
today =datetime.date.today()
print('{} , {}'.format(today,calendar.isleap(2021)))

print(os.getcwd())
print(os.__file__)
