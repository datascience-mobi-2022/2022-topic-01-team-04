#Packages
from matplotlib import figure
from matplotlib.pyplot import imshow
import numpy as np
from scipy import stats
from nuclei_segmentation import otsu
from nuclei_segmentation import two_level_otsu

# otsu, ignores NaNs
def nanignore_otsu(image):
    #if the array contains NaN values
    if np.isnan(np.sum(image)):

        #remove columns and rows that contain NaN values
        img1 = image[:, ~np.isnan(image).all(axis=0)]
        img2 = img1[~np.isnan(image).all(axis=1), :]

        #apply otsu thresholding
        img=otsu.otsu_thresholding(img2, 256)
    else :

        #apply otsu thresholding
        img=otsu.otsu_thresholding(image, 256)
    return img

#local thresholding, counts how many times a pixel has been assigned to foreground or background#
#if the proportion foreground_assignment/(foreground_assgnment+background_assignment) is over a set percentile (sensitivity), the pixel is assigned to foreground
def local_thresholding_counts(image,stepsize,framesize, sensitivity):

    # add an empty bottom right edge to the array, so that some frames can be  for pixels located on the far right or very bottom of the image 
    img=np.empty([image.shape[0]+framesize,image.shape[1]+framesize,])
    img[:]=np.NaN
    for i,j in np.ndindex(image.shape[0], image.shape[1]):
        img[i,j]=image[i,j]

    #create a new array to count the foreground/background assignment of each pixel
    it=np.zeros([img.shape[0],img.shape[1],2])
    x=0
    y=0

    # iterate over the image (sliding window)
    while x+framesize<=img.shape[0]:
        while y+framesize<=img.shape[1]:

            #perform thresholding on the part of an image
            post_otsu = nanignore_otsu(img[x:x+framesize,y:y+framesize])
            #transfer the foreground/background assignment for each pixel position to according position in the it array
            for a,b in np.ndindex(post_otsu.shape[0],post_otsu.shape[1]):
                it[x+a,y+b,0] +=post_otsu[a,b]
                it[x+a,y+b,1] += sensitivity
            y+=stepsize
        y=0
        x+=stepsize
    #redefine image to remove the NaN edges
    img=img[0:image.shape[0],0:image.shape[1]]
    
    #for every pixel compare the proportion foreground/(foreground+background)
    for i, j in np.ndindex(img.shape[0], img.shape[1]):
        #if proportion is larger than the chosen percentile (sensitivity), assign it to foreground, set intensity
        if it[i,j,0]>it[i,j,1]:
            img[i,j]=1
        #if proportion is smaller than the chosen percentile, assign it to background, set intensity
        else:
            img[i,j]=0

    return img


# average thresholding method
def otsu_t(img,x):
    import matplotlib.pyplot
    import numpy

   

   
    # load histogram, Mathematische werte aus Histogramm rausgreifen
    n, bins = numpy.histogram(img.flatten(),bins = x)
    
    # initialize threshold value (T = 0) 
    thres = 0
    copy = img.copy()

    # create list to store values of within class variance for each threshold value
    wcv = list()

    
        
    # set up initial values
    for i in range(0,len(n)):
        wclv = 0
        w0_sum = 0
        mean_sum0 = 0
        v0_sum = 0
        mean_sum1 = 0
        v1_sum = 0
        w0 = 0
        w1 = 0
        w1_sum = 0

        #sum up the probabilites of each intensity value;  and the mean value (sind noch nicht happy mit der definition :()
        w0_sum = numpy.sum(numpy.array(n[0:i+1]))
        mean_sum0 = numpy.sum((numpy.array(bins[0:i+1])*numpy.array(n[0:i+1])))
                    
        # background class probabilites and class mean levels
        w0 = w0_sum / sum(n)  
        if(sum(n[0:i+1]) != 0):  
            mean_0 = mean_sum0 / sum(n[0:i+1])
        else: mean_0 = 0
                
        # compute background class variance

        v0_sum = numpy.sum((numpy.array((bins[0:i+1]-mean_0)** 2)*numpy.array(n[0:i+1])))
        v0 = v0_sum / sum(n[0:i+1])
                
        # sum up the probabilites of each intensity value;  and the mean value
        w1_sum = numpy.sum(numpy.array(n[i+1:len(n)]))
        mean_sum1 = numpy.sum((numpy.array(bins[i+1:len(n)])*numpy.array(n[i+1:len(n)])))
                    
        # compute foreground class probabilities and class mean levels    
        w1 = w1_sum / sum(n)
        if(sum(n[i+1:len(n)]) != 0):
            mean_1 = mean_sum1 / sum(n[i+1:len(n)])
        else: mean_1 = 0

        # compute foreground class variance 
        v1_sum = numpy.sum((numpy.array((bins[i+1:len(n)]-mean_1)** 2)*numpy.array(n[i+1:len(n)])))
            
        if( sum(n[i+1:len(n)]) != 0):
            v1 = v1_sum / sum(n[i+1:len(n)])
        else: v1 = 0

        # compute within class variance and append to list
        wclv = (w0 * v0) + (w1 * v1)
        wcv.append(wclv)

    # select optimal threshold value, minimum value of within class variance
    optimal_thres = min(wcv)

    #select optimal threshold in the list
    l = 0
    while l < len(wcv):
        if wcv[l] == optimal_thres: thres = bins[l]
        l += 1
    
        
    return thres

#otsu thresholding which ignores NaN values for the local_thresholding_mean function
def pre_otsu(img,x):
    if np.isnan(np.sum(img)):
        img1 = img[:, ~np.isnan(img).all(axis=0)]
        img2 = img1[~np.isnan(img).all(axis=1), :]
        thres = otsu_t(img2,x)
         
    else: 
        thres = otsu_t(img,x)
        
    return thres

def local_thresholding_mean(image,stepsize,framesize):

    img=np.empty([image.shape[0]+framesize,image.shape[1]+framesize,])
    img[:]=np.NaN
    for i,j in np.ndindex(image.shape[0], image.shape[1]):
        img[i,j]=image[i,j]

    #initiate a 3-dimensional array to store unique threshold values, number of times thresholding has been performed in set pixel positon and calculated average threshold values for each pixel position 
    array=np.zeros([img.shape[0],img.shape[1],3])
    x=0
    y=0

    #iterate over image
    while x+framesize<=img.shape[0]:    
        while y+framesize<=img.shape[1]:

            #define the frame to which thresholding is applied
            post_otsu=img[x:x+framesize, y:y+framesize]

            #apply otsu thresholding which ignores NaN values to the frame
            threshold = pre_otsu(post_otsu,256)
            
            #add up unique threshold values and number of unique thresholds for pixels in the according unique pixel positions in the 3-dimensional array
            for a, b in np.ndindex(post_otsu.shape[0], post_otsu.shape[1]):
                c=a+x
                d=b+y
                array[c,d,0]+=threshold
                array[c,d,1]+=1
            y+=stepsize
        y=0
        x+=stepsize 
    
    #remove the NaN edge
    img=img[0:image.shape[0], 0:image.shape[1]]

    #for each pixel calculate the average threshold and store into array
    for i, j in np.ndindex(img.shape[0], img.shape[1]):
        array[i,j,2]=array[i,j,0]/array[i,j,1]

        #if the pixel intensity in original image is above the average threshold, assign it to foreground (set intensity to 1)
        if img[i,j]>array[i,j,2]:
            img[i,j]=1

        #if the pixel intensity in original image is below or the same as the average threshold, assign it to background (set intensity to 0)
        else:
            img[i,j]=0

    return img

# Forwards and backwards local thresholding: does the same thing as average (mean) thresholding without adding the NaN edge, forwards starts at [x,y]=[0,0] and continues right and downwards, backwards starts at the very last pixel and continues left and upwards
# If joined together return smooth thresholding including the edges, except for top left and bottom right corners.
# The joined function takes twice as much time as previously defined local adaptive thresholding algorithms

def local_thresholding_mean_forward(image, stepsize, framesize):
    img=np.copy(image)
    for i,j in np.ndindex(image.shape[0], image.shape[1]):
        img[i,j]=image[i,j]

    array=np.zeros([img.shape[0],img.shape[1],3])
    x=0
    y=0
    while x+framesize<=img.shape[0]:    
        while y+framesize<=img.shape[1]:
            post_otsu=img[x:x+framesize, y:y+framesize]
            threshold = otsu_t(post_otsu,256)
            for a, b in np.ndindex(post_otsu.shape[0], post_otsu.shape[1]):
                c=a+x
                d=b+y
                array[c,d,0]+=threshold
                array[c,d,1]+=1
            y+=stepsize
        y=0
        x+=stepsize 

    return array


def local_thresholding_mean_backward(image, stepsize, framesize):
    img=np.copy(image)
    for i,j in np.ndindex(image.shape[0], image.shape[1]):
        img[i,j]=image[i,j]

    array=np.zeros([img.shape[0],img.shape[1],3])
    x=image.shape[0]
    y=image.shape[1]
    while x+framesize>=0:    
        while y+framesize>=0:
            post_otsu=img[x-framesize:x, y-framesize:y]
            threshold = otsu_t(post_otsu,256)
            for a, b in np.ndindex(post_otsu.shape[0], post_otsu.shape[1]):
                c=a+x-framesize
                d=b+y-framesize
                array[c,d,0]+=threshold
                array[c,d,1]+=1
            y-=stepsize
        y=image.shape[1]
        x-=stepsize

    return array

def local_thresholding_mean_better(img, stepsize, framesize):
    f = local_thresholding_mean_forward(img, stepsize, framesize)
    b = local_thresholding_mean_backward(img, stepsize, framesize)
    fb=f+b


    for i, j in np.ndindex(fb.shape[0], fb.shape[1]):
        fb[i,j,2]=fb[i,j,0]/fb[i,j,1]
        if img[i,j]>fb[i,j,2]:
            img[i,j]=1
        else:
            img[i,j]=0
    return img

      
