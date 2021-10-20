import requests

API_KEY = "qfNfdijpFhbhPhA7j2ZxvtEGkfv8DftTtmTEbnWN"
API_ENDPOINT = "https://api.craft.co/v1/query"
GRAPHQL_QUERY = """
    query getCompany($domain: String!) {
        company(domain: $domain) {
            locations {
                city
                country
            }
        }
    }
"""

request_headers= { "x-craft-api-key": API_KEY }
request_data = {
    "query": GRAPHQL_QUERY,
    "variables": { "domain": "facebook.com" }
}

response = requests.post(API_ENDPOINT, json=request_data, headers=request_headers, timeout=30)
response_data = response.json()

print(response_data)