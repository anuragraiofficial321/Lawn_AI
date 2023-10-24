import requests
import json
import os
import numpy as np
from PIL import Image


api_key = "AUWG2EffOo4"  # AIJ8RfY4"
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

    create_folder("images/Batch_4")
    create_folder("images/Batch_4_roadmap")
    create_folder("images/Batch_4_streetview")

    # create_folder("new_boundary_transparent")

    # print(response_hybrid.content)
    with open(
        f"images/Batch_4/hybrid_{count}_{address}.png",
        "wb",
    ) as f:
        f.write(response_hybrid.content)
    with open(
        f"images/Batch_4_roadmap/roadmap_{count}_{address}.png",
        "wb",
    ) as f:
        f.write(response_roadmap.content)
    with open(
        f"images/Batch_4_streetview/streetview_{count}_{address}.png",
        "wb",
    ) as f:
        f.write(response_streetview.content)
    image_address = f"images/Batch_4/hybrid_{count}_{address}.png"

    return image_address
