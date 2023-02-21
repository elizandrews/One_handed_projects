# Begin with build_profile() from pg. 148
# Build a profile of yourself calling build_profile() & adding 3 key-value pairs

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Liz', 'Andrews', age=34, location='Greenville',
                            field='IT')

print(user_profile)