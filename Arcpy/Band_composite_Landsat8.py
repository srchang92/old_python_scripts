#Script for the band composite of 1 landsat image
#By Stephen Chang

#import necessary libraries/modules, I might only need arcpy here for now.
import os
import sys
import numpy
import arcpy

## assign variables ###

#exact path where to output, front slashes please
output= 'C:/Landsat/composites/composite_2528_20160825.TIF'

#Exact path to different bands, back slashes please
band1='C:\Landsat\LC08_L1TP_025028_20160825_20170221_01_T1 (1).tar\LC08_L1TP_025028_20160825_20170221_01_T1 (1)\LC08_L1TP_025028_20160825_20170221_01_T1_B1.TIF'
band2='C:\Landsat\LC08_L1TP_025028_20160825_20170221_01_T1 (1).tar\LC08_L1TP_025028_20160825_20170221_01_T1 (1)\LC08_L1TP_025028_20160825_20170221_01_T1_B2.TIF'
band3='C:\Landsat\LC08_L1TP_025028_20160825_20170221_01_T1 (1).tar\LC08_L1TP_025028_20160825_20170221_01_T1 (1)\LC08_L1TP_025028_20160825_20170221_01_T1_B3.TIF'
band4='C:\Landsat\LC08_L1TP_025028_20160825_20170221_01_T1 (1).tar\LC08_L1TP_025028_20160825_20170221_01_T1 (1)\LC08_L1TP_025028_20160825_20170221_01_T1_B4.TIF'
band5='C:\Landsat\LC08_L1TP_025028_20160825_20170221_01_T1 (1).tar\LC08_L1TP_025028_20160825_20170221_01_T1 (1)\LC08_L1TP_025028_20160825_20170221_01_T1_B5.TIF'
band6='C:\Landsat\LC08_L1TP_025028_20160825_20170221_01_T1 (1).tar\LC08_L1TP_025028_20160825_20170221_01_T1 (1)\LC08_L1TP_025028_20160825_20170221_01_T1_B6.TIF'
band7='C:\Landsat\LC08_L1TP_025028_20160825_20170221_01_T1 (1).tar\LC08_L1TP_025028_20160825_20170221_01_T1 (1)\LC08_L1TP_025028_20160825_20170221_01_T1_B7.TIF'
band8='C:\Landsat\LC08_L1TP_025028_20160825_20170221_01_T1 (1).tar\LC08_L1TP_025028_20160825_20170221_01_T1 (1)\LC08_L1TP_025028_20160825_20170221_01_T1_B8.TIF'
band9='C:\Landsat\LC08_L1TP_025028_20160825_20170221_01_T1 (1).tar\LC08_L1TP_025028_20160825_20170221_01_T1 (1)\LC08_L1TP_025028_20160825_20170221_01_T1_B9.TIF'
band10='C:\Landsat\LC08_L1TP_025028_20160825_20170221_01_T1 (1).tar\LC08_L1TP_025028_20160825_20170221_01_T1 (1)\LC08_L1TP_025028_20160825_20170221_01_T1_B10.TIF'
band11='C:\Landsat\LC08_L1TP_025028_20160825_20170221_01_T1 (1).tar\LC08_L1TP_025028_20160825_20170221_01_T1 (1)\LC08_L1TP_025028_20160825_20170221_01_T1_B11.TIF'

# create list of bands
in_rasters=[]
in_rasters.append(band1)
in_rasters.append(band2)
in_rasters.append(band3)
in_rasters.append(band4)
in_rasters.append(band5)
in_rasters.append(band6)
in_rasters.append(band7)
in_rasters.append(band8)
in_rasters.append(band9)
in_rasters.append(band10)
in_rasters.append(band11)
print in_rasters
#Run band composite
#arcpy.CompositeBands_management(in_rasters, output)
#print "finished homes"
