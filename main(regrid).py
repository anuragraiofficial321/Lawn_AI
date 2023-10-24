import requests
import goole_image_hybrid_roadmap
import pandas as pd
import re
import json
import find_area

url = "https://app.regrid.com/api/v1/search.json?query="

add = pd.read_excel("(01-09(friday))_Lawn_AI_Test_Addresses.xlsx")
addresses = [
    re.sub(" +", " ", address.strip()) for address in add["Test Case Address"].tolist()
]

# addresses = [
#   "6005 Aspen Meadow Dr, Indianapolis, IN 46237"
# "6118 Aspen Meadow Dr, Indianapolis, IN 46237",
# "6124 Aspen Meadow Dr, Indianapolis, IN 46237",
# "6130 Aspen Meadow Dr, Indianapolis, IN 46237",
# "8218 Morera Ct, Indianapolis, IN 46237",
# "8224 Morera Ct, Indianapolis, IN 46237",
# "8230 Morera Ct, Indianapolis, IN 46237",
# "8236 Morera Ct, Indianapolis, IN 46237",
# "8242 Morera Ct, Indianapolis, IN 46237",
# "8247 Morera Ct, Indianapolis, IN 46237",
# "8241 Morera Ct, Indianapolis, IN 46237",
# "8235 Morera Ct, Indianapolis, IN 46237",
# "8229 Morera Ct, Indianapolis, IN 46237",
# "8223 Morera Ct, Indianapolis, IN 46237",
# "8217 Morera Ct, Indianapolis, IN 46237",
# "8205 Borland Dr, Indianapolis, IN 46237",
# "8244 Amarillo Dr, Indianapolis, IN 46237",
# "8243 Amarillo Dr, Indianapolis, IN 46237",
# "8249 Amarillo Dr, Indianapolis, IN 46237",
# "6250 Winslow Dr, Indianapolis, IN 46237",
# "6302 Winslow Dr, Indianapolis, IN 46237",
# "6316 Winslow Dr, Indianapolis, IN 46237",
# "6352 Winslow Dr, Indianapolis, IN 46237",
# "6358 Winslow Dr, Indianapolis, IN 46237",
# "6402 Winslow Dr, Indianapolis, IN 46237",
# "6408 Winslow Dr, Indianapolis, IN 46237",
# "6414 Winslow Dr, Indianapolis, IN 46237",
# "6422 Winslow Dr, Indianapolis, IN 46237",
# "6434 Winslow Dr, Indianapolis, IN 46237",
# "8119 S Southern Trails Pl, Indianapolis, IN 46237",
# "8045 Southern Springs Blvd, Indianapolis, IN 46237",
# "8028 Southern Springs Blvd, Indianapolis, IN 46237",
# "8020 Southern Springs Blvd, Indianapolis, IN 46237",
# "8010 Southern Springs Blvd, Indianapolis, IN 46237",
# "8011 Southern Springs Blvd, Indianapolis, IN 46237",
# "6008 Janel Cir, Indianapolis, IN 46237",
# "6007 Janel Cir, Indianapolis, IN 46237",
# "6015 Janel Cir, Indianapolis, IN 46237",
# "6016 Janel Cir, Indianapolis, IN 46237",
# "6024 Janel Cir, Indianapolis, IN 46237",
# "6017 Cheri Cir, Indianapolis, IN 46237",
# "6025 Cheri Cir, Indianapolis, IN 46237",
# "7816 Janel Dr, Indianapolis, IN 46237",
# "7817 Janel Dr, Indianapolis, IN 46237",
# "7809 Janel Dr, Indianapolis, IN 46237",
# "7746 Janel Dr, Indianapolis, IN 46237",
# "7738 Janel Dr, Indianapolis, IN 46237",
# "6133 Gunyon Way, Indianapolis, IN 46237",
# "7719 Chris Anne Cir, Indianapolis, IN 46237",
# "7638 Muirfield Pl, Indianapolis, IN 46237",
# "7646 Muirfield Pl, Indianapolis, IN 46237",
# "7654 Muirfield Pl, Indianapolis, IN 46237",
# "7675 Muirfield Pl, Indianapolis, IN 46237",
# "7649 Southern Lakes Dr, Indianapolis, IN 46237",
# "7611 Muirfield Pl, Indianapolis, IN 46237",
# "7603 Muirfield Pl, Indianapolis, IN 46237",
# "7559 Muirfield Pl, Indianapolis, IN 46237",
# "7519 Muirfield Pl, Indianapolis, IN 46237",
# "7446 Muirfield Pl, Indianapolis, IN 46237",
# "7438 Muirfield Pl, Indianapolis, IN 46237",
# "7334 Muirfield Pl, Indianapolis, IN 46237",
# "7318 Muirfield Pl, Indianapolis, IN 46237",
# "7314 Carrie Dr, Indianapolis, IN 46237",
# "6209 Carrie Cir, Indianapolis, IN 46237",
# "6241 Carrie Cir, Indianapolis, IN 46237",
# "6249 Carrie Cir, Indianapolis, IN 46237",
# "7384 Southern Lakes Dr, Indianapolis, IN 46237",
# "7410 Southern Lakes Dr, Indianapolis, IN 46237",
# "7352 Southern Lakes Dr N, Indianapolis, IN 46237",
# "6438 Southern Lakes Dr, Indianapolis, IN 46237",
# "6458 Southern Lakes Dr N, Indianapolis, IN 46237",
# "6466 Southern Lakes Dr N, Indianapolis, IN 46237",
# "7321 Bruin Dr, Indianapolis, IN 46237",
# "6628 Wolverine Way, Indianapolis, IN 46237",
# "7274 Bobcat Trail Dr, Indianapolis, IN 46237",
# "7131 Bobcat Trail Dr, Indianapolis, IN 46237",
# "6622 Cougar Ct, Indianapolis, IN 46237",
# "7216 Sycamore Run Dr, Indianapolis, IN 46237",
# "7208 Sycamore Run Dr, Indianapolis, IN 46237",
# "7132 Sycamore Run Dr, Indianapolis, IN 46237",
# "7129 Sycamore Run Dr, Indianapolis, IN 46237",
# "7123 Sycamore Run Dr, Indianapolis, IN 46237",
# "7117 Sycamore Run Dr, Indianapolis, IN 46237",
# "7111 Sycamore Run Dr, Indianapolis, IN 46237",
# "7053 Sycamore Run Dr, Indianapolis, IN 46237",
# "7026 Sycamore Run Dr, Indianapolis, IN 46237",
# "7037 Lavender Ct, Indianapolis, IN 46237",
# "7043 Lavender Ct, Indianapolis, IN 46237",
# "7049 Lavender Ct, Indianapolis, IN 46237",
# "7048 Lavender Ct, Indianapolis, IN 46237",
# "5407 Chico Grey Dr, Indianapolis, IN 46237",
# "5423 Chico Grey Dr, Indianapolis, IN 46237",
# "6403 Mack Farm Ln, Indianapolis, IN 46237",
# "6411 Mack Farm Ln, Indianapolis, IN 46237",
# "6325 Mack Farm Ln, Indianapolis, IN 46237",
# "6315 Mack Farm Ln, Indianapolis, IN 46237",
# "6232 Mack Farm Ln, Indianapolis, IN 46237",
# "6237 Sampson Ct, Indianapolis, IN 46237",
# "6231 Sampson Ct, Indianapolis, IN 46237",
# "6219 Simien Rd, Indianapolis, IN 46237",
# ]

headers = {
    "accept": "application/json",
    "x-regrid-token": "eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJyZWdyaWQuY29CjLDr2xFXSIR0kwEorVgJTZH3dO2shQ",
}
house_areas = []
house_coordinate = []
for count, address in enumerate(addresses, start=786):
    params = {"query": address}

    response = requests.get(url, params=params, headers=headers)
    # with open("json_data.txt", "a") as file:
    # file.write(f"Response:{response}\n")

    # print(response)
    if response.status_code == 200:
        data = response.json()
        with open(f"Batch_5_json_data/{address}.json", "w") as json_file:
            json.dump(data, json_file)
        # with open("json_data.txt", "a") as file:
        # file.write(f"data:{data}\n")
        # print("data", data)
        # print(data)
        try:
            # if count==1 or count==2:
            # print(data,"\n")
            coordinates = data["results"][0]["geometry"]["coordinates"][0]
            total_area = data["results"][0]["properties"]["fields"]["ll_gissqft"]
            try:
                house_coordinates = data["buildings"][0]["geometry"]["coordinates"][0]
                house_area = data["results"][0]["properties"]["fields"][
                    "ll_bldg_footprint_sqft"
                ]
            except:
                house_coordinates = 0
                house_area = 0

            # print("Area coordinates: ", coordinates)
            goole_image_hybrid_roadmap.getimage_google(coordinates, count, address)

            # house_areas.append(house_area)
            # house_coordinate.append(house_coordinates)
            # print("Total House area:", house_area)
            find_area.cal_area(coordinates, address)
            with open(f"Batch_5_text_data/areas_{address}.txt", "w") as file:
                file.write(
                    "Address:"
                    + f"{address}"
                    + "\n"
                    + "Total Area:"
                    + f"{total_area}"
                    + "\n"
                    + "Total Coordinates:"
                    + f"{coordinates}"
                    + "\n"
                    + "House Area:"
                    + f"{house_area}"
                    + "\n"
                    + "House Coordinates:"
                    + f"{house_coordinates}"
                )

        except IndexError:
            print(address)

    else:
        print(f"Error getting data for {address}: {response.status_code}")
        # pass
# for  in house_areas:
