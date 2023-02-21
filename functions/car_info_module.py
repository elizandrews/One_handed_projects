# Using a function you wrote that has one function, store in a separate file

def car_info(manufacturer, model_name, **kwargs):
    """Stores information about a car in a dictionary"""
    kwargs['manufacturer'] = manufacturer
    kwargs['model_name'] = model_name
    return kwargs