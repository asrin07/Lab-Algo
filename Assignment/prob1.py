import gmplot #for google map gui
import requests
import pprint

def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1
        while low <= high and array[low] <= pivot:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high
      
def quick_sort(array, start, end):
    if start >= end:
        return
    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)

############## to create map markers for hubs ##############################
# Create the map plotter:
apikey = "AIzaSyDpGnTkENjkuksN0QzkOG7LzgowI0kavHI" # (your API key here)

gmap = gmplot.GoogleMapPlotter(3.112585695236, 101.6397000538541, 10,apikey=apikey)#untuk spawn kita masuk awal awal kat mana
gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"
gmap.marker(3.0319924887507144,101.37344116244806, color='cornflowerblue', title="Port Klang")
gmap.marker(3.112924170027219,101.63982650389863, color='red', title="Petaling Jaya")
gmap.marker(3.265154613796736,101.68024844550233, color='orange', title="Batu Caves")
gmap.marker(2.9441205329488325,101.7901521759029, color='green', title="Kajang")
gmap.marker(3.2127230893650065,101.57467295692778, color='yellow', title="Sungai Buloh")
gmap.draw("C:\\Users\\asrin\\Documents\\Lab-Algo\\Assignment\\hubs.html")

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
            print("customer "+str(i)+" distance from origin straight to destination: "+b["distance"]["text"])
            customerDistances[i]=b["distance"]["value"]

############ To calculate distance from origin to hub and hub to destination #########################
packagedTravelled1=[0]*len(hub_lat)#this array is used to be sorted
packagedTravelled2=[0]*len(hub_lat)
packagedTravelled3=[0]*len(hub_lat)
hubIndex1=[0]*len(hub_lat)#use to find the index of the long and lat of hub shortest based on 0th index of the above array
hubIndex2=[0]*len(hub_lat)
hubIndex3=[0]*len(hub_lat)
hubs=["Port Klang","Petaling Jaya","Batu Caves","Kajang","Sungai Buloh"]

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
            packagedTravelled1[j]=float(originToHub)+float(hubToDestination)
            hubIndex1[j]=packagedTravelled1[j]
            print("total distance 1: ",packagedTravelled1[j]," meters")
        elif i==1:
            packagedTravelled2[j]=float(originToHub)+float(hubToDestination)
            hubIndex2[j]=packagedTravelled2[j]
            print("total distance 2: ",packagedTravelled2[j]," meters")
        elif i==2:
            packagedTravelled3[j]=float(originToHub)+float(hubToDestination)
            hubIndex3[j]=packagedTravelled3[j]
            print("total distance 3: ",packagedTravelled3[j]," meters")


quick_sort(packagedTravelled1, 0, len(packagedTravelled1) - 1)
hub1LatAndLong=hubIndex1.index(packagedTravelled1[0])
print("Customer 1's shortest distance: ",packagedTravelled1[0],"-->",hubs[hub1LatAndLong])

quick_sort(packagedTravelled2, 0, len(packagedTravelled2) - 1)
hub2LatAndLong=hubIndex2.index(packagedTravelled2[0])
print("Customer 2's shortest distance: ",packagedTravelled2[0],"-->",hubs[hub2LatAndLong])

quick_sort(packagedTravelled3, 0, len(packagedTravelled3) - 1)
hub3LatAndLong=hubIndex3.index(packagedTravelled3[0])
print("Customer 3's shortest distance: ",packagedTravelled3[0],"-->",hubs[hub3LatAndLong])

############## To draw line #########################
colour=["cornflowerblue","red","orange","green","yellow"]
gmap = gmplot.GoogleMapPlotter(37.766956, -122.438481, 13, apikey=apikey)
for i in range(len(customer_ori_lat)):
    if i==0:
        hubLat=hub1LatAndLong#hub paling dekat untuk custmer 1 
        hubLong=hub1LatAndLong
    elif i==1:
        hubLat=hub2LatAndLong
        hubLong=hub2LatAndLong
    else:
        hubLat=hub3LatAndLong
        hubLong=hub3LatAndLong
    
    gmap.directions(
    (customer_ori_lat[i],customer_ori_long[i]),
    (customer_dest_lat[i],customer_dest_long[i]),
    waypoints=[(customer_ori_lat[i],customer_ori_long[i]),(hub_lat[hubLat],hub_long[hubLong]),(customer_dest_lat[i],customer_dest_long[i])]
    )

    gmap.marker(hub_lat[hubLat],hub_long[hubLong],color=colour[hubLat],title=hubs[hubLat])
    
gmap.draw('maps.html')