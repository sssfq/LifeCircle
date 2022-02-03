import arcpy

arcpy.CheckOutExtension("3D")
arcpy.env.workspace = "./"

arcpy.CreateTin_3d('NJCommunityField_tinout',None,'./NJCommunityField/NJCommunityField.shp Duration masspoints','Delaunay')

arcpy.SurfaceContour_3d('./NJCommunityField_tinout','./NJCommnityField_tinout_contour/contour.shp',50)