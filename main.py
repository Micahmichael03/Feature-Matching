import cv2  # Import OpenCV library for computer vision tasks
import numpy as np  # Import NumPy library for numerical operations
from tkinter import Tk, filedialog, Button, Label  # Import necessary modules from Tkinter for GUI

def select_image():
    global img1, file_path  # Declare global variables to store the image and file path
    file_path = filedialog.askopenfilename()  # Open file dialog to select an image file
    if file_path:  # If a file is selected
        img1 = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)  # Read the image in grayscale
        label_img.config(text="Image 1: {}".format(file_path.split('/')[-1]))  # Update label with the selected file name

def select_image_2():
    global img2, file_path_2  # Declare global variables to store the image and file path
    file_path_2 = filedialog.askopenfilename()  # Open file dialog to select an image file
    if file_path_2:  # If a file is selected
        img2 = cv2.imread(file_path_2, cv2.IMREAD_GRAYSCALE)  # Read the image in grayscale
        label_img_2.config(text="Image 2: {}".format(file_path_2.split('/')[-1]))  # Update label with the selected file name

def Feature_matching():
    if img1 is None or img2 is None:  # Check if both images are selected
        return  # Exit the function if any image is not selected

    orb = cv2.ORB_create()  # Create ORB detector
    keypoints1, descriptors1 = orb.detectAndCompute(img1, None)  # Detect keypoints and compute descriptors for the first image
    keypoints2, descriptors2 = orb.detectAndCompute(img2, None)  # Detect keypoints and compute descriptors for the second image

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)  # Create BFMatcher object with Hamming distance and cross-check
    matches = bf.match(descriptors1, descriptors2)  # Match descriptors between the two images

    matches = sorted(matches, key = lambda x:x.distance)  # Sort matches based on distance

    img_matches = cv2.drawMatches(img1, keypoints1, img2, keypoints2, matches[:50], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)  # Draw the top 50 matches

    cv2.imshow("Matches", img_matches)  # Display the matches
    cv2.waitKey(0)  # Wait for a key press
    cv2.destroyAllWindows()  # Close all OpenCV windows

root = Tk()  # Create the main window
root.title('Feature Matching')  # Set the window title

img1 = None  # Initialize img1 as None
img2 = None  # Initialize img2 as None

btn_select_image1 = Button(root, text="Select Image 1", command=select_image)  # Create button to select the first image
btn_select_image1.pack()  # Add the button to the window

label_img = Label(root, text="Image 1: Not selected")  # Create label to display the status of the first image
label_img.pack()  # Add the label to the window

btn_select_image2 = Button(root, text="Select Image 2", command=select_image_2)  # Create button to select the second image
btn_select_image2.pack()  # Add the button to the window

label_img_2 = Label(root, text="Image 2: Not selected")  # Create label to display the status of the second image
label_img_2.pack()  # Add the label to the window

btn_match_features = Button(root, text="Match Features", command=Feature_matching)  # Create button to start feature matching
btn_match_features.pack()  # Add the button to the window

root.mainloop()  # Start the Tkinter event loop