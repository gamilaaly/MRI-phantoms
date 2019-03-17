# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:30:53 2019

@author: Gamila
"""
#liver , kidney , spleen , fats 

import numpy as np

import matplotlib.pyplot as pl
n =512
## creating blank black image
square_phantom = np.zeros ((n, n))


kidney =np.full((115,115 ), 255) 
liver=np.full((250, 250), 200)
spleen=np.full((100, 100), 100)
fat=np.full((150, 150), 50)


square_phantom [50:165, 50:165]=kidney
square_phantom [50:300, 200:450]=liver
square_phantom [315:415, 412:512]=spleen
square_phantom [350:500, 100:250]=fat

## assign T1 and T2 to each tissue 
T1=np.full((512,512 ), 0) 

kidneyT1 =np.full((115,115 ), 400) 
liverT1=np.full((250, 250), 400)
spleenT1=np.full((100, 100), 550)
fatT1=np.full((150, 150), 250)

T1 [50:165, 50:165]=kidneyT1
T1[50:300, 200:450]=liverT1
T1[315:415, 412:512]=spleenT1
T1 [350:500, 100:250]=fatT1

T1= (255*T1)/np.max(T1)

T2=np.full((512,512 ), 0)  

kidneyT2 =np.full((115,115 ), 60) 
liverT2=np.full((250, 250), 40)
spleenT2=np.full((100, 100), 60)
fatT2=np.full((150, 150), 70)

T2 [50:165, 50:165]=kidneyT2
T2[50:300, 200:450]=liverT2
T2[315:415, 412:512]=spleenT2
T2 [350:500, 100:250]=fatT2

T2= (255*T2)/np.max(T2)

## to draw T1


All=np.concatenate ((square_phantom,T1,T2)) #concatentation row wise (fo2 b3d)



## assign T1 and T2 to each tissue 

np.savetxt('squrePhantom.txt' ,All, delimiter=',')
#a = open("testout.txt", 'r')# open file in read mode 
#  
#
#
#x= a.read
x= np.loadtxt('squrePhantom.txt', delimiter=',')
print(len(x))
z=(len(x)/3)

I=x[1:int(z),:]
T1=x[1+int(z):2*int(z),:]
T2=x[1+2*int(z):3*int(z),:]
pl.imshow(T2 , cmap='gray', vmin=0, vmax=255)

pl.imsave('g.png', square_phantom , cmap='gray')


