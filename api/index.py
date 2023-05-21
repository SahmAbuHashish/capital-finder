from http.server import BaseHTTPRequestHandler
# from datetime import datetime
import urllib
import requests

class handler(BaseHTTPRequestHandler):
 
  def do_GET(self):
    s = self.path
    url_components = parse.urlsplit(s)
    query_strings_list = parse.parse_qsl(url_components.query)
    dic = dict(query_strings_list)
    country = dic.get('country')
    capital = dic.get('capital')

    if country:
        url = f'https://restcountries.com/v3.1/name/{country}'
        res = requests.get(url)
        data = res.json()
        result = data[0]['capital']
  
    if capital:
        url = f'https://restcountries.com/v3.1/capital/{capital}'
        res = requests.get(url)
        data = res.json()
        result = data[0]['name']

    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(result.encode('utf-8'))
    return 