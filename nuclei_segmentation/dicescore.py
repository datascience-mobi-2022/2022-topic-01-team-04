import numpy as np

def foreground_dice(gt,pt):
    #gt and pt are numpy arrays containing pixel intensities
    product1 = np.multiply(gt,pt)
    gt2 = gt-1
    pt2 = pt-1
    product2 = np.multiply(gt2,pt2)
    tp = np.count_nonzero(product1)
    tn = np.count_nonzero(product2)
    all = np.prod(gt2.shape)            # amount of all pixels
    dsc = 2*tp/(tp + all-tn)            # formular dice score all-tn (= Fp+ Fn)
    return dsc

def background_dice(gt, pt):
    product1 = np.multiply(gt,pt)
    gt2 = gt-1
    pt2 = pt-1
    product2 = np.multiply(gt2,pt2)
    tn = np.count_nonzero(product1)
    tp = np.count_nonzero(product2)
    all = np.prod(gt2.shape)
    dsc = 2*tp/(tp + all-tn)
    return dsc

def dice(picture1,picture2):
    dice = min(foreground_dice(picture1,picture2),background_dice(picture1,picture2)) # reeler Wert
    return dice