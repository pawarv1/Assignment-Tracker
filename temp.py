import requests

# API URL and your API key
url = "https://canvas.instructure.com/api/v1/courses"
headers = {
    "Authorization": "Bearer 19~xAwnz9KzuAAZGEDtJtzkaF9C7rCEDMvLNPtGFHRfXUc8GeGWtmA2TLEyJCXzWKcf"
}

# Send a GET request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print(data)  # Work with the response data
else:
    print(f"Error: {response.status_code}")