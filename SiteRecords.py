import requests
from bs4 import BeautifulSoup
import pandas as pd

#Ask for the required user input
name = str(input("How and where do you want to save the file? (e.g. C:/Users/Woute/Downloads/SRs.xlsx)?: "))
year = int(input("What year is it?: "))
month = int(input("What month is it? (1-12): "))

#The page contains both glitch and no-glitch tables
URL = "https://www.mariokart64.com/mk7/wr.php"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = [soup.find("table", attrs={"class": "c"}),soup.find("table", attrs={"class": "k"})]

NewSRs = [0,0]
for w in range(0,len(results)):
    results_data = results[w].find_all("tr")
    
    
    # Obtain every title of columns with tag <th>
    headers = []
    for i in results[w].find_all('th'):
     title = i.text
     headers.append(title)
     
    # Create a dataframe
    mydata = pd.DataFrame(columns = headers)
    
    for i in range(1,len(results_data)):
        row = [] 
        for j in results_data[i].find_all('td'):
            row.append(j.text)
        mydatalength = len(mydata)
        mydata.loc[mydatalength] = row
        mydata.append(row)
        
    mydata = mydata.drop("Chart", axis = 1)    
    mydata = mydata.drop("Info", axis = 1)
    mydata = mydata[0:(len(mydata)-1)] #drop total times row
    
    dates = mydata["Date"]
    tf = []
    for i in range(0,len(dates)):
        years = dates[i][0:4]
        months = dates[i][5:7]
        tf.append(int(years) == year and int(months) == month)
        
    NewSRs[w] = mydata[tf]
separator = ["GLITCH","GLITCH","GLITCH","GLITCH","GLITCH"]
NewSRs[0].loc[len(NewSRs[0])] = separator
pieces = (NewSRs[0],NewSRs[1])
realSRs = pd.concat(pieces, ignore_index = True)

realSRs.to_excel(name, index = False)
