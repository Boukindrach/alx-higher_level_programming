#!/usr/bin/python3
"""
script that takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter,
and finally displays the body of the response.
"""

import sys
import requests


if __name__ == "__main__":

    URL = sys.argv[1]
    value = {"email": sys.argv[2]}
    request = requests.post(URL, data=value)
    print(request.text)
