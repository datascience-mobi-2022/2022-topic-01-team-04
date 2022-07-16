#Packages
from matplotlib import figure
from matplotlib.pyplot import imshow
import numpy as np
from scipy import stats
from nuclei_segmentation import two_level_otsu
from cmath import nan 

# average threshold

def tlot(img,x):

    """
    ### Two level Otsu threshold
    This function takes an image as well as the amount of wanted thresholds and calculates the class probabilies and mean levels for 
    foreground and background for each threshold. Then, the within class variance using the two-level Otsu's formula is computed 
    and a list of threshold values is returned

    :param img: Input image
    :param x: The number of intensity levels/ wanted thresholds
    :return: List of threshold values


    """
    import matplotlib.pyplot
    import numpy

    #load histogram (numerical values)
    n, bins = numpy.histogram(img.flatten(),bins = x)
  
    #initialize threshold value (T = 0) 
    thres = list()
    copy = img.copy()

    #create list to store values of within class variance for each threshold value as well as a list for the threshold indices 
    wcv = list()
    threshold = list()

    #calculate each within class variance for each possible threshold combination
    for i in range(0,len(n)):
        for t in range(0,len(n)):
            
            # background 
            # compute class probabilities and mean levels 
            w0_sum = numpy.sum(numpy.array(n[0:i+1]))
            mean_sum0 = numpy.sum((numpy.array(bins[0:i+1])*numpy.array(n[0:i+1])))
                
            
            w0 = w0_sum / sum(n)  
            if(sum(n[0:i+1]) != 0):  
                mean_0 = mean_sum0 / sum(n[0:i+1])
            else: mean_0 = 0
            
            # compute background class variance
            v0_sum = numpy.sum((numpy.array((bins[0:i+1]-mean_0)** 2)*numpy.array(n[0:i+1])))
            v0 = v0_sum / sum(n[0:i+1])
            
            # between the two thresholds (counted as foreground)
            # compute class probabilities and mean levels 
            w1_sum = numpy.sum(numpy.array(n[i+1:t]))
            mean_sum1 = numpy.sum((numpy.array(bins[i+1:t])*numpy.array(n[i+1:t])))
                
            w1 = w1_sum / sum(n)
            if(sum(n[i+1:t]) != 0):
                mean_1 = mean_sum1 / sum(n[i+1:t])
            else: mean_1 = 0

            # compute class variance for space between the two thresholds
            v1_sum = numpy.sum((numpy.array((bins[i+1:t]-mean_1)** 2)*numpy.array(n[i+1:t])))
        
            if( sum(n[i+1:t]) != 0):
                v1 = v1_sum / sum(n[i+1:t])
            else: v1 = 0

            # foreground
            # compute class probabilities and mean levels 
            w2_sum = numpy.sum(numpy.array(n[t:len(n)]))
            mean_sum2 = numpy.sum((numpy.array(bins[t:len(n)])*numpy.array(n[t:len(n)])))
                
            
            w2 = w2_sum / sum(n)
            if(sum(n[t:len(n)]) != 0):
                mean_2 = mean_sum2 / sum(n[t:len(n)])
            else: mean_2 = 0

            # compute foreground class variance 
            v2_sum = numpy.sum((numpy.array((bins[t:len(n)]-mean_2)** 2)*numpy.array(n[t:len(n)])))
        
            if( sum(n[t:len(n)]) != 0):
                v2 = v2_sum / sum(n[t:len(n)])
            else: v2 = 0

            # compute within class variance and append to list, append indices to list 
            wclv = (w0 * v0) + (w1 * v1) + (w2 * v2)
            thresholds = [i,t]
            wcv.append(wclv)
            threshold.append(thresholds)


    # select optimal threshold value, minimum value of within class variance
    optimal_thres = min(wcv)

    #select optimal threshold in the list
    l = 0
    while l < len(wcv):
        if wcv[l] == optimal_thres: thres.append(threshold[l])
        l += 1

    #assign first and second threshold 
    thres = thres[0]
    thres1  = bins[thres[0]]
    thres2  = bins[thres[1]]
    return threshold

def nanignore_otsu_two_level_mean(image):
    if np.isnan(np.sum(image)):
        img1 = image[:, ~np.isnan(image).all(axis=0)]
        img2 = img1[~np.isnan(image).all(axis=1), :]
        thres=tlot(img2, 256)
    else :
        thres=tlot(image, 256)
    return thres




def two_level_local_thresholding_mean(image,stepsize,framesize):

    """
    ### Two level local thresholding average
    This function performs local thresholding on a selected picture for a given stepsize and framesize.
    To esnure segmentation of pixels on the right and bottom edges of the picture, rows and columns of NaN values are attached to the intensity array.
    It iterates over the image and computes local threshold for an N x N neighbourhood, where N corresponds to the framesize, calculates an upper and lower threshold value for each pixel in the frame and saves it.
    Once all iterations are done, NaN values are removed and for each pixel a unique threshold is calculated as an average of the previously saved neighbourhood thresholds.
    The image is finally segmented, assigning each pixel to 0 or 1 based on unique lower and upper threshold values, setting the intensity to 1, if initial pixel intensity is higher than the lower intensity threshold. 
    Lastly a binary picture is returned.

    :param image: Input image
    :param stepsize: Distance between two iteration frames
    :param framesize: Length of an edge for a square iteration frame (Note: For local thresholding set stepsize = framesize. For local adaptive thresholding stepsize < framesize)
    :return: Segmented image
    """

    # translate the image array onto a larger, empty array to add a bottom and right edge, fill the empty values with NaN's  
    img=np.empty([image.shape[0]+framesize,image.shape[1]+framesize,])
    img[:]=np.NaN
    for i,j in np.ndindex(image.shape[0], image.shape[1]):
        img[i,j]=image[i,j]

    #initiate a 3-dimensional array to store unique upper and lower threshold values, number of times thresholding has been performed in set pixel positon and calculated average threshold values for each pixel position 
    array=np.zeros([img.shape[0],img.shape[1],3])
    x=0
    y=0

    #iterate over the image
    while x+framesize<=img.shape[0]:    
        while y+framesize<=img.shape[1]:
            #define the neighbourhood for which the thresholds will be calculated
            post_otsu=img[x:x+framesize, y:y+framesize]
            #perform two level Otsu thresholding
            threshold = nanignore_otsu_two_level_mean(post_otsu)
            #save the calculated lower and upper threshold for each pixel in the defined neighbourhood, add 1 to number of thresholds that have been calculated for a unique pixel
            for a, b in np.ndindex(post_otsu.shape[0], post_otsu.shape[1]):
                c=a+x
                d=b+y
                array[c,d,0]+=threshold[0]
                array[c,d,1]+=threshold[1]
                array[c,d,2]+=1
            y+=stepsize
        y=0
        x+=stepsize 
    # remove NaN rows and columns from the image array
    img=img[0:image.shape[0], 0:image.shape[1]]
    #set pixel intensity for each pixel individually
    for i,j in np.ndindex(img.shape):
        #if the pixel intensity is lower than the average lower threshold, set pixel intensity to 0
        if img[i,j]<array[i,j,0]/array[i,j,2]:
            img[i,j]=0
        # if the pixel intensity is between the averages of the upper and lower threshold, set pixel intensity to 1
        elif img[i,j]>=array[i,j,0]/array[i,j,2] and img[i,j]<array[i,j,1]/array[i,j,2]:
            img[i,j]=1
        # if the pixel intensity is hiher than the average lower threshold, set pixel intensity to 1
        else:
            img[i,j]=1

    return img



# assignment counts

# otsu, ignores NaNs
def nanignore_otsu_two_level(image):
    if np.isnan(np.sum(image)):
        img1 = image[:, ~np.isnan(image).all(axis=0)]
        img2 = img1[~np.isnan(image).all(axis=1), :]
        img=two_level_otsu.two_level_otsu_thresholding_clip(img2, 256)
    else :
        img=two_level_otsu.two_level_otsu_thresholding_clip(image, 256)
    return img

def two_level_local_thresholding_counts(image,stepsize,framesize, sensitivity):

    """
    ### Two level local thresholding counts
    This function performs local adaptive thresholding on a selected picture for a given stepsize, framesize and sensitivity and returns a segmented image. 
    It iterates over the image and computes two local thresholds for an N x N neighbourhood, where N corresponds to the framesize. To esnure segmentation of pixels on the right and bottom edges of the picture, rows and columns of NaN values are attached to the intensity array.
    Once the local thresholds are computed, segmentation of the neighbourhood is performed, assigning all pixels with intensity higher than the lower threshold to foreground. The pixel intensity value assignemt is saved for final segmentation. 
    Once all iterations are performed, the NaN edges are removed and each pixel gains the intensity value 1, if it has been assigned to foreground a percentile of times, which is set by the sensitivity.
    The rest of the pixels gain the intensity value 0. After final intensity assignment a whole segmented picture is retrieved.

    :param image: Input image
    :param stepsize: Distance between two iteration frames
    :param framesize: Length of an edge for a square iteration frame (Note: For local thresholding set stepsize = framesize. For local adaptive thresholding stepsize < framesize)
    :param sensitivity: Value in range [0,1], setting the lower proportion boundary for foreground/background assignment of a unique pixel A = F/(F+B). Pixels with A<= sensitivity are assigned to background (Note: for segmentation based on mode of pixel assignment, set sensitivity to 0.5)
    :return: Segmented image


    """
    # translate the image array onto a larger, empty array to add a bottom and right edge, fill the empty values with NaN's 
    img=np.empty([image.shape[0]+framesize,image.shape[1]+framesize,])
    img[:]=np.NaN
    for i,j in np.ndindex(image.shape[0], image.shape[1]):
        img[i,j]=image[i,j]
    #create a new array to count the foreground/background assignment of each pixel
    it=np.zeros([img.shape[0],img.shape[1],2])
    x=0
    y=0

    #iterate over the image
    while x+framesize<=img.shape[0]:
        while y+framesize<=img.shape[1]:
            #segment the local neighbourhood by performing 2 level otsu
            post_otsu = nanignore_otsu_two_level(img[x:x+framesize,y:y+framesize])
            # save segmentation information (foreground/background assignment, how many times segmentation has been performed in respect to a unique pixel) for each pixel
            for a,b in np.ndindex(post_otsu.shape[0],post_otsu.shape[1]):
                it[x+a,y+b,0] +=post_otsu[a,b]
                it[x+a,y+b,1] += sensitivity
            y+=stepsize
        y=0
        x+=stepsize
    # remove rows and columns corresponding to the NaN edges
    img=img[0:image.shape[0],0:image.shape[1]] 
    #for every pixel compare the proportion foreground/(foreground+background)
    for i, j in np.ndindex(img.shape[0], img.shape[1]):
        # if the proportion is larger than sensitivity, set pixel intensity value to 1
        if it[i,j,0]>it[i,j,1]:
            img[i,j]=1
        # set all other pixel intensity values to 0
        else:
            img[i,j]=0

    return img