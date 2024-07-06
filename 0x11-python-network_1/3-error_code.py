#!/usr/bin/python3

"""
script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""

from sys import argv
import urllib.error
import urllib.request


if __name__ == "__main__":

    URL = argv[1]
    request = urllib.request.Request(URL)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as E:
        print("Error code: {}".format(E.code))
