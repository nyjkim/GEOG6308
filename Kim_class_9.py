#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import arcpy


# In[2]:


os.getcwd()


# os.mkdir() creates a new folder in the current directory that we are in

# In[3]:


os.mkdir("output")


# arcpy.env.overwriteOutput = True
# asks jupyter to overwrite any new Outputs without throwing an error message
# *only use if you really want to overwrite

# "arcpy.Select_analysis()" takes three arguments: 1) input feature, 2) output location, and 3) the expression

# In[12]:


arcpy.Select_analysis(
    # Input feature
    "./tl_2018_us_state.shp",
    # Output shapefile
    "./output/DE.shp",
    # Expression
    '"NAME" = \'Delaware\''
)


# Write a function state_select(state) that will perform this process for an arbitrary state and return the path to the output shapefile as a string.

# In[16]:


def select_state(state):
    x = str(state)
    arcpy.Select_analysis(
        "./tl_2018_us_state.shp",
        "./output/%s.shp" %x,
        '"NAME" = \'%s\'' %x
    )
    print x


# In[18]:


select_state('California')


# CLIP

# In[19]:


def state_districts_116(state):
    arcpy.Clip_analysis(
        "./tl_2018_us_cd116.shp",
        "./output/%s.shp" %state,
        "./output/cong_%s.shp" %state
    )


# In[20]:


state_districts_116('California')


# # Loop for List of States 

# In[21]:


state_list = ["Maryland","New York","Florida","Texas","Alaska"]


# In[23]:


for state in state_list:
    select_state(state)
    state_districts_116(state)
print "Completed!"

