#Packages
from matplotlib import figure
from matplotlib.pyplot import imshow
import numpy as np
from scipy import stats
from nuclei_segmentation import otsu
from nuclei_segmentation import two_level_otsu

# otsu, ignores NaNs
def nanignore_otsu(image):
    """
    ### NaN ignore Otsu Thresholding
    This function performs segmentation of input image based on Otsu thresholding.
    Before calculating the intensity threshold, it removes rows and columns, which contain NaN values from the pixel intensity array.

    :param image: Input image
    :return: Segmented image

    """
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

    """
    ### Local thresholding counts
    This function performs local adaptive thresholding on a selected picture for a given stepsize, framesize and sensitivity and returns a segmented image. 
    It iterates over the image and computes local threshold for an N x N neighbourhood, where N corresponds to the framesize. To esnure segmentation of pixels on the right and bottom edges of the picture, rows and columns of NaN values are attached to the intensity array.
    Once a local threshold is computed, segmentation of the neighbourhood is performed and the pixel intensity value assignemt is saved for final segmentation. 
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
    """
    ### Otsu treshold
    This function calculates and returns the threshold value of a grayscale image, calculated by Otsu's method.
    
    :param img: Input image
    :param x: The number of intensity levels/ wanted thresholds
    :return: Threshold value
    """
    import matplotlib.pyplot
    import numpy

   

   
    # load histogram (numerical values)
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
def nanignore_otsu_t(img,x):
    """
    ### NaN ignore Otsu threshold
    This function calculates and returns an Otsu threshold value of a grayscale image.
    Before calculating the threshold, it removes rows and columns, which contain NaN values from the pixel intensity array.

    :param img: Input image
    :param x: The number of intensity levels/ wanted thresholds
    :return: Threshold value
    """

    # check for NaN values
    if np.isnan(np.sum(img)):
        # remove colums and rows with NaN values
        img1 = img[:, ~np.isnan(img).all(axis=0)]
        img2 = img1[~np.isnan(img).all(axis=1), :]
        #calculate the threshold
        thres = otsu_t(img2,x)
         
    else: 
        #calculate the threshold
        thres = otsu_t(img,x)
        
    return thres

def local_thresholding_mean(image,stepsize,framesize):

    """
    ### Local thresholding average
    This function performs local thresholding on a selected picture for a given stepsize and framesize.
    To esnure segmentation of pixels on the right and bottom edges of the picture, rows and columns of NaN values are attached to the intensity array.
    It iterates over the image and computes local threshold for an N x N neighbourhood, where N corresponds to the framesize and saves the threshold value for each pixel in the frame.
    Once all iterations are done, NaN values are removed and for each pixel a unique threshold is calculated as an average of the previously saved neighbourhood thresholds.
    The image is finally segmented, assigning each pixel to 0 or 1 based on it's own unique threshold and lastly a binary picture is returned.

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
            threshold = nanignore_otsu_t(post_otsu,256)
            
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

# Forwards and backwards local thresholding:  preforms local thresholding average, without adding the NaN edge, forwards starts at [x,y]=[0,0] and continues right and downwards, backwards starts at the very last pixel and continues left and upwards
# If joined together return smooth thresholding including the edges, except for top left and bottom right corners.
# The joined function takes twice as much time as previously defined local adaptive thresholding algorithms

def local_thresholding_mean_forward(image, stepsize, framesize):
    """
    Forwards local thresholding average
    This function performs local adaptive thresholding on a selected picture for a given stepsize, framesize and sensitivity and returns a segmented image. 
    It iterates over the image and computes local threshold for an N x N neighbourhood, where N corresponds to the framesize, beginning the iterations at pixel position [0,0]
    Once a local threshold is computed, segmentation of the neighbourhood is performed and the pixel intensity value assignemt is saved for final segmentation. 
    Finally, an array with saved threshold values is returned.

    :param image: Input image
    :param stepsize: Distance between two iteration frames
    :param framesize: Length of an edge for a square iteration frame (Note: For local thresholding set stepsize = framesize. For local adaptive thresholding stepsize < framesize)
    :return: Array of thresholds
    
    """
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
        
    """  
    Backwards local thresholding average
    This function performs local adaptive thresholding on a selected picture for a given stepsize, framesize and sensitivity and returns a segmented image. 
    It iterates over the image and computes local threshold for an N x N neighbourhood, where N corresponds to the framesize, beginning the iterations at pixel position [x,y], where x and y correspond to image height and width.
    Once a local threshold is computed, segmentation of the neighbourhood is performed and the pixel intensity value assignemt is saved for final segmentation. 
    Finally an array with saved threshold values is returned.

    :param image: Input image
    :param stepsize: Distance between two iteration frames
    :param framesize: Length of an edge for a square iteration frame (Note: For local thresholding set stepsize = framesize. For local adaptive thresholding stepsize < framesize)
    :return: Array of thresholds
    
    """
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

def local_thresholding_mean_combined(img, stepsize, framesize):
    """
    ###Combined local thresholding average
    This function performs forwards and backwards segmentation.
    It sums up threshold arrays retreived by forwards and backwards local thresholding average and computes the mean threshold for each pixel position. 
    The input image is finally segmented, assigning each pixel to 0 or 1 based on it's own unique threshold and lastly a binary picture is returned. 

    :param image: Input image
    :param stepsize: Distance between two iteration frames
    :param framesize: Length of an edge for a square iteration frame (Note: For local thresholding set stepsize = framesize. For local adaptive thresholding stepsize < framesize)
    :return: Segmented image
    """

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

      
