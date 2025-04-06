import requests

def get_endpoints(swagger_url):
    response = requests.get(swagger_url)
    if response.status_code == 200:
        data = response.json()
        endpoints = list(data.get("paths", {}).keys())
        print("Endpoints:")
        for ep in endpoints:
            print(ep)
    else:
        print("Could not fetch Swagger data")

# Run with example Swagger JSON:
get_endpoints("https://petstore.swagger.io/v2/swagger.json")
