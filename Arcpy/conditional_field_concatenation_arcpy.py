##script to concatenate 'JAC' to beginning of field, then add appropriate number of '0' based on string length

#import modules
import arcpy
import os
import shutil
import sys
print 'modules imported'

arcpy.env.overwriteOutput = True

#directory to JLSP_Tree_Inventory_Master
fcname = 'PaleoSignificance_toadd'
fcpath = 'C:\\Users\\changs\\Desktop\\Geo_Paleo_Local\\LON_Management_Zones.gdb'
fc = os.path.join(fcpath, fcname)
print 'made directory'

# first field is original data, second is the field to alter.
fields = ['Devl_Recs']
print 'fields defined'

with arcpy.da.UpdateCursor(fc,fields) as cursor:
    #For each row, evaluate length, and enter appropriate if statement
    # to concatenate 0s to the front
    for row in cursor:
        #if statements here for conditional changes
        if row[0] == 'Survey/Monitor':
            row[0] = 'Survey/Monitor'
        if row[0] == 'None':
            row[0] = 'None'
    
      



        cursor.updateRow(row)

print 'finished!'
