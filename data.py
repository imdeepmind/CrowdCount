# Dependencies
import pandas as pd

from tqdm import tqdm

from constants import LABELS_FILE, IMAGES_PATH, SAVE_PATH, IMAGE_SIZE, SAVE_CSV
from utils import make_folder, process_image, get_all_files

# Making the folder to save images
make_folder(SAVE_PATH)

# Read the Labels
label_csv = pd.read_csv(LABELS_FILE)

labels = label_csv["count"].values

del label_csv

# Array to store all the data
dataset = []

# Read and process all images
images = get_all_files(IMAGES_PATH)

for index, image in tqdm(enumerate(images)):
	try:
		saved_path = process_image(IMAGES_PATH, image, SAVE_PATH, (IMAGE_SIZE, IMAGE_SIZE))
		dataset.append([saved_path, labels[index]])
	except Exception as ex:
		pass

del images

# Saving the data into CSV file
df = pd.DataFrame(dataset, columns=["image_path", "count"])

# Shuffling the data
df.sample(frac=1)

# Saving the data into CSV file
df.to_csv(SAVE_CSV, index=False)