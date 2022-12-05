from zillow import Zillow
from gform import Gform


z_url = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.61529005957031%2C%22east%22%3A-122.25136794042969%2C%22south%22%3A37.6552491296774%2C%22north%22%3A37.89513918006007%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Accept-Language": "en-PH,en-US;q=0.9,en;q=0.8",
}
g_url = "https://forms.gle/XM7VxeDokSHk7aRM6"
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"

z_bot = Zillow(url=z_url, headers=headers)
addresses_list = z_bot.find_addresses()
prices_list = z_bot.find_prices()
links_list = z_bot.find_links()
input_list = zip(addresses_list,prices_list,links_list) #to combine all three lists

g_bot = Gform(path=CHROME_DRIVER_PATH)
g_bot.input_results(url=g_url, input_list=input_list)





