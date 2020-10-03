from spacecomms.image_comms import *

# Encrypts the image
encrypt_image("images/oppy.jpg")

encrypt_image("images/oppy_fake.jpg", "image_storage/baz")

# Check for the matching signature
oppy_sig = get_signature("image_storage/bar")
oppy_fake_sig = get_signature("image_storage/baz")

if oppy_sig == oppy_fake_sig:
    print("Same image.")
else:
    print("Not same.")
