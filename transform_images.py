
from pyspark import SparkContext
from PIL import Image
from StringIO import StringIO
import time
import os
import argparse


def read_image(path):
    images = sc.binaryFiles(path)
    return images

def save_image(value):
    output_path = os.path.join(os.getcwd(), "Output/")
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    value.save("%s/%d.ppm"%(output_path, int(time.time()*1000)))

def form_image(value):
    image = Image.open(StringIO(value))
    return image

def transform_image(image):
    transformed_image = image.rotate(45).resize((128,128))
    return transformed_image

def main():
    # Initializing Spark Context
    global sc
    sc = SparkContext("local", "first app")

    path = os.path.join(os.getcwd(), "Testing/00000/*.ppm")
    print "-------------------------------------------------"
    print(path)
    print os.getcwd()
    # Reading the image in binary stream format
    binary_images = read_image(path)

    # Creating image object
    images_rdd = binary_images.values().map(form_image)

    # Transforming the images
    transformed_images_rdd = images_rdd.map(transform_image)

    # Saving the image
    transformed_images_rdd.foreach(save_image)


# Entry point for PySpark Transform Images Application
if __name__ == '__main__':
    main()


