import requests

url = "http://localhost:8000/predict"
data = {
    "features": [0.5, 0.2, 0.1, 0.3, 0.4, 0.6, 0.7, 0.8, 0.9, 0.1, 
                 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1, 0.2]
}

response = requests.post(url, json=data)
print(response.json())