# Spacecomms

This is a concept of transmitting image as text file with unique signature of each file.

The code is developed as a part of NASA Space App challenge 2020.

## Installations

Install virtual environment: `pip install virtualenv`

If there are some errors while installing `virtualenv` try:
`pip install virtualenv --ignore-installed`

Once inside the root project directory create a virtual environment:

**MAC Instructions**:

`virtualenv venv`

Activate virtualenv: `source venv/bin/activate`


**Windows Instructions**:

Type to create a virtual environment:
`python -m vevn venv`

Type to activate virtual environment:
`venv\Scripts\activate`

### Install dependencies

`pip install -r requirements.txt`

## Usage

There are two images of Opportunity rover in `images` directory.

Call the functions in python terminal:

* Make sure you have activated virtual environment.

* Import the  `spacecomms` python module: `from spacecomms.image_comms import *`

## Example

The following code reads the image `oppy.jpg` from `images` directory and stores the signature and text files in `image_storage/encrypted_files` by default.

You can provide any path you want. Use `help()` with the funtion name while in the python console.

Example: `help(encypt_image)`

**OUTPUT**:

```
Help on function encrypt_image in module spacecomms.image_comms:

encrypt_image(image, directory='image_storage/encrypted_files')
    Creates text files out of the images and a signature using encryption.
    Every channel of the image is stored in a separate text file.
    The output will be stored in the `directory` which is default to `image_storage/encrypted_files`.
    
    :param image: Image to be encrypted.
    :param derectory: Path to store the files (DEFAULT="image_storage/encrypted_files").
(END)
```

Press `q` to exit.

**Encryption**:

```
from spacecomms.image_comms import *

encrypt_image("images/oppy.jpg")
```

**Decryption**:

```
decrypt_image("image_storage/encrypted_files")
```
