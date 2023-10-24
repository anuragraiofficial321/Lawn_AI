from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    send_file,
    abort,
    jsonify,
)
import pandas as pd
from regrid import get_image
from yolo_detection import predict_image
import shutil
import os
import glob
import base64
from PIL import Image


app = Flask(__name__)

global lawn_area
global total_area
global driveway_pixel


@app.errorhandler(404)
def file_not_found(error):
    return "File Not Found", 404


def serve_file(file_path, download_name):
    try:
        return send_file(file_path, as_attachment=True, download_name=download_name)
    except FileNotFoundError:
        abort(404)


@app.route("/download_data")
def download_system_message():
    source_folder = "Property_Data"
    zip_filename = "Property_Data.zip"

    try:
        shutil.make_archive(zip_filename, "zip", source_folder)
    except FileNotFoundError:
        abort(404)

    return serve_file(f"{zip_filename}.zip", download_name=zip_filename)


@app.route("/")
def index():
    try:
        total_area = 0
        lawn_area = 0
        for filename in glob.glob("mask*"):
            os.remove(filename)
        shutil.rmtree("runs")
        os.remove("static/images/image0.jpg")
        shutil.rmtree("static/images/image0.jpg")
    except:
        pass
    return render_template("start.html")


@app.route("/submit", methods=["GET", "POST"])
def submit():
    total_area = 0
    driveway_pixel = 0
    driveway_area = 0
    lawn_area = 0
    address = ""
    try:
        for filename in glob.glob("mask*"):
            os.remove(filename)
        os.remove("static/images/image0.jpg")
        shutil.rmtree("static/images/image0.jpg")
        shutil.rmtree("runs")
    except:
        pass
    if request.method == "POST":
        # Get the text input from the form
        total_area = 0
        driveway_pixel = 0
        driveway_area = 0
        lawn_area = 0
        address = ""
        user_text = request.form["user_text"]
        address = user_text.strip()
        # print("Addressess = ", address)
        image_address, total_area, house_area, coordinates = get_image(address)
        driveway_house_pixel, house_pixel, driveway_pixel = predict_image(image_address)
        # print(image_address)
        print("Driveway pixel:", driveway_pixel)
        driveway__house_area_sqft = round(
            driveway_house_pixel * ((house_area + 1280) / (house_pixel)) * 0.5 - 1800
        )
        if driveway_pixel != 0:
            driveway_area = round(driveway_pixel * ((house_area) / (house_pixel)) - 190)
        # print(((house_area) / (house_pixel)))
        # driveway_area = driveway_pixel
        # driveway_area = driveway_pixel * 0.0582
        lawn_area = round(total_area - driveway__house_area_sqft)
        total_area = round(total_area)
        house_area = round(house_area)

        # print("Driveway = ", driveway_area)
        # lawn_area = lawn_area - lawn_area / 4
        #     (total_area - 1234)
        #     - driveway_area * 0.5
        #     - (35 / 100) * (total_area - driveway_area)
        # )
        print("Total area: ", total_area)
        print("Driveway + House area:", driveway_pixel)
        print("Lawn area:", lawn_area)
        try:
            shutil.copy("runs/segment/predict/image0.jpg", "static/images")
            shutil.copy("runs/segment/predict/image0.jpg", "Property_Data")

        except:
            pass
        coordinates = [{"lat": lat, "lng": lng} for lng, lat in coordinates]

        # Download

        data = {
            "Property": [
                "Address",
                "Total Area",
                "House Area",
                "Lawn Area",
                "Driveway Area",
            ],
            "Area in sqft": [
                address,
                total_area,
                house_area,
                lawn_area,
                driveway_area,
            ],
        }

        df = pd.DataFrame(data)

        excel_file = "Property_Data/property_data.xlsx"
        df.to_excel(excel_file, index=False)

        # return redirect("/display")
        return render_template(
            "googlemap.html",
            address=address,
            coordinates=coordinates,
            house_area=house_area,
            total_area=total_area,
            lawn_area=lawn_area,
            driveway_area=driveway_area,
        )
        # return render_template("index1.html", coordinates="done")

    return render_template("error.html")


@app.route("/display")
def display():
    total_area = 0
    lawn_area = 0
    return render_template("index1.html", total_area=total_area, lawn_area=lawn_area)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
