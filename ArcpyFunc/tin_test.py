import arcpy

sr = "C:\Program Files (x86)\ArcGIS\Desktop10.4\Reference Systems\International Map Of The World.prj"
featureclasses = arcpy.ListFeatureClasses()
for i in featureclasses:
    ot=i.split(".shp")[0]
    feat="{0} Shape.Z Hard_Line level".format(i)
    print feat
    arcpy.CreateTin_3d(out_tin=ot, spatial_reference=sr, in_features=feat, constrained_delaunay="DELAUNAY")