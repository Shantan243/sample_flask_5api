#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/print_arguments', methods=['GET'])
def print_arguments():
    arg1 = request.args.get('arg1')
    arg2 = request.args.get('arg2')
    arg3 = request.args.get('arg3')
    arg4 = request.args.get('arg4')
    arg5 = request.args.get('arg5')

    # Concatenate the arguments
    result = f"Arguments: {arg1}, {arg2}, {arg3}, {arg4}, {arg5}"
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)

