import arcpy

# arcpy.CheckOutExtension("3D")
arcpy.env.workspace = "./"

arcpy.FeatureToPolygon_management(["./NJCommunityField_tinout_contour/contour.shp"],"./NJCommunityField_tinout_polygon/polygon.shp","","NO_ATTRIBUTES")