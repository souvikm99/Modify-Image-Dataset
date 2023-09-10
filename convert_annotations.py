import os
import cv2
import numpy as np
from tqdm import tqdm

def convert(image_path, coords):
    image = cv2.imread(image_path)
    coords[2] -= coords[0]
    coords[3] -= coords[1]
    x_diff = int(coords[2]/2)
    y_diff = int(coords[3]/2)
    coords[0] = coords[0]+x_diff
    coords[1] = coords[1]+y_diff
    coords[0] /= int(image.shape[1])
    coords[1] /= int(image.shape[0])
    coords[2] /= int(image.shape[1])
    coords[3] /= int(image.shape[0])
    return coords

# Input folder paths
image_folder = input("Enter the folder path of images: ")
label_folder = input("Enter the folder path of labels: ")
target_folder = input("Enter the target folder path to save normalized labels: ")

# Ensure target folder exists
os.makedirs(target_folder, exist_ok=True)

# Iterate over label files
for filename in tqdm(os.listdir(label_folder)):
    if filename.endswith(".txt"):
        label_path = os.path.join(label_folder, filename)
        image_path = os.path.join(image_folder, filename.replace(".txt", ".jpg"))
        annotations = []

        with open(label_path, 'r') as f:
            for line in f:
                labels = line.split()
                coords = np.asarray([float(labels[1]), float(labels[2]), float(labels[3]), float(labels[4])])
                coords = convert(image_path, coords)
                labels[1], labels[2], labels[3], labels[4] = coords[0], coords[1], coords[2], coords[3]
                newline = str(labels[0]) + " " + str(labels[1]) + " " + str(labels[2]) + " " + str(labels[3]) + " " + str(labels[4])
                annotations.append(newline)

        # Save the normalized labels in the target folder
        target_path = os.path.join(target_folder, filename)
        with open(target_path, 'w') as outfile:
            for line in annotations:
                outfile.write(line)
                outfile.write("\n")

print("Normalization complete!")
