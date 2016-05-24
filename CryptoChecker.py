from __future__ import print_function
from urlparse import urlparse
import urllib2
import urllib
import json


print('Loading function')
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

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    
    repro = "nope " 
    events = str(event["request"]["intent"]["slots"]["Coin"]["value"])

        
    if (events == "ETH" or events == "Ethereum" or events == "Etherium"):
        repro "The price of Etherium is "+getPrice("ETH","XBT")+" bitcoins, "+ getPrice("ETH","USD")+" US Dollars."
    if (events == "BTC" or event == "Bitcoin"):
        repro "The price of Bitcoin is "+getPrice("XBT","USD")+" US Dollars."
    
    return build_speechlet_response(titles, reply, repro, end)# Echo back the first key value
    #raise Exception('Something went wrong')
    
def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
  "version": "1.0",
  "response": {
    "outputSpeech": {
      "type": "PlainText",
      "text": reprompt_text
    },
    "card": {
      "content": "SessionSpeechlet - Welcome to the Alexa Skills Kit sample. Please tell me your favorite color by saying, my favorite color is red",
      "title": "SessionSpeechlet - Welcome",
      "type": "Simple"
    },
    "reprompt": {
      "outputSpeech": {
        "type": "PlainText",
        "text": "waddup do"
      }
    },
    "shouldEndSession": "true"
  },
  "sessionAttributes": {}
}
