import cv2

from os import makedirs, listdir
from os.path import exists, join

def make_folder(folder_name):	
	if not exists(folder_name):
		makedirs(folder_name)

def process_image(read_path, image, save_path, size):
	try:
		img = cv2.imread(join(read_path, image), 1)
		
		img = cv2.resize(img, size)
		
		cv2.imwrite(join(save_path, image), img)

		return join(save_path, image)
	except Exception as ex:
		print(ex)
		raise Exception("Not able to read the image")

def get_all_files(path):
	return listdir(path)