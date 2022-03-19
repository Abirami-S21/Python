#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask #Import flask


# In[2]:

#Pass the main module or package of the application to the flask class constructor(dunder name)

app = Flask(__name__)


# In[4]:


@app.route('/')
def print_fib(): 
    return '<h1>Fibonacci</h1>'  #Define a function Print_fib which will print the string fibonacci on our web browser as an HTML heading

#When we send a request to a web server from our web browser, this request is forwarded to the flask application instance. The flask instance #has to know what code to run for each URL requested. So, a mapping is needed between the URL and the associated python function. This is #called a route or root. This is done by app.route decorator in flask. This decoartor tells flask which URL will trigger the print fib #function.
# In[ ]:




