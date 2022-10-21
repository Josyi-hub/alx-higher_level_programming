#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL & displays the body of the response
"""

if __name__ == "__main__":
    import urllib.error as error
    from sys import argv
    import urllib.request as request
    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as r:
            print(r.read().decode('utf-8'))
    except error.HTTPError:
        print(f"Error code: {e.code}")
