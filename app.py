import requests
import json

country_name = input("Input full country's name:")

url =  f"https://restcountries.com/v3.1/name/{country_name}"
url2 = "https://catfact.ninja/fact"
url3 = "https://zenquotes.io/api/random"
responce = requests.get(url)
responce_facts1= requests.get(url2)
responce_facts2= requests.get(url3)

content_dict = responce.json()
content_dict2 = responce_facts1.json()
content_dict3 = responce_facts2.json()

population_num= content_dict[0]["population"]
print (f"""
       Official name: {content_dict[0]["name"]["official"]}
       Capital: {content_dict[0]["capital"][0]}
       Flag: {content_dict[0]["flag"]}                                                    
       Population: {population_num:,}                                                     
       Location: {content_dict[0]["latlng"][0]}, {content_dict[0]["latlng"][1]}
"""                                                                                                          
                                                            )
print (f"""
       ==FUN FACTS==
Fact 1: {content_dict2["fact"]}
Fact 2: {content_dict3[0]["q"]}
""")