Just inside of Makefile

change

ifeq ($(OPENCV), 1) Just inside of Makefile

change

ifeq ($(OPENCV), 1) 
COMMON+= -DOPENCV
CFLAGS+= -DOPENCV
LDFLAGS+= `pkg-config --libs opencv` -lstdc++
COMMON+= `pkg-config --cflags opencv` 
endif
to

ifeq ($(OPENCV), 1) 
COMMON+= -DOPENCV
CFLAGS+= -DOPENCV
LDFLAGS+= `pkg-config --libs opencv4` -lstdc++
COMMON+= `pkg-config --cflags opencv4` 
endif

after that you'll have this problem: ./src/image_opencv.cpp:12:1: error: ‘IplImage’ does not name a type; did you mean ‘image’?

but you can solve it using the solution #1347 (comment)

in file ./src/image_opencv.cpp

add these two functions

Mat image_to_mat(image im)
{
image copy = copy_image(im);
constrain_image(copy);
if(im.c == 3) rgbgr_image(copy);

Mat m(cv::Size(im.w,im.h), CV_8UC(im.c));
int x,y,c;

int step = m.step;
for(y = 0; y < im.h; ++y){
    for(x = 0; x < im.w; ++x){
        for(c= 0; c < im.c; ++c){
            float val = im.data[c*im.h*im.w + y*im.w + x];
            m.data[y*step + x*im.c + c] = (unsigned char)(val*255);
        }
    }
}

free_image(copy);
return m;

}

image mat_to_image(Mat m)
{

int h = m.rows;
int w = m.cols;
int c = m.channels();
image im = make_image(w, h, c);
unsigned char *data = (unsigned char *)m.data;
int step = m.step;
int i, j, k;

for(i = 0; i < h; ++i){
    for(k= 0; k < c; ++k){
        for(j = 0; j < w; ++j){
            im.data[k*w*h + i*w + j] = data[i*step + j*c + k]/255.;
        }
    }
}
rgbgr_image(im);
return im;

}

AFTER THAT REMOVE THESE THREE FUNCTIONS

/*
IplImage *image_to_ipl(image im)
{
    int x,y,c;
    IplImage *disp = cvCreateImage(cvSize(im.w,im.h), IPL_DEPTH_8U, im.c);
    int step = disp->widthStep;
    for(y = 0; y < im.h; ++y){
        for(x = 0; x < im.w; ++x){
            for(c= 0; c < im.c; ++c){
                float val = im.data[c*im.h*im.w + y*im.w + x];
                disp->imageData[y*step + x*im.c + c] = (unsigned char)(val*255);
            }
        }
    }
    return disp;
}

image ipl_to_image(IplImage* src)
{
    int h = src->height;
    int w = src->width;
    int c = src->nChannels;
    image im = make_image(w, h, c);
    unsigned char *data = (unsigned char *)src->imageData;
    int step = src->widthStep;
    int i, j, k;

    for(i = 0; i < h; ++i){
        for(k= 0; k < c; ++k){
            for(j = 0; j < w; ++j){
                im.data[k*w*h + i*w + j] = data[i*step + j*c + k]/255.;
            }
        }
    }
    return im;
}

Mat image_to_mat(image im)
{
    image copy = copy_image(im);
    constrain_image(copy);
    if(im.c == 3) rgbgr_image(copy);

    IplImage *ipl = image_to_ipl(copy);
    Mat m = cvarrToMat(ipl, true);
    cvReleaseImage(&ipl);
    free_image(copy);
    return m;
}

image mat_to_image(Mat m)
{
    IplImage ipl = m;
    image im = ipl_to_image(&ipl);
    rgbgr_image(im);
    return im;
}*/

and remove all CV_ from opencv flags, for example:

    if(w) cap->set(CV_CAP_PROP_FRAME_WIDTH, w);
    if(h) cap->set(CV_CAP_PROP_FRAME_HEIGHT, w);
    if(fps) cap->set(CV_CAP_PROP_FPS, w);

to

    if(w) cap->set(CAP_PROP_FRAME_WIDTH, w);
    if(h) cap->set(CAP_PROP_FRAME_HEIGHT, w);
    if(fps) cap->set(CAP_PROP_FPS, w);
COMMON+= -DOPENCV
CFLAGS+= -DOPENCV
LDFLAGS+= `pkg-config --libs opencv` -lstdc++
COMMON+= `pkg-config --cflags opencv` 
endif
to

ifeq ($(OPENCV), 1) 
COMMON+= -DOPENCV
CFLAGS+= -DOPENCV
LDFLAGS+= `pkg-config --libs opencv4` -lstdc++
COMMON+= `pkg-config --cflags opencv4` 
endif

after that you'll have this problem: ./src/image_opencv.cpp:12:1: error: ‘IplImage’ does not name a type; did you mean ‘image’?

but you can solve it using the solution #1347 (comment)

in file ./src/image_opencv.cpp

add these two functions

Mat image_to_mat(image im)
{
image copy = copy_image(im);
constrain_image(copy);
if(im.c == 3) rgbgr_image(copy);

Mat m(cv::Size(im.w,im.h), CV_8UC(im.c));
int x,y,c;

int step = m.step;
for(y = 0; y < im.h; ++y){
    for(x = 0; x < im.w; ++x){
        for(c= 0; c < im.c; ++c){
            float val = im.data[c*im.h*im.w + y*im.w + x];
            m.data[y*step + x*im.c + c] = (unsigned char)(val*255);
        }
    }
}

free_image(copy);
return m;

}

image mat_to_image(Mat m)
{

int h = m.rows;
int w = m.cols;
int c = m.channels();
image im = make_image(w, h, c);
unsigned char *data = (unsigned char *)m.data;
int step = m.step;
int i, j, k;

for(i = 0; i < h; ++i){
    for(k= 0; k < c; ++k){
        for(j = 0; j < w; ++j){
            im.data[k*w*h + i*w + j] = data[i*step + j*c + k]/255.;
        }
    }
}
rgbgr_image(im);
return im;

}

AFTER THAT REMOVE THESE THREE FUNCTIONS

/*
IplImage *image_to_ipl(image im)
{
    int x,y,c;
    IplImage *disp = cvCreateImage(cvSize(im.w,im.h), IPL_DEPTH_8U, im.c);
    int step = disp->widthStep;
    for(y = 0; y < im.h; ++y){
        for(x = 0; x < im.w; ++x){
            for(c= 0; c < im.c; ++c){
                float val = im.data[c*im.h*im.w + y*im.w + x];
                disp->imageData[y*step + x*im.c + c] = (unsigned char)(val*255);
            }
        }
    }
    return disp;
}

image ipl_to_image(IplImage* src)
{
    int h = src->height;
    int w = src->width;
    int c = src->nChannels;
    image im = make_image(w, h, c);
    unsigned char *data = (unsigned char *)src->imageData;
    int step = src->widthStep;
    int i, j, k;

    for(i = 0; i < h; ++i){
        for(k= 0; k < c; ++k){
            for(j = 0; j < w; ++j){
                im.data[k*w*h + i*w + j] = data[i*step + j*c + k]/255.;
            }
        }
    }
    return im;
}

Mat image_to_mat(image im)
{
    image copy = copy_image(im);
    constrain_image(copy);
    if(im.c == 3) rgbgr_image(copy);

    IplImage *ipl = image_to_ipl(copy);
    Mat m = cvarrToMat(ipl, true);
    cvReleaseImage(&ipl);
    free_image(copy);
    return m;
}

image mat_to_image(Mat m)
{
    IplImage ipl = m;
    image im = ipl_to_image(&ipl);
    rgbgr_image(im);
    return im;
}*/

and remove all CV_ from opencv flags, for example:

    if(w) cap->set(CV_CAP_PROP_FRAME_WIDTH, w);
    if(h) cap->set(CV_CAP_PROP_FRAME_HEIGHT, w);
    if(fps) cap->set(CV_CAP_PROP_FPS, w);

to

    if(w) cap->set(CAP_PROP_FRAME_WIDTH, w);
    if(h) cap->set(CAP_PROP_FRAME_HEIGHT, w);
    if(fps) cap->set(CAP_PROP_FPS, w);
