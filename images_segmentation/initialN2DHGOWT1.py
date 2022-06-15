
from matplotlib.pyplot import pyplot as plt


gt1 = plt.imread(r'data\Otsu_data\N2DH-GOWT1\gt\man_seg01.tif')
gt2 = plt.imread(r'data\Otsu_data\N2DH-GOWT1\gt\man_seg21.tif')
gt3 = plt.imread(r'data\Otsu_data\N2DH-GOWT1\gt\man_seg31.tif')
gt4 = plt.imread(r'data\Otsu_data\N2DH-GOWT1\gt\man_seg39.tif')
gt5 = plt.imread(r'data\Otsu_data\N2DH-GOWT1\gt\man_seg52.tif')
gt6 = plt.imread(r'data\Otsu_data\N2DH-GOWT1\gt\man_seg72.tif')


ground_truth_N2DH = [gt1, gt2, gt3, gt4, gt5, gt6]

img1 = plt.imread(r'data\Otsu_data\N2DH-GOWT1\img\t01.tif')
img2 = plt.imread(r'data\Otsu_data\N2DH-GOWT1\img\t21.tif')
img3 = plt.imread(r'data\Otsu_data\N2DH-GOWT1\img\t31.tif')
img4 = plt.imread(r'data\Otsu_data\N2DH-GOWT1\img\t39.tif')
img5 = plt.imread(r'data\Otsu_data\N2DH-GOWT1\img\t52.tif')
img6 = plt.imread(r'data\Otsu_data\N2DH-GOWT1\img\t72.tif')



img_N2DL= [img1,img2,img3,img4, img5, img6]