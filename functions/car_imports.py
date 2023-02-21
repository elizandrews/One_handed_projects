# Import the function car_info() and call using multiple approaches

import car_info_module
from car_info_module import car_info
from car_info_module import car_info as ci
import car_info_module as cim
from car_info_module import *

car1 = car_info_module.car_info('Nissan', 'Versa', year=2015, color='blue')
print(car1)

car2 = car_info('Nissan', 'Versa', year=2020, color='yellow')
print(car2)

car3 = ci('Nissan', 'Versa', year=2012, color='green')
print(car3)

car4 = cim.car_info('Nissan', 'Versa', year=2023, color='red')
print(car4)

car5 = car_info('Nissan', 'Versa', year=2022, color='blue')
print(car5)