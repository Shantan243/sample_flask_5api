#!/usr/bin/env python
# coding: utf-8

# In[2]:


from flask import Flask, request


# Initializing flask app
app = Flask(__name__)


@app.route("/api", methods=['GET'])
def arguments():
 
    arg1 = request.args.get("hello_world")
    arg2 = request.args.get("Flask_is_awesome")
    arg3 = request.args.get('Apis_make_life_easier')
    arg4 = request.args.get('python_rules')
    arg5 = request.args.get('lets_build_cool_stuff')

    print(f"Argument 1: {arg1}")
    print(f"Argument 2: {arg2}")
    print(f"Argument 3: {arg3}")
    print(f"Argument 4: {arg4}")
    print(f"Argument 5: {arg5}")

    return "args printed successfully"

# Running the api
if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




