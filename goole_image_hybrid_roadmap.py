import requests
import json
import os
import numpy as np

# api_key = "" #mike
api_key = ""  # AIzaSyDI"
map_size = "640x640"
size = "640x640"
zoom = 20
map_type = "satellite"
fov = 110  # Field of view in degrees
pitch = 0
heading = 0  # hybrid"
# satellite


def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


def getimage_google(parcel_coordinates, count, address):
    center_lat = (
        max(lat for lon, lat in parcel_coordinates)
        + min(lat for lon, lat in parcel_coordinates)
    ) / 2  # &scale=2.0
    center_lon = (
        max(lon for lon, lat in parcel_coordinates)
        + min(lon for lon, lat in parcel_coordinates)
    ) / 2

    static_map_url_hybrid = f"https://maps.googleapis.com/maps/api/staticmap?center={center_lat},{center_lon}&zoom={zoom}&size={map_size}&maptype={map_type}&key={api_key}&path=color:red|fillcolor:transparent|"
    static_map_url_roadmap = f"https://maps.googleapis.com/maps/api/staticmap?center={center_lat},{center_lon}&zoom={zoom}&size={map_size}&maptype=roadmap&key={api_key}&path=color:red|fillcolor:transparent|"
    streetview_url = f"https://maps.googleapis.com/maps/api/streetview?size={size}&location={address}&fov={fov}&pitch={pitch}&heading={heading}&key={api_key}"

    for lon, lat in parcel_coordinates:
        static_map_url_hybrid += f"{lat},{lon}|"
        static_map_url_roadmap += f"{lat},{lon}|"

    static_map_url_hybrid = static_map_url_hybrid[:-1]
    static_map_url_roadmap = static_map_url_roadmap[:-1]

    response_hybrid = requests.get(static_map_url_hybrid)
    response_roadmap = requests.get(static_map_url_roadmap)
    # Send a GET request to the Street View URL and save the response
    response_streetview = requests.get(streetview_url)

    # create_folder("Batch_5")
    # create_folder("Batch_5_roadmap")
    # create_folder("Batch_5_streetview")

    # create_folder("new_boundary_transparent")

    # print(response_hybrid.content)
    with open(
        f"Batch_5/{count}_{address}.png",
        "wb",
    ) as f:
        f.write(response_hybrid.content)
    with open(
        f"Batch_5_roadmap/roadmap_{count}_{address}.png",
        "wb",
    ) as f:
        f.write(response_roadmap.content)

    with open(
        f"Batch_5_streetview/streetview_{count}_{address}.png",
        "wb",
    ) as f:
        f.write(response_streetview.content)

    """image_path = f'red_boundary_google_images/hybrid_{count}_address.png'
    image_path1=f'red_boundary_google_images/roadmap_{count}_address.png'

    original_image = cv2.imread(image_path)
    original_image1 = cv2.imread(image_path1)

    hsv_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)
    hsv_image1 = cv2.cvtColor(original_image1, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds for blue in the HSV color space
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    blue_mask = cv2.inRange(hsv_image, lower_blue, upper_blue)
    blue_mask1 = cv2.inRange(hsv_image1, lower_blue, upper_blue)

    # Find contours of the blue boundary
    contours, _ = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours1, _ = cv2.findContours(blue_mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create a mask for the detected blue boundary
    blue_boundary_mask = np.zeros_like(blue_mask)
    cv2.drawContours(blue_boundary_mask, contours, -1, (255), thickness=cv2.FILLED)
    blue_boundary_mask1 = np.zeros_like(blue_mask1)
    cv2.drawContours(blue_boundary_mask1, contours1, -1, (255), thickness=cv2.FILLED)

    # Define the lower and upper bounds for yellow in the HSV color space
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])

    # Create a mask for yellow regions within the blue boundary
    yellow_mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)
    yellow_mask1 = cv2.inRange(hsv_image1, lower_yellow, upper_yellow)

    # Apply the blue boundary mask to the yellow mask
    yellow_within_blue_mask = cv2.bitwise_and(yellow_mask, blue_boundary_mask)
    yellow_within_blue_mask1 = cv2.bitwise_and(yellow_mask1, blue_boundary_mask1)

    # Save the masks
    #cv2.imwrite(f'Yellow_polygon_mask/yellow_within_blue_mask_image_hybrid_{count}.png', yellow_within_blue_mask)
    #cv2.imwrite(f'Yellow_polygon_mask/yellow_within_blue_mask_image_roadmap_{count}.png', yellow_within_blue_mask1)


    cv2.imwrite(f'Red_boundary_transparent/red_mask_image_hybrid_{count}.png', yellow_within_blue_mask)
    cv2.imwrite(f'Red_boundary_transparent/red_mask_image_roadmap_{count}.png', yellow_within_blue_mask1)"""
