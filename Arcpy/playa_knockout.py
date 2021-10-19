####Script that takes a shapefile with wind farm points and
    ###1. defines an affected area
    ###2. Identifies playas within the affected area. 

##initial legwork##

#Import Libraries
import os
import sys
import numpy
import arcpy
from arcpy import env
import timeit
import time
import datetime

#Timer for processing time start
timeBegin= timeit.default_timer()
timeSt= time.localtime()
print ('Start time: '+time.strftime('%a %b %d %H:%M:%S %Y', timeSt)+'\n')


## ---------- assign variables -------------##

# directories for workspace and output
root = 'X:\\Stephen_work'
ws = os.path.join(root, 'Practice_layers')
outDir = os.path.join(ws, 'output')

#directory for input wind turbine layer
windpath = 'Z:\\Wind\\faa_products\\wind_turbines_nov_08_2017'
windname = 'wind_turbines_nov_08_2017'
windlyr = os.path.join(windpath, windname+'.shp')

#directory to playa layer
playapath = 'Z:\\Hydrology\\Playas'
playaname = 'LD_Playas'
playalyr = os.path.join(playapath,playaname+'.shp')

#directory to PLJV boundary
pljvpath = 'Z:\\PLJV'
pljvname = 'PLJV_Boundary'
pljvlyr = os.path.join(pljvpath,pljvname+'.shp')

field = 'knock_date'


##---------------Geoprocessing for new wind layer -----------------##

# Create feature layer of wind turbines for selection outside Arcmap
print 'converting wind turbines to a feature class...'
timeStart = timeit.default_timer()
windfeature = os.path.join(windpath,windname+'_ftr.shp')
arcpy.MakeFeatureLayer_management(windlyr,windfeature)
print 'feature layer complete'
timeEnd = timeit.default_timer()
print ('Processing Time: '+ '{0:.2f}'.format(((timeEnd - timeStart)/60))+' minutes'+'\n')
print ('\n'+'-----------------------------------------'+'\n')

#Select from wind turbines intersecting the PLJV boundary
print 'making selection of windmills...'
timeStart = timeit.default_timer()
selection = arcpy.SelectLayerByLocation_management(windfeature,"INTERSECT",pljvlyr,"#","NEW_SELECTION")
print 'selection complete'
timeEnd = timeit.default_timer()
print ('Processing Time: '+ '{0:.2f}'.format(((timeEnd - timeStart)/60))+' minutes'+'\n')
print ('\n'+'-----------------------------------------'+'\n')

#Export wind turbines to new layer
print 'creating "PLJV wind turbines" layer...'
timeStart = timeit.default_timer()
pljvwind = os.path.join(outDir,windname+'_pljv.shp')
arcpy.CopyFeatures_management(selection,pljvwind,"#","0","0","0")
print 'layer completed'
timeEnd = timeit.default_timer()
print ('Processing Time: '+ '{0:.2f}'.format(((timeEnd - timeStart)/60))+' minutes'+'\n')
print ('\n'+'-----------------------------------------'+'\n')

##-----------------last new directory----------------##


#New directory to pljvwind with root in output directory
pljvwindname = 'wind_turbines_nov_08_2017_pljv'
pljvwindlyr = os.path.join(outDir,pljvwindname+'.shp')

##---------------Back to Geoprocessing---------------##

#Buffer - 1000m
print 'buffering wind turbines...'
timeStart = timeit.default_timer()
bufferout = os.path.join(outDir,pljvwindname+'_buffer.shp')
arcpy.Buffer_analysis(pljvwindlyr,bufferout,"1000 Meters","FULL","ROUND","NONE","#")
print 'Buffer Complete'
timeEnd = timeit.default_timer()
print ('Processing Time: '+ '{0:.2f}'.format(((timeEnd - timeStart)/60))+' minutes'+'\n')
print ('\n'+'-----------------------------------------'+'\n')

#Dissolve buffers - 'create multipart features = unchecked; FID = checked; 
print 'Dissolving buffer...'
timeStart = timeit.default_timer()
dissolveout = os.path.join(outDir,pljvwindname+'_dissolve.shp')
arcpy.Dissolve_management(bufferout,dissolveout,"FID","#","SINGLE_PART","DISSOLVE_LINES")
print "Dissolve complete"
timeEnd = timeit.default_timer()
print ('Processing Time: '+ '{0:.2f}'.format(((timeEnd - timeStart)/60))+' minutes'+'\n')
print ('\n'+'-----------------------------------------'+'\n')

#Identity - join attributes = ONLY_FID ; input is windmill points, identity is dissolved buffers
print 'identifying unique windfarm ID for each turbine...'
timeStart = timeit.default_timer()
IDout = os.path.join(outDir,pljvwindname+'_identity.shp')
arcpy.Identity_analysis(pljvwindlyr,dissolveout,IDout,"ONLY_FID","#","NO_RELATIONSHIPS")
print 'Identity complete'
timeEnd = timeit.default_timer()
print ('Processing Time: '+ '{0:.2f}'.format(((timeEnd - timeStart)/60))+' minutes'+'\n')
print ('\n'+'-----------------------------------------'+'\n')

#Minimum bounding geometry - Group Option = List; Group Fields = unique farm ID Column; Windmills w/ farm ID for input.
print 'Creating convex hulls...'
timeStart = timeit.default_timer()
geometryout = os.path.join(outDir,pljvwindname+'_geometry.shp')

    #creates a list of all field names, changes list to str type, then loops through and selects unique farm_ID field and sets it as a variable
field_names = [f.name for f in arcpy.ListFields(IDout)]
counter = 0
for field in field_names:
    field_names[counter] = str(field_names[counter])
    counter +=1
for field in field_names:
    if 'FID' in field and field.endswith('1'):
        farm_id = field
print farm_id

arcpy.MinimumBoundingGeometry_management(IDout,geometryout,"CONVEX_HULL","LIST",farm_id,"NO_MBG_FIELDS")
print 'Convex hulls complete'
timeEnd = timeit.default_timer()
print ('Processing Time: '+ '{0:.2f}'.format(((timeEnd - timeStart)/60))+' minutes'+'\n')
print ('\n'+'-----------------------------------------'+'\n')


#Make Feature Layer - a necessary step to select features outside of Arcmap
print 'converting LD_playas to a feature class...'
timeStart = timeit.default_timer()
playafeature = os.path.join(playapath,playaname+'_ftr.shp')
arcpy.MakeFeatureLayer_management(playalyr,playafeature)
print 'feature layer complete'
timeEnd = timeit.default_timer()
print ('Processing Time: '+ '{0:.2f}'.format(((timeEnd - timeStart)/60))+' minutes'+'\n')
print ('\n'+'-----------------------------------------'+'\n')


#Select by location - selecting playas that intersect with convex hulls
print 'making selection of affected playas...'
timeStart = timeit.default_timer()
arcpy.SelectLayerByLocation_management(playafeature,"INTERSECT",geometryout,"#","NEW_SELECTION")
print 'selection complete'
timeEnd = timeit.default_timer()
print ('Processing Time: '+ '{0:.2f}'.format(((timeEnd - timeStart)/60))+' minutes'+'\n')
print ('\n'+'-----------------------------------------'+'\n')

with arcpy.da.SearchCursor(playafeature, field) as cursor:
    for row in cursor:
        if row[0]=='null':
            row[0]=str(datetime.date.today())
            cursor.updateRow(row)
print 'knockout dates have been updated'
        

# Copy affected playas to new layer
#print 'creating "affected playas" layer...'
#timeStart = timeit.default_timer()
#affplayas = os.path.join(outDir,windname+'_affplayas.shp')
#arcpy.CopyFeatures_management(selection,affplayas,"#","0","0","0")
#print 'layer completed'
#timeEnd = timeit.default_timer()
#print ('Processing Time: '+ '{0:.2f}'.format(((timeEnd - timeStart)/60))+' minutes'+'\n')
#print ('\n'+'-----------------------------------------'+'\n')

