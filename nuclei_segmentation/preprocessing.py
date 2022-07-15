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
    This function takes an image with intensity values between 0 and 1 and binarizes them. It is used to binarize
    our given ground truth images. 

    :param x: Input image
    :return: binarized image
    
    """
    img = x.copy()

    img[img > 0] = 1
    img[img <= 0] = 0
    
    
    return img

#histogram stretching 
def stretch(x):
    """
    This function takes an image and performs histogram stretching but first clips the upper and lower quantile (outliers)

    :param x: Input image
    :return: Stretched image
    
    """
    intensities = []
   
    img = x.copy()
    lower_quantile, upper_quantile = np.percentile(x, (2,  98))

    #clipping upper and lower quantile
    img[img < lower_quantile] = lower_quantile
    img[img > upper_quantile] = upper_quantile
    
    for i in np.ndindex(img.shape):
        intensities.append(img[i])
    
    #histogram stretching 
    img_max = max(intensities)
    img_min = min(intensities)
    img_stretch = (img-img_min)*(256 / (img_max-img_min))
    return img_stretch

#holefilling (post processing)
def holefilling(x, y):
    """
    This function takes a thresholded image and performs hole filling as post processing.

    :param x: Input image
    :param y: kernel size 
    :return: Filled image
    
    """
    
    img = x.copy()
    k1 = np.ones((y,y))
    filled = cv2.morphologyEx(img , cv2.MORPH_CLOSE, k1 )
    return filled


#boxplot function
def dataset_boxplot_otsu(data , title , plot = True):
    """
    This function takes the complete analysis data for a dataset and plots the boxplot. 

    :param data: Input data (complete analysis)
    :param title: Boxplot title
    :param plot: Set plot = True
    
    """
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

    #set boxplot parameters 
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

    #add legend 
    plt.legend([bp["medians"][0], bp["means"][0]] , ["median", 'mean'], loc = 'lower right' , facecolor = 'gray')


def subplot(image1, image2, image3, title1, title2, title3, plot=True):
    fig, ax = plt.subplots(1, 3, figsize=(10,900))
   
    ax[0].imshow(image1, 'gray')
    ax[0].set_title(title1, pad=10, loc="left")
    ax[1].imshow(image2, 'gray')
    ax[1].set_title(title2, pad=10, loc="left")
    ax[2].imshow(image3, 'gray')
    ax[2].set_title(title3, pad=10, loc="left")
    ax[0].set_axis_off()
    ax[1].set_axis_off()
    ax[2].set_axis_off()
    plt.tight_layout()

