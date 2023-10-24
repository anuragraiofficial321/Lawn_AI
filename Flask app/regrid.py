import requests
import goole_image_hybrid_roadmap
import pandas as pd
import re
import json
import find_area

url = "https://app.regrid.com/api/v1/search.json?query="


# add = pd.read_excel("(01-09(friday))_Lawn_AI_Test_Addresses.xlsx")
# addresses = [
#     re.sub(" +", " ", address.strip()) for address in add["Test Case Address"].tolist()
# ]


def get_image(address):
    addresses = []
    addresses.append(address)
    headers = {
        "accept": "application/json",
        "x-regrid-token": "eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJyZWdyaWQuY29tIiwiaWF0IjoxNjk1Mzc0NTM5LCJleHAiOjE2OTc5NjY1MzksInUiOjMxNjU1MCwiZyI6MjMxNTMsImNhcCI6InBhOnRzOnBzOmJmOm1hOnR5OmVvOnNiIn0.7Fj4hTJE1OLP1dhYrkhpHlCTpxcGxbuHqLjyzyhv_dU",
    }
    house_areas = []
    for count, address in enumerate(addresses, start=23):
        params = {"query": address}

        response = requests.get(url, params=params, headers=headers)
        # with open("json_data.txt", "a") as file:
        # file.write(f"Response:{response}\n")

        # print(response)
        if response.status_code == 200:
            data = response.json()
            with open("data.json", "w") as json_file:
                json.dump(data, json_file)
            # with open("json_data.txt", "a") as file:
            #     file.write(f"data:{data}\n")
            # print("data", data)
            # print(data)
            try:
                # if count==1 or count==2:
                # print(data,"\n")
                coordinates = data["results"][0]["geometry"]["coordinates"][0]
                # print("Area coordinates: ", coordinates)
                image = goole_image_hybrid_roadmap.getimage_google(
                    coordinates, count, address
                )
                # print(type(image))
                house_area = data["buildings"][0]["properties"][
                    "ed_bldg_footprint_sqft"
                ]
                house_areas.append(house_area)
                # print("Total House area:", house_area)
                find_area.cal_area(coordinates, address)
                with open("data.json", "r") as f:
                    data = json.load(f)
                    total_sqft = data["results"][0]["properties"]["fields"]["sqft"]
                    house_area = data["buildings"][-1]["properties"][
                        "ed_bldg_footprint_sqft"
                    ]
                    print("House Area:", house_area)

                return image, total_sqft, house_area, coordinates

            except IndexError:
                print(address)

        else:
            print(f"Error getting data for {address}: {response.status_code}")
            # pass
    # with open("house_areas.txt", "w") as file:
    #     for area in house_areas:
    #         file.write(str(area) + "\n")
