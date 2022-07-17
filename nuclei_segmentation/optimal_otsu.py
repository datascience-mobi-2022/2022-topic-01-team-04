###Optimal otsu boxplots 

#import packages 
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage
import cv2
from nuclei_segmentation import otsu as ot
from nuclei_segmentation import dicescore as dsc
from nuclei_segmentation import preprocessing as pp
from nuclei_segmentation import local_thresholding as lt
from nuclei_segmentation import two_level_otsu as tlo
import statistics as st
import os
import os.path
import scipy

from matplotlib import pylab, mlab

from IPython.core.pylabtools import figsize, getfigs


#optimal otsu boxplot NIH3T3
def dataset_boxplot_optimal_NIH3T3(plot = True):
    """
    This function prints the optimal otsu boxplot for NIH3T3. 

    :param plot: sets plot = True for boxplot
    
    """
    
    # optimal dice scores for the different Otsu variations for NIH3T3 dataset obtained by calculating the median for each preprocessing method in combination with the different Otsu variations
    aa = [0.9080295797878731, 0.9080746699707551, 0.8240269286695534, 0.7523092096313426, 0.7667266042242559, 0.7210834846002242, 0.6796112266384551, 0.7467162829788587, 0.1537407710034592, 0.61035447425189, 0.6454520836896415, 0.676574551172507, 0.5441254230662401, 0.5872934791498239, 0.6104348417019902, 0.6002316933870171, 0.737465149556319, 0.7870066342425532]
    ba = [0.9417263695042412, 0.9439370328532631, 0.5938264317277092, 0.758336987687637, 0.7993590316749856, 0.7272126154647645, 0.6814227277548294, 0.7181630754976537, 0.39260486580391374, 0.6171748562804691, 0.6454109779570866, 0.41456195234474275, 0.49592209998602965, 0.5905319096281916, 0.5107143326635717, 0.6345225131588169, 0.7434112841158013, 0.40626796678720645]
    ca = [0.8175567059223432, 0.7641330523780855, 0.3169086905969374, 0.7575338566025459, 0.7559234810310762, 0.7445915361959387, 0.6921118996297072, 0.7097600154594973, 0.4124606744520657, 0.6165896391376976, 0.6524872222683588, 0.20382743562653202, 0.5091473215831288, 0.47106917681277655, 0.3218088876557375, 0.6462982808860389, 0.7373557667869669, 0.15138678296573033]
    da = [0.909851734525395, 0.9117883553247301, 0.8642202159617313, 0.8311333937141283, 0.8420626200068814, 0.7710455256051921, 0.7590575059124861, 0.8182634981946427, 0.6282697486177428, 0.8273864920561058, 0.7128379428216284, 0.8400582412248973, 0.7435017953802454, 0.8594178859443339, 0.8761816046626265, 0.7522463087392705, 0.806145953898524, 0.8588434821780346]
    data = [aa, ba, ca, da]
    fig_1 = plt.figure(figsize = (14 , 10))
    ax = fig_1.add_axes([0 , 0 , 1 , 1])
    ax.set_xticklabels(['Global Otsu thresholding \n histogram stretching and median filter' , 'Two-level Otsu thresholding \n no preprocessing', 'Two-level Otsu thresholding clip \n no preprocessing', ' Local adaptive Otsu thresholding average \n histogram stretchingand gaussian filter' ])
    ax.set_ylim([0, 1])

    plt.title('Optimal Otsu segmentation method - NIH3T3', size = 18)
    plt.ylabel('Dice score' , size = 14)
    plt.xlabel('Otsu thresholding methods' , size = 14)


    bp = ax.boxplot(data, patch_artist = True , showmeans = True , meanline = True , meanprops = dict(color = "white" , linewidth = 1.5))
    colors = ['#FF3030', '#FF7F24','#FFB90F', '#BCEE68' ]
   
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)

    for median in bp['medians']:
        median.set(color = 'black' , linewidth = 1)
    
    print(bp["means"][0])
    plt.legend([bp["medians"][0], bp["means"][0]] , ["median", 'mean'], loc = 'lower right' , facecolor = 'gray')

#optimal otsu boxplot N2DH-GOWT1
def dataset_boxplot_optimal_N2DH_GOWT1 (plot = True):
    """
    This function prints the optimal otsu boxplot for N2DH-GOWT1.  

    :param plot: sets plot = True for boxplot
    
    """
    # optimal dice scores for the different Otsu variations for N2DH_GOWT1 dataset obtained by calculating the median for each preprocessing method in combination with the different Otsu variations
    ab = [0.6573057536130297, 0.8889624027757476, 0.8888822505843782, 0.8840789866507442, 0.8466965877165696, 0.915678984885556]
    bb = [0.9012671046140265, 0.8003354141432963, 0.8060750740862693, 0.8040329829223495, 0.9048154915767894, 0.9191552972412177]

    data = [ab, bb]

    fig_1 = plt.figure(figsize = (14 , 10))
    ax = fig_1.add_axes([0 , 0 , 1 , 1])
    ax.set_xticklabels(['Global Otsu thresholding \n histogram stretching' , 'Two-level Otsu thresholding \n median filter'])
    ax.set_ylim([0, 1])

    plt.title( 'Optimal Otsu segmentation method - N2DH-GOWT1' , size = 18)
    plt.ylabel('Dice score' , size = 14)
    plt.xlabel('Otsu thresholding methods' , size = 14)


    bp = ax.boxplot(data, patch_artist = True , showmeans = True , meanline = True , meanprops = dict(color = "white" , linewidth = 1.5))
    colors = ['#FF3030', '#FF7F24']
   
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)

    for median in bp['medians']:
        median.set(color = 'black' , linewidth = 1)
    
    print(bp["means"][0])
    plt.legend([bp["medians"][0], bp["means"][0]] , ["median", 'mean'], loc = 'lower right' , facecolor = 'gray')

#optimal otsu boxplot N2DL-HeLa
def dataset_boxplot_optimal_N2DL_HeLa (plot= True):
    """
    This function prints the optimal otsu boxplot for N2DL-HeLa. 

    :param plot: sets plot = True for boxplot
    
    """
    # optimal dice scores for the different Otsu variations for N2DL-HeLa dataset obtained by calculating the median for each preprocessing method in combination with the different Otsu variations
    ac = [0.8083639705882353, 0.8141226945021894, 0.8011127367379153, 0.8013222347823108]
    bc = [0.8817603654829008, 0.9000374463509011, 0.8842740559972709, 0.8889154796216717]
    cc = [0.8098539100544256, 0.8413827288204996, 0.8078548688897104, 0.8063821812316849]
    data = [ac,  bc, cc ]
    
    
    
    fig_1 = plt.figure(figsize = (14 , 10))
    ax = fig_1.add_axes([0 , 0 , 1 , 1])
    ax.set_xticklabels(['Global Otsu thresholding \n histogram stretching and median filter' , 'Two-level Otsu thresholding\n histogram stretching',  'Local adaptive Otsu thresholding average \n histogram stretching and median filter'])
    ax.set_ylim([0, 1])

    plt.title( 'Optimal Otsu segmentation method - N2DL-HeLa' , size = 18)
    plt.ylabel('Dice score' , size = 14)
    plt.xlabel('Otsu thresholding methods ' , size = 14)


    bp = ax.boxplot(data, patch_artist = True , showmeans = True , meanline = True , meanprops = dict(color = "white" , linewidth = 1.5))
    colors = ['#FF3030', '#FF7F24','#FFB90F']
   
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)

    for median in bp['medians']:
        median.set(color = 'black' , linewidth = 1)
    
    print(bp["means"][0])
    plt.legend([bp["medians"][0], bp["means"][0]] , ["median", 'mean'], loc = 'lower right' , facecolor = 'gray')


#optimal otsu boxplots for all datasets 
def data_boxplot_optimal_otsu_thresholding_method(x , plot = True):
    """
    This function prints the optimal otsu boxplots for all datasets. 

    :param x: parameter for function 'all'
    
    """
    if x == 'all' :
        dataset_boxplot_optimal_N2DH_GOWT1()
        dataset_boxplot_optimal_N2DL_HeLa()
        dataset_boxplot_optimal_NIH3T3()


