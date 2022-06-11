from django.shortcuts import render
import requests
import json

# Create your views here.


def index(request):
    #Crypto Prices data data/pricemultifull?fsyms
    api_price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX,ETH&tsyms=USD")
    api_price = json.loads(api_price_request.content)
    
    # Crypto News 
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'crypto/index.html', {'api':api, 'price':api_price})


def prices(request):
    if request.method == 'POST':
        quote = request.POST['quote']
        quote = quote.upper()
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
        api_quote = json.loads(crypto_request.content)
        
        
      
        return render(request, 'crypto/prices.html', {"quote":quote, 'crypto':api_quote})
    
    else:
        found = "Invalid input, Please input right keyword"
        return render(request, 'crypto/prices.html', {'not_found':found})
    