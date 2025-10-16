from bs4 import BeautifulSoup
import requests
import csv

source=requests.get('https://quotes.toscrape.com/').text

soup=BeautifulSoup(source,'lxml')

csv_file=open('web_scrpe.csv','w')
csv_write=csv.writer(csv_file)
csv_write.writerow(['quote','author'])

for div in soup.find_all('div',class_='quote'):
    quote=div.find('span',class_='text').text
    author=div.find('small',class_='author').text
    print()
    print(quote)
    print(author)
    print()
    csv_write.writerow([quote,author])


csv_file.close()
