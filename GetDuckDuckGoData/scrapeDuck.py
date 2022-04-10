from bs4 import BeautifulSoup
import cloudscraper
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv

with open('../multi_fc_publicdata/all.tsv', 'r') as file:
    tsv_read = list(csv.reader(file, delimiter="\t"))
    
options = Options()
options.add_experimental_option("detach", True)
#options.headless = True
driver = webdriver.Chrome('/Users/shivasaravanan/Downloads/chromedriver', options=options)
try:
    with open('FullDuckResults.tsv', 'a', newline='\n') as tsvfile:
        writer = csv.writer(tsvfile, delimiter='\t')
        link = "https://duckduckgo.com/?q="
        for i in range(0, len(tsv_read)):
            line = tsv_read[i]
            index = str(line[0])
            snippets = [index]
            query = str(line[1]).strip()
            print(query.replace(" ", "+"))
            driver.get(link+query.replace(" ", "+"))
            page = driver.page_source
            soup = BeautifulSoup(page)
            new = soup.prettify()
            print(new)
            snippetDivs = soup.find_all("div", {"class": "js-result-snippet"})
            for j in range(0, min(10, len(snippetDivs))):
                snippets.append(snippetDivs[j].text)
            print(i)
            writer.writerow(snippets)
except Exception as e:
    print(e)
    #driver.quit()
#driver.quit()