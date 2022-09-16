import requests
from bs4 import BeautifulSoup
import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def create_dataframe(results):
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
        if len(row) > 2: # To prevent a value error from the total times row
            mydata.loc[mydatalength] = row
        #mydata.append(row)
    return mydata


#name = str(input("How do you want to save the file? (e.g. C:/Users/Woute/Downloads/AF_Cut.xlsx)?: "))
URL = "https://mkwrs.com/mk7/"
page = requests.get(URL, verify=False)

soup = BeautifulSoup(page.content, "html.parser")
tables = soup.find_all("table")  # returns a list of tables

mydata_noglitch = create_dataframe(tables[0])
mydata_glitch = create_dataframe(tables[1])

mydata_noglitch.to_excel("C:/Users/WouterMuldersinin/Documents/inwerkopdracht1/noglitchwrs.xlsx", index = False)
mydata_glitch.to_excel("C:/Users/WouterMuldersinin/Documents/inwerkopdracht1/glitchwrs.xlsx", index = False)