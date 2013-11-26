#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <cv.h>
#include <highgui.h>

int main(int argc, char *argv[])
{
    IplImage* img = 0;
    int height,width,step,channels;
    uchar *data;
    int i,j,k;

    img = cvLoadImage("image.jpg");
    if(!img) {
        printf("Could not load image file:%s\n",argv[1]);
        exit(0);
    }

    height = img->height;
    width = img->width;
    step = img->widthStep;
    channels = img->nChannels;
    data = (uchar *)img->imageData;
    printf("Processing a %dx %d image with %d channels with step %d\n",height,width,channels,step);

    cvNamedWindow("example2",CV_WINDOW_AUTOSIZE);
    cvMoveWindow("example2",100,100);

    for(i=0;i<height;i++)
        for(j=0;j<width;j++)
            for(k=0;k<channels; k++)
                data[i*step+j*channels+k] = 255-data[i*step+j*channels+k];
    cvShowImage("example2",img);

    cvWaitKey(0);

    cvReleaseImage(&img);
    cvDestroyWindow("example2");
    return 0;

}
