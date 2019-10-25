#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


iris = pd.read_csv("S:/GEOG_6308.80_Programming_Geospatial_201903/Class-Shared/iris_csv.csv")


# To create a markdown cell: cread a new cell with 'b', navigate to it, and press 'm', write text, and then Ctrl + Enter.

# In[5]:


print iris


# In[6]:


type(iris)


# This means that within the pandas library, there is the core module. Within that core module, there is a submodule called frame.
# The dir command below gives us a list of all the methods that we can use with this file.

# In[8]:


dir(iris)


# In[11]:


iris.head()


# In[12]:


iris.tail()


# In[13]:


iris.info()


# What makes a dataframe a dataframe is that it can store columns of different data type (e.g. the information above shows that the first four columns are floats while the fifth column contains objects).

# To select a single column within the dataframe:

# In[14]:


iris["species"]


# To select multiple columns, we pass a list of column names.

# In[15]:


iris[["sepal_length", "sepal_width"]]


# What is the type of a single column? In pandas, a single column is called a series.

# In[17]:


type(iris["species"])


# One way to do indexing that is not very powerful:

# In[18]:


iris[3:5]


# A more powerful way to do indexing:

# In[19]:


iris["sepal_length"] > 5


# This can be, then, subset like the following way, which only gives us the rows that have sepal_length > 5:

# In[20]:


iris[iris["sepal_length"] > 5]


# The code below will give you everything with "sepal_length"> 5 AND "species" == "setosa":

# In[21]:


gts = iris[iris["sepal_length"] > 5]
gts[gts["species"] == "setosa"]


# To create a new column called "sepal_area":

# In[25]:


iris["sepal_area"] = iris["sepal_length"] * iris["sepal_width"]
iris.head()


# # Split-Apply-Combine

# Grouping the data by species: 

# In[28]:


iris_grouped = iris.groupby("species")
print iris_grouped


# In[29]:


iris_grouped.sum()


# In[30]:


iris_grouped.mean()


# In[31]:


iris_grouped.aggregate(["mean", "std"])


# In[32]:


iris.aggregate(["mean", "std"])


# Creating a scatter plot graph with pandas:

# In[34]:


plt = iris.plot.scatter(x = "sepal_length", y = "sepal_width")

