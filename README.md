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
  
  This datset contains 6 images showing embryonic stem cells from the organism mouse (Mus musculus). The images have a size of 1024x1024 pixels and an approximate cell nuclei count of 10 to 20 per image. For visualization of the nuclei they tagged Oct4 with GFP. In the attributable studies they found out about UV-damaged Chromatin in embryonic stem cells by detecting different amounts of Oct4 accumulations. The images were received using the confocal microscope Leica TGS SP5. (Bártová, E. et al., 2011). The main challenge of this dataset is the low contrast as well as stained parts within the cells. 
  
  ### N2DL-HeLa dataset
  
  In this dateset 4 images from human cells (Homo sapiens) derived from cervical cancer can be seen. The images have a size of 1100x700 pixels and contain an average of 30-50 nuclei per image. The cells are modified to stably express H2b-GFP in order to make the nuclei visible. This dataset was used for the development of a phenotypic screening platform for the identification of human genes important for specific biological functions like cell division. The images were made using an Olympus IX81 microscope (Neumann, B. et al., 2010). A problem that occurs is the varying brightness.
  
  ### NIH3T3 dataset
  
  As for this dataset, 18 images that show mouse (Mus musculus) embryonic fibroblast cells, are shown. The images have a size of 1344x1024 pixels and contain about 60 nuclei per image. For these images Hoechst is used to stain the nuclei. 
  (Coelho, L.P. et al., 2009). The challenges faced here are the varying brightnesses of the images, the reflections and overlapping nuclei.
