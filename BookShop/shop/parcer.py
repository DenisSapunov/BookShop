import requests
from bs4 import BeautifulSoup as Bs
from slugify import slugify
import json
from shop.models import Book, Category, Author

r = requests.get('https://chitatel.by/catalog/book/467015')
html = Bs(r.content, 'html.parser')
one_category_hrefs = html.find('h1')
print(one_category_hrefs.text)

# Book.objects.create(name=, description=, price=, pub_year=, image=, language=,num_pages=, slug=slugify())



# one_category_hrefs = html.findAll(class_='frame')
#
# for book in one_category_hrefs:
#     book_hrefs = book.select('.product-name__link')
#     for i in book_hrefs:
#         with open('one_category_books.txt', 'a') as file:
#             file.writelines(i.attrs['href']+'\n')


# with open('one_category_books.txt', 'r') as file:



# https://chitatel.by/catalog/book/467015
# https://chitatel.by/catalog/book/33982
# https://chitatel.by/catalog/book/525226
# https://chitatel.by/catalog/book/264642
# https://chitatel.by/catalog/book/1741821
# https://chitatel.by/catalog/book/27566
# https://chitatel.by/catalog/book/546299
# https://chitatel.by/catalog/book/489149
# https://chitatel.by/catalog/book/1214348
# https://chitatel.by/catalog/book/378865
# https://chitatel.by/catalog/book/1434904
# https://chitatel.by/catalog/book/525030
# https://chitatel.by/catalog/book/1538541
# https://chitatel.by/catalog/book/901436
# https://chitatel.by/catalog/book/412614
# https://chitatel.by/catalog/book/474072
# https://chitatel.by/catalog/book/1191761
# https://chitatel.by/catalog/book/1273562
# https://chitatel.by/catalog/book/307819
# https://chitatel.by/catalog/book/1221982
# https://chitatel.by/catalog/book/574545
# https://chitatel.by/catalog/book/345013
# https://chitatel.by/catalog/book/468413
# https://chitatel.by/catalog/book/360420
# https://chitatel.by/catalog/book/1410380
# https://chitatel.by/catalog/book/76514
# https://chitatel.by/catalog/book/207757
# https://chitatel.by/catalog/book/259653
# https://chitatel.by/catalog/book/395635
# https://chitatel.by/catalog/book/420325
# https://chitatel.by/catalog/book/595803
# https://chitatel.by/catalog/book/265158
# https://chitatel.by/catalog/book/314910
# https://chitatel.by/catalog/book/326747
# https://chitatel.by/catalog/book/42300
# https://chitatel.by/catalog/book/46092
# https://chitatel.by/catalog/book/1544912
# https://chitatel.by/catalog/book/540991
# https://chitatel.by/catalog/book/568484
# https://chitatel.by/catalog/book/515918
# https://chitatel.by/catalog/book/1191451
