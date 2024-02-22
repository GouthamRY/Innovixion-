import requests 
from bs4 import BeautifulSoup
import pandas as pd
def scrape_website(url):
    response=requests.get(url)
    s=BeautifulSoup(response.content,"html.parser")
    results=s.find(id="ResultsContainer")
    elements=results.find_all("h2",string=lambda text: "python" in text.lower())
    titles=[i.text.strip() for i in elements]
    df=pd.DataFrame(titles,columns=['Titles'])
    file_format=input("Enter the file format (excel/csv):").lower()
    if file_format=='excel':
        name=input("Enter the file name:")
        df.to_excel(f"{name}.xlsx",index=True)
        print("Data is stored in Excel file successfully")
    elif file_format=='csv':
        name=input("Enter the file name:")
        df.to_csv(f"{name}.csv",index=True)
        print("Data stored in CSV file successfully")
    else:
        print("Invalid File Format..")
#Example usage of scrape website
url="https://realpython.github.io/fake-jobs"
#For user input>>
#url=input("Enter URL:")
scrape_website(url)