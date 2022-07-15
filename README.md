# 2022-topic-01-team-04
  ## Cell nuclei segmentation: Implementation and evaluation of Otsu's thresholding
  
  **Team:** Marie-Claire Indilewitsch, Helen Jade, Maribel Schneider, Ieva Sorokina-Ozola  
  **Supervisors:** PD Dr. Karl Rohr, Christian Ritter  
  **Tutor:** Marie Becker 
  
  ## Abstract 
  
  
  This project deals with  Otsu's thresholding, which is a common image segmentation method.
  Using different preprocessing methods and Otsu's thresholding variations the segmentation for 3 different datasets (N2DH-GOWT1, N2DL-HeLa, NIH3T3) was analyzed to achieve the best thresholding. For preprocessing median filter, gaussian filter and histogram stretching were used. For thresholding we applied the global otsus´s thresholding, two-level Otsu as well as local adaptive thresholding. The images were then compared with ground truth images using the Dice Score for the evaluation of the thresholding.
  Each dataset has different challenges (reflections, noise, varying brightness), therefore they were individually considered. To find the best segmentation outcome the different combinations of preprocessing and otsu variations were applied, receiving the optimal combination for each dataset. Finally, we obtained the optimal thresholded images for each dataset using the individualized combination. 

  ## Description of datasets 
  ###  N2DH-GOWT1 dataset
  
  The datset N2DH-GOWT1 of the cell tracking challenge contains 6 images, showing GFP transfected mouse (Mus musculus) embryonic stem cells. These images were captured using a confocal microscope system (Leica TGS SP5). Moreover, the images have a size of 1024x1024 pixels and an approximate cell nuclei count of 10 to 20 per image. To visualize the cell nuclei, the transcription factor Oct4 was tagged with GFP. However, unstained regions (holes) can be identified within the cell nuclei, which can be attributed to the fact that Oct4 is only located in the nulei and not in the nucleolus (Bártová et al., 2011). This might not influence the thresholding algorithm itself, but further evaluation and comparison to the ground truth images. The main challenge of this dataset is varying brightness within the cell nuclei as well as partly low contrast to the background and noise. Without further image preprocessing the semgmentation algorithm might fail to distinguish all cell nuclei correctly from the background. 
  
  ### N2DL-HeLa dataset
  
 The N2DL-Hela dataset of the cell tracking challenge contains 4 images, showing human (Homo sapiens) epithelial cells of cervical cancer. These images were captured using an Olympus IX81 microscope. Furthermore, the images have a size of 1100x700 pixels and contain an average of 30-50 cell nuclei per image. The cells are modified to stably express H2b-GFP in order to visualize the cell nuclei (Neumann et al., 2010). For this dataset the segmentation algorithm is challenged by varying brigthness of the cell nuclei. 
 
  ### NIH3T3 dataset
  
 The NIH3T3 dataset contains 18 images, showing mouse Mus musculus) emryonic fibroblast cells. These images were captured using fluorescence microscopy, have a size of 1344x1024 pixels and contain about 60 cell nuclei per image. To visualize the cell nuclei, Hoechst was used as a staining method (Coelho et al., 2009). This dataset embodies challenging features like bright spots and reflectations as well as non-uniformal background, which might influence the segmentation algorithm in a strong way. 
 
 ## Folder and module structure
 
 1. [weekly reports](https://github.com/datascience-mobi-2022/2022-topic-01-team-04/tree/main/weekly-reports), [meetings](https://github.com/datascience-mobi-2022/2022-topic-01-team-04/tree/main/meetings):  notes from weekly meetings with tutor and team meetings
 2. [data](https://github.com/datascience-mobi-2022/2022-topic-01-team-04/tree/main/data):  all used data sets and ground truth images 
 3. [nuclei_segmentation](https://github.com/datascience-mobi-2022/2022-topic-01-team-04/tree/main/nuclei_segmentation):  package with all used functions 
        - complete_analysis.py   
        - dicescore.py  
        - dicescore_nonvectorized.py  
        - local_thresholding.py  
        - otsu.py  
        - otsu_nonvectorized.py  
        - optimal_otsu.py
        - preprocessing.py    
        - two_level_otsu.py  
        - two_level_local_thresholding.py
  4. [preprocessing](https://github.com/datascience-mobi-2022/2022-topic-01-team-04/tree/main/preprocessing):  all preprocessing combination files (Mac and Windows version) 
  5. [presentation](https://github.com/datascience-mobi-2022/2022-topic-01-team-04/tree/main/presentation): presentation files
  6. [report](https://github.com/datascience-mobi-2022/2022-topic-01-team-04/tree/main/report):  report files
  7. [archive](https://github.com/datascience-mobi-2022/2022-topic-01-team-04/tree/main/archive):  old files
  8. [Final picture](https://github.com/datascience-mobi-2022/2022-topic-01-team-04/tree/main/Final%20picture):  final picture for the final presentation
 
