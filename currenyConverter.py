import requests
import json
import sys

class Currency:
  def get_quotation(self, income, outcome):
    self.income = income
    self.outcome = outcome
    quotationUrl = 'https://api.exchangeratesapi.io/latest?'
    quotationPayload = {
      'symbols': self.income + ',' + self.outcome,
      'base': self.income
    }

    response = requests.get(quotationUrl, params=quotationPayload)
    quotation = json.loads(response.text)
    return quotation['rates'][self.outcome]

def menu_loop():
  # income = 'BRL'
  # outcome = 'USD'
  cur = Currency()
  while(1):
    print("1 - Cotação em dolar")
    print("2 - Conversão de real para euro")
    print("3 - Conversão de euro para dolar")
    num = input("Digite o número da opção desejada:")
    if num == 1:
      income = 'BRL'
      outcome = 'USD'
      out_rate = cur.get_quotation(income, outcome)  
    elif num == 2:
    
    elif num == 4:
      print("Programa finalizado")
      sys.exit(-1)
  
if __name__ == "__main__":
  income = 'BRL'
  outcome = 'USD'
  cur = Currency(income)
  out_rate = cur.get_quotation(outcome)

  print("{} to {}: {}".format(income, outcome, out_rate))