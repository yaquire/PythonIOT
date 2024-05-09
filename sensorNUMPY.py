import csv
import matplotlib.pyplot as plt 

n= []
temp = []
humi = []

with open('sensordata.csv','r') as file:
    data=csv.reader(file,delimiter=',')
    for data_row in data:
        n.append(data_row[0])
        temp.append(data_row[1])
        humi.append(data_row[2])

#ploting graph 
plt.plot(n,temp,label='temperature')
plt.plot(n,humi,label='humidity')
plt.xlabel('2 sec sample intervals')
plt.ylabel('temperature in deg C & humidity in %')
plt.title('sensor data from AM2302')
plt.legend()
plt.show()
