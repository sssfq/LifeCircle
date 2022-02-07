import requests,urllib
import json
import shapefile

## request api for distance info
bdak = 'zvcAtSx9oQAw1qFyW1QGz0CGVbDwLBjV' #ex'zvcAtSx9oQAw1qFyW1QGz0CGVbDwLBjV'
origin_lati = 32.03458655
origin_long = 118.7418109
destin_lati = 32.03658655
destin_long = 118.752562
origin = "%f"%origin_lati +","+"%f"%origin_long
destin = "%f"%destin_lati +","+"%f"%destin_long
vehicle = 'walking'
url_head = 'https://api.map.baidu.com/directionlite/v1/'

url = url_head + vehicle + '?origin='+origin + '&destination='+destin + '&ak='+bdak

jsondata = requests.get(url)
read_json = json.loads(jsondata.text)
print(read_json)
distance = read_json['result']['routes'][0]['distance']  # unit: meter
duration = read_json['result']['routes'][0]['duration']  # unit: second

print(distance,duration)
print
## convert to .shp file

data_address = './test_point_20220206.shp'
file = shapefile.Writer(data_address)#,shapeType=1,autoBalance=1
file.field('Distance','N')
file.field('Duration','N')
# adding geometry
file.point(origin_lati,origin_long)
# creating attributes
file.record(distance,duration)

file.point(destin_lati,destin_lati)
file.record(duration,distance)

file.close()