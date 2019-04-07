def make_car(model_list, type_list, **description):
    car_profile = {'car_model': model_list, 'car_type': type_list}
    for key, value in description.items():
        car_profile[key] = value
    return car_profile


car = make_car('honda', 'outback', color='red', tow_package=True)
print(car)

# {'car_model': 'honda',
# 'car_type': 'outback',
# 'color': 'red',
# 'tow_package': True}
