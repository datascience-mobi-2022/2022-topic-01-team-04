
import numpy as np
import scipy.ndimage
import matplotlib.pyplot as plt


def b_dice(x,gt): # POSITIVE PIXELS = BACKGROUND x=picture number, same number for gt and post tresholding image):
    gt = ground_truth[x] #gt picture x
    pt = tresholded[x] #post tresholding picture x
    tp=0
    tn=0
    fp=0
    fn=0
    h = gt.shape[0]
    w = gt.shape[1]
    for x, y in np.ndindex((h,w)):
        if gt[x,y]==0:
            if pt[x,y]==0:
                tp+=1
            else:
                fn+=1
        else:
            if pt[x,y]==0:
                fp+=1
            else:
                tn+=1 #not really needed, but does not influence the runtime
    b_dsc= 2*tp/(2*tp+fn+fp)
    return b_dsc
    print(b_dsc)

def f_dice(x): # POSITIVE PIXELS = FOREGROUND
    gt = ground_truth[x] 
    pt = tresholded[x] 
    tp=0
    tn=0
    fp=0
    fn=0
    h = gt.shape[0]
    w = gt.shape[1]
    for x, y in np.ndindex((h,w)):
        if gt[x,y]!=0:
            if pt[x,y]!=0:
                tp+=1
            else:
                fn+=1
        else:
            if pt[x,y]!=0:
                fp+=1
            else:
                tn+=1 
    f_dsc= 2*tp/(2*tp+fn+fp)
    return f_dsc
    print(f_dsc)
    



bice = []
for i in range(0,18):
    bice.append(b_dice(i))

print(bice)
print(mean(bice))




fice = []
for i in range(0,18):
    fice.append(f_dice(i))

print(fice)
print(mean(fice))




def dice(x): #x=picture number, same number for gt and post tresholding image):
    gt = ground_truth[x] #somehow define that we are taking gt picture x
    pt = tresholded[x] #somehow define that we are taking post tresholding picture x
    tp=0
    tn=0
    fp=0
    fn=0
    for i in shape(gt): # shape(gt) should be equalt to shape(pt)
        if gt[i]==256:
            if pt[i]==256:
                tp+=1
            else:
                fn+=1
        else:
            if pt[i]==256:
                fp+=1
            else:
                tn+=1 #this part not rly needed tbh
    dsc= 2*tp/(2*tp+fn+fp)
    return dsc



    # we can then make it run trough a whole dataset like
def dice_avg(y):
    sum = 0
    for x in range(0,len(tresholded)+1):
        dice(x)
        sum += dsc
    dsc_avg = sum/len(tresholded)
    return dsc_avg

