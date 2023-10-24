import csv

# Set the paths to your text files
file1_path = "house_areas.txt"
file2_path = "house_pixels.txt"
output_csv_path = "output.csv"


# Function to read a text file and handle division by zero
def read_file(file_path):
    data = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                value = float(line.strip()) if float(line.strip()) != 0 else 0
                data.append(value)
        return data
    except (ValueError, FileNotFoundError):
        return []


# Read data from both files
data1 = read_file(file1_path)
data2 = read_file(file2_path)

# Create a CSV file and write the data
with open(output_csv_path, "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(
        ["Area Covered by the house", "Total number of pixels", "Division Result"]
    )

    # Ensure both lists have the same length
    min_length = min(len(data1), len(data2))

    for i in range(min_length):
        divisor = data2[i]
        if data2[i] != 0:
            division_result = data1[i] / divisor
            csv_writer.writerow([data1[i], data2[i], division_result])

        else:  # Avoid division by zero
            division_result = 0
            csv_writer.writerow([data1[i], data2[i], division_result])
