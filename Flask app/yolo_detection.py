from ultralytics import YOLO
import cv2
import numpy as np

# Load the YOLO model
model = YOLO("best.pt")


# Define a Gradio function to make predictions on an uploaded image


def predict_image(input_image):
    # Make predictions using the YOLO model
    area = []
    # print(input_image)
    image = cv2.imread(input_image)
    results_image = model(image, save=True)
    house_pixel = 0
    driveway_pixels = 0
    for r in results_image:
        for i in range(len(results_image[0].masks)):
            classid = int(results_image[0].boxes[i].cls[0].item())
            if classid == 0 or classid == 4:
                mask = results_image[0].masks[i].data[0].numpy()
                num_pixels = np.count_nonzero(mask)
                if classid == 4:
                    house_pixel = num_pixels
                else:
                    driveway_pixels = num_pixels
                print(f"{i} " + "Num_pixels: " + f"{num_pixels}")
                mask = mask * 255
                # Convert the mask to a uint8 array
                mask = mask.astype(np.uint8)
                # Save the mask as an image
                area.append(num_pixels)
                cv2.imwrite(f"mask{i}.png", mask)
        im_array = r.plot(font_size=0.2, labels=False, boxes=False)
    # area calculation
    cv2.imwrite("runs/segment/predict/image0.jpg", im_array)
    return sum(area), house_pixel, driveway_pixels
