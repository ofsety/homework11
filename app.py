import requests
import json

country_name = input("Input full country's name:")

url =  f"https://restcountries.com/v3.1/name/{country_name}"
responce = requests.get(url)
content_dict = responce.json()
population_num= content_dict[0]["population"]
print (f"""
       Official name: {content_dict[0]["name"]["official"]}
       Capital: {content_dict[0]["capital"][0]}
       Flag: {content_dict[0]["flag"]}                                                    
       Population: {population_num:,}                                                     
       Location: {content_dict[0]["latlng"][0]}, {content_dict[0]["latlng"][1]}
"""                                                                                                          
                                                            )