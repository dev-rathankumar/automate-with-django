from bs4 import BeautifulSoup
import requests

week_52_range = 133.77 - 199.62


def scrape_stock_data(symbol, exchange):
    if exchange == 'NASDAQ':
        url = f"https://finance.yahoo.com/quote/{symbol}"
    elif exchange == 'NSE':
        symbol = symbol+'.NS'
        url = f'https://finance.yahoo.com/quote/{symbol}?p={symbol}&.tsrc=fin-srch'

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(url, headers=headers)
    
    soup = BeautifulSoup(response.content, 'html.parser')
    current_price = soup.find(f"fin-streamer", {"data-symbol": {symbol}})['value']
    previous_close = soup.find('td', {'data-test': 'PREV_CLOSE-value'}).text
    week_52_range = soup.find('td', {'data-test': 'FIFTY_TWO_WK_RANGE-value'}).text
    week_52_low, week_52_high = week_52_range.split(' - ')

    print("Week 52 Low:", week_52_low)
    print("Week 52 High:", week_52_high)



scrape_stock_data('INFY', 'NSE')