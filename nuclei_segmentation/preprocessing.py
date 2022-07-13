# Set ground truth images from N2DH-GOWT1 dataset and N2DL-HeLa dataset to 0 and 1


import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage
#import pandas as pd
#import seaborn as sns
import math
#import cv2           
import numpy as np
import os
from PIL import Image
import os, os.path

    
# Set ground truth images from N2DH-GOWT1 dataset and N2DL-HeLa dataset to 0 and 1

def binarize(x):
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



#def holefilling(x):
    #img = x.copy()
   # k1 = np.ones((3,3))
    #filled = cv2.morphologyEx(img , cv2.MORPH_CLOSE, k1 )
    #return filled





# Preprocessing - Boxplot
  
def dataset_boxplot_global_otsu(data , title , plot = True):
    ymax = max(max(data))
    ymin = min(min(data))
    if ymin >=0.05:
        floor = (math.floor(ymin * 10)) / 10 - 0.05
    else:
        floor= 0.00
    if ymax<=0.95:
        ceil = (math.ceil(ymax * 10)) / 10 + 0.05
    else:
        ceil=1.00
    fig_1 = plt.figure(figsize = (14 , 10))
    ax = fig_1.add_axes([0 , 0 , 1 , 1])
    ax.set_xticklabels(['No preprocessing' , 'Median filter' , 'Gaussian filter' , 'Histogram \n stretching' , 'Histogram stretching and \n median filter' , 'Histogram stretching and \n gaussian filter'])
    ax.set_ylim([floor, ceil])

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



def dataset_boxplot_two_level_otsu(data , title , yaxis , plot = True):
    import matplotlib.pyplot as plt
 
    fig_1 = plt.figure(figsize = (14 , 10))
    ax = fig_1.add_axes([0 , 0 , 1 , 1])
    ax.set_xticklabels(['No preprocessing' , 'Median filter' , 'Gaussian filter' , 'Histogram \n stretching' , 'Histogram stretching and \n median filter' , 'Histogram stretching and \n gaussian filter'])
    if yaxis == 0:
        ax.set_ylim([0.2 , 0.95])
    if yaxis == 1:
        ax.set_ylim([0.6, 0.95])
    if data == 2:
        ax.set_ylim([0.3 , 1])

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



def dataset_boxplot_two_level_otsu_clip(data , title , yaxis , plot = True):
    import matplotlib.pyplot as plt
 
    fig_1 = plt.figure(figsize = (14 , 10))
    ax = fig_1.add_axes([0 , 0 , 1 , 1])
    ax.set_xticklabels(['No preprocessing' , 'Median filter' , 'Gaussian filter' , 'Histogram \n stretching' , 'Histogram stretching and \n median filter' , 'Histogram stretching and \n gaussian filter'])
    if yaxis == 0:
        ax.set_ylim([0 , 1])
    if yaxis == 1:
        ax.set_ylim([0, 1])
    if data == 2:
        ax.set_ylim([0.1 , 0.9])

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


def dataset_boxplot_local_otsu(data , title , yaxis , plot = True):
    import matplotlib.pyplot as plt
 
    fig_1 = plt.figure(figsize = (14 , 10))
    ax = fig_1.add_axes([0 , 0 , 1 , 1])
    ax.set_xticklabels(['No preprocessing' , 'Median filter' , 'Gaussian filter' , 'Histogram \n stretching' , 'Histogram stretching and \n median filter' , 'Histogram stretching and \n gaussian filter'])
    if yaxis == 0:
        ax.set_ylim([0 , 0.85])
    if yaxis == 1:
        ax.set_ylim([0.6, 0.85])
    if data == 2:
        ax.set_ylim([0 , 1])

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



def dataset_boxplot_local_two_level_otsu(data , title , yaxis , plot = True):
    import matplotlib.pyplot as plt
 
    fig_1 = plt.figure(figsize = (14 , 10))
    ax = fig_1.add_axes([0 , 0 , 1 , 1])
    ax.set_xticklabels(['No preprocessing' , 'Median filter' , 'Gaussian filter' , 'Histogram \n stretching' , 'Histogram stretching and \n median filter' , 'Histogram stretching and \n gaussian filter'])
    if yaxis == 0:
        ax.set_ylim([0 , 0.85])
    if yaxis == 1:
        ax.set_ylim([0.6, 0.85])
    if data == 2:
        ax.set_ylim([0 , 1])

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



def dataset_boxplot_local_two_level_otsu_clip(data , title , yaxis , plot = True):
    import matplotlib.pyplot as plt
 
    fig_1 = plt.figure(figsize = (14 , 10))
    ax = fig_1.add_axes([0 , 0 , 1 , 1])
    ax.set_xticklabels(['No preprocessing' , 'Median filter' , 'Gaussian filter' , 'Histogram \n stretching' , 'Histogram stretching and \n median filter' , 'Histogram stretching and \n gaussian filter'])
    if yaxis == 0:
        ax.set_ylim([0 , 0.85])
    if yaxis == 1:
        ax.set_ylim([0.6, 0.85])
    if data == 2:
        ax.set_ylim([0 , 1])

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