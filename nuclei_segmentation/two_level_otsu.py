###Two level Otsu and two level Otsu clip 

from cmath import nan


def two_level_otsu_thresholding_within(img,x):
    """
    This function takes an image as well as the amount of wanted thresholds and calculates the class probabilies and mean levels for 
    foreground and background for each threshold. Then, the within class variance using the two-level Otsu's formula is computed 
    and the optimal threshold value is found. Lastly, the image is clipped based on the optimal threshold values and the thresholded 
    image is returned.(everything above the first threshold counts as foreground) 

    :param img: Input image
    :param x: The number of intensity levels/ wanted thresholds
    :return: thresholded image 

    """
    import matplotlib.pyplot
    import numpy

    #load histogram (numerical values)
    n, bins = numpy.histogram(img.flatten(),bins = x)
  
    #initialize threshold value (T = 0) 
    thres = list()
    copy = img.copy()

    #create list to store values of within class variance for each threshold value as well as a list for the threshold indices 
    wcv = list()
    threshold = list()

    #calculate each within class variance for each possible threshold combination
    for i in range(0,len(n)):
        for t in range(0,len(n)):
            
            # background 
            # compute class probabilities and mean levels 
            w0_sum = numpy.sum(numpy.array(n[0:i+1]))
            mean_sum0 = numpy.sum((numpy.array(bins[0:i+1])*numpy.array(n[0:i+1])))
                
            
            w0 = w0_sum / sum(n)  
            if(sum(n[0:i+1]) != 0):  
                mean_0 = mean_sum0 / sum(n[0:i+1])
            else: mean_0 = 0
            
            # compute background class variance
            v0_sum = numpy.sum((numpy.array((bins[0:i+1]-mean_0)** 2)*numpy.array(n[0:i+1])))
            v0 = v0_sum / sum(n[0:i+1])
            
            # between the two thresholds (counted as foreground)
            # compute class probabilities and mean levels 
            w1_sum = numpy.sum(numpy.array(n[i+1:t]))
            mean_sum1 = numpy.sum((numpy.array(bins[i+1:t])*numpy.array(n[i+1:t])))
                
            w1 = w1_sum / sum(n)
            if(sum(n[i+1:t]) != 0):
                mean_1 = mean_sum1 / sum(n[i+1:t])
            else: mean_1 = 0

            # compute class variance for space between the two thresholds
            v1_sum = numpy.sum((numpy.array((bins[i+1:t]-mean_1)** 2)*numpy.array(n[i+1:t])))
        
            if( sum(n[i+1:t]) != 0):
                v1 = v1_sum / sum(n[i+1:t])
            else: v1 = 0

            # foreground
            # compute class probabilities and mean levels 
            w2_sum = numpy.sum(numpy.array(n[t:len(n)]))
            mean_sum2 = numpy.sum((numpy.array(bins[t:len(n)])*numpy.array(n[t:len(n)])))
                
            
            w2 = w2_sum / sum(n)
            if(sum(n[t:len(n)]) != 0):
                mean_2 = mean_sum2 / sum(n[t:len(n)])
            else: mean_2 = 0

            # compute foreground class variance 
            v2_sum = numpy.sum((numpy.array((bins[t:len(n)]-mean_2)** 2)*numpy.array(n[t:len(n)])))
        
            if( sum(n[t:len(n)]) != 0):
                v2 = v2_sum / sum(n[t:len(n)])
            else: v2 = 0

            # compute within class variance and append to list, append indices to list 
            wclv = (w0 * v0) + (w1 * v1) + (w2 * v2)
            thresholds = [i,t]
            wcv.append(wclv)
            threshold.append(thresholds)


    # select optimal threshold value, minimum value of within class variance
    optimal_thres = min(wcv)

    #select optimal threshold in the list
    l = 0
    while l < len(wcv):
        if wcv[l] == optimal_thres: thres.append(threshold[l])
        l += 1

    #assign first and second threshold 
    thres = thres[0]
    thres1  = bins[thres[0]]
    thres2  = bins[thres[1]]
    
    #perform image clipping, counting everything above the first threshold as foreground 
    for o in numpy.ndindex(copy.shape):
        if copy[o] <= (thres1): 
            copy[o] = 0
        elif copy[o] > thres1 and copy[o] <= thres2:  
            copy[o] = 1
        else: 
            copy[o] = 1
            
    return copy 



def two_level_otsu_thresholding_clip_within(img,x):

    """
    This function takes an image as well as the amount of wanted thresholds and calculates the class probabilies and mean levels for 
    foreground and background for each threshold. Then, the within class variance using the two-level Otsu's formula is computed 
    and the optimal threshold value is found. Lastly, the image is clipped based on the optimal threshold values, only counting the space between
    the two thresholds as foreground and thereby removing the reflections, and the thresholded image is returned. 

    :param img: Input image
    :param x: The number of intensity levels/ wanted thresholds
    :return: thresholded image 

    """
    import matplotlib.pyplot
    import numpy

    #load histogram (numerical values)
    n, bins = numpy.histogram(img.flatten(),bins = x)
  
    #initialize threshold value (T = 0) 
    thres = list()
    copy = img.copy()

    #create list to store values of within class variance for each threshold value as well as a list for the threshold indices 
    wcv = list()
    threshold = list()
    
    #calculate each within class variance for each possible threshold combination
    for i in range(0,len(n)):
        for t in range(0,len(n)):
         
            # background 
            # compute class probabilities and mean levels
            w0_sum = numpy.sum(numpy.array(n[0:i+1]))
            mean_sum0 = numpy.sum((numpy.array(bins[0:i+1])*numpy.array(n[0:i+1])))
                
            w0 = w0_sum / sum(n)  
            if(sum(n[0:i+1]) != 0):  
                mean_0 = mean_sum0 / sum(n[0:i+1])
            else: mean_0 = 0
            
            # compute background class variance
            v0_sum = numpy.sum((numpy.array((bins[0:i+1]-mean_0)** 2)*numpy.array(n[0:i+1])))
            v0 = v0_sum / sum(n[0:i+1])
            
            # foreground
            # compute class probabilities and mean levels 
            w1_sum = numpy.sum(numpy.array(n[i+1:t]))
            mean_sum1 = numpy.sum((numpy.array(bins[i+1:t])*numpy.array(n[i+1:t])))
                    
            w1 = w1_sum / sum(n)
            if(sum(n[i+1:t]) != 0):
                mean_1 = mean_sum1 / sum(n[i+1:t])
            else: mean_1 = 0

            # compute foreground class variance 
            v1_sum = numpy.sum((numpy.array((bins[i+1:t]-mean_1)** 2)*numpy.array(n[i+1:t])))
        
            if( sum(n[i+1:t]) != 0):
                v1 = v1_sum / sum(n[i+1:t])
            else: v1 = 0

            # reflections(interval above second threshold)
            # compute class probabilities and mean levels 
            w2_sum = numpy.sum(numpy.array(n[t:len(n)]))
            mean_sum2 = numpy.sum((numpy.array(bins[t:len(n)])*numpy.array(n[t:len(n)])))

            w2 = w2_sum / sum(n)
            if(sum(n[t:len(n)]) != 0):
                mean_2 = mean_sum2 / sum(n[t:len(n)])
            else: mean_2 = 0

            # compute class variance 
            v2_sum = numpy.sum((numpy.array((bins[t:len(n)]-mean_2)** 2)*numpy.array(n[t:len(n)])))
        
            if( sum(n[t:len(n)]) != 0):
                v2 = v2_sum / sum(n[t:len(n)])
            else: v2 = 0

            # compute within class variance and append to list, append indices to list 
            wclv = (w0 * v0) + (w1 * v1) + (w2 * v2)
            thresholds = [i,t]
            wcv.append(wclv)
            threshold.append(thresholds)


    # select optimal threshold value, minimum value of within class variance
    optimal_thres = min(wcv)

    #select optimal threshold in the list
    l = 0
    while l < len(wcv):
        if wcv[l] == optimal_thres: thres.append(threshold[l])
        l += 1
    
    #assign first and second threshold 
    thres = thres[0]
    thres1  = bins[thres[0]]
    thres2  = bins[thres[1]]

    #perform image clipping, only counting the interval between the first and second threshold as foreground 
    for o in numpy.ndindex(copy.shape):
        if copy[o] <= (thres1): 
            copy[o] = 0
        elif copy[o] > thres1 and copy[o] <= thres2:  
            copy[o] = 1
        else: 
            copy[o] = 0
            
    return copy 

def two_level_otsu_thresholding(img,x):
    """
    This function takes an image as well as the amount of wanted thresholds and calculates the class probabilies and mean levels for 
    foreground and background for each threshold. Then, the between class variance using the two-level Otsu's formula is computed 
    and the optimal threshold value is found. Lastly, the image is clipped based on the optimal threshold values and the thresholded 
    image is returned. (everything above the first threshold counts as foreground)

    :param img: Input image
    :param x: The number of intensity levels/ wanted thresholds
    :return: thresholded image 

    """
    import matplotlib.pyplot
    import numpy

    #load histogram (numerical values)
    n, bins = numpy.histogram(img.flatten(),bins = x)

    #initialize threshold value (T = 0) 
    thres = list()
    copy = img.copy()

    #calculate each within class variance for each possible threshold combination
    bcv = list()
    threshold = list()
    # set up initial values
    for i in range(0,len(n)):
        for t in range(0,len(n)):
         
            # background 
            # compute class probabilities and mean levels
            w0_sum = numpy.sum(numpy.array(n[0:i+1]))
            mean_sum0 = numpy.sum((numpy.array(bins[0:i+1])*numpy.array(n[0:i+1])))
                
            w0 = w0_sum / sum(n)  
            if(sum(n[0:i+1]) != 0):  
                mean_0 = mean_sum0 / sum(n[0:i+1])
            else: mean_0 = 0
            
            # between the two thresholds (counted as foreground)
            # compute class probabilities and mean levels 
            w1_sum = numpy.sum(numpy.array(n[i+1:t]))
            mean_sum1 = numpy.sum((numpy.array(bins[i+1:t])*numpy.array(n[i+1:t])))
                  
            w1 = w1_sum / sum(n)
            if(sum(n[i+1:t]) != 0):
                mean_1 = mean_sum1 / sum(n[i+1:t])
            else: mean_1 = 0

            # foreground
            # compute class probabilities and mean levels 
            w2_sum = numpy.sum(numpy.array(n[t:len(n)]))
            mean_sum2 = numpy.sum((numpy.array(bins[t:len(n)])*numpy.array(n[t:len(n)])))
    
            w2 = w2_sum / sum(n)
            if(sum(n[t:len(n)]) != 0):
                mean_2 = mean_sum2 / sum(n[t:len(n)])
            else: mean_2 = 0

            # compute between class variance and append to list, append indices to list 
            bclv = w0*w1*((mean_1-mean_0)**2) + w0*w2*((mean_2 - mean_0)**2)+ w1*w2*((mean_2-mean_1)**2)
            thresholds = [i,t]
            bcv.append(bclv)
            threshold.append(thresholds)


    # select optimal threshold value, maximum value of between class variance
    optimal_thres = max(bcv)

    #select optimal threshold in the list
    l = 0
    while l < len(bcv):
        if bcv[l] == optimal_thres: thres.append(threshold[l])
        l += 1

    #assign first and second threshold 
    thres = thres[0]
    thres1  = bins[thres[0]]
    thres2  = bins[thres[1]]

    #perform image clipping, counting everything above the first threshold as foreground 
    for o in numpy.ndindex(copy.shape):
        if copy[o] <= (thres1): 
            copy[o] = 0
        elif copy[o] > thres1 and copy[o] <= thres2:  
            copy[o] = 1
        else: 
            copy[o] = 1
            
    return copy 


def two_level_otsu_thresholding_clip(img,x):
    """
    This function takes an image as well as the amount of wanted thresholds and calculates the class probabilies and mean levels for 
    foreground and background for each threshold. Then, the between class variance using the two-level Otsu's formula is computed 
    and the optimal threshold value is found. Lastly, the image is clipped based on the optimal threshold values, only counting the space between
    the two thresholds as foreground and thereby removing the reflections, and the thresholded image is returned. 

    :param img: Input image
    :param x: The number of intensity levels/ wanted thresholds
    :return: thresholded image 

    """
    import matplotlib.pyplot
    import numpy

    #load histogram (numerical values)
    n, bins = numpy.histogram(img.flatten(),bins = x)
  
    #initialize threshold value (T = 0) 
    thres = list()
    copy = img.copy()

    #create list to store values of within class variance for each threshold value as well as a list for the threshold indices 
    bcv = list()
    threshold = list()
    
    #calculate each within class variance for each possible threshold combination
    for i in range(0,len(n)):
        for t in range(0,len(n)):
            
            # background 
            # compute class probabilities and mean levels
            w0_sum = numpy.sum(numpy.array(n[0:i+1]))
            mean_sum0 = numpy.sum((numpy.array(bins[0:i+1])*numpy.array(n[0:i+1])))
                
            w0 = w0_sum / sum(n)  
            if(sum(n[0:i+1]) != 0):  
                mean_0 = mean_sum0 / sum(n[0:i+1])
            else: mean_0 = 0
 
            # foreground
            # compute class probabilities and mean levels 
            w1_sum = numpy.sum(numpy.array(n[i+1:t]))
            mean_sum1 = numpy.sum((numpy.array(bins[i+1:t])*numpy.array(n[i+1:t])))
                
            w1 = w1_sum / sum(n)
            if(sum(n[i+1:t]) != 0):
                mean_1 = mean_sum1 / sum(n[i+1:t])
            else: mean_1 = 0

            # reflections(interval above second threshold)
            # compute class probabilities and mean levels 
            w2_sum = numpy.sum(numpy.array(n[t:len(n)]))
            mean_sum2 = numpy.sum((numpy.array(bins[t:len(n)])*numpy.array(n[t:len(n)])))
              
            w2 = w2_sum / sum(n)
            if(sum(n[t:len(n)]) != 0):
                mean_2 = mean_sum2 / sum(n[t:len(n)])
            else: mean_2 = 0
          
            # compute between class variance and append to list, append indices to list 
            
            bclv = w0*w1*((mean_1-mean_0)**2) + w0*w2*((mean_2 - mean_0)**2)+ w1*w2*((mean_2-mean_1)**2)
            thresholds = [i,t]
            bcv.append(bclv)
            threshold.append(thresholds)


    # select optimal threshold value, maximum value of between class variance
    optimal_thres = max(bcv)

    #select optimal threshold in the list
    l = 0
    while l < len(bcv):
        if bcv[l] == optimal_thres: thres.append(threshold[l])
        l += 1

    #assign first and second threshold 
    thres = thres[0]
    thres1  = bins[thres[0]]
    thres2  = bins[thres[1]]
    
    #perform image clipping, only counting the interval between the first and second threshold as foreground 
    for o in numpy.ndindex(copy.shape):
        if copy[o] <= (thres1): 
            copy[o] = 0
        elif copy[o] > thres1 and copy[o] <= thres2:  
            copy[o] = 1
        else: 
            copy[o] = 0
            
    return copy 