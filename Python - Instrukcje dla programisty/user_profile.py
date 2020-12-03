def build_profile(first, last, **user_info):
    user_info['first_name'] = first.title()
    user_info['last_name'] = last.title()
    return user_info


user_profile = build_profile('krzysztof', 'tkacz',
                             city='warszawa',
                             university='sggw',
                             wife='Kasia',
                             )


print(user_profile)
