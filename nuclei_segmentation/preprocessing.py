# Set ground truth images from N2DH-GOWT1 dataset and N2DL-HeLa dataset to 0 and 1
def package():

    import matplotlib.pyplot as plt
    import numpy as np
    import scipy.ndimage
    import pandas as pd
    import seaborn as sns
    from images_segmentation import otsu as ot
    import numpy as np
    import os
    from PIL import Image
    import os, os.path

    
def binarize(x):
    img = x.copy()

    for o in np.ndindex(img.shape):
        if img[o] > 0: 
           img[o] = 1
        else:
            img[o] = 0
    
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




# Preprocessing - Boxplot

def dataset_boxplot(data , title , plot = True):
    import matplotlib.pyplot as plt
 
    fig_1 = plt.figure(figsize = (14 , 10))
    ax = fig_1.add_axes([0 , 0 , 1 , 1])
    ax.set_xticklabels(['No preprocessing' , 'Median filter' , 'Gaussian filter' , 'Histogram \n stretching' , 'Median filter and \n histogram stretching' , 'Histogram stretching and \n median filter' , 'Gaussian filter and \n histogram stretching' , 'Histogram stretching and \n gaussian filter'])
    plt.title(title , size = 18)
    plt.ylabel('Preprocessing methods' , size = 14)
    plt.xlabel('Dice score' , size = 14)


    bp = ax.boxplot(data, patch_artist = True , showmeans = True , meanline = True , meanprops = dict(color = "white" , linewidth = 1.5))
    colors = ['#FF3030', '#FF7F24','#FFB90F', '#BCEE68' , '#00B2EE' , '#BF3EFF' , '#8B4513' , '#808A87']
   
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)

    for median in bp['medians']:
        median.set(color = 'black' , linewidth = 1)
    
    plt.legend([bp["medians"][0]] , ["median"] , loc = 'lower right')
