import requests

if __name__ == "__main__":
    payload = {"first": "Kylie", "last":"Scharf"}
    r = requests.get("https://httpbin.org/get", params=payload)
    print(r.text)
