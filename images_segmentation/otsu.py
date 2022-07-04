# otsu thresholding


from cmath import nan


def otsu_thresholding_within(img,x):
    import matplotlib.pyplot
    import numpy

   # load histogram, Mathematische werte aus Histogramm rausgreifen
    n, bins = numpy.histogram(img.flatten(),bins = x)
  
   # initialize threshold value (T = 0) 
    thres = 0
    copy = img.copy()

    # create list to store values of within class variance for each threshold value
    wcv = list()
    
    # set up initial values
    for i in range(0,len(n)):
        wclv = 0
        w0_sum = 0
        mean_sum0 = 0
        v0_sum = 0
        mean_sum1 = 0
        v1_sum = 0
        w0 = 0
        w1 = 0
        w1_sum = 0

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
        w1_sum = numpy.sum(numpy.array(n[i+1:len(n)]))
        mean_sum1 = numpy.sum((numpy.array(bins[i+1:len(n)])*numpy.array(n[i+1:len(n)])))
            
        # compute foreground class probabilities and class mean levels    
        w1 = w1_sum / sum(n)
        if(sum(n[i+1:len(n)]) != 0):
            mean_1 = mean_sum1 / sum(n[i+1:len(n)])
        else: mean_1 = 0

        # compute foreground class variance 
        v1_sum = numpy.sum((numpy.array((bins[i+1:len(n)]-mean_1)** 2)*numpy.array(n[i+1:len(n)])))
       
        if( sum(n[i+1:len(n)]) != 0):
            v1 = v1_sum / sum(n[i+1:len(n)])
        else: v1 = 0

        # compute within class variance and append to list
        wclv = (w0 * v0) + (w1 * v1)
        wcv.append(wclv)

    # select optimal threshold value, minimum value of within class variance
    optimal_thres = min(wcv)

    #select optimal threshold in the list
    l = 0
    while l < len(wcv):
        if wcv[l] == optimal_thres: thres = bins[l]
        l += 1
   # index = numpy.where(numpy.array(wcv) == optimal_thres)
    #thres = bins[index]
    #perform image clipping 
    copy[copy < thres] = 0
    copy[copy >= thres] = 1

    return copy 



from cmath import nan


def otsu_thresholding(img,x):
    import matplotlib.pyplot
    import numpy

   # load histogram, Mathematische werte aus Histogramm rausgreifen
    n, bins = numpy.histogram(img.flatten(),bins = x)
  
   # initialize threshold value (T = 0) 
    thres = 0
    copy = img.copy()

    # create list to store values of within class variance for each threshold value
    bcv = list()
    
    # set up initial values
    for i in range(0,len(n)):
        bclv = 0
        w0_sum = 0
        mean_sum0 = 0
        mean_sum1 = 0
        w0 = 0
        w1 = 0
        w1_sum = 0

        #sum up the probabilites of each intensity value;  and the mean value (sind noch nicht happy mit der definition :()
        w0_sum = numpy.sum(numpy.array(n[0:i+1]))
        mean_sum0 = numpy.sum((numpy.array(bins[0:i+1])*numpy.array(n[0:i+1])))
            
        # background class probabilites and class mean levels
        w0 = w0_sum / sum(n)  
        if(sum(n[0:i+1]) != 0):  
             mean_0 = mean_sum0 / sum(n[0:i+1])
        else: mean_0 = 0
        
        # compute background class variance

        #v0_sum = numpy.sum((numpy.array((bins[0:i+1]-mean_0)** 2)*numpy.array(n[0:i+1])))
        #v0 = v0_sum / sum(n[0:i+1])
        
        # sum up the probabilites of each intensity value;  and the mean value
        w1_sum = numpy.sum(numpy.array(n[i+1:len(n)]))
        mean_sum1 = numpy.sum((numpy.array(bins[i+1:len(n)])*numpy.array(n[i+1:len(n)])))
            
        # compute foreground class probabilities and class mean levels    
        w1 = w1_sum / sum(n)
        if(sum(n[i+1:len(n)]) != 0):
            mean_1 = mean_sum1 / sum(n[i+1:len(n)])
        else: mean_1 = 0

        # compute foreground class variance 
        #v1_sum = numpy.sum((numpy.array((bins[i+1:len(n)]-mean_1)** 2)*numpy.array(n[i+1:len(n)])))
       
        #if( sum(n[i+1:len(n)]) != 0):
         #   v1 = v1_sum / sum(n[i+1:len(n)])
        #else: v1 = 0

        # compute within class variance and append to list
        bclv = w0*w1*((mean_1-mean_0)**2)
        bcv.append(bclv)

    # select optimal threshold value, minimum value of within class variance
    optimal_thres = max(bcv)

    #select optimal threshold in the list
    l = 0
    while l < len(bcv):
        if bcv[l] == optimal_thres: thres = bins[l]
        l += 1
   # index = numpy.where(numpy.array(wcv) == optimal_thres)
    #thres = bins[index]
    #perform image clipping 
    copy[copy < thres] = 0
    copy[copy >= thres] = 1

    return copy 