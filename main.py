import cv2
import numpy as np
from tkinter import Tk, filedialog, Button, Label

def select_image():
    global img1, file_path
    file_path = filedialog.askopenfilename()
    if file_path:
        img1 = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        label_img.config(text="Image 1: {}".format(file_path.split('/')[-1]))

def select_image_2():
    global img2, file_path_2
    file_path_2 = filedialog.askopenfilename()
    if file_path_2:
        img2 = cv2.imread(file_path_2, cv2.IMREAD_GRAYSCALE)
        label_img_2.config(text="Image 2: {}".format(file_path_2.split('/')[-1]))

def Feature_matching():
    if img1 is None or img2 is None:
        return

    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(img1, None)