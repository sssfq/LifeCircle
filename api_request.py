import requests,urllib
import json
class BDAPI():
    def __init__(self,bdak='zvcAtSx9oQAw1qFyW1QGz0CGVbDwLBjV',vehicle='walking',
                 url_head='https://api.map.baidu.com/directionlite/v1/'
                ):
        self.bdak = bdak
        self.vehicle = vehicle
        self.url_head = url_head

    def data_request(self,origin_lati,origin_long,destin_lati,destin_long):
        self.origin_lati = origin_lati
        self.origin_long = origin_long
        self.destin_lati = destin_lati
        self.destin_long = destin_long
        self.origin = "%f"%origin_lati +","+"%f"%origin_long
        self.destin = "%f"%destin_lati +","+"%f"%destin_long

        self.origin = "%f"%origin_lati +","+"%f"%origin_long
        self.destin = "%f"%destin_lati +","+"%f"%destin_long

        self.url = self.url_head + self.vehicle + '?origin='+self.origin + '&destination='+self.destin + '&ak='+self.bdak

        jsondata = requests.get(self.url)
        read_json = json.loads(jsondata.text)
        distance = read_json['result']['routes'][0]['distance']  # unit: meter
        duration = read_json['result']['routes'][0]['duration']  # unit: second

        return distance, duration

if __name__ == '__main__':
    hundredmeter2lati = 0.000899
    hundredmeter2long = 0.001141
    origin_lati = [32.102907]
    origin_long = [118.790444]
    destin_lati = [32.093917000000005]
    destin_long = [118.779034]

    api = BDAPI()
    distance=[]
    duration=[]

    for i in range(1):
        try:
            dist, dura = api.data_request(origin_lati[i],origin_long[i],destin_lati[i],destin_long[i])
            print(10086)
            distance.append(dist)
            duration.append(dura)
        except:
            print('No.%i group occurs Error\n'%i+'origin:'+api.origin+'\n' +'destination:'+api.destin+'\n')

    print(distance)
    print(duration)

