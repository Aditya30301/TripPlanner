#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json
import folium
import datetime



checkin=str(datetime.date.today())
checkout=str(datetime.date.today()+datetime.timedelta(days=5))
adults=str(2)
children=str(0)
infants=str(0)

name1='Paris'
name2='Hyderabad'

print("--------------------------------------------------------")
print("*hold on tight fetching your Airport Details*")

#This API is used to fetch the details of the airbnb available at the best price mentioned in the city

url = "https://airbnb13.p.rapidapi.com/search-location"
querystring = {"location":name1,"checkin":checkin,"checkout":checkout,"adults":adults,"children":children,"infants":infants,"page":"1"}
headers = {
    'X-RapidAPI-Host': 'airbnb13.p.rapidapi.com',
    'X-RapidAPI-Key': '8f69f696camsh068afae434deb09p16f3e0jsnf1814b39d70e'
}
response = requests.request("GET", url, headers=headers, params=querystring)
data7=json.loads(response.text)
data=data7["results"][0]["price"]["rate"]



#This API fetches the details of the best Possible flight route to the Mentioned city and then the trip back to home town

url1 = "https://priceline-com-provider.p.rapidapi.com/v1/flights/locations"


querystring1 = {"name":name1}
querystring2= {"name":name2}


headers = {
	"X-RapidAPI-Host": "priceline-com-provider.p.rapidapi.com",
	"X-RapidAPI-Key": "ec4640b2e6msh94b71fd4760b657p142badjsnc3839d3a7a09"
}

response1 = requests.request("GET", url1, headers=headers, params=querystring1)
response2 = requests.request("GET", url1, headers=headers, params=querystring2)
data1=json.loads(response1.text)
data2=json.loads(response2.text)

data1=data1[0]["id"]
data2=data2[0]["id"]
print("--------------------------------------------------------")
print("----------Round Trip Details--------")
print("---Journey Starts from----")
print("Departure Airport-"+str(data1))
print("Arrival Airport-"+str(data2))
print("----Return Journey Starts from----")
print("Departure Airport-"+str(data2))
print("Arrival Airport-"+str(data1))
data3=str(data1+","+data2)
data4=str(data2+","+data1)
print("--------------------------------------------------------")
print("*Hold on tight fetching your Flight and Hotel Details*")



#This API fetches the airport code of the city and finds the nearest airport to the mentioned city
url2 = "https://priceline-com-provider.p.rapidapi.com/v2/flight/roundTrip"

querystring3 = {"departure_date":checkin+","+checkout,"adults":"1","sid":"iSiX639",
               "origin_airport_code":data3,"destination_airport_code":data4}

headers = {
	"X-RapidAPI-Host": "priceline-com-provider.p.rapidapi.com",
    
	"X-RapidAPI-Key": "ec4640b2e6msh94b71fd4760b657p142badjsnc3839d3a7a09"
}

response3 = requests.request("GET", url2, headers=headers, params=querystring3)
data6=json.loads(response3.text)
#print(data5)

data5=data6["getAirFlightRoundTrip"]["results"]["air_search_rsp"]["total_trip_summary"]["minTotalFareWithTaxesAndFees"]

total=int(data)+int(data5)

print("Airbnb link-"+str(data7["results"][0]["deeplink"]))
print("Airbnb Name-"+str(data7["results"][0]["name"]))
print("Airbnb Name-"+str(data7["results"][0]["address"]))
print("Airbnb Name-"+str(data7["results"][0]["rating"]))

print("Airline name-"+str(data6["getAirFlightRoundTrip"]["results"]["air_search_rsp"]["airline"][0]["name"]))
print("No of Stops-"+str(data6["getAirFlightRoundTrip"]["results"]["air_search_rsp"]["total_trip_summary"]["stop"][0]["numberOfStops"]))
print("stops-")
i=0
while i<int(data6["getAirFlightRoundTrip"]["results"]["air_search_rsp"]["total_trip_summary"]["stop"][0]["numberOfStops"]):
    print(data6["getAirFlightRoundTrip"]["results"]["air_search_rsp"]["total_trip_summary"]["layoverAirport"][i]["name"])
    i=i+1


print("----------------Cost Break up-------------")
print("Total cost of AirTravel and Stay-"+str(total))
print("Round Trip flight cost (inc. of all taxes)-" +str(data5)) 

print("Best AirBNB price (inc. of Taxes)-"+str(data))

print("------------------------Location of Your Hotel--------------------------------")

mymap=folium.Map(
    location=[float(data7["results"][0]["lat"]),int(data7["results"][0]["lng"])],
    zoom_start=12
    )
folium.Marker(
    location=[float(data7["results"][0]["lat"]),int(data7["results"][0]["lng"])],
    popup="Your Hotel",
    tooltip="Your Hotel"
).add_to(mymap)

mymap


# In[ ]:





# In[ ]:




