# 2022-topic-01-team-04
  ## Cell nuclei segmentation: Implementation and evaluation of Otsu thresholding
  
  **Team:** Marie-Claire Indilewitsch, Helen Jade, Maribel Schneider, Ieva Sorokina-Ozola  
  **Supervisors:** PD Dr. Karl Rohr, Christian Ritter  
  **Tutor:** Marie Becker 
  
  ## Abstract 
  
Otsu thresholding is a common image segmentation method. In our project we focused on cell nuclei segmentation using Otsu thresholding as well as its variations to achieve optimal image segmentation. Different preprocessing methods and Otsu thresholding variations were applied to three different datasets (N2DH-GOWT1, N2DL-HeLa, NIH3T3) in order to achieve optimal cell nuclei segmentation for each dataset. Median filter, gaussian filter and histogram stretching as well as their combinations served as preprocessing methods, whereas global Otsu thresholding, two-level Otsu and local adaptive thresholding were used as thresholding algorithms. Furthermore, a hole filling algorithm was introduced as a postprocessing method for one dataset. Lastly, the processed images were compared to the corresponding ground truth images, using Dice score as the evaluation method. Each dataset had different challenges (reflections, noise, varying brightness) which were individually considered in the image analysis. To find the best segmentation outcome, the different combinations of preprocessing methods and Otsu thresholding variations were applied and the optimal one for each dataset was selected. Finally, we obtained the ideal segmented images for each dataset using the best individualized combination. 

  ## Description of datasets 
  ###  N2DH-GOWT1 dataset
  
The datset N2DH-GOWT1 contains 6 images, showing GFP transfected mouse (<I>Mus musculus</I>) embryonic stem cells. These images were captured using a confocal microscope system (Leica TGS SP5). Moreover, the images have a size of 1024x1024 pixels and an approximate cell nuclei count of 10 to 20 per image. To visualize the cell nuclei, the transcription factor Oct4 was tagged with GFP. However, unstained regions (holes) can be identified within the cell nuclei, which can be attributed to the fact that Oct4 is only located in the nuclei and not in the nucleolus (Bártová <I>et al.</I>, 2011). This might not influence the thresholding algorithm itself, but further evaluation and comparison to the ground truth images. The main challenge of this dataset is varying brightness within the cell nuclei as well as partly low contrast to the background and noise. Without further image preprocessing the segmentation algorithm might fail to distinguish all cell nuclei correctly from the background.
  
  ### N2DL-HeLa dataset
  
The N2DL-Hela dataset contains 4 images, showing human (<I>Homo sapiens</I>) epithelial cells of cervical cancer. These images were captured using an Olympus IX81 microscope. Furthermore, the images have a size of 1100x700 pixels and contain an average of 30-50 cell nuclei per image. The cells are modified to stably express H2b-GFP in order to visualize the cell nuclei (Neumann <I>et al.</I>, 2010). For this dataset the segmentation algorithm is challenged by varying brigthness of the cell nuclei.
 
  ### NIH3T3 dataset
  
The NIH3T3 dataset contains 18 images, showing mouse (<I>Mus musculus</I>) embryonic fibroblast cells. These images were captured using fluorescence microscopy, have a size of 1344x1024 pixels and contain about 60 cell nuclei per image. To visualize the cell nuclei, Hoechst was used as a staining method (Coelho <I>et al.</I>, 2009). This dataset embodies challenging features like bright spots and reflections as well as a non-uniformal background, which might massively disturb the segmentation.
 
 ## Folder and module structure
 
 1. [weekly reports](https://github.com/datascience-mobi-2022/2022-topic-01-team-04/tree/main/weekly-reports): notes from weekly meetings with our tutor
 2. [data](https://github.com/datascience-mobi-2022/2022-topic-01-team-04/tree/main/data):  all used data sets, ground truth images and outputs
 3. [nuclei_segmentation](https://github.com/datascience-mobi-2022/2022-topic-01-team-04/tree/main/nuclei_segmentation):  package with all used functions   
        - complete_analysis.py   
        - dicescore.py   
        - local_thresholding.py  
        - otsu.py  
        - optimal_otsu.py  
        - preprocessing.py    
        - two_level_otsu.py  
        - two_level_local_thresholding.py
  4. [preprocessing](https://github.com/datascience-mobi-2022/2022-topic-01-team-04/tree/main/preprocessing):  all preprocessing combination files (Mac and Windows version) 
  5. [presentation](https://github.com/datascience-mobi-2022/2022-topic-01-team-04/tree/main/presentation): presentation files
  6. [report](https://github.com/datascience-mobi-2022/2022-topic-01-team-04/tree/main/report):  report files
  7. [archive](https://github.com/datascience-mobi-2022/2022-topic-01-team-04/tree/main/archive):  old files
  
 
