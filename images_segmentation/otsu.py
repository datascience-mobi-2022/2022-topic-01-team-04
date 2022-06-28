## Otsu Thresholding 
### Algorithm

#### **1.** load the input image<br>
#### **2.** calculate histogram: probabilities P(i) of each intensitiy level i<br>
#### **3.** Set up the initial threshold value (T=0) with its corresponding class probabilities wi(0) and class mean intensities µi(0)<br>
#### **4.** iterate over all possible threshold values (from T = 0 to T = maximum intensity of the image)<br>
#### **5.** compute an update corresponding values (wi(T) and µi(T)) and within class vairance σw² and between class variance σb² for each treshold value T <br>
#### **6.** when all possible threshold values are examined select the threshold intensity T which minimizes σw² or maximize  σb² (or use criterion measure)<br>
#### **7.** Image clipping: pixels in the input image with intensity values g(x,y) ≤ T are set to 0 (background) <br>    pixels in the input image with intensity values g(x,y) > T are set to 255 (foreground) <br>
#### **8.** segmented output image received





# otsu thresholding


def otsu_thresholding(img,x):
    import matplotlib.pyplot
    import numpy
#bins optimieren.... alles zu 0-255 machen

#img = img[~numpy.isnan(img)]
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
        for j in range(0,i+1):
            if(n[j] != numpy.NaN & bins[j] != numpy.NaN): 
                w0_sum += n[j]
                mean_sum0 += bins[j]*n[j]
            
        # background class probabilites and class mean levels
        w0 = w0_sum / sum(n)  
        if(sum(n[0:i+1]) != 0):  
             mean_0 = mean_sum0 / sum(n[0:i+1])
        else: mean_0 = 0
        
        # compute background class variance
        for m in range(0,i+1):
            if(n[m] != numpy.NaN & bins[m] != numpy.NaN): 
                v0_sum += ((bins[m]-mean_0)** 2) * n[m]
        
        v0 = v0_sum / sum(n[0:i+1])
        
        # sum up the probabilites of each intensity value;  and the mean value
        for k in range(i+1, len(n)): 
            if(n[k] != numpy.NaN & bins[k] != numpy.NaN): 
                w1_sum += n[k]
          
                mean_sum1 += bins[k]*n[k]

        # compute foreground class probabilities and class mean levels    
        w1 = w1_sum / sum(n)
     
        if(sum(n[i+1:len(n)]) != 0):
            mean_1 = mean_sum1 / sum(n[i+1:len(n)])
        else: mean_1 = 0
        # compute foreground class variance 
        for s in range(i+1,len(n)):
            if(n[s] != numpy.NaN & bins[s] != numpy.NaN): 
                v1_sum += ((bins[s]-mean_1) ** 2) * n[s]
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


    #perform image clipping 
    for o in numpy.ndindex(copy.shape):
        if copy[o] < (thres): 
            copy[o] = 0
        else:
            copy[o] = 1


    return copy 
