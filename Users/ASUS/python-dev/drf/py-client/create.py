import requests

endpoint = "http://localhost:8000/api/products/" 


data = {
  'title':"Title testing Now for new created",
  'price':39.99
}
get_response = requests.post(endpoint,json=data)

print(get_response.json())