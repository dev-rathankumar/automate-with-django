from bs4 import BeautifulSoup
import requests


def scrape_stock_data(symbol, exchange):
    if exchange == 'NASDAQ':
        url = f"https://finance.yahoo.com/quote/{symbol}"
    elif exchange == 'NSE':
        symbol = symbol+'.NS'
        url = f'https://finance.yahoo.com/quote/{symbol}?p={symbol}&.tsrc=fin-srch'

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            current_price = soup.find(f"fin-streamer", {"data-symbol": {symbol}})['value']
            price_changed = soup.find(f"fin-streamer", {"data-symbol": {symbol}, "data-test": "qsp-price-change"}).span.text
            percentage_changed = soup.find(f"fin-streamer", {"data-symbol": {symbol}, "data-field": "regularMarketChangePercent"}).span.text
            previous_close = soup.find('td', {'data-test': 'PREV_CLOSE-value'}).text
            week_52_range = soup.find('td', {'data-test': 'FIFTY_TWO_WK_RANGE-value'}).text
            week_52_low, week_52_high = week_52_range.split(' - ')
            market_cap = soup.find('td', {'data-test': 'MARKET_CAP-value'}).text
            pe_ratio = soup.find('td', {'data-test': 'PE_RATIO-value'}).text
            dividend_yield = soup.find('td', {'data-test': 'DIVIDEND_AND_YIELD-value'}).text

            stock_response = {
                'current_price': current_price,
                'previous_close': previous_close,
                'price_changed': price_changed,
                'percentage_changed': percentage_changed,
                'week_52_low': week_52_low,
                'week_52_high': week_52_high,
                'market_cap': market_cap,
                'pe_ratio': pe_ratio,
                'dividend_yield': dividend_yield,
            }
            return stock_response
        
    except Exception as e:
        # print(f'Error scraping the data: {e}')
        return None