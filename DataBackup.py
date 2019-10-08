# Download RPZ Vote Data from AGO
# Site:
# Script Last Updated: 2019-3-20
# Author: mmurnane
# Login: https://developers.arcgis.com/python/guide/working-with-different-authentication-schemes/#Connecting-through-ArcGIS-Pro
# Works in 3.6.6

# Import libraries
from arcgis.gis import GIS  # https://esri.github.io/arcgis-python-api/apidoc/html/arcgis.gis.toc.html
import time
import logging

# Variables
agoID = "0fd58eff3877462393b45041a6df7795"   #Vote RPZ

# Login to AGOL
gis = GIS("pro") # To work ArcPro must be currently logged in (can be closed).
print("")
print("Logged in as: " + gis.properties.user.username)
print("")
print("Starting time: {}".format(time.asctime( time.localtime(time.time()) )))
print("")

try:
  #Download AGOL data
  print("")
  print("Downloading existing AGOL data ...")
  data_item = gis.content.get(agoID) #Find VoteRPZ
  title="Data_Export" + time.strftime("%Y%m%d_%H%M%S")
  print(data_item)
  outputgdb = data_item.export(title=title,export_format="Shapefile",wait=True)
  #outputgdb.download(save_path = r'./Data')  #Download to current location.
  outputgdb.download(save_path = '\\\\geobase-win\\ced\\GADS\\R2019\\R013\\DataBackup\\Data')  #Download to current location.
except:
  logging.exception('\n Unexpected error with website, could not download successfully: \n')
else:
  print("")
  print("Successfully downloaded data.")
  print("")
  print("Stopping time: {}".format(time.asctime( time.localtime(time.time()) )))
