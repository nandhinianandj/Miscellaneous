#include <cv.h>
#include <highgui.h>

int main(int argc, char* argv[])
{
    IplImage* img = cvLoadImage("image.jpg");
    cvNamedWindow("example_input");

    cvNamedWindow("example_output");
    cvShowImage("example_input",img);

    IplImage* out = cvCreateImage(cvGetSize(img),IPL_DEPTH_8U,3);

    cvSmooth(img,out,CV_GAUSSIAN,15,15);

    cvShowImage("example_output",out);

    cvWaitKey(0);
    cvReleaseImage(&img);
    cvReleaseImage(&out);
    cvDestroyWindow("example_input");
    cvDestroyWindow("example_output");
    return 0;
}

