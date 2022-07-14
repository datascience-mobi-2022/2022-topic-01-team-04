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




    data = [ aa, ba, dice_otsu_tlot_c_stretch_median_img_NIH3T3, dice_otsu_lt_count_stretch_median_img_NIH3T3, dice_otsu_lt_mean_stretch_median_img_NIH3T3 ]
    aa = [0.9080295797878731, 0.9080746699707551, 0.8240269286695534, 0.7523092096313426, 0.7667266042242559, 0.7210834846002242, 0.6796112266384551, 0.7467162829788587, 0.1537407710034592, 0.61035447425189, 0.6454520836896415, 0.676574551172507, 0.5441254230662401, 0.5872934791498239, 0.6104348417019902, 0.6002316933870171, 0.737465149556319, 0.7870066342425532]
    ba = [0.9417263695042412, 0.9439370328532631, 0.5938264317277092, 0.758336987687637, 0.7993590316749856, 0.7272126154647645, 0.6814227277548294, 0.7181630754976537, 0.39260486580391374, 0.6171748562804691, 0.6454109779570866, 0.41456195234474275, 0.49592209998602965, 0.5905319096281916, 0.5107143326635717, 0.6345225131588169, 0.7434112841158013, 0.40626796678720645]
    ca = 
    fig_1 = plt.figure(figsize = (14 , 10))
    ax = fig_1.add_axes([0 , 0 , 1 , 1])
    ax.set_xticklabels(['global otsu /n histogram stretching median' , 'two level otsu /n no preprocessing', 'two level otsu clip', ' local adaptive thresholding counts', 'local adaptive thresholding average' ])
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

    data = [ab, bb, cb, dice_otsu_tlot_stretch_img_N2DH_GOWT1, dice_otsu_tlot_clip_stretch_img_N2DH_GOWT1 ]
    ab = [0.9012671046140265, 0.8003354141432963, 0.8060750740862693, 0.8040329829223495, 0.9048154915767894, 0.9191552972412177]
    bb =
    cb =
    
    fig_1 = plt.figure(figsize = (14 , 10))
    ax = fig_1.add_axes([0 , 0 , 1 , 1])
    ax.set_xticklabels(['global otsu /n histogram stretching' , 'two level otsu /n median filter', 'two level otsu clip'])
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