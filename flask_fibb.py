#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app = Flask(__name__)


# In[4]:


@app.route('/')
def print_fib():
    return '<h1>Fibonacci</h1>'


# In[ ]:


#Roots or Routes are where our decorator functions are


# In[ ]:


#Creating another webpage besides the previous one


# In[ ]:


@app.route('/fib') #Adding app.route decorator with /fib as argument
def list_fib():
    return '<b>1, 1, 2, 3, 5, 8, 13, 21 ...</b>' #These are few first fibonacci numbers

