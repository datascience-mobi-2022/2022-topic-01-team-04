# General
## Objective & Methods
- Implement and evaluate methods for nuclei segmentation (**otsu clustering**)
- Implement **dice score**
- Local tresholding using the **sliding window scheme**

*literature (more or less theoretical)*

- Otsu tresholding:  
https://ieeexplore.ieee.org/document/4310076 (Stand in Beschreibung)

- Dice score:  
https://towardsdatascience.com/metrics-to-evaluate-your-semantic-segmentation-model-6bcb99639aa2

- Sliding window scheme *feel free to add more*:  
https://pyimagesearch.com/2015/03/23/sliding-windows-for-object-detection-with-python-and-opencv/

## Datasets
- (6) 1024x1024; GFP transfected GOWT1mouse cells; 10-20 *nuclei/img*
- (18) 1344x1024; Mouse embryonic cells stained with Hoechst; ~60 *nuclei/img*
- (4) 1100x700; HeLa cells expressing H2b-GFP; 30-50 *nuclei/img*

- Tif files have to be opened with a different program


*literature*
- https://bbbc.broadinstitute.org/image_sets (war in Beschreibung)

## Project structure
PROJECT PROPOSAL: until 18.05
- List of planned analysis steps
- Milestones (improtant achievements)
- Deliverables (result for each milestone)
- Approximate timetable

- Presentation auf Englisch
- Report auf Englisch

## Project proposal
1/3 + 1/3 + 1/3
### Data:
- data type
- data bsp
- what do we see?

### Algorithm
- What is otsu tresholding?
- Dice score
- _Dice score coefficient is a measure of similarity between 2 data sets, one of which has been acquired using in our example otsu tresholding, the other one being the ground truth dataset.  
In presentation: Eluer's diagram of TPs, FPs and FNs to visualize the comparison  
typical version vs perfect version aka full overlap  
all positives etc can be visualized as area, ground truth data consists of TP+FN, acquired data consists of TP+FP  
if our tresholding worked perfectly there would be no FPs and FNs, leaving TP+FN=TP+FP=TP, thus the amount of positive data over the 2 datasets would be 2TP+FN+FP=2TP  
DSC is the ratio between what we want (2TP) and what we get (2TP+FP+FN);  
the two extremes of dice score are as follows:   
positive data in gt and acquired dataset match perfectly: DSC=2TP/2TP=1  
there is no overlay between the two datasets: TP=0 => DSC=2TP/(2TP+FP+FN)=0_  

--->Implementation via python: for gt pictures and acq pictures:  
positive data in cell nuclei segmentation : white pixels of the region  
gt = ground truth data; acq = acquired data after otsu tresholding  
<img width="953" alt="image" src="https://user-images.githubusercontent.com/104202992/167428772-3e03a352-c4a3-46ed-8dc4-82efdab0f783.png">



 
  
- Ideas

### Project management

- Milestones
- How stuff is going to be organised
- Github implementation
- 
