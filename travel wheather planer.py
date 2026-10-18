distance_mi = 60
is_raining = False
has_bike = True
has_car = False
has_ride_share_app = False

if has_car or has_ride_share_app:
    print('It is possible to travel')

elif distance_mi >= 60 or not is_raining and hs_bike:
    print('It will be hard to arrive at your destination')

elif distance_mi < 10 and not is_raining:
    print('It will be easy to arrive')

else:
    print('It is not possible to travel')
#In free code camp this is a laboratory so i have to cum up with my own text I tried to pick the conditionals above in a way that it covers all posibilites

if not distance_mi:
    print('You are alreadt at your destination')