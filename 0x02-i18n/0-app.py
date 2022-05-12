#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__, static_url_path='')


app.route('/', methods=['GET'], strict_slashes=False)
def root():
    """"
    Root end point
    """
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
