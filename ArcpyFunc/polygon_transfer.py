import arcpy

# arcpy.CheckOutExtension("3D")
arcpy.env.workspace = "./"

arcpy.FeatureToPolygon_management(["./NJCommunityField_tinout_contour/contour.shp"],"./NJCommunityField_tinout_polygon_arcpy/polygon.shp",0,"NO_ATTRIBUTES")
