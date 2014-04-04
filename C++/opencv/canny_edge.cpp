# include <cv.h>
# include <highgui.h>

int main(int argc, char **argv)
{
    IplImage *img = cvLoadImage("image.jpg",0);
    cvNamedWindow("example-input");
    cvNamedWindow("example-output");

    cvShowImage("example-input",img);

    assert(img->width%2 == 0 && img->height%2 == 0);

    IplImage* out = cvCreateImage(cvSize(img->width/2,img->height/2),img->depth,img->nChannels );

    cvPyrDown(img,out);

    cvCanny(out,out,10,100,3);

    cvShowImage("example-output",img);

    cvWaitKey(0);
    cvReleaseImage(&img);
    cvReleaseImage(&out);
    cvDestroyWindow("example-output");
    cvDestroyWindow("example-input");

    return 0;

}
