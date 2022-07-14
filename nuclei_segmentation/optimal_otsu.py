%pylab
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage
import scipy
import pandas as pd
import seaborn as sns
path =  (os.path.abspath(os.path.join(r'.', os.pardir)))
import sys
sys.path.append(path)
from nuclei_segmentation import otsu as ot
from nuclei_segmentation import dicescore as dsc
from nuclei_segmentation import two_level_otsu as tlot
from nuclei_segmentation import local_thresholding as lt
from PIL import Image
import os
import os.path
import statistics as st
from nuclei_segmentation import complete_analysis as ca


def dataset_boxplot_optimal_NIH3T3(data , plot = True):
    data = [dice_otsu_stretch_median_img_NIH3T3, dice_otsu_tlot_stretch_median_img_NIH3T3, dice_otsu_tlot_c_stretch_median_img_NIH3T3, dice_otsu_lt_count_stretch_median_img_NIH3T3, dice_otsu_lt_mean_stretch_median_img_NIH3T3 ]
    fig_1 = plt.figure(figsize = (14 , 10))
    ax = fig_1.add_axes([0 , 0 , 1 , 1])
    ax.set_xticklabels(['normal otsu' , 'two level otsu', 'two level otsu clip', ' local adaptive thresholding counts', 'local adaptive thresholding average' ])
    ax.set_ylim([0, 1])

    plt.title('optimal Otsu NIH3T3', size = 18)
    plt.ylabel('Optimal Otsu' , size = 14)
    plt.xlabel('Dice score' , size = 14)


    bp = ax.boxplot(data, patch_artist = True , showmeans = True , meanline = True , meanprops = dict(color = "white" , linewidth = 1.5))
    colors = ['#FF3030', '#FF7F24','#FFB90F', '#BCEE68' , '#00B2EE' , '#BF3EFF']
   
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)

    for median in bp['medians']:
        median.set(color = 'black' , linewidth = 1)
    
    print(bp["means"][0])
    plt.legend([bp["medians"][0], bp["means"][0]] , ["median", 'mean'], loc = 'lower right' , facecolor = 'gray')


def dataset_boxplot_optimal_N2DH_GOWT1(data , plot = True):

    data = [ice_otsu_stretch_img_N2DH_GOWT1,  dice_otsu_tlot_stretch_img_N2DH_GOWT1, dice_otsu_tlot_clip_stretch_img_N2DH_GOWT1 ]
    fig_1 = plt.figure(figsize = (14 , 10))
    ax = fig_1.add_axes([0 , 0 , 1 , 1])
    ax.set_xticklabels(['normal otsu' , 'two level otsu', 'two level otsu clip'])
    ax.set_ylim([0, 1])

    plt.title( 'Optimal Otsu N2DH-GOWT1' , size = 18)
    plt.ylabel('optimal Otsu' , size = 14)
    plt.xlabel('Dice score' , size = 14)


    bp = ax.boxplot(data, patch_artist = True , showmeans = True , meanline = True , meanprops = dict(color = "white" , linewidth = 1.5))
    colors = ['#FF3030', '#FF7F24','#FFB90F']
   
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)

    for median in bp['medians']:
        median.set(color = 'black' , linewidth = 1)
    
    print(bp["means"][0])
    plt.legend([bp["medians"][0], bp["means"][0]] , ["median", 'mean'], loc = 'lower right' , facecolor = 'gray')


def dataset_boxplot_optimal_N2DL_HeLa(data, plot= True):

    data = [dice_otsu_stretch_img_N2DH_GOWT1,  dice_otsu_tlot_stretch_img_N2DH_GOWT1, dice_otsu_tlot_clip_stretch_img_N2DH_GOWT1, dice_otsu_lt_mean_stretch_median_img_N2DL_HeLa ]
    fig_1 = plt.figure(figsize = (14 , 10))
    ax = fig_1.add_axes([0 , 0 , 1 , 1])
    ax.set_xticklabels(['normal otsu' , 'two level otsu', 'two level otsu clip', 'local adaptive thresholding average'])
    ax.set_ylim([0, 1])

    plt.title( 'Optimal Otsu N2DL-HeLa' , size = 18)
    plt.ylabel('optimal Otsu' , size = 14)
    plt.xlabel('Dice score' , size = 14)


    bp = ax.boxplot(data, patch_artist = True , showmeans = True , meanline = True , meanprops = dict(color = "white" , linewidth = 1.5))
    colors = ['#FF3030', '#FF7F24','#FFB90F']
   
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)

    for median in bp['medians']:
        median.set(color = 'black' , linewidth = 1)
    
    print(bp["means"][0])
    plt.legend([bp["medians"][0], bp["means"][0]] , ["median", 'mean'], loc = 'lower right' , facecolor = 'gray')