import gmplot #for google map gui
from geopy import distance # for shortest distance on earth
# import googlemaps #to calculate distance on route
import requests
import pprint

############## to create map markers for hubs ##############################
# Create the map plotter:
apikey = 'AIzaSyDpGnTkENjkuksN0QzkOG7LzgowI0kavHI' # (your API key here)
gmap = gmplot.GoogleMapPlotter(3.112585695236, 101.6397000538541, 10,apikey=apikey)#untuk spawn kita masuk awal awal kat mana

# hub_lat, hub_long = zip(#zip is to convert touples to list and create a list of touples
#     *[
#         (3.0319924887507144,101.37344116244806), (3.112924170027219,101.63982650389863), 
#         (3.265154613796736,101.68024844550233), (2.9441205329488325,101.7901521759029),
#         (3.2127230893650065,101.57467295692778)
#     ]
# )
gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"
# gmap.scatter(hub_lat, hub_long,color='cornflowerblue', title="Hubs")
gmap.marker(3.0319924887507144,101.37344116244806, color='cornflowerblue', title="Port Klang")
gmap.marker(3.112924170027219,101.63982650389863, color='red', title="Petaling Jaya")
gmap.marker(3.265154613796736,101.68024844550233, color='orange', title="Batu Caves")
gmap.marker(2.9441205329488325,101.7901521759029, color='green', title="Kajang")
gmap.marker(3.2127230893650065,101.57467295692778, color='yellow', title="Sungai Buloh")

gmap.draw("C:\\Users\\USER\\OneDrive - Universiti Malaya\\Desktop\\Sem 4\\ALGO\\Algo assignment\\hubs.html")

############# To calculate distance customer origin and destination ##############################
customer_ori_lat,customer_ori_long= zip(#zip is to convert touples to list and create a list of touples
    *[
        (3.3615395462207878,101.56318183511695), (3.049398375759954,101.58546611160301), 
        (3.141855957281073,101.76158583424586)
    ]
)
customer_dest_lat,customer_dest_long = zip(#zip is to convert touples to list and create a list of touples
    *[
        (3.1000170516638885,101.53071480907951), (3.227994355250716,101.42730357605375), 
        (2.9188704151716256,101.65251821655471)
    ]
)
hub_lat, hub_long = zip(#zip is to convert touples to list and create a list of touples
    *[
        (3.0319924887507144,101.37344116244806), (3.112924170027219,101.63982650389863), 
        (3.265154613796736,101.68024844550233), (2.9441205329488325,101.7901521759029),
        (3.2127230893650065,101.57467295692778)
    ]
)
customerDistances=[0]*len(list(customer_ori_lat))

for i in range(len(list(customer_ori_lat))):
    customer_ori = str(customer_ori_lat[i])+","+str(customer_ori_long[i])
    customer_dest = str(customer_dest_lat[i])+","+str(customer_dest_long[i])    
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&"+"origins="+customer_ori+"&destinations="+customer_dest+"&key="+apikey
    output = requests.get(url).json()
    for a in output["rows"]:
        for b in a["elements"]:
            print("customer "+str(i)+": "+b["distance"]["text"])
            customerDistances[i]=b["distance"]["value"]

print(customerDistances)

############ To calculate distance from origin to hub and hub to destination #########################
packagedTravelled1=[0]*len(hub_lat)
packagedTravelled2=[0]*len(hub_lat)
packagedTravelled3=[0]*len(hub_lat)

for i in range(len(customer_ori_lat)):
    originToHub=0
    hubToDestination=0
    for j in range(len(hub_lat)):
        customer_ori = str(customer_ori_lat[i])+","+str(customer_ori_long[i])
        hub_destination = str(hub_lat[j])+","+str(hub_long[j])
        url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&"+"origins="+customer_ori+"&destinations="+hub_destination+"&key="+apikey
        output = requests.get(url).json()
        for a in output["rows"]:
            for b in a["elements"]:
                originToHub=b["distance"]["value"]

        hub_destination = str(hub_lat[j])+","+str(hub_long[j])
        customer_dest = str(customer_dest_lat[i])+","+str(customer_dest_long[i])
        url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&"+"origins="+customer_dest+"&destinations="+hub_destination+"&key="+apikey
        output = requests.get(url).json()
        for a in output["rows"]:
            for b in a["elements"]:
                hubToDestination=b["distance"]["value"]

        if i==0:
            packagedTravelled1[i]=float(originToHub)+float(hubToDestination)
            print("total distance 1: ",packagedTravelled1[i]," meters")
        elif i==1:
            packagedTravelled2[i]=float(originToHub)+float(hubToDestination)
            print("total distance 2: ",packagedTravelled2[i]," meters")
        elif i==2:
            packagedTravelled3[i]=float(originToHub)+float(hubToDestination)
            print("total distance 3: ",packagedTravelled3[i]," meters")
