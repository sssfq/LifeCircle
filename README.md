# 安装Python包
安装HTTP库***requests***用于API接口访问
``pip install requests``

安装json库***json***用于解码JSON对象
``pip install json``

安装.shp文件处理库***shapefile***用于导出.shp矢量文件
``pip install pyshp``

安装数据分析库***pandas***用于读取数据文件
``conda install pandas``

# ***shapefile***文件处理
[Python Shapefile Library](https://pythonhosted.org/Python%20Shapefile%20Library/)

[中文版](https://www.osgeo.cn/pygis/others_pyshp.html#%E5%86%99shapefile)

[GitHub](https://github.com/GeospatialPython/pyshp)

# 参数选取
## 百米经纬度换算
100m = 0.000899° 纬度

100m = 0.001141° 经度

## 坐标转换程序
https://www.jianshu.com/p/6e69737cffaa

# Arcpy
## 配置PyCharm + ArcGIS 10.6中Python 2.7开发环境
https://www.cnblogs.com/suncf/p/12357913.html

## arcpy.da.SearchCursor() 读取shp文件
https://blog.csdn.net/pushhy/article/details/108948476

## arcpy.CreateTin_3d() 矢量shapefile文件创建TIN图层
https://desktop.arcgis.com/zh-cn/arcmap/latest/tools/3d-analyst-toolbox/create-tin.html

## arcpy.SurfaceContour_3d() TIN图层绘制等值线
https://desktop.arcgis.com/zh-cn/arcmap/latest/tools/3d-analyst-toolbox/surface-contour.html

## arcpy.FeatureToPolygon_management() 等值线要素转换为等值面
https://pro.arcgis.com/zh-cn/pro-app/latest/tool-reference/data-management/feature-to-polygon.htm

特别的，需要将cluster_tolerance参数设置为0，不应保持默认。


