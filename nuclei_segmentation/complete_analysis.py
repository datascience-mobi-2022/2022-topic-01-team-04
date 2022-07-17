###Complete analysis functions for all Otsu varations 
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
from pylab import *

#complete analysis function for global otsu (for each dataset)
def complete_analysis_global_otsu(x):
    """
    This function takes a string indicating the dataset, performs the complete analysis with global otsu (all pre- and postprocessing methods)
    on this datasets and returns the boxplot.

    :param x: string (name of dataset)
    :return: boxplot of complete analysis
    
    """
    if x == 'N2DH-GOWT1':
        
        #load dataset 
        img_N2DH_GOWT1 = []
        path = os.path.join(os.path.abspath(os.path.join(r'.', os.pardir)),r"data\Otsu_data\N2DH-GOWT1\img")
        for f in os.listdir(path):
            img_N2DH_GOWT1.append(imread(os.path.join(path , f)))

        gt_N2DH_GOWT1 = []
        path = os.path.join(os.path.abspath(os.path.join(r'.', os.pardir)),r"data\Otsu_data\N2DH-GOWT1\gt")
        for f in os.listdir(path):
            gt_N2DH_GOWT1.append(imread(os.path.join(path , f)))

        #binarize ground truth
        binary_gt_N2DH_GOWT1 = []
        for i in range(0,len(gt_N2DH_GOWT1)):
            binary_gt_N2DH_GOWT1.append(pp.binarize(gt_N2DH_GOWT1[i])) 

        copy_img_N2DH_GOWT1 = img_N2DH_GOWT1.copy()

        #perform preprocessing and otsu
        median_img_N2DH_GOWT1 = []
        for i in range(0,len(copy_img_N2DH_GOWT1)):
            median_img_N2DH_GOWT1.append(scipy.ndimage.median_filter(copy_img_N2DH_GOWT1[i] , 9))

        gauss_img_N2DH_GOWT1 = []
        for i in range(0,len(copy_img_N2DH_GOWT1)):
            gauss_img_N2DH_GOWT1.append(scipy.ndimage.gaussian_filter(copy_img_N2DH_GOWT1[i] , 9))

        stretch_img_N2DH_GOWT1 = []
        for i in range(0,len(copy_img_N2DH_GOWT1)):
            stretch_img_N2DH_GOWT1.append(pp.stretch(copy_img_N2DH_GOWT1[i]))

        median_stretch_img_N2DH_GOWT1 = []
        for i in range(0,len(median_img_N2DH_GOWT1)):
            median_stretch_img_N2DH_GOWT1.append(pp.stretch(median_img_N2DH_GOWT1[i]))

        stretch_median_img_N2DH_GOWT1 = []
        for i in range(0,len(stretch_img_N2DH_GOWT1)):
            stretch_median_img_N2DH_GOWT1.append(scipy.ndimage.median_filter(stretch_img_N2DH_GOWT1[i] , 9))

        gauss_stretch_img_N2DH_GOWT1 = []
        for i in range(0,len(gauss_img_N2DH_GOWT1)):
            gauss_stretch_img_N2DH_GOWT1.append(pp.stretch(gauss_img_N2DH_GOWT1[i]))
        
        stretch_gauss_img_N2DH_GOWT1 = []
        for i in range(0,len(stretch_img_N2DH_GOWT1)):
            stretch_gauss_img_N2DH_GOWT1.append(scipy.ndimage.gaussian_filter(stretch_img_N2DH_GOWT1[i] , 9))

        otsu_img_N2DH_GOWT1 = []
        for i in range(0,len(copy_img_N2DH_GOWT1)):
            otsu_img_N2DH_GOWT1.append(pp.holefilling(ot.otsu_thresholding(copy_img_N2DH_GOWT1[i] , 256),15))

        otsu_median_img_N2DH_GOWT1 = []
        for i in range(0,len(median_img_N2DH_GOWT1)):
            otsu_median_img_N2DH_GOWT1.append(pp.holefilling(ot.otsu_thresholding(median_img_N2DH_GOWT1[i] , 256),15))

        otsu_gauss_img_N2DH_GOWT1 = []
        for i in range(0,len(gauss_img_N2DH_GOWT1)):
            otsu_gauss_img_N2DH_GOWT1.append(pp.holefilling(ot.otsu_thresholding(gauss_img_N2DH_GOWT1[i] , 256),15))

        otsu_stretch_img_N2DH_GOWT1 = []
        for i in range(0,len(stretch_img_N2DH_GOWT1)):
            otsu_stretch_img_N2DH_GOWT1.append(pp.holefilling(ot.otsu_thresholding(stretch_img_N2DH_GOWT1[i] , 256),15))

        otsu_median_stretch_img_N2DH_GOWT1 = []
        for i in range(0,len(median_stretch_img_N2DH_GOWT1)):
            otsu_median_stretch_img_N2DH_GOWT1.append(pp.holefilling(ot.otsu_thresholding(median_stretch_img_N2DH_GOWT1[i] , 256),15))
            
        otsu_stretch_median_img_N2DH_GOWT1 = []
        for i in range(0,len(stretch_median_img_N2DH_GOWT1)):
            otsu_stretch_median_img_N2DH_GOWT1.append(pp.holefilling(ot.otsu_thresholding(stretch_median_img_N2DH_GOWT1[i] , 256),15))

        otsu_gauss_stretch_img_N2DH_GOWT1 = []
        for i in range(0,len(gauss_stretch_img_N2DH_GOWT1)):
            otsu_gauss_stretch_img_N2DH_GOWT1.append(pp.holefilling(ot.otsu_thresholding(gauss_stretch_img_N2DH_GOWT1[i] , 256),15))
        
        otsu_stretch_gauss_img_N2DH_GOWT1 = []
        for i in range(0,len(stretch_gauss_img_N2DH_GOWT1)):
            otsu_stretch_gauss_img_N2DH_GOWT1.append(pp.holefilling(ot.otsu_thresholding(stretch_gauss_img_N2DH_GOWT1[i] , 256),15))

        #calculate dice scores
        dice_otsu_img_N2DH_GOWT1 = []
        for j in range(0,len(otsu_img_N2DH_GOWT1)):
            dice_otsu_img_N2DH_GOWT1.append(dsc.dice(otsu_img_N2DH_GOWT1[j] , binary_gt_N2DH_GOWT1[j]))

        dice_otsu_median_img_N2DH_GOWT1 = []
        for j in range(0,len(otsu_median_img_N2DH_GOWT1)):
            dice_otsu_median_img_N2DH_GOWT1.append(dsc.dice(otsu_median_img_N2DH_GOWT1[j] , binary_gt_N2DH_GOWT1[j]))

        dice_otsu_gauss_img_N2DH_GOWT1 = []
        for j in range(0,len(otsu_gauss_img_N2DH_GOWT1)):
            dice_otsu_gauss_img_N2DH_GOWT1.append(dsc.dice(otsu_gauss_img_N2DH_GOWT1[j] , binary_gt_N2DH_GOWT1[j]))

        dice_otsu_stretch_img_N2DH_GOWT1 = []
        for j in range(0,len(otsu_stretch_img_N2DH_GOWT1)):
            dice_otsu_stretch_img_N2DH_GOWT1.append(dsc.dice(otsu_stretch_img_N2DH_GOWT1[j] , binary_gt_N2DH_GOWT1[j]))

        dice_otsu_median_stretch_img_N2DH_GOWT1 = []
        for j in range(0,len(otsu_median_stretch_img_N2DH_GOWT1)):
            dice_otsu_median_stretch_img_N2DH_GOWT1.append(dsc.dice(otsu_median_stretch_img_N2DH_GOWT1[j] , binary_gt_N2DH_GOWT1[j]))
        
        dice_otsu_stretch_median_img_N2DH_GOWT1 = []
        for j in range(0,len(otsu_stretch_median_img_N2DH_GOWT1)):
            dice_otsu_stretch_median_img_N2DH_GOWT1.append(dsc.dice(otsu_stretch_median_img_N2DH_GOWT1[j] , binary_gt_N2DH_GOWT1[j]))

        #choose best combination histogram stretching and median filter 
        median1 = st.median(dice_otsu_median_stretch_img_N2DH_GOWT1)
        median2 = st.median(dice_otsu_stretch_median_img_N2DH_GOWT1)

        if(max(median1,median2) == median1):
            optimal_dice_stretch_median = dice_otsu_median_stretch_img_N2DH_GOWT1
        else: optimal_dice_stretch_median = dice_otsu_stretch_median_img_N2DH_GOWT1
        
        dice_otsu_gauss_stretch_img_N2DH_GOWT1 = []
        for j in range(0,len(otsu_gauss_stretch_img_N2DH_GOWT1)):
            dice_otsu_gauss_stretch_img_N2DH_GOWT1.append(dsc.dice(otsu_gauss_stretch_img_N2DH_GOWT1[j] , binary_gt_N2DH_GOWT1[j]))
        
        dice_otsu_stretch_gauss_img_N2DH_GOWT1 = []
        for j in range(0,len(otsu_stretch_gauss_img_N2DH_GOWT1)):
            dice_otsu_stretch_gauss_img_N2DH_GOWT1.append(dsc.dice(otsu_stretch_gauss_img_N2DH_GOWT1[j] , binary_gt_N2DH_GOWT1[j]))
        
        #choose best combination histogram stretching and gaussian filter 
        median3 = st.median(dice_otsu_gauss_stretch_img_N2DH_GOWT1)
        median4 = st.median(dice_otsu_stretch_gauss_img_N2DH_GOWT1)

        if(max(median3,median4) == median3):
            optimal_dice_stretch_gauss = dice_otsu_gauss_stretch_img_N2DH_GOWT1
        else: optimal_dice_stretch_gauss = dice_otsu_stretch_gauss_img_N2DH_GOWT1

    
        data_N2DH_GOWT1 = [dice_otsu_img_N2DH_GOWT1 , dice_otsu_median_img_N2DH_GOWT1 , dice_otsu_gauss_img_N2DH_GOWT1 , dice_otsu_stretch_img_N2DH_GOWT1  , optimal_dice_stretch_median  , optimal_dice_stretch_gauss]

        #load boxplot 
        boxplot = pp.dataset_boxplot_otsu(data_N2DH_GOWT1 , 'Preprocessing methods - N2DH-GOWT1 - Global Otsu Thresholding')
    
    
    if x == 'N2DL-HeLa' :     
        #load dataset
        img_N2DL_HeLa = []
        path = os.path.join(os.path.abspath(os.path.join(r'.', os.pardir)),r"data\Otsu_data\N2DL-HeLa\img")
        for f in os.listdir(path):
            img_N2DL_HeLa.append(imread(os.path.join(path , f)))

        gt_N2DL_HeLa = []
        path = os.path.join(os.path.abspath(os.path.join(r'.', os.pardir)),r"data\Otsu_data\N2DL-HeLa\gt")
        for f in os.listdir(path):
            gt_N2DL_HeLa.append(imread(os.path.join(path , f)))

        #binarize ground truth image
        binary_gt_N2DL_HeLa = []
        for i in range(0,len(gt_N2DL_HeLa)):
            binary_gt_N2DL_HeLa.append(pp.binarize(gt_N2DL_HeLa[i])) 

        copy_img_N2DL_HeLa = img_N2DL_HeLa.copy()

        #perform preprocessing and otsu
        median_img_N2DL_HeLa = []
        for i in range(0,len(copy_img_N2DL_HeLa)):
            median_img_N2DL_HeLa.append(scipy.ndimage.median_filter(copy_img_N2DL_HeLa[i] , 2))

        gauss_img_N2DL_HeLa = []
        for i in range(0,len(copy_img_N2DL_HeLa)):
            gauss_img_N2DL_HeLa.append(scipy.ndimage.gaussian_filter(copy_img_N2DL_HeLa[i] , 4))

        stretch_img_N2DL_HeLa = []
        for i in range(0,len(copy_img_N2DL_HeLa)):
            stretch_img_N2DL_HeLa.append(pp.stretch(copy_img_N2DL_HeLa[i]))

        median_stretch_img_N2DL_HeLa = []
        for i in range(0,len(median_img_N2DL_HeLa)):
            median_stretch_img_N2DL_HeLa.append(pp.stretch(median_img_N2DL_HeLa[i]))

        stretch_median_img_N2DL_HeLa = []
        for i in range(0,len(stretch_img_N2DL_HeLa)):
            stretch_median_img_N2DL_HeLa.append(scipy.ndimage.median_filter(stretch_img_N2DL_HeLa[i] , 2))
        
        gauss_stretch_img_N2DL_HeLa = []
        for i in range(0,len(gauss_img_N2DL_HeLa)):
            gauss_stretch_img_N2DL_HeLa.append(pp.stretch(gauss_img_N2DL_HeLa[i]))
        
        stretch_gauss_img_N2DL_HeLa = []
        for i in range(0,len(stretch_img_N2DL_HeLa)):
            stretch_gauss_img_N2DL_HeLa.append(scipy.ndimage.gaussian_filter(stretch_img_N2DL_HeLa[i] , 4))

        otsu_img_N2DL_HeLa = []
        for i in range(0,len(copy_img_N2DL_HeLa)):
            otsu_img_N2DL_HeLa.append(ot.otsu_thresholding(copy_img_N2DL_HeLa[i] , 256))

        otsu_median_img_N2DL_HeLa = []
        for i in range(0,len(median_img_N2DL_HeLa)):
            otsu_median_img_N2DL_HeLa.append(ot.otsu_thresholding(median_img_N2DL_HeLa[i] , 256))

        otsu_gauss_img_N2DL_HeLa = []
        for i in range(0,len(gauss_img_N2DL_HeLa)):
            otsu_gauss_img_N2DL_HeLa.append(ot.otsu_thresholding(gauss_img_N2DL_HeLa[i] , 256))

        otsu_stretch_img_N2DL_HeLa = []
        for i in range(0,len(stretch_img_N2DL_HeLa)):
            otsu_stretch_img_N2DL_HeLa.append(ot.otsu_thresholding(stretch_img_N2DL_HeLa[i] , 256))

        otsu_median_stretch_img_N2DL_HeLa = []
        for i in range(0,len(median_stretch_img_N2DL_HeLa)):
            otsu_median_stretch_img_N2DL_HeLa.append(ot.otsu_thresholding(median_stretch_img_N2DL_HeLa[i] , 256))
        
        otsu_stretch_median_img_N2DL_HeLa = []
        for i in range(0,len(stretch_median_img_N2DL_HeLa)):
            otsu_stretch_median_img_N2DL_HeLa.append(ot.otsu_thresholding(stretch_median_img_N2DL_HeLa[i] , 256))
        
        otsu_gauss_stretch_img_N2DL_HeLa = []
        for i in range(0,len(gauss_stretch_img_N2DL_HeLa)):
            otsu_gauss_stretch_img_N2DL_HeLa.append(ot.otsu_thresholding(gauss_stretch_img_N2DL_HeLa[i] , 256))
        
        otsu_stretch_gauss_img_N2DL_HeLa = []
        for i in range(0,len(stretch_gauss_img_N2DL_HeLa)):
            otsu_stretch_gauss_img_N2DL_HeLa.append(ot.otsu_thresholding(stretch_gauss_img_N2DL_HeLa[i] , 256))

        #calculate dice scores 
        dice_otsu_img_N2DL_HeLa = []
        for j in range(0,len(otsu_img_N2DL_HeLa)):
            dice_otsu_img_N2DL_HeLa.append(dsc.dice(otsu_img_N2DL_HeLa[j] , binary_gt_N2DL_HeLa[j]))

        dice_otsu_median_img_N2DL_HeLa = []
        for j in range(0,len(otsu_median_img_N2DL_HeLa)):
            dice_otsu_median_img_N2DL_HeLa.append(dsc.dice(otsu_median_img_N2DL_HeLa[j] , binary_gt_N2DL_HeLa[j]))

        dice_otsu_gauss_img_N2DL_HeLa = []
        for j in range(0,len(otsu_gauss_img_N2DL_HeLa)):
            dice_otsu_gauss_img_N2DL_HeLa.append(dsc.dice(otsu_gauss_img_N2DL_HeLa[j] , binary_gt_N2DL_HeLa[j]))

        dice_otsu_stretch_img_N2DL_HeLa = []
        for j in range(0,len(otsu_stretch_img_N2DL_HeLa)):
            dice_otsu_stretch_img_N2DL_HeLa.append(dsc.dice(otsu_stretch_img_N2DL_HeLa[j] , binary_gt_N2DL_HeLa[j]))

        dice_otsu_median_stretch_img_N2DL_HeLa = []
        for j in range(0,len(otsu_median_stretch_img_N2DL_HeLa)):
            dice_otsu_median_stretch_img_N2DL_HeLa.append(dsc.dice(otsu_median_stretch_img_N2DL_HeLa[j] , binary_gt_N2DL_HeLa[j]))

        dice_otsu_stretch_median_img_N2DL_HeLa = []
        for j in range(0,len(otsu_stretch_median_img_N2DL_HeLa)):
            dice_otsu_stretch_median_img_N2DL_HeLa.append(dsc.dice(otsu_stretch_median_img_N2DL_HeLa[j] , binary_gt_N2DL_HeLa[j]))
        
        #choose best combination histogram stretching and median filter 
        median1 = st.median(dice_otsu_median_stretch_img_N2DL_HeLa)
        median2 = st.median(dice_otsu_stretch_median_img_N2DL_HeLa)

        if(max(median1,median2) == median1):
            optimal_dice_stretch_median = dice_otsu_median_stretch_img_N2DL_HeLa
        else: optimal_dice_stretch_median = dice_otsu_stretch_median_img_N2DL_HeLa

        dice_otsu_gauss_stretch_img_N2DL_HeLa = []
        for j in range(0,len(otsu_gauss_stretch_img_N2DL_HeLa)):
            dice_otsu_gauss_stretch_img_N2DL_HeLa.append(dsc.dice(otsu_gauss_stretch_img_N2DL_HeLa[j] , binary_gt_N2DL_HeLa[j]))    
        
        dice_otsu_stretch_gauss_img_N2DL_HeLa = []
        for j in range(0,len(otsu_stretch_gauss_img_N2DL_HeLa)):
            dice_otsu_stretch_gauss_img_N2DL_HeLa.append(dsc.dice(otsu_stretch_gauss_img_N2DL_HeLa[j] , binary_gt_N2DL_HeLa[j]))

        #choose best combination histogram stretching and gaussian filter 
        median3 = st.median(dice_otsu_gauss_stretch_img_N2DL_HeLa)
        median4 = st.median(dice_otsu_stretch_gauss_img_N2DL_HeLa)

        if(max(median3,median4) == median3):
            optimal_dice_stretch_gauss = dice_otsu_gauss_stretch_img_N2DL_HeLa
        else: optimal_dice_stretch_gauss = dice_otsu_stretch_gauss_img_N2DL_HeLa

        data_N2DLHeLa = [dice_otsu_img_N2DL_HeLa , dice_otsu_median_img_N2DL_HeLa , dice_otsu_gauss_img_N2DL_HeLa , dice_otsu_stretch_img_N2DL_HeLa , optimal_dice_stretch_median , optimal_dice_stretch_gauss]

        #load boxplot 
        boxplot = pp.dataset_boxplot_otsu(data_N2DLHeLa , 'Preprocessing methods - N2DL-HeLa - Global Otsu Thresholding')

    
    if x == 'NIH3T3' :
        
        #load dataset 
        img_NIH3T3 = []
        path = os.path.join(os.path.abspath(os.path.join(r'.', os.pardir)),r"data\Otsu_data\NIH3T3\img")
        for f in os.listdir(path):
            img_NIH3T3.append(imread(os.path.join(path , f)))

        gt_NIH3T3 = []
        path = os.path.join(os.path.abspath(os.path.join(r'.', os.pardir)),r"data\Otsu_data\NIH3T3\gt")
        for f in os.listdir(path):
            gt_NIH3T3.append(imread(os.path.join(path , f)))

        copy_img_NIH3T3 = img_NIH3T3.copy()

        #perform preprocessing and otsu
        median_img_NIH3T3 = []
        for i in range(0,len(copy_img_NIH3T3)):
            median_img_NIH3T3.append(scipy.ndimage.median_filter(copy_img_NIH3T3[i] , 16))

        gauss_img_NIH3T3 = []
        for i in range(0,len(copy_img_NIH3T3)):
            gauss_img_NIH3T3.append(scipy.ndimage.gaussian_filter(copy_img_NIH3T3[i] , 8))

        stretch_img_NIH3T3 = []
        for i in range(0,len(copy_img_NIH3T3)):
            stretch_img_NIH3T3.append(pp.stretch(copy_img_NIH3T3[i]))

        median_stretch_img_NIH3T3 = []
        for i in range(0,len(median_img_NIH3T3)):
            median_stretch_img_NIH3T3.append(pp.stretch(median_img_NIH3T3[i]))

        stretch_median_img_NIH3T3 = []
        for i in range(0,len(stretch_img_NIH3T3)):
            stretch_median_img_NIH3T3.append(scipy.ndimage.median_filter(stretch_img_NIH3T3[i] , 16))

        gauss_stretch_img_NIH3T3 = []
        for i in range(0,len(gauss_img_NIH3T3)):
            gauss_stretch_img_NIH3T3.append(pp.stretch(gauss_img_NIH3T3[i]))

        stretch_gauss_img_NIH3T3 = []
        for i in range(0,len(stretch_img_NIH3T3)):
            stretch_gauss_img_NIH3T3.append(scipy.ndimage.gaussian_filter(stretch_img_NIH3T3[i] , 8))

        otsu_img_NIH3T3 = []
        for i in range(0,len(copy_img_NIH3T3)):
            otsu_img_NIH3T3.append(ot.otsu_thresholding(copy_img_NIH3T3[i] , 256))

        otsu_median_img_NIH3T3 = []
        for i in range(0,len(median_img_NIH3T3)):
            otsu_median_img_NIH3T3.append(ot.otsu_thresholding(median_img_NIH3T3[i] , 256))

        otsu_gauss_img_NIH3T3 = []
        for i in range(0,len(gauss_img_NIH3T3)):
            otsu_gauss_img_NIH3T3.append(ot.otsu_thresholding(gauss_img_NIH3T3[i] , 256))

        otsu_stretch_img_NIH3T3 = []
        for i in range(0,len(stretch_img_NIH3T3)):
            otsu_stretch_img_NIH3T3.append(ot.otsu_thresholding(stretch_img_NIH3T3[i] , 256))
        
        otsu_median_stretch_img_NIH3T3 = []
        for i in range(0,len(median_stretch_img_NIH3T3)):
            otsu_median_stretch_img_NIH3T3.append(ot.otsu_thresholding(median_stretch_img_NIH3T3[i] , 256))
        
        otsu_stretch_median_img_NIH3T3 = []
        for i in range(0,len(stretch_median_img_NIH3T3)):
            otsu_stretch_median_img_NIH3T3.append(ot.otsu_thresholding(stretch_median_img_NIH3T3[i] , 256))
        
        otsu_gauss_stretch_img_NIH3T3 = []
        for i in range(0,len(gauss_stretch_img_NIH3T3)):
            otsu_gauss_stretch_img_NIH3T3.append(ot.otsu_thresholding(gauss_stretch_img_NIH3T3[i] , 256))

        otsu_stretch_gauss_img_NIH3T3 = []
        for i in range(0,len(stretch_gauss_img_NIH3T3)):
            otsu_stretch_gauss_img_NIH3T3.append(ot.otsu_thresholding(stretch_gauss_img_NIH3T3[i] , 256))
        
        #calculate dice scores
        dice_otsu_img_NIH3T3 = []
        for j in range(0,len(otsu_img_NIH3T3)):
            dice_otsu_img_NIH3T3.append(dsc.dice(otsu_img_NIH3T3[j] , gt_NIH3T3[j]))

        dice_otsu_median_img_NIH3T3 = []
        for j in range(0,len(otsu_median_img_NIH3T3)):
            dice_otsu_median_img_NIH3T3.append(dsc.dice(otsu_median_img_NIH3T3[j] , gt_NIH3T3[j]))

        dice_otsu_gauss_img_NIH3T3 = []
        for j in range(0,len(otsu_gauss_img_NIH3T3)):
            dice_otsu_gauss_img_NIH3T3.append(dsc.dice(otsu_gauss_img_NIH3T3[j] , gt_NIH3T3[j]))

        dice_otsu_stretch_img_NIH3T3 = []
        for j in range(0,len(otsu_stretch_img_NIH3T3)):
            dice_otsu_stretch_img_NIH3T3.append(dsc.dice(otsu_stretch_img_NIH3T3[j] , gt_NIH3T3[j]))
        
        dice_otsu_median_stretch_img_NIH3T3 = []
        for j in range(0,len(otsu_median_stretch_img_NIH3T3)):
            dice_otsu_median_stretch_img_NIH3T3.append(dsc.dice(otsu_median_stretch_img_NIH3T3[j] , gt_NIH3T3[j]))

        dice_otsu_stretch_median_img_NIH3T3 = []
        for j in range(0,len(otsu_stretch_median_img_NIH3T3)):
            dice_otsu_stretch_median_img_NIH3T3.append(dsc.dice(otsu_stretch_median_img_NIH3T3[j] , gt_NIH3T3[j]))
        
        #choose best combination histogram stretching and median filter 
        median1 = st.median(dice_otsu_median_stretch_img_NIH3T3)
        median2 = st.median(dice_otsu_stretch_median_img_NIH3T3)

        if(max(median1,median2) == median1):
            optimal_dice_stretch_median = dice_otsu_median_stretch_img_NIH3T3
        else: optimal_dice_stretch_median = dice_otsu_stretch_median_img_NIH3T3

        dice_otsu_gauss_stretch_img_NIH3T3 = []
        for j in range(0,len(otsu_gauss_stretch_img_NIH3T3)):
            dice_otsu_gauss_stretch_img_NIH3T3.append(dsc.dice(otsu_gauss_stretch_img_NIH3T3[j] , gt_NIH3T3[j]))
        
        dice_otsu_stretch_gauss_img_NIH3T3 = []
        for j in range(0,len(otsu_stretch_gauss_img_NIH3T3)):
            dice_otsu_stretch_gauss_img_NIH3T3.append(dsc.dice(otsu_stretch_gauss_img_NIH3T3[j] , gt_NIH3T3[j]))

        #choose best combination histogram stretching and gaussian filter 
        median3 = st.median(dice_otsu_gauss_stretch_img_NIH3T3)
        median4 = st.median(dice_otsu_stretch_gauss_img_NIH3T3)

        if(max(median3,median4) == median3):
            optimal_dice_stretch_gauss = dice_otsu_gauss_stretch_img_NIH3T3
        else: optimal_dice_stretch_gauss = dice_otsu_stretch_gauss_img_NIH3T3

        data_NIH3T3 = [dice_otsu_img_NIH3T3 , dice_otsu_median_img_NIH3T3 , dice_otsu_gauss_img_NIH3T3 , dice_otsu_stretch_img_NIH3T3 , optimal_dice_stretch_median , optimal_dice_stretch_gauss]

        #load boxplot
        boxplot = pp.dataset_boxplot_otsu(data_NIH3T3 , 'Preprocessing methods - NIH3T3 - Global Otsu Thresholding')
        
    return boxplot

#complete analysis for all datasets in one function (for global otsu)
def complete_analysis_global_otsu_all(x):
    """
    This function performs the complete analysis for global otsu on all datasets. 

    :param x: parameter for function 'all'
    
    """
    if x == 'all':
        complete_analysis_global_otsu("N2DH-GOWT1")
        complete_analysis_global_otsu("N2DL-HeLa")
        complete_analysis_global_otsu("NIH3T3")

#complete analysis for two level otsu clip (for NIH3T3)
def complete_analysis_two_level_clip():
    complete_analysis_two_level_otsu_clip('NIH3T3')

#complete analysis function for two level otsu clip (for each dataset)
def complete_analysis_two_level_otsu_clip(x):
    """
    This function takes a string indicating the dataset, performs the complete analysis with two level otsu clip(all pre- and postprocessing methods)
    on this datasets and returns the boxplot.

    :param x: string (name of dataset), in this case only NIH3T3
    :return: boxplot of complete analysis
    
    """
    if x == 'NIH3T3' :
        
        #load dataset
        img_NIH3T3 = []
        path = os.path.join(os.path.abspath(os.path.join(r'.', os.pardir)),r"data/Otsu_data/NIH3T3/img")
        for f in os.listdir(path):
            img_NIH3T3.append(imread(os.path.join(path , f)))

        gt_NIH3T3 = []
        path = os.path.join(os.path.abspath(os.path.join(r'.', os.pardir)),r"data/Otsu_data/NIH3T3/gt")
        for f in os.listdir(path):
            gt_NIH3T3.append(imread(os.path.join(path , f)))

        copy_img_NIH3T3 = img_NIH3T3.copy()

        #perform preprocessing and otsu
        median_img_NIH3T3 = []
        for i in range(0,len(copy_img_NIH3T3)):
            median_img_NIH3T3.append(scipy.ndimage.median_filter(copy_img_NIH3T3[i] , 16))

        gauss_img_NIH3T3 = []
        for i in range(0,len(copy_img_NIH3T3)):
            gauss_img_NIH3T3.append(scipy.ndimage.gaussian_filter(copy_img_NIH3T3[i] , 8))

        stretch_img_NIH3T3 = []
        for i in range(0,len(copy_img_NIH3T3)):
            stretch_img_NIH3T3.append(pp.stretch(copy_img_NIH3T3[i]))

        median_stretch_img_NIH3T3 = []
        for i in range(0,len(median_img_NIH3T3)):
            median_stretch_img_NIH3T3.append(pp.stretch(median_img_NIH3T3[i]))

        stretch_median_img_NIH3T3 = []
        for i in range(0,len(stretch_img_NIH3T3)):
            stretch_median_img_NIH3T3.append(scipy.ndimage.median_filter(stretch_img_NIH3T3[i] , 16))

        gauss_stretch_img_NIH3T3 = []
        for i in range(0,len(gauss_img_NIH3T3)):
            gauss_stretch_img_NIH3T3.append(pp.stretch(gauss_img_NIH3T3[i]))

        stretch_gauss_img_NIH3T3 = []
        for i in range(0,len(stretch_img_NIH3T3)):
            stretch_gauss_img_NIH3T3.append(scipy.ndimage.gaussian_filter(stretch_img_NIH3T3[i] , 8))

        otsu_img_NIH3T3 = []
        for i in range(0,len(copy_img_NIH3T3)):
            otsu_img_NIH3T3.append(tlo.two_level_otsu_thresholding_clip(copy_img_NIH3T3[i] , 256))

        otsu_median_img_NIH3T3 = []
        for i in range(0,len(median_img_NIH3T3)):
            otsu_median_img_NIH3T3.append(tlo.two_level_otsu_thresholding_clip(median_img_NIH3T3[i] , 256))

        otsu_gauss_img_NIH3T3 = []
        for i in range(0,len(gauss_img_NIH3T3)):
            otsu_gauss_img_NIH3T3.append(tlo.two_level_otsu_thresholding_clip(gauss_img_NIH3T3[i] , 256))

        otsu_stretch_img_NIH3T3 = []
        for i in range(0,len(stretch_img_NIH3T3)):
            otsu_stretch_img_NIH3T3.append(tlo.two_level_otsu_thresholding_clip(stretch_img_NIH3T3[i] , 256))
        
        
        otsu_median_stretch_img_NIH3T3 = []
        for i in range(0,len(median_stretch_img_NIH3T3)):
            otsu_median_stretch_img_NIH3T3.append(tlo.two_level_otsu_thresholding_clip(median_stretch_img_NIH3T3[i] , 256))
        
        otsu_stretch_median_img_NIH3T3 = []
        for i in range(0,len(stretch_median_img_NIH3T3)):
            otsu_stretch_median_img_NIH3T3.append(tlo.two_level_otsu_thresholding_clip(stretch_median_img_NIH3T3[i] , 256))
        
        otsu_gauss_stretch_img_NIH3T3 = []
        for i in range(0,len(gauss_stretch_img_NIH3T3)):
            otsu_gauss_stretch_img_NIH3T3.append(tlo.two_level_otsu_thresholding_clip(gauss_stretch_img_NIH3T3[i] , 256))

        otsu_stretch_gauss_img_NIH3T3 = []
        for i in range(0,len(stretch_gauss_img_NIH3T3)):
            otsu_stretch_gauss_img_NIH3T3.append(tlo.two_level_otsu_thresholding_clip(stretch_gauss_img_NIH3T3[i] , 256))

        #calculate dice score
        dice_otsu_img_NIH3T3 = []
        for j in range(0,len(otsu_img_NIH3T3)):
            dice_otsu_img_NIH3T3.append(dsc.dice(otsu_img_NIH3T3[j] , gt_NIH3T3[j]))

        dice_otsu_median_img_NIH3T3 = []
        for j in range(0,len(otsu_median_img_NIH3T3)):
            dice_otsu_median_img_NIH3T3.append(dsc.dice(otsu_median_img_NIH3T3[j] , gt_NIH3T3[j]))

        dice_otsu_gauss_img_NIH3T3 = []
        for j in range(0,len(otsu_gauss_img_NIH3T3)):
            dice_otsu_gauss_img_NIH3T3.append(dsc.dice(otsu_gauss_img_NIH3T3[j] , gt_NIH3T3[j]))
        
        dice_otsu_stretch_img_NIH3T3 = []
        for j in range(0,len(otsu_stretch_img_NIH3T3)):
            dice_otsu_stretch_img_NIH3T3.append(dsc.dice(otsu_stretch_img_NIH3T3[j] , gt_NIH3T3[j]))
        
        dice_otsu_median_stretch_img_NIH3T3 = []
        for j in range(0,len(otsu_median_stretch_img_NIH3T3)):
            dice_otsu_median_stretch_img_NIH3T3.append(dsc.dice(otsu_median_stretch_img_NIH3T3[j] , gt_NIH3T3[j]))

        dice_otsu_stretch_median_img_NIH3T3 = []
        for j in range(0,len(otsu_stretch_median_img_NIH3T3)):
            dice_otsu_stretch_median_img_NIH3T3.append(dsc.dice(otsu_stretch_median_img_NIH3T3[j] , gt_NIH3T3[j]))
        
        #choose best combination histogram stretching and median filter 
        median1 = st.median(dice_otsu_median_stretch_img_NIH3T3)
        median2 = st.median(dice_otsu_stretch_median_img_NIH3T3)

        if(max(median1,median2) == median1):
            optimal_dice_stretch_median = dice_otsu_median_stretch_img_NIH3T3
        else: optimal_dice_stretch_median = dice_otsu_stretch_median_img_NIH3T3

        dice_otsu_gauss_stretch_img_NIH3T3 = []
        for j in range(0,len(otsu_gauss_stretch_img_NIH3T3)):
            dice_otsu_gauss_stretch_img_NIH3T3.append(dsc.dice(otsu_gauss_stretch_img_NIH3T3[j] , gt_NIH3T3[j]))
        
        dice_otsu_stretch_gauss_img_NIH3T3 = []
        for j in range(0,len(otsu_stretch_gauss_img_NIH3T3)):
            dice_otsu_stretch_gauss_img_NIH3T3.append(dsc.dice(otsu_stretch_gauss_img_NIH3T3[j] , gt_NIH3T3[j]))

        #choose best combination histogram stretching and gaussian filter 
        median3 = st.median(dice_otsu_gauss_stretch_img_NIH3T3)
        median4 = st.median(dice_otsu_stretch_gauss_img_NIH3T3)

        if(max(median3,median4) == median3):
            optimal_dice_stretch_gauss = dice_otsu_gauss_stretch_img_NIH3T3
        else: optimal_dice_stretch_gauss = dice_otsu_stretch_gauss_img_NIH3T3
        

        data_NIH3T3 = [dice_otsu_img_NIH3T3 , dice_otsu_median_img_NIH3T3 , dice_otsu_gauss_img_NIH3T3 , dice_otsu_stretch_img_NIH3T3 , optimal_dice_stretch_median , optimal_dice_stretch_gauss]

        #load boxplot
        boxplot = pp.dataset_boxplot_otsu(data_NIH3T3 , 'Preprocessing methods - NIH3T3-two-level-Otsu')        
   
    return boxplot



#complete analysis function for two level otsu (for each dataset)

def complete_analysis_two_level_otsu(x):
    """
    This function takes a string indicating the dataset, performs the complete analysis with two level otsu (all pre- and postprocessing methods)
    on this datasets and returns the boxplot.

    :param x: string (name of dataset)
    :return: boxplot of complete analysis
    
    """
    if x == 'N2DH-GOWT1':
        #load dataset
        img_N2DH_GOWT1 = []
        path = os.path.join(os.path.abspath(os.path.join(r'.', os.pardir)),r"data\Otsu_data\N2DH-GOWT1\img")
        for f in os.listdir(path):
            img_N2DH_GOWT1.append(imread(os.path.join(path , f)))

        gt_N2DH_GOWT1 = []
        path = os.path.join(os.path.abspath(os.path.join(r'.', os.pardir)),r"data\Otsu_data\N2DH-GOWT1\gt")
        for f in os.listdir(path):
            gt_N2DH_GOWT1.append(imread(os.path.join(path , f)))

        #binarize ground truth image 
        binary_gt_N2DH_GOWT1 = []
        for i in range(0,len(gt_N2DH_GOWT1)):
            binary_gt_N2DH_GOWT1.append(pp.binarize(gt_N2DH_GOWT1[i])) 

        copy_img_N2DH_GOWT1 = img_N2DH_GOWT1.copy()

        #perform preprocessing and otsu
        median_img_N2DH_GOWT1 = []
        for i in range(0,len(copy_img_N2DH_GOWT1)):
            median_img_N2DH_GOWT1.append(scipy.ndimage.median_filter(copy_img_N2DH_GOWT1[i] , 9))

        gauss_img_N2DH_GOWT1 = []
        for i in range(0,len(copy_img_N2DH_GOWT1)):
            gauss_img_N2DH_GOWT1.append(scipy.ndimage.gaussian_filter(copy_img_N2DH_GOWT1[i] , 9))

        stretch_img_N2DH_GOWT1 = []
        for i in range(0,len(copy_img_N2DH_GOWT1)):
            stretch_img_N2DH_GOWT1.append(pp.stretch(copy_img_N2DH_GOWT1[i]))

        median_stretch_img_N2DH_GOWT1 = []
        for i in range(0,len(median_img_N2DH_GOWT1)):
            median_stretch_img_N2DH_GOWT1.append(pp.stretch(median_img_N2DH_GOWT1[i]))

        stretch_median_img_N2DH_GOWT1 = []
        for i in range(0,len(stretch_img_N2DH_GOWT1)):
            stretch_median_img_N2DH_GOWT1.append(scipy.ndimage.median_filter(stretch_img_N2DH_GOWT1[i] , 9))

        gauss_stretch_img_N2DH_GOWT1 = []
        for i in range(0,len(gauss_img_N2DH_GOWT1)):
            gauss_stretch_img_N2DH_GOWT1.append(pp.stretch(gauss_img_N2DH_GOWT1[i]))
        
        stretch_gauss_img_N2DH_GOWT1 = []
        for i in range(0,len(stretch_img_N2DH_GOWT1)):
            stretch_gauss_img_N2DH_GOWT1.append(scipy.ndimage.gaussian_filter(stretch_img_N2DH_GOWT1[i] , 9))

        otsu_img_N2DH_GOWT1 = []
        for i in range(0,len(copy_img_N2DH_GOWT1)):
            otsu_img_N2DH_GOWT1.append(pp.holefilling(tlo.two_level_otsu_thresholding(copy_img_N2DH_GOWT1[i] , 256),15))

        otsu_median_img_N2DH_GOWT1 = []
        for i in range(0,len(median_img_N2DH_GOWT1)):
            otsu_median_img_N2DH_GOWT1.append(pp.holefilling(tlo.two_level_otsu_thresholding(median_img_N2DH_GOWT1[i] , 256),15))

        otsu_gauss_img_N2DH_GOWT1 = []
        for i in range(0,len(gauss_img_N2DH_GOWT1)):
            otsu_gauss_img_N2DH_GOWT1.append(pp.holefilling(tlo.two_level_otsu_thresholding(gauss_img_N2DH_GOWT1[i] , 256),15))

        otsu_stretch_img_N2DH_GOWT1 = []
        for i in range(0,len(stretch_img_N2DH_GOWT1)):
            otsu_stretch_img_N2DH_GOWT1.append(tlo.two_level_otsu_thresholding(stretch_img_N2DH_GOWT1[i] , 256),15)

        otsu_median_stretch_img_N2DH_GOWT1 = []
        for i in range(0,len(median_stretch_img_N2DH_GOWT1)):
            otsu_median_stretch_img_N2DH_GOWT1.append(pp.holefilling(tlo.two_level_otsu_thresholding(median_stretch_img_N2DH_GOWT1[i] , 256),15))
            
        otsu_stretch_median_img_N2DH_GOWT1 = []
        for i in range(0,len(stretch_median_img_N2DH_GOWT1)):
            otsu_stretch_median_img_N2DH_GOWT1.append(pp.holefilling(tlo.two_level_otsu_thresholding(stretch_median_img_N2DH_GOWT1[i] , 256),15))

        otsu_gauss_stretch_img_N2DH_GOWT1 = []
        for i in range(0,len(gauss_stretch_img_N2DH_GOWT1)):
            otsu_gauss_stretch_img_N2DH_GOWT1.append(pp.holefilling(tlo.two_level_otsu_thresholding(gauss_stretch_img_N2DH_GOWT1[i] , 256),15))
        
        otsu_stretch_gauss_img_N2DH_GOWT1 = []
        for i in range(0,len(stretch_gauss_img_N2DH_GOWT1)):
            otsu_stretch_gauss_img_N2DH_GOWT1.append(pp.holefilling(tlo.two_level_otsu_thresholding(stretch_gauss_img_N2DH_GOWT1[i] , 256),15))

        #calculate dice scores
        dice_otsu_img_N2DH_GOWT1 = []
        for j in range(0,len(otsu_img_N2DH_GOWT1)):
            dice_otsu_img_N2DH_GOWT1.append(dsc.dice(otsu_img_N2DH_GOWT1[j] , binary_gt_N2DH_GOWT1[j]))

        dice_otsu_median_img_N2DH_GOWT1 = []
        for j in range(0,len(otsu_median_img_N2DH_GOWT1)):
            dice_otsu_median_img_N2DH_GOWT1.append(dsc.dice(otsu_median_img_N2DH_GOWT1[j] , binary_gt_N2DH_GOWT1[j]))

        dice_otsu_gauss_img_N2DH_GOWT1 = []
        for j in range(0,len(otsu_gauss_img_N2DH_GOWT1)):
            dice_otsu_gauss_img_N2DH_GOWT1.append(dsc.dice(otsu_gauss_img_N2DH_GOWT1[j] , binary_gt_N2DH_GOWT1[j]))

        dice_otsu_stretch_img_N2DH_GOWT1 = []
        for j in range(0,len(otsu_stretch_img_N2DH_GOWT1)):
            dice_otsu_stretch_img_N2DH_GOWT1.append(dsc.dice(otsu_stretch_img_N2DH_GOWT1[j] , binary_gt_N2DH_GOWT1[j]))

        dice_otsu_median_stretch_img_N2DH_GOWT1 = []
        for j in range(0,len(otsu_median_stretch_img_N2DH_GOWT1)):
            dice_otsu_median_stretch_img_N2DH_GOWT1.append(dsc.dice(otsu_median_stretch_img_N2DH_GOWT1[j] , binary_gt_N2DH_GOWT1[j]))
        
        dice_otsu_stretch_median_img_N2DH_GOWT1 = []
        for j in range(0,len(otsu_stretch_median_img_N2DH_GOWT1)):
            dice_otsu_stretch_median_img_N2DH_GOWT1.append(dsc.dice(otsu_stretch_median_img_N2DH_GOWT1[j] , binary_gt_N2DH_GOWT1[j]))

        #choose best combination histogram stretching and median filter 
        median1 = st.median(dice_otsu_median_stretch_img_N2DH_GOWT1)
        median2 = st.median(dice_otsu_stretch_median_img_N2DH_GOWT1)

        if(max(median1,median2) == median1):
            optimal_dice_stretch_median = dice_otsu_median_stretch_img_N2DH_GOWT1
        else: optimal_dice_stretch_median = dice_otsu_stretch_median_img_N2DH_GOWT1
        
        dice_otsu_gauss_stretch_img_N2DH_GOWT1 = []
        for j in range(0,len(otsu_gauss_stretch_img_N2DH_GOWT1)):
            dice_otsu_gauss_stretch_img_N2DH_GOWT1.append(dsc.dice(otsu_gauss_stretch_img_N2DH_GOWT1[j] , binary_gt_N2DH_GOWT1[j]))
        
        dice_otsu_stretch_gauss_img_N2DH_GOWT1 = []
        for j in range(0,len(otsu_stretch_gauss_img_N2DH_GOWT1)):
            dice_otsu_stretch_gauss_img_N2DH_GOWT1.append(dsc.dice(otsu_stretch_gauss_img_N2DH_GOWT1[j] , binary_gt_N2DH_GOWT1[j]))
        
        #choose best combination histogram stretching and gaussian filter 
        median3 = st.median(dice_otsu_gauss_stretch_img_N2DH_GOWT1)
        median4 = st.median(dice_otsu_stretch_gauss_img_N2DH_GOWT1)

        if(max(median3,median4) == median3):
            optimal_dice_stretch_gauss = dice_otsu_gauss_stretch_img_N2DH_GOWT1
        else: optimal_dice_stretch_gauss = dice_otsu_stretch_gauss_img_N2DH_GOWT1

        data_N2DH_GOWT1 = [dice_otsu_img_N2DH_GOWT1 , dice_otsu_median_img_N2DH_GOWT1 , dice_otsu_gauss_img_N2DH_GOWT1 , dice_otsu_stretch_img_N2DH_GOWT1  , optimal_dice_stretch_median  , optimal_dice_stretch_gauss]

        #load boxpot 
        boxplot = pp.dataset_boxplot_otsu(data_N2DH_GOWT1 , 'Preprocessing methods - N2DH-GOWT1 - Two-level Otsu Thresholding')
    
    
    if x == 'N2DL-HeLa' :     
        
        #load dataset
        img_N2DL_HeLa = []
        path = os.path.join(os.path.abspath(os.path.join(r'.', os.pardir)),r"data\Otsu_data\N2DL-HeLa\img")
        for f in os.listdir(path):
            img_N2DL_HeLa.append(imread(os.path.join(path , f)))

        gt_N2DL_HeLa = []
        path = os.path.join(os.path.abspath(os.path.join(r'.', os.pardir)),r"data\Otsu_data\N2DL-HeLa\gt")
        for f in os.listdir(path):
            gt_N2DL_HeLa.append(imread(os.path.join(path , f)))

        #binarize ground truth image 
        binary_gt_N2DL_HeLa = []
        for i in range(0,len(gt_N2DL_HeLa)):
            binary_gt_N2DL_HeLa.append(pp.binarize(gt_N2DL_HeLa[i])) 

        copy_img_N2DL_HeLa = img_N2DL_HeLa.copy()

        #perform preprocessing and otsu
        median_img_N2DL_HeLa = []
        for i in range(0,len(copy_img_N2DL_HeLa)):
            median_img_N2DL_HeLa.append(scipy.ndimage.median_filter(copy_img_N2DL_HeLa[i] , 2))

        gauss_img_N2DL_HeLa = []
        for i in range(0,len(copy_img_N2DL_HeLa)):
            gauss_img_N2DL_HeLa.append(scipy.ndimage.gaussian_filter(copy_img_N2DL_HeLa[i] , 4))

        stretch_img_N2DL_HeLa = []
        for i in range(0,len(copy_img_N2DL_HeLa)):
            stretch_img_N2DL_HeLa.append(pp.stretch(copy_img_N2DL_HeLa[i]))

        median_stretch_img_N2DL_HeLa = []
        for i in range(0,len(median_img_N2DL_HeLa)):
            median_stretch_img_N2DL_HeLa.append(pp.stretch(median_img_N2DL_HeLa[i]))

        stretch_median_img_N2DL_HeLa = []
        for i in range(0,len(stretch_img_N2DL_HeLa)):
            stretch_median_img_N2DL_HeLa.append(scipy.ndimage.median_filter(stretch_img_N2DL_HeLa[i] , 2))
        
        gauss_stretch_img_N2DL_HeLa = []
        for i in range(0,len(gauss_img_N2DL_HeLa)):
            gauss_stretch_img_N2DL_HeLa.append(pp.stretch(gauss_img_N2DL_HeLa[i]))
        
        stretch_gauss_img_N2DL_HeLa = []
        for i in range(0,len(stretch_img_N2DL_HeLa)):
            stretch_gauss_img_N2DL_HeLa.append(scipy.ndimage.gaussian_filter(stretch_img_N2DL_HeLa[i] , 4))

        otsu_img_N2DL_HeLa = []
        for i in range(0,len(copy_img_N2DL_HeLa)):
            otsu_img_N2DL_HeLa.append(tlo.two_level_otsu_thresholding(copy_img_N2DL_HeLa[i] , 256))

        otsu_median_img_N2DL_HeLa = []
        for i in range(0,len(median_img_N2DL_HeLa)):
            otsu_median_img_N2DL_HeLa.append(tlo.two_level_otsu_thresholding(median_img_N2DL_HeLa[i] , 256))

        otsu_gauss_img_N2DL_HeLa = []
        for i in range(0,len(gauss_img_N2DL_HeLa)):
            otsu_gauss_img_N2DL_HeLa.append(tlo.two_level_otsu_thresholding(gauss_img_N2DL_HeLa[i] , 256))

        otsu_stretch_img_N2DL_HeLa = []
        for i in range(0,len(stretch_img_N2DL_HeLa)):
            otsu_stretch_img_N2DL_HeLa.append(tlo.two_level_otsu_thresholding(stretch_img_N2DL_HeLa[i] , 256))

        otsu_median_stretch_img_N2DL_HeLa = []
        for i in range(0,len(median_stretch_img_N2DL_HeLa)):
            otsu_median_stretch_img_N2DL_HeLa.append(tlo.two_level_otsu_thresholding(median_stretch_img_N2DL_HeLa[i] , 256))
        
        otsu_stretch_median_img_N2DL_HeLa = []
        for i in range(0,len(stretch_median_img_N2DL_HeLa)):
            otsu_stretch_median_img_N2DL_HeLa.append(tlo.two_level_otsu_thresholding(stretch_median_img_N2DL_HeLa[i] , 256))
        
        otsu_gauss_stretch_img_N2DL_HeLa = []
        for i in range(0,len(gauss_stretch_img_N2DL_HeLa)):
            otsu_gauss_stretch_img_N2DL_HeLa.append(tlo.two_level_otsu_thresholding(gauss_stretch_img_N2DL_HeLa[i] , 256))
        
        otsu_stretch_gauss_img_N2DL_HeLa = []
        for i in range(0,len(stretch_gauss_img_N2DL_HeLa)):
            otsu_stretch_gauss_img_N2DL_HeLa.append(tlo.two_level_otsu_thresholding(stretch_gauss_img_N2DL_HeLa[i] , 256))

        #calculate dice scores 
        dice_otsu_img_N2DL_HeLa = []
        for j in range(0,len(otsu_img_N2DL_HeLa)):
            dice_otsu_img_N2DL_HeLa.append(dsc.dice(otsu_img_N2DL_HeLa[j] , binary_gt_N2DL_HeLa[j]))

        dice_otsu_median_img_N2DL_HeLa = []
        for j in range(0,len(otsu_median_img_N2DL_HeLa)):
            dice_otsu_median_img_N2DL_HeLa.append(dsc.dice(otsu_median_img_N2DL_HeLa[j] , binary_gt_N2DL_HeLa[j]))

        dice_otsu_gauss_img_N2DL_HeLa = []
        for j in range(0,len(otsu_gauss_img_N2DL_HeLa)):
            dice_otsu_gauss_img_N2DL_HeLa.append(dsc.dice(otsu_gauss_img_N2DL_HeLa[j] , binary_gt_N2DL_HeLa[j]))

        dice_otsu_stretch_img_N2DL_HeLa = []
        for j in range(0,len(otsu_stretch_img_N2DL_HeLa)):
            dice_otsu_stretch_img_N2DL_HeLa.append(dsc.dice(otsu_stretch_img_N2DL_HeLa[j] , binary_gt_N2DL_HeLa[j]))

        dice_otsu_median_stretch_img_N2DL_HeLa = []
        for j in range(0,len(otsu_median_stretch_img_N2DL_HeLa)):
            dice_otsu_median_stretch_img_N2DL_HeLa.append(dsc.dice(otsu_median_stretch_img_N2DL_HeLa[j] , binary_gt_N2DL_HeLa[j]))

        dice_otsu_stretch_median_img_N2DL_HeLa = []
        for j in range(0,len(otsu_stretch_median_img_N2DL_HeLa)):
            dice_otsu_stretch_median_img_N2DL_HeLa.append(dsc.dice(otsu_stretch_median_img_N2DL_HeLa[j] , binary_gt_N2DL_HeLa[j]))
        
        #choose best combination histogram stretching and median filter 
        median1 = st.median(dice_otsu_median_stretch_img_N2DL_HeLa)
        median2 = st.median(dice_otsu_stretch_median_img_N2DL_HeLa)

        if(max(median1,median2) == median1):
            optimal_dice_stretch_median = dice_otsu_median_stretch_img_N2DL_HeLa
        else: optimal_dice_stretch_median = dice_otsu_stretch_median_img_N2DL_HeLa

       
        dice_otsu_gauss_stretch_img_N2DL_HeLa = []
        for j in range(0,len(otsu_gauss_stretch_img_N2DL_HeLa)):
            dice_otsu_gauss_stretch_img_N2DL_HeLa.append(dsc.dice(otsu_gauss_stretch_img_N2DL_HeLa[j] , binary_gt_N2DL_HeLa[j]))    
        
        dice_otsu_stretch_gauss_img_N2DL_HeLa = []
        for j in range(0,len(otsu_stretch_gauss_img_N2DL_HeLa)):
            dice_otsu_stretch_gauss_img_N2DL_HeLa.append(dsc.dice(otsu_stretch_gauss_img_N2DL_HeLa[j] , binary_gt_N2DL_HeLa[j]))

        #choose best combination histogram stretching and gaussian filter 
        median3 = st.median(dice_otsu_gauss_stretch_img_N2DL_HeLa)
        median4 = st.median(dice_otsu_stretch_gauss_img_N2DL_HeLa)

        if(max(median3,median4) == median3):
            optimal_dice_stretch_gauss = dice_otsu_gauss_stretch_img_N2DL_HeLa
        else: optimal_dice_stretch_gauss = dice_otsu_stretch_gauss_img_N2DL_HeLa

        data_N2DLHeLa = [dice_otsu_img_N2DL_HeLa , dice_otsu_median_img_N2DL_HeLa , dice_otsu_gauss_img_N2DL_HeLa , dice_otsu_stretch_img_N2DL_HeLa , optimal_dice_stretch_median , optimal_dice_stretch_gauss]

        #load boxplot 
        boxplot = pp.dataset_boxplot_otsu(data_N2DLHeLa , 'Preprocessing methods - N2DL-HeLa - Two-level Otsu Thresholding')

    
    if x == 'NIH3T3' :
        
        #load dataset
        img_NIH3T3 = []
        path = os.path.join(os.path.abspath(os.path.join(r'.', os.pardir)),r"data\Otsu_data\NIH3T3\img")
        for f in os.listdir(path):
            img_NIH3T3.append(imread(os.path.join(path , f)))

        gt_NIH3T3 = []
        path = os.path.join(os.path.abspath(os.path.join(r'.', os.pardir)),r"data\Otsu_data\NIH3T3\gt")
        for f in os.listdir(path):
            gt_NIH3T3.append(imread(os.path.join(path , f)))

        copy_img_NIH3T3 = img_NIH3T3.copy()

        #perform preprocessing and otsu
        median_img_NIH3T3 = []
        for i in range(0,len(copy_img_NIH3T3)):
            median_img_NIH3T3.append(scipy.ndimage.median_filter(copy_img_NIH3T3[i] , 16))

        gauss_img_NIH3T3 = []
        for i in range(0,len(copy_img_NIH3T3)):
            gauss_img_NIH3T3.append(scipy.ndimage.gaussian_filter(copy_img_NIH3T3[i] , 8))

        stretch_img_NIH3T3 = []
        for i in range(0,len(copy_img_NIH3T3)):
            stretch_img_NIH3T3.append(pp.stretch(copy_img_NIH3T3[i]))

        median_stretch_img_NIH3T3 = []
        for i in range(0,len(median_img_NIH3T3)):
            median_stretch_img_NIH3T3.append(pp.stretch(median_img_NIH3T3[i]))

        stretch_median_img_NIH3T3 = []
        for i in range(0,len(stretch_img_NIH3T3)):
            stretch_median_img_NIH3T3.append(scipy.ndimage.median_filter(stretch_img_NIH3T3[i] , 16))

        gauss_stretch_img_NIH3T3 = []
        for i in range(0,len(gauss_img_NIH3T3)):
            gauss_stretch_img_NIH3T3.append(pp.stretch(gauss_img_NIH3T3[i]))

        stretch_gauss_img_NIH3T3 = []
        for i in range(0,len(stretch_img_NIH3T3)):
            stretch_gauss_img_NIH3T3.append(scipy.ndimage.gaussian_filter(stretch_img_NIH3T3[i] , 8))

        otsu_img_NIH3T3 = []
        for i in range(0,len(copy_img_NIH3T3)):
            otsu_img_NIH3T3.append(tlo.two_level_otsu_thresholding(copy_img_NIH3T3[i] , 256))

        otsu_median_img_NIH3T3 = []
        for i in range(0,len(median_img_NIH3T3)):
            otsu_median_img_NIH3T3.append(tlo.two_level_otsu_thresholding(median_img_NIH3T3[i] , 256))

        otsu_gauss_img_NIH3T3 = []
        for i in range(0,len(gauss_img_NIH3T3)):
            otsu_gauss_img_NIH3T3.append(tlo.two_level_otsu_thresholding(gauss_img_NIH3T3[i] , 256))

        otsu_stretch_img_NIH3T3 = []
        for i in range(0,len(stretch_img_NIH3T3)):
            otsu_stretch_img_NIH3T3.append(tlo.two_level_otsu_thresholding(stretch_img_NIH3T3[i] , 256))
        
        otsu_median_stretch_img_NIH3T3 = []
        for i in range(0,len(median_stretch_img_NIH3T3)):
            otsu_median_stretch_img_NIH3T3.append(tlo.two_level_otsu_thresholding(median_stretch_img_NIH3T3[i] , 256))
        
        otsu_stretch_median_img_NIH3T3 = []
        for i in range(0,len(stretch_median_img_NIH3T3)):
            otsu_stretch_median_img_NIH3T3.append(tlo.two_level_otsu_thresholding(stretch_median_img_NIH3T3[i] , 256))
        
        otsu_gauss_stretch_img_NIH3T3 = []
        for i in range(0,len(gauss_stretch_img_NIH3T3)):
            otsu_gauss_stretch_img_NIH3T3.append(tlo.two_level_otsu_thresholding(gauss_stretch_img_NIH3T3[i] , 256))

        otsu_stretch_gauss_img_NIH3T3 = []
        for i in range(0,len(stretch_gauss_img_NIH3T3)):
            otsu_stretch_gauss_img_NIH3T3.append(tlo.two_level_otsu_thresholding(stretch_gauss_img_NIH3T3[i] , 256))

        #calculate dice scores 
        dice_otsu_img_NIH3T3 = []
        for j in range(0,len(otsu_img_NIH3T3)):
            dice_otsu_img_NIH3T3.append(dsc.dice(otsu_img_NIH3T3[j] , gt_NIH3T3[j]))

        dice_otsu_median_img_NIH3T3 = []
        for j in range(0,len(otsu_median_img_NIH3T3)):
            dice_otsu_median_img_NIH3T3.append(dsc.dice(otsu_median_img_NIH3T3[j] , gt_NIH3T3[j]))

        dice_otsu_gauss_img_NIH3T3 = []
        for j in range(0,len(otsu_gauss_img_NIH3T3)):
            dice_otsu_gauss_img_NIH3T3.append(dsc.dice(otsu_gauss_img_NIH3T3[j] , gt_NIH3T3[j]))

        dice_otsu_stretch_img_NIH3T3 = []
        for j in range(0,len(otsu_stretch_img_NIH3T3)):
            dice_otsu_stretch_img_NIH3T3.append(dsc.dice(otsu_stretch_img_NIH3T3[j] , gt_NIH3T3[j]))
        
        dice_otsu_median_stretch_img_NIH3T3 = []
        for j in range(0,len(otsu_median_stretch_img_NIH3T3)):
            dice_otsu_median_stretch_img_NIH3T3.append(dsc.dice(otsu_median_stretch_img_NIH3T3[j] , gt_NIH3T3[j]))

        dice_otsu_stretch_median_img_NIH3T3 = []
        for j in range(0,len(otsu_stretch_median_img_NIH3T3)):
            dice_otsu_stretch_median_img_NIH3T3.append(dsc.dice(otsu_stretch_median_img_NIH3T3[j] , gt_NIH3T3[j]))
        
        #choose best combination histogram stretching and median filter 
        
        median1 = st.median(dice_otsu_median_stretch_img_NIH3T3)
        median2 = st.median(dice_otsu_stretch_median_img_NIH3T3)

        if(max(median1,median2) == median1):
            optimal_dice_stretch_median = dice_otsu_median_stretch_img_NIH3T3
        else: optimal_dice_stretch_median = dice_otsu_stretch_median_img_NIH3T3

        dice_otsu_gauss_stretch_img_NIH3T3 = []
        for j in range(0,len(otsu_gauss_stretch_img_NIH3T3)):
            dice_otsu_gauss_stretch_img_NIH3T3.append(dsc.dice(otsu_gauss_stretch_img_NIH3T3[j] , gt_NIH3T3[j]))
        
        dice_otsu_stretch_gauss_img_NIH3T3 = []
        for j in range(0,len(otsu_stretch_gauss_img_NIH3T3)):
            dice_otsu_stretch_gauss_img_NIH3T3.append(dsc.dice(otsu_stretch_gauss_img_NIH3T3[j] , gt_NIH3T3[j]))

        #choose best combination histogram stretching and gaussian filter 
        median3 = st.median(dice_otsu_gauss_stretch_img_NIH3T3)
        median4 = st.median(dice_otsu_stretch_gauss_img_NIH3T3)

        if(max(median3,median4) == median3):
            optimal_dice_stretch_gauss = dice_otsu_gauss_stretch_img_NIH3T3
        else: optimal_dice_stretch_gauss = dice_otsu_stretch_gauss_img_NIH3T3

        data_NIH3T3 = [dice_otsu_img_NIH3T3 , dice_otsu_median_img_NIH3T3 , dice_otsu_gauss_img_NIH3T3 , dice_otsu_stretch_img_NIH3T3 , optimal_dice_stretch_median , optimal_dice_stretch_gauss]

        #load boxplot 
        boxplot = pp.dataset_boxplot_otsu(data_NIH3T3 , 'Preprocessing methods - NIH3T3 - Two-level Otsu Thresholding')
        
    return boxplot

#function for complete analysis for all datasets with two level otsu 
def complete_analysis_two_level_otsu_all(x):
    """
    This function performs the complete analysis for two level Otsu on all datasets. 

    :param x: parameter for function 'all'
    
    """
    if x == 'all':
        complete_analysis_two_level_otsu("N2DH-GOWT1")
        complete_analysis_two_level_otsu("N2DL-HeLa")
        complete_analysis_two_level_otsu("NIH3T3")

# complete analysis function for datasets NIH3T3 and N2DL-HeLa
def complete_analysis_local_otsu(x):
    """
    This function takes a string indicating the dataset, performs the complete analysis with local adaptive otsu (all postprocessing methods)
    on dataset x and returns the boxplot.

    :param x: string (name of dataset)
    :return: boxplot of complete analysis
    
    """
    
    
    if x == 'N2DL-HeLa' :     
        #load dataset
        img_N2DL_HeLa = []
        path = r"data\Otsu_data\N2DL-HeLa\img"
        for f in os.listdir(path):
            img_N2DL_HeLa.append(imread(os.path.join(path , f)))

        gt_N2DL_HeLa = []
        path = r"data\Otsu_data\N2DL-HeLa\gt"
        for f in os.listdir(path):
            gt_N2DL_HeLa.append(imread(os.path.join(path , f)))

        #binarize ground truth image
        binary_gt_N2DL_HeLa = []
        for i in range(0,len(gt_N2DL_HeLa)):
            binary_gt_N2DL_HeLa.append(pp.binarize(gt_N2DL_HeLa[i])) 

        copy_img_N2DL_HeLa = img_N2DL_HeLa.copy()

        #perform preprocessing and otsu
        median_img_N2DL_HeLa = []
        for i in range(0,len(copy_img_N2DL_HeLa)):
            median_img_N2DL_HeLa.append(scipy.ndimage.median_filter(copy_img_N2DL_HeLa[i] , 2))

        gauss_img_N2DL_HeLa = []
        for i in range(0,len(copy_img_N2DL_HeLa)):
            gauss_img_N2DL_HeLa.append(scipy.ndimage.gaussian_filter(copy_img_N2DL_HeLa[i] , 4))

        stretch_img_N2DL_HeLa = []
        for i in range(0,len(copy_img_N2DL_HeLa)):
            stretch_img_N2DL_HeLa.append(pp.stretch(copy_img_N2DL_HeLa[i]))

        median_stretch_img_N2DL_HeLa = []
        for i in range(0,len(median_img_N2DL_HeLa)):
            median_stretch_img_N2DL_HeLa.append(pp.stretch(median_img_N2DL_HeLa[i]))

        stretch_median_img_N2DL_HeLa = []
        for i in range(0,len(stretch_img_N2DL_HeLa)):
            stretch_median_img_N2DL_HeLa.append(scipy.ndimage.median_filter(stretch_img_N2DL_HeLa[i] , 2))
        
        gauss_stretch_img_N2DL_HeLa = []
        for i in range(0,len(gauss_img_N2DL_HeLa)):
            gauss_stretch_img_N2DL_HeLa.append(pp.stretch(gauss_img_N2DL_HeLa[i]))
        
        stretch_gauss_img_N2DL_HeLa = []
        for i in range(0,len(stretch_img_N2DL_HeLa)):
            stretch_gauss_img_N2DL_HeLa.append(scipy.ndimage.gaussian_filter(stretch_img_N2DL_HeLa[i] , 4))

        otsu_img_N2DL_HeLa = []
        for i in range(0,len(copy_img_N2DL_HeLa)):
            otsu_img_N2DL_HeLa.append(lt.local_thresholding_mean(copy_img_N2DL_HeLa[i] , 100, 300 ))

        otsu_median_img_N2DL_HeLa = []
        for i in range(0,len(median_img_N2DL_HeLa)):
            otsu_median_img_N2DL_HeLa.append(lt.local_thresholding_mean(median_img_N2DL_HeLa[i] , 100, 300))

        otsu_gauss_img_N2DL_HeLa = []
        for i in range(0,len(gauss_img_N2DL_HeLa)):
            otsu_gauss_img_N2DL_HeLa.append(lt.local_thresholding_mean(gauss_img_N2DL_HeLa[i] , 100, 300))

        otsu_stretch_img_N2DL_HeLa = []
        for i in range(0,len(stretch_img_N2DL_HeLa)):
            otsu_stretch_img_N2DL_HeLa.append(lt.local_thresholding_mean(stretch_img_N2DL_HeLa[i] , 100, 300))

        otsu_median_stretch_img_N2DL_HeLa = []
        for i in range(0,len(median_stretch_img_N2DL_HeLa)):
            otsu_median_stretch_img_N2DL_HeLa.append(lt.local_thresholding_mean(median_stretch_img_N2DL_HeLa[i] , 100, 300))
        
        otsu_stretch_median_img_N2DL_HeLa = []
        for i in range(0,len(stretch_median_img_N2DL_HeLa)):
            otsu_stretch_median_img_N2DL_HeLa.append(lt.local_thresholding_mean(stretch_median_img_N2DL_HeLa[i] , 100,300))
        
        otsu_gauss_stretch_img_N2DL_HeLa = []
        for i in range(0,len(gauss_stretch_img_N2DL_HeLa)):
            otsu_gauss_stretch_img_N2DL_HeLa.append(lt.local_thresholding_mean(gauss_stretch_img_N2DL_HeLa[i] , 100,300))
        
        otsu_stretch_gauss_img_N2DL_HeLa = []
        for i in range(0,len(stretch_gauss_img_N2DL_HeLa)):
            otsu_stretch_gauss_img_N2DL_HeLa.append(lt.local_thresholding_mean(stretch_gauss_img_N2DL_HeLa[i] , 100,300))

        #calculate dice scores 
        dice_otsu_img_N2DL_HeLa = []
        for j in range(0,len(otsu_img_N2DL_HeLa)):
            dice_otsu_img_N2DL_HeLa.append(dsc.dice(otsu_img_N2DL_HeLa[j] , binary_gt_N2DL_HeLa[j]))

        dice_otsu_median_img_N2DL_HeLa = []
        for j in range(0,len(otsu_median_img_N2DL_HeLa)):
            dice_otsu_median_img_N2DL_HeLa.append(dsc.dice(otsu_median_img_N2DL_HeLa[j] , binary_gt_N2DL_HeLa[j]))

        dice_otsu_gauss_img_N2DL_HeLa = []
        for j in range(0,len(otsu_gauss_img_N2DL_HeLa)):
            dice_otsu_gauss_img_N2DL_HeLa.append(dsc.dice(otsu_gauss_img_N2DL_HeLa[j] , binary_gt_N2DL_HeLa[j]))

        dice_otsu_stretch_img_N2DL_HeLa = []
        for j in range(0,len(otsu_stretch_img_N2DL_HeLa)):
            dice_otsu_stretch_img_N2DL_HeLa.append(dsc.dice(otsu_stretch_img_N2DL_HeLa[j] , binary_gt_N2DL_HeLa[j]))

        dice_otsu_median_stretch_img_N2DL_HeLa = []
        for j in range(0,len(otsu_median_stretch_img_N2DL_HeLa)):
            dice_otsu_median_stretch_img_N2DL_HeLa.append(dsc.dice(otsu_median_stretch_img_N2DL_HeLa[j] , binary_gt_N2DL_HeLa[j]))

        dice_otsu_stretch_median_img_N2DL_HeLa = []
        for j in range(0,len(otsu_stretch_median_img_N2DL_HeLa)):
            dice_otsu_stretch_median_img_N2DL_HeLa.append(dsc.dice(otsu_stretch_median_img_N2DL_HeLa[j] , binary_gt_N2DL_HeLa[j]))
        
        #choose best combination histogram stretching and median filter 
        median1 = st.median(dice_otsu_median_stretch_img_N2DL_HeLa)
        median2 = st.median(dice_otsu_stretch_median_img_N2DL_HeLa)

        if(max(median1,median2) == median1):
            optimal_dice_stretch_median = dice_otsu_median_stretch_img_N2DL_HeLa
        else: optimal_dice_stretch_median = dice_otsu_stretch_median_img_N2DL_HeLa

        dice_otsu_gauss_stretch_img_N2DL_HeLa = []
        for j in range(0,len(otsu_gauss_stretch_img_N2DL_HeLa)):
            dice_otsu_gauss_stretch_img_N2DL_HeLa.append(dsc.dice(otsu_gauss_stretch_img_N2DL_HeLa[j] , binary_gt_N2DL_HeLa[j]))    
        
        dice_otsu_stretch_gauss_img_N2DL_HeLa = []
        for j in range(0,len(otsu_stretch_gauss_img_N2DL_HeLa)):
            dice_otsu_stretch_gauss_img_N2DL_HeLa.append(dsc.dice(otsu_stretch_gauss_img_N2DL_HeLa[j] , binary_gt_N2DL_HeLa[j]))

        #choose best combination histogram stretching and gaussian filter 
        median3 = st.median(dice_otsu_gauss_stretch_img_N2DL_HeLa)
        median4 = st.median(dice_otsu_stretch_gauss_img_N2DL_HeLa)

        if(max(median3,median4) == median3):
            optimal_dice_stretch_gauss = dice_otsu_gauss_stretch_img_N2DL_HeLa
        else: optimal_dice_stretch_gauss = dice_otsu_stretch_gauss_img_N2DL_HeLa

        data_N2DLHeLa = [dice_otsu_img_N2DL_HeLa , dice_otsu_median_img_N2DL_HeLa , dice_otsu_gauss_img_N2DL_HeLa , dice_otsu_stretch_img_N2DL_HeLa , optimal_dice_stretch_median , optimal_dice_stretch_gauss]

        #load boxplot 
        boxplot = pp.dataset_boxplot_otsu(data_N2DLHeLa , 'Preprocessing methods - N2DL-HeLa - Local adaptive Otsu Thresholding')

    
    if x == 'NIH3T3' :
        
        #load dataset 
        img_NIH3T3 = []
        path = r"data\Otsu_data\NIH3T3\img"
        for f in os.listdir(path):
            img_NIH3T3.append(imread(os.path.join(path , f)))

        gt_NIH3T3 = []
        path = r"data\Otsu_data\NIH3T3\gt"
        for f in os.listdir(path):
            gt_NIH3T3.append(imread(os.path.join(path , f)))

        copy_img_NIH3T3 = img_NIH3T3.copy()

        #perform preprocessing and otsu
        median_img_NIH3T3 = []
        for i in range(0,len(copy_img_NIH3T3)):
            median_img_NIH3T3.append(scipy.ndimage.median_filter(copy_img_NIH3T3[i] , 16))

        gauss_img_NIH3T3 = []
        for i in range(0,len(copy_img_NIH3T3)):
            gauss_img_NIH3T3.append(scipy.ndimage.gaussian_filter(copy_img_NIH3T3[i] , 8))

        stretch_img_NIH3T3 = []
        for i in range(0,len(copy_img_NIH3T3)):
            stretch_img_NIH3T3.append(pp.stretch(copy_img_NIH3T3[i]))

        median_stretch_img_NIH3T3 = []
        for i in range(0,len(median_img_NIH3T3)):
            median_stretch_img_NIH3T3.append(pp.stretch(median_img_NIH3T3[i]))

        stretch_median_img_NIH3T3 = []
        for i in range(0,len(stretch_img_NIH3T3)):
            stretch_median_img_NIH3T3.append(scipy.ndimage.median_filter(stretch_img_NIH3T3[i] , 16))

        gauss_stretch_img_NIH3T3 = []
        for i in range(0,len(gauss_img_NIH3T3)):
            gauss_stretch_img_NIH3T3.append(pp.stretch(gauss_img_NIH3T3[i]))

        stretch_gauss_img_NIH3T3 = []
        for i in range(0,len(stretch_img_NIH3T3)):
            stretch_gauss_img_NIH3T3.append(scipy.ndimage.gaussian_filter(stretch_img_NIH3T3[i] , 8))

        otsu_img_NIH3T3 = []
        for i in range(0,len(copy_img_NIH3T3)):
            otsu_img_NIH3T3.append(lt.local_thresholding_mean(copy_img_NIH3T3[i] , 50,150))

        otsu_median_img_NIH3T3 = []
        for i in range(0,len(median_img_NIH3T3)):
            otsu_median_img_NIH3T3.append(lt.local_thresholding_mean(median_img_NIH3T3[i] , 50,150))

        otsu_gauss_img_NIH3T3 = []
        for i in range(0,len(gauss_img_NIH3T3)):
            otsu_gauss_img_NIH3T3.append(lt.local_thresholding_mean(gauss_img_NIH3T3[i] , 50,150))

        otsu_stretch_img_NIH3T3 = []
        for i in range(0,len(stretch_img_NIH3T3)):
            otsu_stretch_img_NIH3T3.append(lt.local_thresholding_mean(stretch_img_NIH3T3[i] , 50,150))
        
        otsu_median_stretch_img_NIH3T3 = []
        for i in range(0,len(median_stretch_img_NIH3T3)):
            otsu_median_stretch_img_NIH3T3.append(lt.local_thresholding_mean(median_stretch_img_NIH3T3[i] , 50,150))
        
        otsu_stretch_median_img_NIH3T3 = []
        for i in range(0,len(stretch_median_img_NIH3T3)):
            otsu_stretch_median_img_NIH3T3.append(lt.local_thresholding_mean(stretch_median_img_NIH3T3[i] , 50,150))
        
        otsu_gauss_stretch_img_NIH3T3 = []
        for i in range(0,len(gauss_stretch_img_NIH3T3)):
            otsu_gauss_stretch_img_NIH3T3.append(lt.local_thresholding_mean(gauss_stretch_img_NIH3T3[i] , 50,150))

        otsu_stretch_gauss_img_NIH3T3 = []
        for i in range(0,len(stretch_gauss_img_NIH3T3)):
            otsu_stretch_gauss_img_NIH3T3.append(lt.local_thresholding_mean(stretch_gauss_img_NIH3T3[i] , 50,150))
        
        #calculate dice scores
        dice_otsu_img_NIH3T3 = []
        for j in range(0,len(otsu_img_NIH3T3)):
            dice_otsu_img_NIH3T3.append(dsc.dice(otsu_img_NIH3T3[j] , gt_NIH3T3[j]))

        dice_otsu_median_img_NIH3T3 = []
        for j in range(0,len(otsu_median_img_NIH3T3)):
            dice_otsu_median_img_NIH3T3.append(dsc.dice(otsu_median_img_NIH3T3[j] , gt_NIH3T3[j]))

        dice_otsu_gauss_img_NIH3T3 = []
        for j in range(0,len(otsu_gauss_img_NIH3T3)):
            dice_otsu_gauss_img_NIH3T3.append(dsc.dice(otsu_gauss_img_NIH3T3[j] , gt_NIH3T3[j]))

        dice_otsu_stretch_img_NIH3T3 = []
        for j in range(0,len(otsu_stretch_img_NIH3T3)):
            dice_otsu_stretch_img_NIH3T3.append(dsc.dice(otsu_stretch_img_NIH3T3[j] , gt_NIH3T3[j]))
        
        dice_otsu_median_stretch_img_NIH3T3 = []
        for j in range(0,len(otsu_median_stretch_img_NIH3T3)):
            dice_otsu_median_stretch_img_NIH3T3.append(dsc.dice(otsu_median_stretch_img_NIH3T3[j] , gt_NIH3T3[j]))

        dice_otsu_stretch_median_img_NIH3T3 = []
        for j in range(0,len(otsu_stretch_median_img_NIH3T3)):
            dice_otsu_stretch_median_img_NIH3T3.append(dsc.dice(otsu_stretch_median_img_NIH3T3[j] , gt_NIH3T3[j]))
        
        #choose best combination histogram stretching and median filter 
        median1 = st.median(dice_otsu_median_stretch_img_NIH3T3)
        median2 = st.median(dice_otsu_stretch_median_img_NIH3T3)

        optimal_dice_stretch_median = dice_otsu_stretch_median_img_NIH3T3

        dice_otsu_gauss_stretch_img_NIH3T3 = []
        for j in range(0,len(otsu_gauss_stretch_img_NIH3T3)):
            dice_otsu_gauss_stretch_img_NIH3T3.append(dsc.dice(otsu_gauss_stretch_img_NIH3T3[j] , gt_NIH3T3[j]))
        
        dice_otsu_stretch_gauss_img_NIH3T3 = []
        for j in range(0,len(otsu_stretch_gauss_img_NIH3T3)):
            dice_otsu_stretch_gauss_img_NIH3T3.append(dsc.dice(otsu_stretch_gauss_img_NIH3T3[j] , gt_NIH3T3[j]))

        #choose best combination histogram stretching and gaussian filter 
        median3 = st.median(dice_otsu_gauss_stretch_img_NIH3T3)
        median4 = st.median(dice_otsu_stretch_gauss_img_NIH3T3)


        optimal_dice_stretch_gauss = dice_otsu_stretch_gauss_img_NIH3T3

        data_NIH3T3 = [dice_otsu_img_NIH3T3 , dice_otsu_median_img_NIH3T3 , dice_otsu_gauss_img_NIH3T3 , dice_otsu_stretch_img_NIH3T3 , optimal_dice_stretch_median , optimal_dice_stretch_gauss]

        #load boxplot
        boxplot = pp.dataset_boxplot_otsu(data_NIH3T3 , 'Preprocessing methods - NIH3T3 - Local adaptive Otsu Thresholding')
        
    return boxplot

    #complete analysis for both datasets in one function (for local adaptive otsu)
def complete_analysis_local_otsu_all(x):
    """
    This function performs the complete analysis for local adaptive otsu on all datasets. 

    :param x: parameter for function 'all'
    
    """
    if x == 'all':
        
        complete_analysis_local_otsu("N2DL-HeLa")
        complete_analysis_local_otsu("NIH3T3")

