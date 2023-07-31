import joblib
import numpy as np
import base64
import cv2
import pywt

__model = None

def load_saved_artifacts():
    global __model
    # Load the pre-trained machine learning model
    __model = joblib.load("path/to/model.joblib")

def w2d(img, mode='haar', level=1):
 
    imArray = img
    
    imArray = np.float32(imArray)
    imArray /= 255
    
    coeffs = pywt.wavedec2(imArray, mode, level=level)

    coeffs_H = list(coeffs)
    coeffs_H[0] *= 0

    imArray_H = pywt.waverec2(coeffs_H, mode)
    imArray_H *= 255
    imArray_H = np.uint8(imArray_H)

    return imArray_H

def convert_image(image_base64_data, file_path=None):
    img = get_cv2_image(image_base64_data, file_path)
    img_har = w2d(img, 'db1', 5)
    pred = __model.predict(img_har.reshape(1, -1))[0]
    return pred 
def get_cv2_image(image_base64_data, file_path=None):
    if file_path:
        img = cv2.imread(file_path)
    else:
        decoded_data = base64.b64decode(image_base64_data.split(",")[1])
        np_data = np.frombuffer(decoded_data, np.uint8)
        img = cv2.imdecode(np_data, cv2.IMREAD_UNCHANGED)
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

