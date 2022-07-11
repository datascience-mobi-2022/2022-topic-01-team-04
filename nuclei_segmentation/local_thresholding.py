#Packages
%pylab
%matplotlib inline
import numpy as np
from scipy import stats
from images_segmentation import otsu

# crop function
def crop(image, xmin, ymin, xmax, ymax):
    cropped=np.empty([xmax-xmin, ymax-ymin], dtype=float)
    for a,b in np.ndindex(xmax-xmin, ymax-ymin):
        cropped[a,b]=image[a+xmin,b+ymin]
    return cropped


# otsu, ignores NaNs
def nanignore_otsu(image):
    if numpy.isnan(numpy.sum(image)):
        img1 = image[:, ~np.isnan(image).all(axis=0)]
        img2 = img1[~np.isnan(image).all(axis=1), :]
        img=otsu.otsu_thresholding(img2, 256)
    else :
        img=otsu.otsu_thresholding(image, 256)
    return img

#local thresholding, counts assignment to foreground

def local_thresholding_counts(image,stepsize,framesize, sensitivity):
    img=np.empty([image.shape[0]+framesize,image.shape[1]+framesize,])
    img[:]=np.NaN
    for i,j in np.ndindex(image.shape[0], image.shape[1]):
        img[i,j]=image[i,j]
    it=np.zeros([img.shape[0],img.shape[1],2])
    x=0
    y=0
    while x+framesize<=img.shape[0]:
        while y+framesize<=img.shape[1]:
            post_otsu = nanignore_otsu(img[x:x+framesize,y:y+framesize], sensitivity)
            for a,b in np.ndindex(post_otsu.shape[0],post_otsu.shape[1]):
                it[x+a,y+b,0] +=post_otsu[a,b]
                it[x+a,y+b,1] += sensitivity
            y+=stepsize
        y=0
        x+=stepsize
    print(it)
    img=crop(img,0,0,image.shape[0],image.shape[1])
    for i, j in np.ndindex(img.shape[0], img.shape[1]):
        #img[i,j]=round(array[i,j,0]/(2*array[i,j,1]))
        #img[i,j]=round(it[i,j,0]/(2*it[i,j,1]))
        if it[i,j,0]>it[i,j,1]:
            img[i,j]=1
        else:
            img[i,j]=0
    img=crop(img,0,0,image.shape[0],image.shape[1])
    figure()
    imshow(img,'gray')
    return img

