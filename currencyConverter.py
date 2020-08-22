import requests
import json
# import sys

class Currency:
  def get_quotation(self, income, outcome):
    self.income = income
    self.outcome = outcome
    quotationUrl = 'https://api.exchangeratesapi.io/latest?'
    quotationPayload = {
      'symbols': self.outcome,
      'base': self.income
    }

    response = requests.get(quotationUrl, params=quotationPayload)
    # print(type(response.text))
    # print(response.text)
    quotation = json.loads(response.text)
    # print(type(quotation))
    # print(quotation)
    return quotation['rates'][self.outcome] 

menu = 0
currency = Currency()

while menu != 4:
  print(f"1 - Cotação do dólar\n2 - Conversão real para euro\n3 - Conversão euro para dólar\n4 - sair")
  try:
    menu = int(input("Digite uma opção: "))
    if menu == 1:
      income = 'USD'
      outcome = 'BRL'
      rate = currency.get_quotation(income, outcome)
      print("O valor atual do {} em {} é: {}".format(income, outcome, rate))
    elif menu == 2:
      income = 'BRL'
      outcome = 'EUR'
      rate = currency.get_quotation(income, outcome)
      print("O valor atual do {} em {} é: {}".format(income, outcome, rate))
      value = int(input("Digite um valor: "))
      currencyExchange = value * rate
      print("{} {} é igual a {:.2f} {}".format(value, income, currencyExchange, outcome))
    elif menu == 3:
      income = 'EUR'
      outcome = 'USD'
      rate = currency.get_quotation(income, outcome)
      print("O valor atual do {} em {} é: {}".format(income, outcome, rate))
      value = int(input("Digite um valor: "))
      currencyExchange = value * rate
      print("{} {} é igual a {:.2f} {}".format(value, income, currencyExchange, outcome))
    else:
      print("Não é um número válido")

  except ValueError:
    print("Não é um número ou valor válido")