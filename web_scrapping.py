from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_India'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')

#print(soup)
soup.find_all('table')
soup.find('table')
soup.find_all('table')[1]
soup.find_all('table')[0]
soup.find('th')
table = soup.find_all('table')[0]
world_tables = table.find_all('th')
print(world_tables)
soup.find_all('th')[0:5]
world_titles = soup.find_all('th')[0:5]
print(world_titles)

world_table_titles = [titles.text.strip() for titles in world_titles]

#print(world_table_titles)
df = pd.DataFrame(columns = world_table_titles)

all_data = table.find_all('tr')

for i in all_data[1:]:
    data = i.find_all('td')
    individual_rows = [d.text.strip() for d in data]

    length = len(df)
    df.loc[length] = individual_rows


df.to_csv(r'C:\Users\Shamy\Desktop\DataAnalytics\TopIndCompanies.csv', index = False)