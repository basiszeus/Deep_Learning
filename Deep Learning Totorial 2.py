#!/usr/bin/env python
# coding: utf-8

# # Sigmoid

# In[2]:


import math

def sigmoid(x):
    return 1/(1+math.exp(-x))


# In[3]:


sigmoid(50)


# In[5]:


sigmoid(1)


# # Tanh

# In[13]:


def tanh(x):
    return (math.exp(x)- math.exp(-x))/(math.exp(x)+ math.exp(-x))


# In[14]:


tanh(100)


# In[15]:


tanh(-56)


# # ReLU

# In[17]:


def ReLU(x):
    return max(0,x)


# In[18]:


ReLU(77)


# In[20]:


ReLU(-55)


# # Leaky ReLU

# In[23]:


def LReLU(x):
    return max(0.1*x,x)


# In[24]:


LReLU(100)


# In[25]:


LReLU(-100)


# In[ ]:




