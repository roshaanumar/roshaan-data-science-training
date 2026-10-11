import requests
import pandas as pd
baseurl = "https://rickandmortyapi.com/api/"
endpoint = "character"

def main_request(baseurl, endpoint, x ):
    r = requests.get(baseurl + endpoint + f"?page={x}")
    return r.json()

def get_pages(response):
    return response["info"]["pages"]

def parse_json(response):
    charlist = []
    for item in response["results"]:
        char = {
            "Id" :item["id"],
            "name" :item["name"], 
            "no_ep" :len(item["episode"]),
        }
        charlist.append(char)
    return charlist   

data = main_request(baseurl , endpoint, 3)
mainlist = []
for x in range(1, get_pages(data)+1):
    print(x)
    mainlist.extend(parse_json(main_request(baseurl, endpoint, x )))
print(len(mainlist))
data_frame = pd.DataFrame(mainlist)
#print(data_frame.head(), data_frame.tail())
data_frame.to_csv("charlist5.csv", index=False)



#Practice:
headers = {
    "User-Agent": "Mozilla/5.0"
}

def main_request(baseurl):
    r = rs.get(baseurl, headers=headers)
    return r.text
print(main_request(baseurl))