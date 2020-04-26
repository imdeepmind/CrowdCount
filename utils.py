import cv2

from os import makedirs
from os.path import exists

def make_folder(path):	
	if not os.path.exists(path):
		os.makedirs(path)

def process_image(read_path, save_path, size):
	try:
		img = cv2.imread(read_path, 1)
		img = img.resize(img, size)
		cv2.imread(save_path, img)
	except Exception as ex:
		print(str(ex))
		raise Exception("Not able to read the image")

