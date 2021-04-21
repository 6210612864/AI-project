import cv2 as cv
import os
import shutil


def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    return images


def main():
    path = "NORMAL"
    count = 0
    for img in load_images_from_folder(path):
        
        cv.waitKey(0)

        #r = 255 / img.shape[1]
        dim = (400,400) #int(img.shape[0] * r))
        # perform the actual resizing of the image and show it
        resized = cv.resize(img, dim, interpolation=cv.INTER_AREA)

        
        cv.imwrite("thumbnail.png", resized)

        data = [x for x in os.listdir(path)]
        if ".JPG" in data[count]:
            new = data[count].strip(".JPG")
        elif ".jpg" in data[count]:
            new = data[count].strip(".jpg")
        elif ".png" in data[count]:
            new = data[count].strip(".png")
        elif ".tif" in data[count]:
            new = data[count].strip(".tif")
        count += 1

        destination = "CROP/" + new + "_crop.jpg"
        shutil.move("thumbnail.png", destination)
        cv.waitKey(0)


main()
