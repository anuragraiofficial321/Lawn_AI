from ultralytics import YOLO
import os
from PIL import Image
import cv2
import numpy as np


def detect(model_pt, image_pt):
    # Load a pretrained YOLOv8n model
    model = YOLO(model_pt)

    # Whatever the requirement you want can mention here save_txt=True...etc
    results = model(image_pt)
    # results = model(image_pt, save=True, save_txt=True, save_crop=True)
    mask_areas = []
    # for i in range(len(results[0].masks)):
    mask = results[0].masks[0].data[0].numpy()

    num_pixels = np.count_nonzero(mask)  # White pixel count
    area = num_pixels * 0.109336312
    mask_areas.append(area)
    # mask_areas.append(num_pixels)
    print("Number of pixels = ", num_pixels)
    print("Area of house = ", area)

    return sum(mask_areas)


model_name = "best.pt"

# image = cv2.imread(
#     "images/Batch_4/hybrid_23_6005 Aspen Meadow Dr, Indianapolis, IN 46237.png"
# )
image = cv2.imread("images/Batch_4/hybrid_23_6005 Aspen Meadow Dr, Indianapolis, IN 46237.png")
mask_area = detect(model_name, image)
# print("Total area: ", mask_area)
