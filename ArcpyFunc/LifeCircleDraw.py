import arcpy

arcpy.CheckOutExtension("3D")
arcpy.env.workspace = "./"

for i in range(213):
    print(i)
    # Duration point shapefile-->Duration TIN
    CreateTin_Out = './NJCF_200_TIN/NJCF_200_TIN_'+str(i) # /NJCF_200_TIN_0'
    CreateTin_InFeature = './NJCF_200_bdak_shp_wgs84/NJCF_200_'+str(i)+'.shp Duration masspoints'
    arcpy.CreateTin_3d(CreateTin_Out,None,CreateTin_InFeature,'Delaunay')

    # TIN-->contour polyline shapefile
    Contour_In = './NJCF_200_TIN/NJCF_200_TIN_'+str(i)
    Contour_Out = './NJCF_200_contour/contour_'+str(i)+'.shp'
    Contour_Interval = 300
    arcpy.SurfaceContour_3d(Contour_In,Contour_Out,Contour_Interval)

    # Extract 900 second life circle
    Select_In = './NJCF_200_contour/contour_'+str(i)+'.shp'
    Select_Out = './NJCF_200_contour/contour_arcpy900_'+str(i)+'.shp'
    arcpy.Select_analysis(Select_In, Select_Out, '"Contour" = 900')

    # Contour polyline shapefile-->contour surface polygon shapefile
    Polygon_In = './NJCF_200_contour/contour_arcpy900_'+str(i)+'.shp'
    Polygon_Out = './NJCF_200_polygon/polygon_arcpy900_'+str(i)+'.shp'
    arcpy.FeatureToPolygon_management([Polygon_In],Polygon_Out,0,"NO_ATTRIBUTES")


# # Duration point shapefile-->Duration TIN
# CreateTin_Out = './NJCF_200_TIN/NJCF_200_TIN_0' # /NJCF_200_TIN_0'
# CreateTin_InFeature = './NJCF_200_bdak_shp_wgs84/NJCF_200_0.shp Duration masspoints'
# arcpy.CreateTin_3d(CreateTin_Out,None,CreateTin_InFeature,'Delaunay')
#
# # TIN-->contour polyline shapefile
# Contour_In = './NJCF_200_TIN/NJCF_200_TIN_0'
# Contour_Out = './NJCF_200_contour/contour_0.shp'
# Contour_Interval = 300
# arcpy.SurfaceContour_3d(Contour_In,Contour_Out,Contour_Interval)
#
# # Extract 900 second life circle
# Select_In = './NJCF_200_contour/contour_0.shp'
# Select_Out = './NJCF_200_contour/contour_0_arcpy900.shp'
# arcpy.Select_analysis(Select_In, Select_Out, '"Contour" = 900')
#
# # Contour polyline shapefile-->contour surface polygon shapefile
# Polygon_In = './NJCF_200_contour/contour_0_arcpy900.shp'
# Polygon_Out = './NJCF_200_polygon/polygon_0_arcpy900.shp'
# arcpy.FeatureToPolygon_management([Polygon_In],Polygon_Out,0,"NO_ATTRIBUTES")
