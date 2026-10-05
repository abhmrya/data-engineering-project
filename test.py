import requests

result = requests.get('https://github.com/abhmrya')

print(result.request.body)
print(dir(result.request))
print(repr(result))