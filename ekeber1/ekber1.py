import requests
url = "https://api.exchangerate-api.com/v4/latest/USD"
response = requests.get(url)
data = response.json()

usd_to_azn = data["rates"]["AZN"]
usd_to_euro = data["rates"]["EUR"]
usd_to_try = data["rates"]["TRY"]

print(f"1 USD = {usd_to_azn}AZN")
print(f"1 USD = {usd_to_euro}EURO")
print(f"1 USD = {usd_to_try}TRY")