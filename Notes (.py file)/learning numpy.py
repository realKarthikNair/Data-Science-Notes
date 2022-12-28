#!/usr/bin/env python
# coding: utf-8

# ## <font color=blue>Numpy Notes</font>
#    
#    *by [Karthik Nair](https://realkarthiknair.github.io)*
# 
# #### <font color=maroon><i>Notes compiled from multiple sources including the Official Numpy Documentation</i></font>

# ### <font color=green>Numpy - introduction</font>
# 
# NumPy is the fundamental package for scientific computing in Python. It is a Python library that provides a multi-dimensional array object, various derived objects (such as masked [arrays](https://www.geeksforgeeks.org/introduction-to-arrays/) and [matrices](https://www.mathsisfun.com/algebra/matrix-introduction.html)), and an assortment of routines for
# fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier
# transforms, basic linear algebra, basic statistical operations, random simulation and much more
# 
# ### <font color=green>Why is numpy faster than lists?</font>
# 
# Numpy uses ndarray.
# An ndarray is a collection of homogeneous data-types that are stored in contiguous memory locations. 
# On the other hand, a list in Python is a collection of heterogeneous data types stored in non-contiguous memory locations.
# The NumPy package breaks down a task into multiple fragments and then processes all the fragments parallelly.
# 
# Ndarry classes are used to represent both Matrices and Vectors
# 

# ### <font color=green>How are NumPy Arrays different from Python lists?</font>
# 
# NumPy arrays have a fixed size at creation, unlike Python lists (which can grow dynamically). Changing the size
# of an ndarray will create a new array and delete the original
# 
# The elements in a NumPy array are all required to be of the same data type, and thus will be the same size in
# memory. The exception: one can have arrays of (Python, including NumPy) objects, thereby allowing for array 
# of different sized elements

# <font color=maroon>The NumPy package integrates C, C++, and Fortran codes in Python.<br>
# These programming languages have very little execution time compared to Python</font>

# ### <font color=blue>Importing the NumPy library</font>

# In[1]:


import numpy as np # it has become a convention to use np as the alias for numpy 


# ### <font color=blue>Creating NumPy Arrays</font>

# #### <font color=green>Using `array` function</font>
# You can create an array from a regular Python list or tuple using the array function

# In[2]:


my_array=np.array([1,2,3,4]) #from list

new_array=np.array((34,2,0,2)) #from tuple

print(my_array)
print(new_array)


# An optional parameter `ndmin` specifies the minimum number of dimensions that the resulting array should have. 
# > Ones will be prepended to the shape as needed to meet this requirement.
# 

# In[3]:


new_array=np.array([32,11,43,22],ndmin=3)
print(new_array)
print(new_array.shape) 


# In[4]:


array0=np.array([1,2,3,4]) 

print(type(array0)) # returns <class 'numpy.ndarray'>


# #### <font color=green>Using *placeholder* functions</font>
# Placeholder functions are used when we need to create an array with its size known, but elements unknown (intially)
# For example, we might need to create an array to store data of 10 students where the elements would be filled later

# <font color=maroon>np.zeros</font> : creates an array full of zeros

# In[5]:


np.zeros((2,4))


# <font color=maroon>np.ones</font> : returns an array full of ones

# In[6]:


np.ones((2,4))


# <font color=maroon>np.empty</font> : returns an array whose initial content is random

# In[7]:


np.empty((2,2)) #values could be anything


# <font color=maroon>np.full : </font> returns an array of the given shape filled with the fill_value

# In[8]:


np.full((2,2), fill_value=10)
np.full((2,2), 10)


# 

# #### <font color=green>Functions to create `sequence` of numbers</font>

# <font color=maroon>np.arange</font> : create sequences of numbers in a format analogous to Python's built-in `range`

# In[9]:


a=np.arange(10)
a


# In[10]:


np.arange( 10, 30, 5 )


# In[11]:


np.arange( 0, 2, 0.3 ) # it also accepts float arguments


# <font color=maroon>np.linspace</font> : receives as an argument the number of elements that we want, instead of the step values

# In[12]:


np.linspace( 0, 2, 9 )


# ### <font color=blue>Dimensions of an array</font>
# 
# Ndarrays can be of different dimensions or **Axes**
# e.g. 0D , 1D (known as Vector), 2D (known as Matrix), 3D, etc 
# Arrays of dimensions 3 or higher are commonly known as **Tensors** 
# 
# <font color=maroon><b>Rank</b> of an Array is the number of dimensions in an array</font>

# ### <font color=blue>Shape of an array</font>
# 
# Shape of an array is a tuple with 
# 

# ### <font color=blue>Arrays of different dimensions</font>

# #### <font color=green>0D Arrays</font>
# 
# Zero dimensional arrays are **scalars**.
# They can't be accessed using indices but can be converted into scalars
# Zero dimensional arrays are NOT equivalent to length-1 1D arrays
# 

# In[13]:


# Creating a zero dimensional array

array1=np.array(27)

array1


# In[14]:


array1.shape # returns () , which indicates zero  dimension


# In[15]:


array1.ndim # returns 0, which indicates 0 dimension


# In[16]:


# converting zero-dimensional arrays to scalars
scalar_array=array1.item()
scalar_array


# ### <font color=brown>Note</font>
# <font color=purple>For a zero dimensional array:</font><br>
# <font color=maroon>
# `print(array1[0]) #results in an error`
# - Trying to access the value in a 0D array using index results in an error</font>  
# reason : 0D ndarrays are considered scalars
# 

# #### <font color=green>1D Arrays</font>
# In a 1D array, a single argument is passed to access a specific value
# e.g in array [1,2,3,4], element '3' can be accessed with its index 2

# In[17]:


# Creating a length-1 one dimensional array

array2=np.array([27]) #unlike zero-dimensional arrays, in len1 1D arrays, we pass the array element in sq brackets

array2


# In[18]:


# with length more than 1

array3=np.array([1,2,3,4]) 

array3


# In[19]:


array2[0] # element can be accessed using index


# In[20]:


array3[2] # accessing the third element in array


# In[21]:


array3.shape # returns (4,) which indicates an array with 1 dimension and 4 elements 


# In[22]:


array3.ndim # returns 1, indicating 1 dimension


# #### <font color=green>2D Arrays</font>
# In 2D array, 2 arguments needs to be passed to access a single element

# In[23]:


array4=np.array([[1,2,3],[43,22,11]]) # Creating a 2D numpy array 

array4

# for instance, np.array([[1,2,3],[3,4,22],[43,22,11]]) indicates a 2D array with 3 layers and 3 elements in each layer


# In[24]:


array4[1][1] 
# Accessing the second element from the 2nd layer of the 2nd dimension


# In[25]:


array4.shape # returns (2,3)


# In[26]:


array4.ndim


# #### <font color=green>3D Arrays</font>
# 
# In 3D array, 3 argument needs to be passed to access a single element

# In[27]:


array5=np.array([[[22,3,32],[33,1,32]],[[44,34,21],[3,29,32]]]) 
# creating a 3D array with 2 layers and 2 sub-layers within each layer and 3 elements in each sub-layer

array5


# In[28]:


array5[1][1][1] 
# accessing the 2nd element of the 2nd sub-layer of the second layer, ie 29


# In[29]:


array5.ndim


# In[30]:


array5.shape


# In[31]:


array6=np.array([[[22,3,32],[33,1,32],[33,42,38]],[[44,34,21],[3,22,32],[99,43,88]]])
# creating a 3D array with 2 layers and 3 sub-layers within each layer and 3 elements in each layer

array6


# In[32]:


array6.ndim


# In[33]:


array6.shape


# ### <font color=blue>Printing Arrays</font>

# When you print an array, NumPy displays it in a similar way to nested lists, but with the following layout:
# • the last axis is printed from left to right,
# • the second-to-last is printed from top to bottom,
# • the rest are also printed from top to bottom, with each slice separated from the next by an empty line.

# <div>
# <img src="demo.jpeg" width="400"/>
# </div>

# <font color=maroon>One-dimensional arrays are then printed as rows, bidimensionals as matrices and tridimensionals as lists of matrices</font>

# <font color=green>If an array is too large to be printed, NumPy automatically skips the central part of the array and only prints the corners:</font>
# 
# To disable this behaviour and force numpy to print the whole array, we can change the printing options by using the np.set_printoptions method and passing either of the two arguments :
#     
#  - np.set_printoptions(threshold=np.inf)
#  - np.set_printoptions(threshold=sys.maxsize)    <i>after importing sys</i>

# In[34]:


import sys
np.set_printoptions(threshold=sys.maxsize)
# now printing array a would print all the numbers


# ### <font color=blue>Some important attributes of an Ndarray</font>  
# 
# `ndarray.ndim` Lets you see the number of axes(dimensions) of a numpy array  
# `ndarray.shape` Returns a tuple of integers indicating the size of the array in each dimension  
# e.g. for a
# matrix with n rows and m columns, shape will be (n,m). (len(ndarray.shape)==ndarray.ndim)  
# `ndarray.size` Displays the total number of elements in an array. (This is equal to the product of elements of
# shape)  
# `ndarray.dtype` returns an object describing the type of elements in the array  
# `ndarray.itemsize` returns size (in bytes) of each element of the array (Equivalent to ndarray.dtype.itemsize)  
# `ndarray.data` returns the buffer containing the actual elements of the array
# 

# ### <font color=blue>Basic Array Operations</font>

# <font color=maroon>Arithmetic operators on arrays apply elementwise</font>

# In[35]:


a = np.array( [20,30,40,50] )
b = np.arange( 4 )
b


# In[36]:


c=a-b
c


# In[37]:


b**2


# In[38]:


10*np.sin(a)


# In[39]:


a<30


# <font color=maroon>The product operator * operates elementwise in NumPy arrrays</font>

# In[40]:


a2=np.array([[1,2,3],[4,5,6]])


# In[41]:


a3=np.array([[7,8,9],[10,11,12]])


# In[42]:


a2*a3


# <font color=maroon>The matrix product
# can be performed using the @ operator (in python >=3.5) or the dot function or method:</font>

# In[43]:


a4=np.array([[3,4],[2,2]])


# In[44]:


a5=np.array([[4,2],[9,4]])


# In[45]:


a4@a5 #using @ operator


# In[46]:


a4.dot(a5) #using dot function


# In[47]:


a6=np.array([[1,2,3],[4,5,6]])


# In[48]:


a7=np.array([[7,8],[9,10],[11,12]])


# In[49]:


a6@a7 # matrix product of a 2*3 and 3*2 matrix


# In[50]:


a6.dot(a7) # also does matrix product


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




