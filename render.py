import os
import cv2
import sys
import numpy as np
import time



filename = sys.argv[1]
manip = sys.argv[2]

img = cv2.imread('../' + filename)
dimensions = img.shape
img_manip = cv2.resize(img, (dimensions[1], dimensions[0]))

white = [255, 255, 255]

start_time = time.time()

for x in range(dimensions[0]):
    for y in range(dimensions[1]):
        if manip == 'flip':
            img_manip[x, y] = img[dimensions[0] - 1 - x, y]
            output_filename = 'flip_image.jpg'
        elif manip == 'mirror':
            img_manip[x, y] = img[x, dimensions[1] - 1 - y]
            output_filename = 'mirror_image.jpg'
        elif manip == 'invert':
            pixel = img[x, y]
            inverted_pixel = (255 - pixel[0], 255 - pixel[1], 255 - pixel[2])
            img_manip[x, y] = inverted_pixel
            output_filename = 'invert_image.jpg'
            pass

end_time = time.time()
processing_time = end_time - start_time
# Print the processing time to the console
print("Processing time: {:.2f} seconds".format(processing_time))

# Save the manipulated image in the same folder as the script
script_directory = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_directory, output_filename)
cv2.imwrite(output_path, img_manip)

image = 'Original image'
cv2.namedWindow(image)
cv2.moveWindow(image, 0, 0)
cv2.imshow(image, img)
# Display the manipulated image alongside the original image.
image2 = 'Manipulated image'
cv2.namedWindow(image2)
cv2.moveWindow(image2, dimensions[1], 0)
cv2.imshow(image2, img_manip)


while True:
    k = cv2.waitKey(1)
    if k == 27:
        cv2.destroyAllWindows()
        exit()