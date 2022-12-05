A capstone project for data entry automation using Beautiful Soup, Selenium Webdriver, and Object
Oriented Programming.

Using beautiful soup, property listings were scraped from the zillow website to get their addresses,
prices, and links to the listings. The lists were combined into one using `zip()` function and were
passed as data to google form for input.

Using selenium webdriver, the above data were inputted one by one to the address, price, and link fields
of the Google form link. An Excel file can be created out of the responses.

Notable codes:

Use this instead of if-else statement to shorten the code.
```
if 'http' not in href:
    links.append(f"https://www.zillow.com{href}")
links.append(href)
```


Use this instead of creating a second list in order to remove duplicates inside the list.
```
list(dict.fromkeys(links))
```

Use zip function to combine the lists then iterate using for loop method.
```
input_list = zip(addresses_list,prices_list,links_list)
for (address, price, link) in input_list:
```

All input fields have the same class so you can just use find_elements method then specify the 
proper field using their indexes.
```
input_fields = self.driver.find_elements(By.CSS_SELECTOR, 'input[class="whsOnd zHQkBf"]')
input_fields[0].send_keys(address)
input_fields[1].send_keys(price)
input_fields[2].send_keys(link)
```