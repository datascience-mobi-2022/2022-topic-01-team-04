import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage
import math
import cv2           
import numpy as np
import os
from PIL import Image
import os, os.path
from nuclei_segmentation import complete_analysis as ca


def dataset_boxplot_otsu(data , title , plot = True):

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






