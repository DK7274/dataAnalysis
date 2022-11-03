#importing the required libraries
import matplotlib.pyplot as plt
import numpy as np

#define data values
x = np.array([1,2,3,4]) #x-axis points
y = x*2 #Y-axis points

plt.plot(x,y) #plot the chart
plt.xlabel("X-axis") #add x-axis label
plt.ylabel("Y-axis") #add y-axis label
plt.title("Chart") #add title
plt.show() #display