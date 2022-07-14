#Packages
from matplotlib import figure
from matplotlib.pyplot import imshow
import numpy as np
from scipy import stats
from nuclei_segmentation import two_level_otsu


# average threshold

def tlot(img,x):
    import matplotlib.pyplot
    import numpy

   # load histogram, Mathematische werte aus Histogramm rausgreifen
    n, bins = numpy.histogram(img.flatten(),bins = x)
  
   # initialize threshold value (T = 0) 
    thres = list()
    copy = img.copy()

    # create list to store values of within class variance for each threshold value
    wcv = list()
    threshold = list()
    # set up initial values
    for i in range(0,len(n)):
        for t in range(0,len(n)):
            
            #sum up the probabilites of each intensity value;  and the mean value (sind noch nicht happy mit der definition :()
            w0_sum = numpy.sum(numpy.array(n[0:i+1]))
            mean_sum0 = numpy.sum((numpy.array(bins[0:i+1])*numpy.array(n[0:i+1])))
                
            # background class probabilites and class mean levels
            w0 = w0_sum / sum(n)  
            if(sum(n[0:i+1]) != 0):  
                mean_0 = mean_sum0 / sum(n[0:i+1])
            else: mean_0 = 0
            
            # compute background class variance

    
            # sum up the probabilites of each intensity value;  and the mean value
            w1_sum = numpy.sum(numpy.array(n[i+1:t]))
            mean_sum1 = numpy.sum((numpy.array(bins[i+1:t])*numpy.array(n[i+1:t])))
                
            # compute foreground class probabilities and class mean levels    
            w1 = w1_sum / sum(n)
            if(sum(n[i+1:t]) != 0):
                mean_1 = mean_sum1 / sum(n[i+1:t])
            else: mean_1 = 0

            # compute foreground class variance 
            
            # sum up the probabilites of each intensity value;  and the mean value
            w2_sum = numpy.sum(numpy.array(n[t:len(n)]))
            mean_sum2 = numpy.sum((numpy.array(bins[t:len(n)])*numpy.array(n[t:len(n)])))
                
            # compute foreground class probabilities and class mean levels    
            w2 = w2_sum / sum(n)
            if(sum(n[t:len(n)]) != 0):
                mean_2 = mean_sum2 / sum(n[t:len(n)])
            else: mean_2 = 0

            # compute foreground class variance 
          
            # compute within class variance and append to list
            m_t = w0*mean_0 + w1*mean_1 + w2*mean_2 
            wclv = w0*w1*((mean_1-mean_0)**2) + w0*w2*((mean_2 - mean_0)**2)+ w1*w2*((mean_2-mean_1)**2)
            thresholds = [i,t]
            wcv.append(wclv)
            threshold.append(thresholds)


    # select optimal threshold value, minimum value of within class variance
    optimal_thres = max(wcv)

    #select optimal threshold in the list
    l = 0
    while l < len(wcv):
        if wcv[l] == optimal_thres: thres.append(threshold[l])
        l += 1

    thres = thres[0]
    thres1  = bins[thres[0]]
    thres2  = bins[thres[1]]
    threshold=[thres1,thres2]
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

    img=np.empty([image.shape[0]+framesize,image.shape[1]+framesize,])
    img[:]=np.NaN
    #img=np.copy(image)
    for i,j in np.ndindex(image.shape[0], image.shape[1]):
        img[i,j]=image[i,j]

    array=np.zeros([img.shape[0],img.shape[1],3])
    x=0
    y=0
    while x+framesize<=img.shape[0]:    
        while y+framesize<=img.shape[1]:
            post_otsu=img[x:x+framesize, y:y+framesize]
            threshold = nanignore_otsu_two_level_mean(post_otsu,256)
            for a, b in np.ndindex(post_otsu.shape[0], post_otsu.shape[1]):
                c=a+x
                d=b+y
                array[c,d,0]+=threshold[0]
                array[c,d,1]+=threshold[1]
                array[c,d,2]+=1
            y+=stepsize
        y=0
        x+=stepsize 
    img=img[0:image.shape[0], 0:image.shape[1]]#(img,0,0,image.shape[0],image.shape[1])
    for i,j in np.ndindex(img.shape):
        if img[i,j]<array[i,j,0]/array[i,j,2]:
            img[i,j]=0
        elif img[i,j]>=array[i,j,0]/array[i,j,2] and img[i,j]<array[i,j,1]/array[i,j,2]:
            img[i,j]=1
        else:
            img[i,j]=0

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
    img=np.empty([image.shape[0]+framesize,image.shape[1]+framesize,])
    img[:]=np.NaN
    for i,j in np.ndindex(image.shape[0], image.shape[1]):
        img[i,j]=image[i,j]
    it=np.zeros([img.shape[0],img.shape[1],2])
    x=0
    y=0
    while x+framesize<=img.shape[0]:
        while y+framesize<=img.shape[1]:
            post_otsu = nanignore_otsu_two_level(img[x:x+framesize,y:y+framesize])
            for a,b in np.ndindex(post_otsu.shape[0],post_otsu.shape[1]):
                it[x+a,y+b,0] +=post_otsu[a,b]
                it[x+a,y+b,1] += sensitivity
            y+=stepsize
        y=0
        x+=stepsize
    print(it)
    img=img[0:image.shape[0],0:image.shape[1]]
    for i, j in np.ndindex(img.shape[0], img.shape[1]):
        if it[i,j,0]>it[i,j,1]:
            img[i,j]=1
        else:
            img[i,j]=0
    img=img[0:image.shape[0],0:image.shape[1]]

    return img