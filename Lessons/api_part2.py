# Nov 23,2023
## api part2
import requests

#user = {"username":"manaha", "password":"12345"}
user = {"username":"manaha", "password":"12345"}
ip = "192.168.6.153"

# register user
# answer = requests.post(f'http://{ip}/register', json=user)
# print(answer.json())

# login to get cookie
answer = requests.post(f'http://{ip}/login', json=user)
# print(answer.json())
cookie = answer.json()["access_token"]


# create a sensor
# sensor_a = {
#     'type':'Temperature',
#     'location':'Asama25',
#     'name':'manaha2_temp_1',
#     'unit':'C'
# }

# put the cookie in the header of the request
header = {'Authorization':f'Bearer {cookie}'}
# answer = requests.post(f'http://{ip}/sensor/new',
#                        json=sensor_a,
#                        headers=header)
# print(answer.json())

#send a recording to the sencor id 19
# record = {'sensor_id':27, 'value':30}
# answer = requests.post(f'http://{ip}/reading/new',
#                        json=record,
#                        headers=header)
# print(f"send recordings {answer.json()}")


# get all my recordings
answer = requests.get(f'http://{ip}/user/readings',
                      headers=header)
print(f"user readings{answer.json()}")

answer = requests.get(f'http://{ip}/sensors', # see information of the sensor
                      headers=header)
print(answer.json())

data = requests.get(f'http://{ip}/readings')
data = data.json()

x = data['readings']
print(x)
print(f"There are {len(x)} recprds in the server")


