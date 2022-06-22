#Packages
%pylab
%matplotlib inline
import numpy as np
from images_segmentation import otsu as ot
from images_segmentation import dicescore as dsc

# crop function, can be useful outside the sliding window, returns an array equivalent to a rectangular "cut-out" of the picture :)
def crop(image, xmin, ymin, xmax, ymax):
    cropped=np.empty([xmax-xmin, ymax-ymin], dtype=float)
    for a,b in np.ndindex(xmax-xmin, ymax-ymin):
        cropped[a,b]=image[a+xmin,b+ymin]
    return cropped


 #define an otsu_i function, which sums up intensity values(zeros or ones) for each pixel 
 #and counts the amount of times a new value has been added for the pixel
def otsu_i(image, selectivity):
    img=ot.otsu_thresholding(image, 256)
    it = np.zeros([img.shape[0],img.shape[1],2])
    for x, y in np.ndindex(img.shape[0],img.shape[1]):
            if img[x,y] == 0:
                it[x,y,0]+=1
            else: 
                if np.isnan(img[x,y])==True:
                    it[x,y,0]=img[x,y]
                else:
                    it[x,y,0]+=0
            it[x,y,1]+=selectivity
    return it

#method 1 : mode of foreground and background assignment
def i_sw(image,stepsize,framesize, sensitivity):

    #copy the image so it does not influence the original + add NA corners
    img=np.empty([image.shape[0]+framesize,image.shape[1]+framesize,])
    img[:]=np.NaN
    #img=copy(image)
    for i,j in np.ndindex(image.shape[0], image.shape[1]):
        img[i,j]=image[i,j]
    
    #create a 3 dimensional null array, the size of the image * 2, we can now save 2 separate values for each pixel
    array=np.empty([img.shape[0],img.shape[1],2], dtype=float)

    #set the first coordinates for iteration over the image
    x=0
    y=0

   

        #iterate crop function with a given size over the picture, while the "window" fits inside the image, 
        #for each window crop the image to window coordinates and perform otsu_i 
    
    while x+framesize<=img.shape[0]:
        while y+framesize<=img.shape[1]:
            window=crop(img,x,y,x+framesize, y+framesize)
            print(np.count_nonzero(np.isnan(window)))
            it = otsu_i(window, sensitivity)

            # for each pixel that fits into the current window, add the values from otsu_i 
            #generated array to according pixels in the big array
            for a, b in np.ndindex(window.shape[0], window.shape[1]):
                c=a+x
                d=b+y
                array[c,d,0]+=it[a,b,0]
                array[c,d,1]+=it[a,b,1]
            y+=stepsize
        y=0
        x+=stepsize

    # because array is 3 dimensional and picture is 2 dimensional the final intensities will
    # be determined by 'array', but saved into a final 'img' array (rewriting the copy of image)
    #img=crop(img,0,0,image.shape[0],image.shape[1])
    print(array)
    img=crop(img,0,0,image.shape[0],image.shape[1])
    for i, j in np.ndindex(img.shape[0], img.shape[1]):
        #img[i,j]=round(array[i,j,0]/(2*array[i,j,1]))
        if array[i,j,0]>array[i,j,1]:
            img[i,j]=0
        else:
            img[i,j]=255
    #img=crop(img,0,0,image.shape[0],image.shape[1])
    figure()
    imshow(img,'gray')
    return img