#import section
import requests
import pandas
from bs4 import BeautifulSoup

#requesting website response "zigwheels.com"
response=requests.get('https://www.zigwheels.com/newcars/Tata')
#print(response)

cars=BeautifulSoup(response.content,'html.parser')
#print(cars)

#car names
names=cars.find_all('h3',class_='lnk-hvr fnt-16 b block of-hid h-height ml-0 mb-0-imp')
name=[]
for i in names[0:13]:
    x=i.get_text()
    name.append(x)
#print(name)

#car features
features=cars.find_all('div',class_='clr-pry fnt-12 pb-10 h-height lh-18 of-hid')
feature=[]
for i in features[0:13]:
    x=i.get_text()
    feature.append(x)
#print(feature)

#car prices
prices=cars.find_all('div',class_='clr-bl')
price=[]
for i in prices[0:13]:
    x=i.get_text()
    price.append(x)
#print(price)


#car images
images=cars.find_all('img',class_='i-b c-p')
image=[]
for i in images[0:13]:
    x=i['src']
    image.append(x)
#print(image)


#car ratings
ratings=cars.find_all('div',class_='r-w fnt-12 rel i-b rt-g')
rating=[]
for i in ratings[0:13]:
    x=i.get_text()
    rating.append(x)
#print(rating)

#arranging in structured format csv format 
data={'names':pandas.Series(name),
      'images':pandas.Series(image),
      'features':pandas.Series(feature),
      'ratings':pandas.Series(rating),
      'prices':pandas.Series(price)
      }
tata=pandas.DataFrame(data)
tata.to_csv('tata cars_data.csv')







