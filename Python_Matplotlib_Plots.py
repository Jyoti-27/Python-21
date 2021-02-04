#!/usr/bin/env python
# coding: utf-8

# ## Matplotlib initial setup in Jupyter Notebook

# In[1]:


import numpy as np
import matplotlib.pyplot as plt  #pyplot is a submodule in matplotlib and is imported as plt
#so in our programs the plotting package can be referred as plt.
print(plt.style.available)    #print all available styles
plt.style.use('classic')     #change style and see
get_ipython().run_line_magic('matplotlib', 'inline')
# static images of the plot embedded in the notebook


# ## Line Plots

# In[2]:


#For a simple line plot we need to specify the x and y axis values
#Univariate Plot
plt.plot([1, 2, 3, 4, 8])   #Univariate default values on x-axis are 0,1,2,3,4   line(x,y) (0,1) (1,2) (2,3) (3,4), (4,8)
plt.show()


# In[3]:


#Bivariate Plot/Analysis
x=[0, 2, 4, 6, 8]
y=[0, 6,12,10,12]
plt.plot(x,y)
plt.show()


# In[4]:


import matplotlib.pyplot as plt
x = range(8)  #values for 0 to 7  #create x-axis
print(x)
y=[0, 1, 4, 9, 16, 25, 36, 49]
plt.plot(x, y, marker = '*')  #y as a function of x   [0, 1, 4, 9, 16, 25, 36, 49]
#List comprehension
# [0 1 2 3 4 5 6 7]  [0, 1, 4, 9, 16, 25, 36. 49]
#plt.show()


# In[ ]:





# Time taken by Lists to perform multiplication: 0.3377840518951416 seconds
# 
# Time taken by NumPy Arrays to perform multiplication: 0.003999233245849609 seconds

# In[5]:


x=[1,2,3,4]
for x1 in x:
    y=x1**2
    print(x1**2)


# In[6]:


x = np.arange(8)  #values for 0 to 7  #create x-axis
print(x)
y1=[x1**2 for x1 in x]     #creating a y variable
y2=[x1**3 for x1 in x]
y3=[x1**4 for x1 in x]
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.show()


# Equivalent to the previous code

# In[7]:


#another way for Multiline plots all defined in one plot statement
x = range(8)  #values for 0 to 7  #create x-axis
print(x)
plt.plot(x, [x1 for x1 in x], x,
         [x1*x1 for x1 in x], x, [x1*x1*x1 for x1 in x])
plt.show()


# #How to label to distinguish between multiple lines

# In[8]:


#another way for Multiline plots all defined in one plot statement
x =x = np.arange(8)  #values for 0 to 7  #create x-axis
print(x)
plt.plot(x, [x1 for x1 in x], color='g')  # short color code (rgbcmyk) 
plt.plot(x, [x1*x1 for x1 in x], color ='m')
plt.plot(x, [x1*x1*x1 for x1 in x], color='c')
plt.show()


# In[9]:


#another way for Multiline plots all defined in one plot statement
#Different linestyles
x = np.arange(8)  #values for 0 to 7  #create x-axis
print(x)
plt.plot(x, [x1 for x1 in x], color='g', linestyle='solid' )  # short color code (rgbcmyk) 
plt.plot(x, [x1*x1 for x1 in x], color ='m', linestyle='dotted')
plt.plot(x, [x1*x1*x1 for x1 in x], color='c', linestyle='dashed')
plt.show()


# In[10]:


#Different linestyles and Linewidths
x = np.arange(8)  #values for 0 to 7  #create x-axis
print(x)
plt.plot(x, [x1 for x1 in x], color='g', linestyle='solid' , linewidth =3.0)  # short color code (rgbcmyk) 
plt.plot(x, [x1*x1 for x1 in x], color ='m', linestyle='dotted', linewidth =4.0)
plt.plot(x, [x1*x1*x1 for x1 in x], color='c', linestyle='dashed', linewidth =5.0)
plt.show()


# In[11]:


#Different Markesr
x = np.arange(8)  #values for 0 to 7  #create x-axis
print(x)
plt.plot(x, [x1 for x1 in x], color='g', linestyle='solid' , linewidth =3.0, marker= '*')  # short color code (rgbcmyk) 
plt.plot(x, [x1*x1 for x1 in x], color ='m', linestyle='dotted', linewidth =4.0, marker = 'v')
plt.plot(x, [x1*x1*x1 for x1 in x], color='c', linestyle='dashed', linewidth =5.0, marker ='o')
plt.show()


# In[12]:


#Exercise:  Specify all properties in one shot
x = np.linspace(0, 10, 10)   #generating 100 points between 0 and 10
plt.plot(x, x + 0, '-*b')  # solid green
plt.plot(x, x + 1, '--+c') # dashed cyan
plt.plot(x, x + 2, '-.^k') # dashdot black     
plt.plot(x, x + 3, ':vr')  # dotted red
plt.show()


# ## Graph Labels

# In[13]:


#When using a List use List comprehension to generate y
#When we are using a numpy array arr we can directly do arr*arr
import numpy as np
x = np.arange(5)
plt.plot(x, x,'*g', label='linear')
plt.plot(x, x*x,'^r', label='square')
plt.plot(x, x*x*x, 'oy',label='cube')
plt.grid(True)
plt.legend()
plt.show()


# In[14]:


#When using a List use List comprehension to generate y
#When we are using a numpy array arr we can directly do arr*arr
import numpy as np
x = np.arange(5)
plt.plot(x, x,'g', label='linear')
plt.plot(x, x*x,'r', label='square')
plt.plot(x, x*x*x, 'y',label='cube')
plt.grid(True)
plt.legend()
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title("Simpe X-Y plot")
plt.show()


# In[15]:


#Adjusting the Plot
#Adjust the axis limits
#three ways plt.axis([]). plt.xlim. plt.ylim,  plt.axis('tight')
import numpy as np
x = np.arange(5)
plt.plot(x, x, label='linear')
plt.plot(x, x*x, label='square')
plt.plot(x, x*x*x, label='cube')
plt.grid(True)
plt.legend()        #display labels
plt.xlabel('X-axis')    #x-axis title
plt.ylabel('Y-axis')    #y-axis title
plt.title('Polynomial Graph')   #graph title
#plt.axis([-1, 5, -1, 40])   #axis(lower limit ofx, upper limit of x, lower limit of y, upper limit of y)
#plt.xlim(-1,5)
#plt.ylim(-1,40)
plt.axis('tight')   #choose the limits as per the values in the data


# ## Save the figure use savefig()

# In[16]:


import numpy as np
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x))
plt.axis('tight')
#plt.axis('equal')   #sets the x-axis and y-axis equal
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sine Graph')
plt.savefig('plot.png')   #saves the fig
plt.show()    


# In[ ]:




