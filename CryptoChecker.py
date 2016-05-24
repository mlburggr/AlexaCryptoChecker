from urlparse import urlparse
import urllib2
import urllib

import json
def getJSON():
    
    
    url = 'https://api.kraken.com/0/public/Ticker'
    values = { 'pair': 'ETHXBT, ETHUSD, XBTUSD' }
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    result = response.read()
    
    #r=requests.post("https://api.kraken.com/0/public/Ticker", data={"pair":"ETHXBT, ETHUSD, XBTUSD"})
    #return r.content
    return result

def getPrice(orig, dest):
    r=getJSON()
    parsed=json.loads(r)
    res = parsed["result"]
    ethxbt = res["XETHXXBT"]
    ethusd = res["XETHZUSD"]
    xbtusd = res["XXBTZUSD"]

    cEthxbt = ethxbt["c"]
    cEthusd = ethusd["c"]
    cXbtusd = xbtusd["c"]

    if (orig == "ETH" and dest == "XBT"):
        return cEthxbt[0]
    if (orig == "ETH" and dest == "USD"):
        return cEthusd[0]
    if (orig == "XBT" and dest == "USD"):
        return cXbtusd[0]
        
def getCoinHandler(event, context):
    if (event == "ETH" or event == "Ethereum" or event == "Etherium"):
        return "The price of Etherium is "+getPrice("ETH","XBT")+" bitcoins, "+getPrice("ETH","USD")+" US Dollars."
    if (event == "BTC" or event == "Bitcoin"):
        return "The price of Bitcoin is "+getPrice("XBT","USD")+" US Dollars."


    
print(getPrice("ETH","XBT"))
