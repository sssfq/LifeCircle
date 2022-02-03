import arcpy

arcpy.CheckOutExtension("3D")
arcpy.env.workspace = "./"

arcpy.SurfaceContour_3d('./NJCommunityField_tinout','./NJCommunityField_tinout_contour/contour.shp',300)