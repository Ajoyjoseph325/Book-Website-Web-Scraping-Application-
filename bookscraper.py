import requests
import pandas as pd
from bs4 import BeautifulSoup
  

url = "https://books.toscrape.com/"
booksdict = {'book_title':[],'book_price':[]}


res = requests.get(url)


soup = BeautifulSoup(res.content, "html.parser")


allbooks = soup.find_all("li",class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")




for book in allbooks:
    title_text = book.find('img')
    if title_text:
        bt = title_text.get('alt')

    bookprice = book.find("p","price_color")



    if bookprice:
        bp = bookprice.get_text(strip=True)
    print(f"{bt}|{bp}")
    booksdict['book_title'].append(bt)
    booksdict['book_price'].append(bp)

bookdf = pd.DataFrame(booksdict)

bookdf.to_csv('books.csv', index=False)
print('testing....')


    

