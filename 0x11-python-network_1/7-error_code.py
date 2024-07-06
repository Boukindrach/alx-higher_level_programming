#!/usr/bin/python3

"""
script that takes in a URL, sends a request to
the URL and displays the body of the response.
"""

from sys import argv
import requests


if __name__ == "__main__":

    URL = argv[1]
    request = requests.get(URL)
    if request.status_code >= 400:
        print("Error code: {}".format(request.status_code))
    else:
        print(request.text)
