# Write a function that stores info about a car in a dictionary
# Should always receive a manufacturer and model name
# Should accept arbitrary number of keyword arguments
# Call function with required info and 2 other name-value pairs
# Print dictionary to ensure all info stored correctly

def car_info(manufacturer, model_name, **kwargs):
    """Stores information about a car in a dictionary"""
    kwargs['manufacturer'] = manufacturer
    kwargs['model_name'] = model_name
    return kwargs

my_car = car_info('Nissan', 'Versa Note', year=2015, color='blue')
print(my_car)