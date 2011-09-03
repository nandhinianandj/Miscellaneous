## Basic code sample adopted from http://opencv.willowgarage.com/documentation/python/cookbook.html

#TODO: Use object identifications. And then try to train an ML algorithm for those objects.
import os
import cv
import sys
from copy import deepcopy

def detect_face():
    storage = cv.CreateMemStorage()
    haar = cv.LoadHaarClassifierCascade('haarcascade_frontalface_default.xml')
    detected = cv.HaarDetectObjects(image,haar,storage, 2,cv.CV_HAAR_DO_CANNY_PRUNING,(100,100))
    return detected

def move_images_to_folder(from_folder,to_folder):
    # for file in
    #for file_tuple in os.walk(from_folder)
    pass

def check_image_size(image,size):
    image = cv.LoadImageM(image)
    if image.cols < size[0] and image.rows < size[1]:
        return True
    else:
        return False

def delete_small_images(folder,size):
    for img_file in os.listdir(folder):
        if not os.path.isdir(os.path.join(folder,img_file)):
            if check_image_size(os.path.join(folder,img_file),size):
                os.remove(os.path.join(folder,img_file))
                print "Removing file:" + os.path.join(folder,img_file)


def good_features():

    base_path = os.path.dirname(sys.argv[1])
    pics = os.listdir(sys.argv[1])

    try:
        os.mkdir(os.path.join(base_path,"OpenCV_BestFeatures"))
    except Exception,e:
        if e.args == 17:
            pass

    for picture in pics:
        BestFeatures = []
        image = cv.LoadImageM(os.path.join(sys.argv[1],picture))
        img_gray = cv.LoadImageM(os.path.join(sys.argv[1],picture),cv.CV_LOAD_IMAGE_GRAYSCALE)
        eig_image = cv.CreateMat(img_gray.rows,img_gray.cols,cv.CV_32FC1)
        temp_image = deepcopy(eig_image)

        x_coordinates = []
        y_coordinates = []


        for (x,y) in cv.GoodFeaturesToTrack(img_gray,eig_image,temp_image,5,0.04,10.0,useHarris = True):
            BestFeatures.append((x,y))


        for feature in BestFeatures:
            x_coordinates.append(feature[0])
            y_coordinates.append(feature[1])


        sub_image = cv.GetSubRect(image,(int(min(x_coordinates)),int(min(y_coordinates)),int(max(x_coordinates)),int(max(y_coordinates))))
        cv.SaveImage(os.path.join(base_path,"OpenCV_BestFeatures",picture))


def main():
    size = (1600,1200)
    if sys.argv[1] == 'goodfeatures':
        goodfeatures()
    elif sys.argv[1] == 'delete':
        delete_small_images(sys.argv[2],size)


if __name__ == '__main__':
    main()
