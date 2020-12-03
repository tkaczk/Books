def car(maker, model, **car_info):
    car_info['Producer'] = maker.title()
    car_info['Model'] = model.title()
    return car_info


car_profile = car('ford', 'mustang',
                   fuel='gasoline',
                   engine='5000',
                   power='1500-100-900',
                   )


print(car_profile)
