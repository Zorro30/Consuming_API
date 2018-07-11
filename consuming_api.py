import requests

parameters = {"lat":40.71, "lon": -74}

response = requests.get("http://api.open-notify.org/astros.json",params=parameters)

#print (response.content.decode("utf-8"))
data = (response.json())

#since the response has a dictionary in a list and that list is in a dictionary. So to get the exact name below code is written. 
value = (data['people'])

for i in value:
    print ("Name: {}".format(i['name']))

print ("*"*75)

print ("Number of astronauts at ISS: {}" .format(data["number"]))