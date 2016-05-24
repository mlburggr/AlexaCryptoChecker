package AlexaCryptoChecker;
import java.io.*;
import java.net.*;
import org.json.*;
import com.amazonaws.services.lambda.runtime.Context;

public class PriceGrabber {
    // Download JSON data (string) using HTTP Get Request
    private static String urlString = "https://api.kraken.com/0/public/Ticker";
    public static String getJSON(){
	BufferedReader reader=null;
	String text = "";
	try {
	    URL url = new URL(urlString);
	    String data = URLEncoder.encode("pair", "UTF-8") + "=" + URLEncoder.encode("ETHXBT, ETHUSD, XBTUSD", "UTF-8");
	    URLConnection conn = url.openConnection();
	    conn.setDoOutput(true);
	    OutputStreamWriter wr = new OutputStreamWriter(conn.getOutputStream());
	    wr.write(data);
	    wr.flush();

	    reader = new BufferedReader(new InputStreamReader(conn.getInputStream()));
	    StringBuilder sb = new StringBuilder();
	    String line = null;

	    while ((line = reader.readLine()) != null) {
		sb.append(line + "\n");
	    }
	    text = sb.toString();
	} catch (Exception e){

	} finally {
	    try {
		reader.close();
	    } catch(Exception e){

	    }
	}
	return text;
    }

    public String getCoinHandler(String input, Context context){
	if(input.equals("ETH") ||
	   input.equals("Ethereum") ||
	   input.equals("Etherium")){
	    return "The price of Etherium is "+
		getPrice("ETH","XBT")+"bitcoins, "+
		getPrice("ETH","USD")+"US Dollars";
	       
	}
	if(input.equals("BTC") ||
	   input.equals("Bitcoin")){
	    return "The price of Bitcoin is "+
		getPrice("XBT","USD")+"US Dollars";
	}
    }

    public static String getPrice(String orig, String dest){
	String result = getJSON();
	JSONObject reader = new JSONObject(result);
	JSONObject res = reader.getJSONObject("result");
	JSONObject ethxbt = res.getJSONObject("XETHXXBT");
	JSONObject ethusd = res.getJSONObject("XETHZUSD");
	JSONObject xbtusd = res.getJSONObject("XXBTZUSD");

	JSONArray cEthusd = ethusd.getJSONArray("c");
	JSONArray cXbtusd = xbtusd.getJSONArray("c");
	JSONArray cEthxbt = ethxbt.getJSONArray("c");

	if(orig.equals("XBT") && dest.equals("USD")){
	    return cXbtusd.getString(0);
	}
	if(orig.equals("ETH") && dest.equals("XBT")){
	    return cEthxbt.getString(0);
	}
	if(orig.equals("ETH") && dest.equals("USD")){
	    return cEthusd.getString(0);
	}
	return null;
    }
    public static void main(String[] args) throws Exception
    {
	System.out.println(getPrice("ETH", "USD"));
    }
}
