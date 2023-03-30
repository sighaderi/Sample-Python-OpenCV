import cv2

# Load the image from file
image = cv2.imread("input.jpg")

# Check for failure
if image is None:
    print("Could not open or find the image")
    exit()

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to the image
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Apply Canny edge detection to the image
edges = cv2.Canny(blurred_image, 50, 150)

# Save the output image
cv2.imwrite("output.jpg", edges)

# Display the input and output images
cv2.imshow("Input Image", image)
cv2.imshow("Output Image", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
