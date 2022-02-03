import arcpy

arcpy.CheckOutExtension("3D")
arcpy.env.workspace = "./"
shpfilename = "contour.shp"
shpfilepath = "./NJCommunityField_tinout_contour/"+shpfilename # D:/OneDrive/Code/LifeCircle/ArcpyFunc/NJCommunityField
# print shpfilepath
# read attribute list
PointMetaArray = arcpy.ListFields(shpfilepath)
PointMetaList = []
for i in PointMetaArray:
    PointMetaList.append(i.aliasName)
# read data
FeaturePoint =[]
for i in arcpy.da.SearchCursor(shpfilepath,PointMetaList):
    FeaturePoint.append(i)
print FeaturePoint



