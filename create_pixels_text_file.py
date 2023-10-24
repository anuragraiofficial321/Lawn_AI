import os
import cv2
import numpy as np
from ultralytics import YOLO  # Import the YOLO model class


def detect_images_in_folder(model_pt, folder_path, output_file):
    # Initialize the YOLO model
    model = YOLO(model_pt)
    with open(output_file, "w") as output_txt:
        for filename in os.listdir(folder_path):
            if filename.endswith((".png", ".jpg", ".jpeg")):
                # Load an image from the folder
                image_path = os.path.join(folder_path, filename)
                image = cv2.imread(image_path)

                # Perform object detection on the image
                results = model(image)  # Ensure your model returns masks

                # Check if any objects were detected
                try:
                    if results and len(results[0].masks) > 0:
                        # Get the mask data of the first object
                        mask_data = results[0].masks[0].data[0].cpu().numpy()

                        # Calculate the number of pixels in the mask
                        num_pixels = np.count_nonzero(mask_data)

                        output_txt.write(f"{num_pixels}\n")
                except:
                    output_txt.write(f"{0}\n")


if __name__ == "__main__":
    model_name = "best.pt"
    input_folder = "images/Batch_4"  # Change this to the folder containing your images
    output_file = "house_pixels.txt"  # Change this to the desired output text file path
    detect_images_in_folder(model_name, input_folder, output_file)
