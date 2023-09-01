import requests

api_key = "ASqqsnPRSb_42Pk64MukcQ"
headers = {"Authorization": "Bearer " + api_key}
api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
params = {
    "url": "https://www.linkedin.com/in/fanch-daniel-7474ab24/",
}
response = requests.get(api_endpoint, params=params, headers=headers)


response.json()
