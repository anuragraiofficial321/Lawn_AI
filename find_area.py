import pyproj


def cal_area(coordinates, address):
    # Define the UTM projection for the contiguous United States (Zone 15)
    utm_projection = pyproj.Proj(proj="utm", zone=14, ellps="WGS84")

    # Coordinates of the polygon (example coordinates)
    # coordinates = [
    # ]
    # Convert the coordinates to UTM in feet
    converted_coordinates = [utm_projection(lon, lat) for lon, lat in coordinates]

    # Calculate the area using the shoelace formula
    def calculate_polygon_area(vertices):
        n = len(vertices)
        area = 0.0
        for i in range(n - 1):
            x1, y1 = vertices[i]
            x2, y2 = vertices[i + 1]
            area += x1 * y2 - x2 * y1
        x1, y1 = vertices[n - 1]
        x2, y2 = vertices[0]
        area += x1 * y2 - x2 * y1
        area = abs(area) / 2.0
        return area

    # Calculate the area in square meters
    area_in_square_meters = calculate_polygon_area(converted_coordinates)

    # Convert the area to square feet (1 square meter = 10.7639 square feet)
    area_in_square_feet = area_in_square_meters * 10.7639

    with open(f"Batch_5_Manual_Calculation_area/batch_5.txt", "a") as fi:
        fi.write(
            f"{address} \n\n {coordinates} \n\n {area_in_square_feet}:square feet \n\n"
        )

    print(
        "The area of the polygon is approximately", area_in_square_feet, "square feet"
    )


'''import pyproj

# Define the UTM projection for the contiguous United States (Zone 15)
utm_projection = pyproj.Proj(proj="utm", zone=14, ellps="WGS84")

# Coordinates of the polygon
coordinates = [
    [-96.56379761499994, 32.8350655150001],
    [-96.563776413, 32.8349288110001],
    [-96.56399117099994, 32.8349056380001],
    [-96.564001406, 32.8349716330001],
    [-96.564018361, 32.834969804],
    [-96.564013974, 32.83494152],
    [-96.564053084, 32.8349373],
    [-96.56405656, 32.8349656840001],
    [-96.564069288, 32.8350362],
    [-96.56379761499994, 32.8350655150001],
]

# Convert the coordinates to UTM in feet
converted_coordinates = [utm_projection(lon, lat) for lon, lat in coordinates]


# Calculate the area using the shoelace formula
def calculate_polygon_area(vertices):
    n = len(vertices)
    area = 0.0
    for i in range(n - 1):
        x1, y1 = vertices[i]
        x2, y2 = vertices[i + 1]
        area += x1 * y2 - x2 * y1
    x1, y1 = vertices[n - 1]
    x2, y2 = vertices[0]
    area += x1 * y2 - x2 * y1
    area = abs(area) / 2.0
    return area


# Calculate the area in square meters
area_in_square_meters = calculate_polygon_area(converted_coordinates)

# Convert the area to square feet (1 square meter = 10.7639 square feet)
area_in_square_feet = area_in_square_meters * 10.7639

print("The area of the polygon is approximately", area_in_square_feet, "square feet")

"""If the area you are interested in is located in the western part of the United States, then you would use UTM Zone 15. If the area is located in the eastern part of the United States, then you would use UTM Zone 14."""
'''
