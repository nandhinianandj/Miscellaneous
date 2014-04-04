#include<opencv2/highgui/highgui.hpp>

using namespace cv;

int main()
{
    Mat img = imread("image.jpg");
    imshow("opencvtest1",img);
    waitKey(0);
    return 0;
}
