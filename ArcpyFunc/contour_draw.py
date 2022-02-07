import arcpy

arcpy.CheckOutExtension("3D")
arcpy.env.workspace = "./"

# arcpy.SurfaceContour_3d('./NJCommunityField_tinout','./NJCommunityField_tinout_contour/contour.shp',300)

in_raster = './NJCommunityField_tinout'
out_polyline = './NJCommunityField_tinout_contour/contour_raster.shp'
interval = 300
arcpy.Contour_3d(in_raster,out_polyline,interval)