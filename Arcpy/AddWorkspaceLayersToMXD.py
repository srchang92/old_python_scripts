import arcpy, os
from arcpy import env


mxd = arcpy.mapping.MapDocument ("CURRENT")
# Set the workspace for ListFeatureClasses
arcpy.env.workspace = arcpy.GetParameterAsText(0)
# Set overwrite option
arcpy.env.overwriteOutput = True
df = arcpy.mapping.ListDataFrames(mxd, "*")[0]
arcpy.env.extent = df.extent

dsList = arcpy.ListDatasets("", "Feature")  
for ds in dsList: 

    fcList = arcpy.ListFeatureClasses("*","",ds)
    for FC in fcList:

     try:
            addLayer = arcpy.mapping.Layer(FC)
            addLayer.name = FC
            addLayer.visible = False
            arcpy.mapping.AddLayer(df, addLayer, "AUTO_ARRANGE")
            
            
            for lyr in arcpy.mapping.ListLayers(mxd, ""):
             cnt = int(arcpy.GetCount_management(lyr).getOutput(0))
             if  cnt < 1:
              arcpy.mapping.RemoveLayer(df, lyr)
            del addLayer
            
     except:
            print "problem with: " + str(FC)
            #del addLayer
            pass

            del FC
    del fcList
    

print "FINISHED!"
            #arcpy.AddMessage("Error w/layer: " + str(CurrentFClayer.name)) # skip problematic layers
            #pass


#mxd.save()# need to save the mxd to save the changes
arcpy.RefreshTOC()
arcpy.RefreshActiveView()
arcpy.AddMessage("Appropriate Feature Layers Added")
mxd.save
del mxd

