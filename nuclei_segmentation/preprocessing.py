#import all packages 

import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage
import math
import cv2           
import numpy as np
import os
from PIL import Image
import os, os.path

#binarize function for the ground truth images 
def binarize(x):
    """
    This function takes an image 
    
    """
    img = x.copy()

    img[img > 0] = 1
    img[img <= 0] = 0
    
    
    return img



def stretch(x):
    intensities = []
   
    img = x.copy()
    lower_quantile, upper_quantile = np.percentile(x, (2,  98))

    img[img < lower_quantile] = lower_quantile
    img[img > upper_quantile] = upper_quantile
    
    for i in np.ndindex(img.shape):
        intensities.append(img[i])
   
    img_max = max(intensities)
    img_min = min(intensities)
    img_stretch = (img-img_min)*(256 / (img_max-img_min))
    return img_stretch


def holefilling(x, y):
    img = x.copy()
    k1 = np.ones((y,y))
    filled = cv2.morphologyEx(img , cv2.MORPH_CLOSE, k1 )
    return filled


  
def dataset_boxplot_otsu(data , title , plot = True):
    #ymax = max(max(data))
    #ymin = min(min(data))
    #if ymin >= 0.05:
       # floor = (math.floor(ymin * 10)) / 10 - 0.05
    #else:
        #floor = 0.00
    #if ymax <= 0.95:
        #ceil = (math.ceil(ymax * 10)) / 10 + 0.05
    #else:
        #ceil = 1.00
    fig_1 = plt.figure(figsize = (14 , 10))
    ax = fig_1.add_axes([0 , 0 , 1 , 1])
    ax.set_xticklabels(['No preprocessing' , 'Median filter' , 'Gaussian filter' , 'Histogram \n stretching' , 'Histogram stretching and \n median filter' , 'Histogram stretching and \n gaussian filter'])
    ax.set_ylim([0, 1])

    plt.title(title , size = 18)
    plt.ylabel('Preprocessing methods' , size = 14)
    plt.xlabel('Dice score' , size = 14)


    bp = ax.boxplot(data, patch_artist = True , showmeans = True , meanline = True , meanprops = dict(color = "white" , linewidth = 1.5))
    colors = ['#FF3030', '#FF7F24','#FFB90F', '#BCEE68' , '#00B2EE' , '#BF3EFF']
   
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)

    for median in bp['medians']:
        median.set(color = 'black' , linewidth = 1)
    
    print(bp["means"][0])
    plt.legend([bp["medians"][0], bp["means"][0]] , ["median", 'mean'], loc = 'lower right' , facecolor = 'gray')



