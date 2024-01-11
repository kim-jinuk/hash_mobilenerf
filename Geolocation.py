from PIL import Image, ExifTags
from PIL.ExifTags import TAGS
import os
import sys
import json
from collections import OrderedDict

file_data = OrderedDict()
result_folder = "result"
if not os.path.exists(result_folder):
    os.makedirs(result_folder)

data_name = sys.argv[1]
filedir = "datasets/nerf_llff_data/" + data_name + "/images"
filenames = os.listdir(filedir)
total_Lat = []
total_Lon = []
for filename in filenames:
    extension = filename.split('.')[-1]
    if (extension == 'jpg') | (extension == 'JPG') | (extension == 'jpeg') | (extension == 'JPEG'):
        try:
            img = Image.open(filedir + "/" + filename)
            info = img._getexif()
            exif = {}
            for tag, value in info.items():
                decoded = TAGS.get(tag, tag)
                exif[decoded] = value
            # from the exif data, extract gps
            exifGPS = exif['GPSInfo']
            latData = exifGPS[2]
            lonData = exifGPS[4]
            # calculae the lat / long
            latDeg = latData[0]
            latMin = latData[1]
            latSec = latData[2]
            lonDeg = lonData[0]
            lonMin = lonData[1]
            lonSec = lonData[2]
            # correct the lat/lon based on N/E/W/S
            Lat = (latDeg + (latMin + latSec / 60.0) / 60.0)
            if exifGPS[1] == 'S': Lat = Lat * -1
            Lon = (lonDeg + (lonMin + lonSec / 60.0) / 60.0)
            if exifGPS[3] == 'W': Lon = Lon * -1
            # print file
            #msg = "There is GPS info in this picture located at " + str(Lat) + "," + str(Lon)
            #print (msg)
            #kmlheader = '<?xml version="1.0" encoding="UTF-8"?>' + '<kml xmlns="http://www.opengis.net/kml/2.2">'
            #kml = ('<Placemark><name>%s</name><Point><coordinates>%6f,%6f</coordinates></Point></Placemark></kml>') % (
            #filename, Lon, Lat)
            #with open(filename + '.kml', "w") as f:
            #    f.write(kmlheader + kml)
            #print ('kml file created')
            total_Lat.append(Lat)
            total_Lon.append(Lon)
        except:
            print ('There is no GPS info in this picture')
            pass

center_lat = (max(total_Lat) + min(total_Lat)) / 2
center_lon = (max(total_Lon) + min(total_Lon)) / 2
mean_lat = sum(total_Lat) / len(total_Lat)
mean_lon = sum(total_Lon) / len(total_Lon)

file_data["ModelName"] = data_name
file_data["GeoLocation"] = {'lat': center_lat, 'lon': center_lon, 'alt': 0.0}
file_data["Rotation"] = {'x': -90.0, 'y': 0.0, 'z': 0.0}
file_data["Scale"] = {'x': 0.16, 'y': 0.16, 'z': 0.16}

#print(json.dumps(file_data, ensure_ascii=False, indent="\t"))
with open(result_folder + '/meta.json', 'w', encoding="utf-8") as make_file:
    json.dump(file_data, make_file, ensure_ascii=False, indent="\t")