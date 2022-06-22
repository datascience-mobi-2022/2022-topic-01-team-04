
import numpy as np
import scipy.ndimage
import matplotlib.pyplot as plt

#create a list for ground truth images and thresholded images (is done manually before running the dice score algorithm, supports iteration trough a whole dataset, here empty lists included just for the package to function)
ground_truth=[]
thresholded=[]


# option 1: positive pixels = background pixels. Used for images with foreground > background
# define the algorithm, x = image coordinate in the ground truth and thresholded lists
def b_dice(x): 

    #pick the ground truth and thresholded pictures from the lists
    gt = ground_truth[x] 
    pt = thresholded[x] 

    #set new variables for count of different pixel types
    tp=0 
    tn=0
    fp=0
    fn=0
    #iterate over all pixel coordinates (gt and pt have the same dimensions)
    for x, y in np.ndindex((gt.shape[0],gt.shape[1])):

        #if a pixel belongs to background in ground truth
        if gt[x,y]==0:
            #if it belongs to background in post-otsu
            if pt[x,y]==0:
                #add it to the true positive variable
                tp+=1
            #count all other pixel kinds
            else:
                fn+=1
        else:
            if pt[x,y]==0:
                fp+=1

                #else: tn+=1 not included, as tn is not needed in calculations
    b_dsc= 2*tp/(2*tp+fn+fp)
    return b_dsc

def f_dice(x): # same thing for positive pixels = foreground pixels
    gt = ground_truth[x] 
    pt = thresholded[x] 
    tp=0
    tn=0
    fp=0
    fn=0
    for x, y in np.ndindex((gt.shape[0],gt.shape[1])):
        if gt[x,y]!=0:
            if pt[x,y]!=0:
                tp+=1
            else:
                fn+=1
        else:
            if pt[x,y]!=0:
                fp+=1 
    f_dsc= 2*tp/(2*tp+fn+fp)
    return f_dsc


def dice(x, method):
    if method=='background' or method=='b':
        b_dice(x)
    if method=='foreground' or method == 'f':
        f_dice(x)
    else:
        print('write <foreground> or <f> for forward dsc and <bacground> or <b> for background dsc')


