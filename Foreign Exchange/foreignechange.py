import requests 
#api key currency
url = 'https://v6.exchangerate-api.com/v6/0186cc237319c2ae8316bdc6/latest/USD'

#request to get data
response = requests.get(url)
data = response.json()
print (data)
