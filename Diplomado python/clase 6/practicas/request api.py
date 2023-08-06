import requests

response = requests.get('https://www.google.com/')
print('Response: ', response)
print("Response content: ",response.content)
print('URL: ', response.url)
print('Status code: ', response.status_code)
print('HTTP header: ', response.headers)