import pandas as pd
from bs4 import BeautifulSoup
import requests

brighteststars= "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(brighteststars)
print(page)
templist = []
name = []
distance = []
mass = []
radius = []

for i in range (1,len(templist)):
    name.append(templist[i][1])
    distance.append(templist[i][3])
    mass.append(templist[i][5])
    radius.append(templist[i][6])

dataframe = pd.DataFrame(list(zip(starnames)))
dataframe.to_csv("stars.csv")