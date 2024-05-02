"""
Security headers
    play a crucial role in enhancing the security of web applications by
    providing instructions to the web browser on handling certain aspects
    of the page. These headers are transmitted as part of the response from
    the server to the client's browser.

Security headers
    are used on the Application Layer of the OSI model to prevent some types
    of cyber attacks.

Commonly used security headers
    Strict-Transport-Security (HSTS):
        Enforces the use of HTTPS by instructing the browser to only connect
        to the website over secure, encrypted connections.
        Mitigates man-in-the-middle attacks, prevents protocol downgrade
        attacks, and enhances the overall security of data in transit.
    Content-Security-Policy (CSP):
        Specifies which resources (scripts, styles, images, etc.) the browser
        should load, reducing the risk of Cross-Site Scripting (XSS) attacks.
        Provides control over the sources of content, preventing the execution
        of malicious scripts injected by attackers.
    X-Content-Type-Options:
        Prevents browsers from interpreting files as a different type than
        declared by the server, reducing the risk of different attacks.
        Helps prevent attackers from tricking browsers into interpreting files
        as executable scripts.
    X-Frame-Options:
        Prevents a web page from being embedded within an iframe, reducing the
        risk of clickjacking attacks.
        Protects against attempts to trick users into interacting with a hidden
        frame containing malicious content.
    Cross-Origin-Resource-Policy (CORP):
        Controls whether the browser should allow a cross-origin resource to be
        shared.
        Mitigates the risk of data leakage from cross-origin requests, limiting
        access to resources from untrusted domains.
"""
import requests
from pprint import pprint


def get_security_headers(url):
    try:
        response = requests.get(url)
        headers = response.headers

        security_headers = {}
        header_keys = [
            ('Strict-Transport-Security', 'HSTS'),
            ('Content-Security-Policy', 'CPS'),
            ('X-Content-Type-Options', 'Content-Type'),
            ('X-Frame-Options', 'X-Frame'),
            ('Cross-Origin-Resource-Policy', 'CORP'),
        ]

        for head_sec, key in header_keys:
            security_headers[key] = headers.get(head_sec, f'{key} header not found')  # noqa          # noqa
        return security_headers

    except requests.exceptions.RequestException as e:
        return {'Error': e}


if __name__ == '__main__':
    url_to_check = 'http://gmail.com'

    security_headers = get_security_headers(url_to_check)
    pprint(security_headers)
