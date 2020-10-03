import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
import hashlib
import os
import zipfile


def encrypt_image(image, directory="image_storage/encrypted_files"):
    """
    :param image: Image to be encrypted
    :param derectory: Path to store the files.
    """

    img = cv2.imread(image)

    blue, green, red = cv2.split(img)


    if not os.path.exists(directory):
        os.mkdir(directory)
    else:
        print(f"Directory: {directory} already exists!")
        response = input("Do you wish to override? (y/n): ")
        if response == "n":
            sys.exit(0)

    blue_path = directory + "/" + "blue.txt"
    green_path = directory + "/" + "green.txt"
    red_path = directory + "/" + "red.txt"

    np.savetxt(blue_path, blue, fmt="%d")
    np.savetxt(green_path, green, fmt="%d")
    np.savetxt(red_path, red, fmt="%d")

    img_flatten = img.flatten()

    signature = hashlib.sha256(img_flatten).hexdigest()

    with open(directory + "/" + "signature.txt", "w") as file:
        file.write(signature)


def get_signature(directory):
    """
    :param directory: Directory where the signature file is located.
    :returns signature: signature created using image.
    """

    path = directory + "/" + "signature.txt"

    try:
        with open(path, "r") as file:
            signature = file.read()
            return signature

    except FileNotFoundError:
        print("Signature does not exist!")

def verify_signature(signature, directory):
    """
    :param signature: Hash of signature to verify.
    :param directory: Directory where the signature of image is placed.

    :return boolean: True if the signature matches.
    """

    present_signature = get_signature(directory)

    if present_signature == signature:
        return True
    else:
        return False


def decrypt_image(directory):
    """
    :param directory: directory to read the image files from.
    """

    blue_path = directory + "/" + "blue.txt"
    green_path = directory + "/" + "green.txt"
    red_path = directory + "/" + "red.txt"

    blue = np.loadtxt(blue_path)
    green = np.loadtxt(green_path)
    red = np.loadtxt(red_path)

    image = cv2.merge((blue, green, red))

    cv2.imwrite(directory + "/" + "image.jpg", image)
