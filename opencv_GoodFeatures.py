## Basic code sample adopted from http://opencv.willowgarage.com/documentation/python/cookbook.html

#TODO: Use object identifications. And then try to train an ML algorithm for those objects.
import os
import cv
import sys
from copy import deepcopy
import pdb

def main():

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

        pdb.set_trace()

        for (x,y) in cv.GoodFeaturesToTrack(img_gray,eig_image,temp_image,10,0.04,1.0,useHarris = True):
            BestFeatures.append((x,y))
        

        for feature in BestFeatures:
            x_coordinates.append(feature[0])
            y_coordinates.append(feature[1])

            
        sub_image = cv.GetSubRect(image,(int(min(x_coordinates)),int(min(y_coordinates)),int(max(x_coordinates)),int(max(y_coordinates))))
        cv.SaveImage(os.path.join(base_path,"OpenCV_BestFeatures",picture))


if __name__ == '__main__':
    main()
