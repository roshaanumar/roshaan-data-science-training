import requests as rs
import pandas as pd 
from bs4 import BeautifulSoup
baseurl = "https://www.bbc.com/news/articles/ckgvk9p2n7ko"
source = rs.get(baseurl).text
soup = BeautifulSoup(source , "lxml")
#print(soup.prettify())
article = soup.find("article")
#print(article.prettify()[:5000])
#headline = article.h1.text
#print(headline)
#start = article.find("p", class_="Paragraph-styles__ParagraphStyled-sc-ffb5f5ba-0 fqhmpl").text
#print(start)
#summaries = article.find_all("p", class_="Paragraph-styles__ParagraphStyled-sc-ffb5f5ba-0 fqhmpl")
#for summary in summaries:
   # print(summary.text)
#video_block = article.find("div", attrs={"data-component": "video-block"})#
#print(video_block.prettify())
#print(".mpd" in source)
blocks = article.find_all(attrs={"data-component": True})
for block in blocks:
    print(block["data-component"])