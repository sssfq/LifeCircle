# Inputs is NJCF_200.csv
# Output is Duration attribution

import api_request
import shapefile
import pandas as pd
import numpy as np
import coordinate_transfer as ct
# import xlrd

# wb = xlrd.open_workbook('南京鼓楼小区.xlsx')
# sh = wb.sheet_by_name('数据')
file = 'NJCF_200.csv'
njcommunity = pd.read_csv(file)

ID = njcommunity['ID'].astype(int)
origin_longitude_wgs84 = njcommunity['POINT_X'].astype(float)
origin_latitude_wgs84 = njcommunity['POINT_Y'].astype(float)


api = api_request.BDAPI()

hundredmeter2lati = 0.000899
hundredmeter2long = 0.001141

for i in range(204,len(ID)):#range(len(ID)):#range(1) #range(i) --> 0 ~ i-1 #len(name)=932

    [origin_long,origin_lati] = ct.wgs84_to_bd09(origin_longitude_wgs84[i],origin_latitude_wgs84[i])
    print(ID[i])
    # create the table of search points
    destin_latitude = origin_lati + np.arange(-10,11)*hundredmeter2lati
    destin_longitude = origin_long + np.arange(-10,11)*hundredmeter2long
    # print(destin_latitude[0],destin_longitude[0])

    data_address = './NJCF_200_bdak_shp_wgs84/NJCF_200_'+str(i)+'.shp'
    file = shapefile.Writer(data_address)#,shapeType=1,autoBalance=1
    file.field('ID','N')
    # file.field('Distance','N')
    file.field('Duration','N')

    j = 0
    for destin_long in destin_longitude:
        # print(x)
        for destin_lati in destin_latitude: 
            try:
                j += 1
                print(j)
                distance, duration = api.data_request(origin_lati,origin_long,destin_lati,destin_long)
                # print(duration)
            
            except:
                print('No.%i group occurs Error\n'%i+'origin:'+api.origin+'\n' +'destination:'+api.destin+'\n')

            # output needs wgs84 coordinate
            [destin_long_wgs84,destin_lati_wgs84] = ct.bd09_to_wgs84(destin_long,destin_lati)

            # adding geometry
            file.point(destin_long_wgs84,destin_lati_wgs84)
            # creating attributes
            file.record(ID[i],duration)

    file.close()