import requests

currancyFrom = "USD"
currancyTo = "GBP"
amount = 100


apiEndpoint = "https://open.er-api.com/v6/latest/" + currancyFrom

responce = requests.get(apiEndpoint)

if responce == "400":
  raise Exception("Request has failed")

dataSheet = responce.json()['rates']['']
print(dataSheet)

exchangeRates = responce.json()['rates'][currancyTo]

tAmount = (amount * exchangeRates)

print(f"{amount} {currancyFrom} in {currancyTo} is {tAmount:.2f}")