#importing the required libraries
import matplotlib.pyplot as plt
import numpy as np

#define data values
x = np.array([1,1,2,2,1,4,4,3,3,3,2,2]) #x-axis points
y = np.array([1,2,2,1,1,1,2,2,1,4,4,1]) #Y-axis points

plt.plot(x,y) #plot the chart
plt.xlabel("ball size") #add x-axis label
plt.ylabel("length (inches)") #add y-axis label
plt.title("penis") #add title
plt.show() #display