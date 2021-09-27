import os
import shutil
import imghdr
try:
	import PIL
	from PIL import Image
except ImportError as e:
	print("This script requires the Python Imaging Library (PIL) to run\nExiting...")
	quit()

spotdir = os.getenv('LOCALAPPDATA') + '\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets'
tardir = os.getenv('USERPROFILE') + '\\Documents\\spotlight_extract'

# Creating the extraction directory if it does not existe yet
if not os.access(tardir,os.F_OK): 
	os.mkdir(tardir)
	print("Creating target directory at " + tardir + "\n")
else: 
	print("Target directory already exists. Skipping...\n")

spot_content = os.listdir(path=spotdir)

for file in spot_content: 
	curr_sourcepath = spotdir + "\\" + file
	curr_destpath = tardir + "\\" + file + "." + imghdr.what(curr_sourcepath)

	img = Image.open(curr_sourcepath)
	asp_ratio = float(img.size[0] / img.size[1])

	if not asp_ratio == 1.0: # Ignoring thumbnails
		if not os.access(curr_destpath,os.F_OK): # Checking if file already exists
			print("Copying " + file + " to target directory...")
			shutil.copyfile(curr_sourcepath,curr_destpath)
		else:
			print(file + " already exists...Skipping")