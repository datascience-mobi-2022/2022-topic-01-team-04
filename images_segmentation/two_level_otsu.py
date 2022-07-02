from cmath import nan


def two_level_otsu_thresholding_within(img,x):
    import matplotlib.pyplot
    import numpy

   # load histogram, Mathematische werte aus Histogramm rausgreifen
    n, bins = numpy.histogram(img.flatten(),bins = x)
  
   # initialize threshold value (T = 0) 
    thres = list()
    copy = img.copy()

    # create list to store values of within class variance for each threshold value
    wcv = list()
    threshold = list()
    # set up initial values
    for i in range(0,len(n)):
        for t in range(0,len(n)):
            wclv = 0
            w0_sum = 0
            mean_sum0 = 0
            v0_sum = 0
            mean_sum1 = 0
            v1_sum = 0
            w0 = 0
            w1 = 0
            w1_sum = 0
            w2_sum = 0
            w2 = 0
            mean_sum2 = 0
            mean_2 = 0
            v2 = 0
            v2_sum = 0
            #sum up the probabilites of each intensity value;  and the mean value (sind noch nicht happy mit der definition :()
            w0_sum = numpy.sum(numpy.array(n[0:i+1]))
            mean_sum0 = numpy.sum((numpy.array(bins[0:i+1])*numpy.array(n[0:i+1])))
                
            # background class probabilites and class mean levels
            w0 = w0_sum / sum(n)  
            if(sum(n[0:i+1]) != 0):  
                mean_0 = mean_sum0 / sum(n[0:i+1])
            else: mean_0 = 0
            
            # compute background class variance

            v0_sum = numpy.sum((numpy.array((bins[0:i+1]-mean_0)** 2)*numpy.array(n[0:i+1])))
            v0 = v0_sum / sum(n[0:i+1])
            
            # sum up the probabilites of each intensity value;  and the mean value
            w1_sum = numpy.sum(numpy.array(n[i+1:t]))
            mean_sum1 = numpy.sum((numpy.array(bins[i+1:t])*numpy.array(n[i+1:t])))
                
            # compute foreground class probabilities and class mean levels    
            w1 = w1_sum / sum(n)
            if(sum(n[i+1:t]) != 0):
                mean_1 = mean_sum1 / sum(n[i+1:t])
            else: mean_1 = 0

            # compute foreground class variance 
            v1_sum = numpy.sum((numpy.array((bins[i+1:t]-mean_1)** 2)*numpy.array(n[i+1:t])))
        
            if( sum(n[i+1:t]) != 0):
                v1 = v1_sum / sum(n[i+1:t])
            else: v1 = 0

            # sum up the probabilites of each intensity value;  and the mean value
            w2_sum = numpy.sum(numpy.array(n[t:len(n)]))
            mean_sum2 = numpy.sum((numpy.array(bins[t:len(n)])*numpy.array(n[t:len(n)])))
                
            # compute foreground class probabilities and class mean levels    
            w2 = w2_sum / sum(n)
            if(sum(n[t:len(n)]) != 0):
                mean_2 = mean_sum2 / sum(n[t:len(n)])
            else: mean_2 = 0

            # compute foreground class variance 
            v2_sum = numpy.sum((numpy.array((bins[t:len(n)]-mean_2)** 2)*numpy.array(n[t:len(n)])))
        
            if( sum(n[t:len(n)]) != 0):
                v2 = v2_sum / sum(n[t:len(n)])
            else: v2 = 0

            # compute within class variance and append to list
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

    thres = thres[0]
    thres1  = bins[thres[0]]
    thres2  = bins[thres[1]]
    
    #index = numpy.where(numpy.array(wcv) == optimal_thres)
    #thres = bins[index]
    #perform image clipping 
    #copy[copy < thres[0]] = 0
    #copy[copy >= thres[0] and copy < thres[1]] = 0.5
    #copy[copy >= thres[1]] = 1

    for o in numpy.ndindex(copy.shape):
        if copy[o] < (thres1): 
            copy[o] = 0
        elif copy[o] >= thres1 and copy[o] < thres2:  
            copy[o] = 1
        else: 
            copy[o] = 1
            
    return copy 








def two_level_otsu_thresholding_clip_within(img,x):
    import matplotlib.pyplot
    import numpy

   # load histogram, Mathematische werte aus Histogramm rausgreifen
    n, bins = numpy.histogram(img.flatten(),bins = x)
  
   # initialize threshold value (T = 0) 
    thres = list()
    copy = img.copy()

    # create list to store values of within class variance for each threshold value
    wcv = list()
    threshold = list()
    # set up initial values
    for i in range(0,len(n)):
        for t in range(0,len(n)):
            wclv = 0
            mean_0 = 0
            mean_1 = 0
            w0_sum = 0
            mean_sum0 = 0
            v0_sum = 0
            mean_sum1 = 0
            v1_sum = 0
            w0 = 0
            w1 = 0
            w1_sum = 0
            w2_sum = 0
            w2 = 0
            mean_sum2 = 0
            mean_2 = 0
            v2 = 0
            v2_sum = 0
            #sum up the probabilites of each intensity value;  and the mean value (sind noch nicht happy mit der definition :()
            w0_sum = numpy.sum(numpy.array(n[0:i+1]))
            mean_sum0 = numpy.sum((numpy.array(bins[0:i+1])*numpy.array(n[0:i+1])))
                
            # background class probabilites and class mean levels
            w0 = w0_sum / sum(n)  
            if(sum(n[0:i+1]) != 0):  
                mean_0 = mean_sum0 / sum(n[0:i+1])
            else: mean_0 = 0
            
            # compute background class variance

            v0_sum = numpy.sum((numpy.array((bins[0:i+1]-mean_0)** 2)*numpy.array(n[0:i+1])))
            v0 = v0_sum / sum(n[0:i+1])
            
            # sum up the probabilites of each intensity value;  and the mean value
            w1_sum = numpy.sum(numpy.array(n[i+1:t]))
            mean_sum1 = numpy.sum((numpy.array(bins[i+1:t])*numpy.array(n[i+1:t])))
                
            # compute foreground class probabilities and class mean levels    
            w1 = w1_sum / sum(n)
            if(sum(n[i+1:t]) != 0):
                mean_1 = mean_sum1 / sum(n[i+1:t])
            else: mean_1 = 0

            # compute foreground class variance 
            v1_sum = numpy.sum((numpy.array((bins[i+1:t]-mean_1)** 2)*numpy.array(n[i+1:t])))
        
            if( sum(n[i+1:t]) != 0):
                v1 = v1_sum / sum(n[i+1:t])
            else: v1 = 0

            # sum up the probabilites of each intensity value;  and the mean value
            w2_sum = numpy.sum(numpy.array(n[t:len(n)]))
            mean_sum2 = numpy.sum((numpy.array(bins[t:len(n)])*numpy.array(n[t:len(n)])))
                
            # compute foreground class probabilities and class mean levels    
            w2 = w2_sum / sum(n)
            if(sum(n[t:len(n)]) != 0):
                mean_2 = mean_sum2 / sum(n[t:len(n)])
            else: mean_2 = 0

            # compute foreground class variance 
            v2_sum = numpy.sum((numpy.array((bins[t:len(n)]-mean_2)** 2)*numpy.array(n[t:len(n)])))
        
            if( sum(n[t:len(n)]) != 0):
                v2 = v2_sum / sum(n[t:len(n)])
            else: v2 = 0

            # compute within class variance and append to list
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

    thres = thres[0]
    thres1  = bins[thres[0]]
    thres2  = bins[thres[1]]
    
    #index = numpy.where(numpy.array(wcv) == optimal_thres)
    #thres = bins[index]
    #perform image clipping 
    #copy[copy < thres[0]] = 0
    #copy[copy >= thres[0] and copy < thres[1]] = 0.5
    #copy[copy >= thres[1]] = 1

    for o in numpy.ndindex(copy.shape):
        if copy[o] < (thres1): 
            copy[o] = 0
        elif copy[o] >= thres1 and copy[o] < thres2:  
            copy[o] = 1
        else: 
            copy[o] = 0
            
    return copy 

def two_level_otsu_thresholding(img,x):
    import matplotlib.pyplot
    import numpy

    # load histogram, Mathematische werte aus Histogramm rausgreifen
    n, bins = numpy.histogram(img.flatten(),bins = x)

    # initialize threshold value (T = 0) 
    thres = list()
    copy = img.copy()

    # create list to store values of within class variance for each threshold value
    wcv = list()
    threshold = list()
    # set up initial values
    for i in range(0,len(n)):
        for t in range(0,len(n)):
            mean_0 = 0
            mean_1 = 0
            wclv = 0
            w0_sum = 0
            mean_sum0 = 0
            v0_sum = 0
            mean_sum1 = 0
            v1_sum = 0
            w0 = 0
            w1 = 0
            w1_sum = 0
            w2_sum = 0
            w2 = 0
            mean_sum2 = 0
            mean_2 = 0
            v2 = 0
            v2_sum = 0
            #sum up the probabilites of each intensity value;  and the mean value (sind noch nicht happy mit der definition :()
            w0_sum = numpy.sum(numpy.array(n[0:i+1]))
            mean_sum0 = numpy.sum((numpy.array(bins[0:i+1])*numpy.array(n[0:i+1])))
                
            # background class probabilites and class mean levels
            w0 = w0_sum / sum(n)  
            if(sum(n[0:i+1]) != 0):  
                mean_0 = mean_sum0 / sum(n[0:i+1])
            else: mean_0 = 0
            
            # compute background class variance

            
            # sum up the probabilites of each intensity value;  and the mean value
            w1_sum = numpy.sum(numpy.array(n[i+1:t]))
            mean_sum1 = numpy.sum((numpy.array(bins[i+1:t])*numpy.array(n[i+1:t])))
                
            # compute foreground class probabilities and class mean levels    
            w1 = w1_sum / sum(n)
            if(sum(n[i+1:t]) != 0):
                mean_1 = mean_sum1 / sum(n[i+1:t])
            else: mean_1 = 0

            # compute foreground class variance 
        

            # sum up the probabilites of each intensity value;  and the mean value
            w2_sum = numpy.sum(numpy.array(n[t:len(n)]))
            mean_sum2 = numpy.sum((numpy.array(bins[t:len(n)])*numpy.array(n[t:len(n)])))
                
            # compute foreground class probabilities and class mean levels    
            w2 = w2_sum / sum(n)
            if(sum(n[t:len(n)]) != 0):
                mean_2 = mean_sum2 / sum(n[t:len(n)])
            else: mean_2 = 0

            # compute foreground class variance 
        

            # compute within class variance and append to list
            m_t = w0*mean_0 + w1*mean_1 + w2*mean_2 
            wclv = w0*((mean_0 - m_t)**2)+ w1*((mean_1 - m_t)**2) + w2*((mean_2 - m_t)**2)
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

    thres = thres[0]
    thres1  = bins[thres[0]]
    thres2  = bins[thres[1]]

    #index = numpy.where(numpy.array(wcv) == optimal_thres)
    #thres = bins[index]
    #perform image clipping 
    #copy[copy < thres[0]] = 0
    #copy[copy >= thres[0] and copy < thres[1]] = 0.5
    #copy[copy >= thres[1]] = 1

    for o in numpy.ndindex(copy.shape):
        if copy[o] < (thres1): 
            copy[o] = 0
        elif copy[o] >= thres1 and copy[o] < thres2:  
            copy[o] = 1
        else: 
            copy[o] = 1
            
    return copy 








def two_level_otsu_thresholding_clip(img,x):
    import matplotlib.pyplot
    import numpy

   # load histogram, Mathematische werte aus Histogramm rausgreifen
    n, bins = numpy.histogram(img.flatten(),bins = x)
  
   # initialize threshold value (T = 0) 
    thres = list()
    copy = img.copy()

    # create list to store values of within class variance for each threshold value
    wcv = list()
    threshold = list()
    # set up initial values
    for i in range(0,len(n)):
        for t in range(0,len(n)):
            wclv = 0
            w0_sum = 0
            mean_sum0 = 0
            v0_sum = 0
            mean_sum1 = 0
            v1_sum = 0
            w0 = 0
            w1 = 0
            w1_sum = 0
            w2_sum = 0
            w2 = 0
            mean_sum2 = 0
            mean_2 = 0
            v2 = 0
            v2_sum = 0
            #sum up the probabilites of each intensity value;  and the mean value (sind noch nicht happy mit der definition :()
            w0_sum = numpy.sum(numpy.array(n[0:i+1]))
            mean_sum0 = numpy.sum((numpy.array(bins[0:i+1])*numpy.array(n[0:i+1])))
                
            # background class probabilites and class mean levels
            w0 = w0_sum / sum(n)  
            if(sum(n[0:i+1]) != 0):  
                mean_0 = mean_sum0 / sum(n[0:i+1])
            else: mean_0 = 0
            
            # compute background class variance

    
            # sum up the probabilites of each intensity value;  and the mean value
            w1_sum = numpy.sum(numpy.array(n[i+1:t]))
            mean_sum1 = numpy.sum((numpy.array(bins[i+1:t])*numpy.array(n[i+1:t])))
                
            # compute foreground class probabilities and class mean levels    
            w1 = w1_sum / sum(n)
            if(sum(n[i+1:t]) != 0):
                mean_1 = mean_sum1 / sum(n[i+1:t])
            else: mean_1 = 0

            # compute foreground class variance 
            
            # sum up the probabilites of each intensity value;  and the mean value
            w2_sum = numpy.sum(numpy.array(n[t:len(n)]))
            mean_sum2 = numpy.sum((numpy.array(bins[t:len(n)])*numpy.array(n[t:len(n)])))
                
            # compute foreground class probabilities and class mean levels    
            w2 = w2_sum / sum(n)
            if(sum(n[t:len(n)]) != 0):
                mean_2 = mean_sum2 / sum(n[t:len(n)])
            else: mean_2 = 0

            # compute foreground class variance 
          
            # compute within class variance and append to list
            m_t = w0*mean_0 + w1*mean_1 + w2*mean_2 
            wclv = w0*((mean_0 - m_t)**2)+ w1*((mean_1 - m_t)**2) + w2*((mean_2 - m_t)**2)
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

    thres = thres[0]
    thres1  = bins[thres[0]]
    thres2  = bins[thres[1]]
    
    #index = numpy.where(numpy.array(wcv) == optimal_thres)
    #thres = bins[index]
    #perform image clipping 
    #copy[copy < thres[0]] = 0
    #copy[copy >= thres[0] and copy < thres[1]] = 0.5
    #copy[copy >= thres[1]] = 1

    for o in numpy.ndindex(copy.shape):
        if copy[o] < (thres1): 
            copy[o] = 0
        elif copy[o] >= thres1 and copy[o] < thres2:  
            copy[o] = 1
        else: 
            copy[o] = 0
            
    return copy 