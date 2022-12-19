import cv2
import matplotlib.pyplot as plt
import numpy as np
import keras



class Recognizer:
    def __init__(self, path) -> None:
        self.path = path
        self.model = keras.models.load_model('cnn_rest.h5')



    def recognize(self):
        test_img = cv2.imread(self.path)
        gray_test = cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY)
        gray_test = cv2.resize(gray_test,(200,200),interpolation=cv2.INTER_LANCZOS4)
        gray_test = gray_test / 255.0
        plt.imshow(gray_test)
        gray_test = gray_test[np.newaxis]

        return np.argmax(self.model.predict(gray_test))
    