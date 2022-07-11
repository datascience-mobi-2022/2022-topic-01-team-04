#Packages
from matplotlib import figure
from matplotlib.pyplot import imshow
import numpy as np
from scipy import stats
from nuclei_segmentation import otsu

# crop function
def crop(image, xmin, ymin, xmax, ymax):
    cropped=np.empty([xmax-xmin, ymax-ymin], dtype=float)
    for a,b in np.ndindex(xmax-xmin, ymax-ymin):
        cropped[a,b]=image[a+xmin,b+ymin]
    return cropped


# otsu, ignores NaNs
def nanignore_otsu(image):
    if np.isnan(np.sum(image)):
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
            post_otsu = nanignore_otsu(img[x:x+framesize,y:y+framesize])
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

def pre_otsu(img,x):
    #counting NaNs cause I like dat
    #count=0
    #for i in np.ndindex(img.shape[0], img.shape[1]):
        #if np.isnan(img[i]):
            #count += 1
    #print(count)
    #if count>0:
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
    #img=copy(image)
    for i,j in np.ndindex(image.shape[0], image.shape[1]):
        img[i,j]=image[i,j]

    array=np.zeros([img.shape[0],img.shape[1],3])
    x=0
    y=0
    while x+framesize<=img.shape[0]:    
        while y+framesize<=img.shape[1]:
            window=crop(img,x,y,x+framesize, y+framesize)
            threshold = pre_otsu(window,255)
            for a, b in np.ndindex(window.shape[0], window.shape[1]):
                c=a+x
                d=b+y
                array[c,d,0]+=threshold
                array[c,d,1]+=1
            y+=stepsize
        y=0
        x+=stepsize 
    img=img[0:image.shape[0], 0:image.shape[1]]#(img,0,0,image.shape[0],image.shape[1])
    for i, j in np.ndindex(img.shape[0], img.shape[1]):
        array[i,j,2]=array[i,j,0]/array[i,j,1]
        if img[i,j]>array[i,j,2]:
            img[i,j]=1
        else:
            img[i,j]=0
    figure()
    imshow(img,'gray')
    return img

      
