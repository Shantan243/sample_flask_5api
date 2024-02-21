#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request
 
app = Flask(__name__)
 
@app.route('/arguments', methods=['GET'])
def arguments():
    arg1 = "Hello"
    arg2 = "world"
    arg3 = "from"
    arg4 = "Python"
    arg5 = "API"
    return f"{arg1} {arg2} {arg3} {arg4} {arg5}"
 
result = arguments()
print(result)
 
if __name__ == '__main__':
    app.run(debug=True)

