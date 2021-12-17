import requests
from bs4 import BeautifulSoup
import pandas as pd

name = str(input("How do you want to save the file? (e.g. C:/Users/Woute/Downloads/AF_Cut.xlsx)?: "))
URL = "https://www.mariokart64.com/mk7/afc.php?cfilter=&full=on"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find("table", attrs={"class": "c"})
results_data = results.find_all("tr")


# Obtain every title of columns with tag <th>
headers = []
for i in results.find_all('th'):
 title = i.text
 headers.append(title)
 


# Create a dataframe
mydata = pd.DataFrame(columns = headers)

for i in range(1,len(results_data)):
    row = [] #row with player info
    for j in results_data[i].find_all('td'):
        row.append(j.text)
    mydatalength = len(mydata)
    mydata.loc[mydatalength] = row
    #mydata.append(row)
        
mydata = mydata.drop("Info", axis = 1)    
mydata = mydata.drop("Proof", axis = 1)
mydata['Rank'] = pd.to_numeric(mydata['Rank'],errors='coerce')
mydata['Score'] = pd.to_numeric(mydata['Score'],errors='coerce')
mydata['Change'] = pd.to_numeric(mydata['Change'],errors='coerce')


AF_cut = mydata[mydata['Change'] < 0]

AF_cut.to_excel(name, index = False)

