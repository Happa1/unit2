# Nov 23,2023
## api part2
import requests

user = {"username":"manaha", "password":"12345"}
# user = {"username":"MMproject", "password":"MMproject2"}
ip = "192.168.6.153"

# register user
# answer = requests.post(f'http://{ip}/register', json=user)
# print(answer.json())

# # login to get cookie
answer = requests.post(f'http://{ip}/login', json=user)
# # print(answer.json())
cookie = answer.json()["access_token"]
# cookie = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6dHJ1ZSwiaWF0IjoxNzAxMzg3OTg0LCJqdGkiOiJiMDc2YjVhOC1iMTgzLTQxYmMtODcyMC05NWUwMTFhZGEwNGUiLCJ0eXBlIjoiYWNjZXNzIiwic3ViIjoyMSwibmJmIjoxNzAxMzg3OTg0LCJleHAiOjE3MDEzODg4ODQsImlzX2FkbWluIjpmYWxzZX0.Nlfr4hmSZeS3A4aF_tGuz28Pp1QtqRO_gbpYDXDP3nE"


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
# answer = requests.get(f'http://{ip}/user/readings',
#                       headers=header)
# print(f"user readings{answer.json()}")

# answer = requests.get(f'http://{ip}/sensors', # see information of the sensor
#                       headers=header)
# print(answer.json())

# data = requests.get(f'http://{ip}/readings',
#                     headers=header)
# data = data.json()
# print(data)
# x = data['readings']
# print(x)
# print(f"There are {len(x)} records in the server")

def get_sensor(id:int=1, ip:str="192.168.6.153"):
    request = requests.get(f'http://{ip}/readings')
    data = request.json()
    sensors=data['readings'][0]
    sensor = []

    for s in sensors:
        if s['sensor_id']==id:
            sensor.append(s['value'])
    return sensor

sensor3=get_sensor(id=29)
print(sensor3)

