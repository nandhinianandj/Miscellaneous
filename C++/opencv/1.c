#include <stdio.h>
#include <iostream>

#include <opencv2/core/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>

using namespace cv;
using namespace std;

#define DEMO_MIXED_API_USE


int main(int argc, char **argv)
{
    const char * imagename = argc > 1 ? argv[1] : "lena.jpg";
    #ifdef DEMO_MIXED_API_USE
        Ptr<IplImage> IplI = cvLoadImage(imagename);

        if(IplI.empty())
        {
            cerr << "Can not load image"  <<imagename <<endl;
            return -1;
        }
        Mat I();
    #else
        Mat I = imread(imagename);
        if(I.empty())
        {
            cerr << "Can not load image"  <<imagename <<endl;
            return -1;
        }

    #endif
}

