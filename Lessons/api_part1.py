# API part1
## Nov 22, 2023
import requests
import matplotlib.pyplot as plt

ip_server = "192.168.6.153"

data = requests.get(f'http://{ip_server}/readings')
data = data.json()

x = data['readings'][0]
print(f"There are {len(x)} recprds in the server")

my_sensors = {1:[], 2:[]} # I want to graph this two sensors
for record in x:
    id_sensor = record['sensor_id']
    if id_sensor in my_sensors:
        value = record['value']
        my_sensors[id_sensor].append(value)

print(my_sensors)

#create a graph
fig = plt.Figure(figsize=(10,8))
plt.subplot(2,1,1) # rows, colums, id
plt.plot(my_sensors[1], color="red")
plt.title("Sensor Outside")

plt.subplot(2,1,2)
plt.plot(my_sensors[2],color="black")
plt.title("Sensor Inside")

plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.4,
                    hspace=0.4)

plt.show()