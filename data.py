import cv2

import pandas as pd
import numpy as np

from os import listdir
from os.path import join
from tqdm import tqdm

from constants import LABELS_FILE, IMAGES_PATH, SAVE_FILE, IMAGE_SIZE, IMAGE_CHANNEL

# Reading the label file
data = pd.read_csv(LABELS_FILE)
labels = data["count"].values

# Getting a list of all images
images = listdir(IMAGES_PATH)

# Setting the channel
channel = 1 if IMAGE_CHANNEL == 3 else 0

# Array to store all the images
dataset = []

# Iterating through the images
for index, image in tqdm(enumerate(images)):
	# Reading the image
	img = cv2.imread(join(IMAGES_PATH, image), channel)

	# Resizing the images
	img = cv2.resize(img, (IMAGE_SIZE, IMAGE_SIZE))

	# Appending the images
	img = np.append(img.flatten(), labels[index])	

	# String the image and labels into main dataset array
	dataset.append(img)


# Cleaning some memory
del data, labels, images, channel


