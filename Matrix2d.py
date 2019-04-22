
# coding: utf-8

# In[17]:


import numpy as np
import matplotlib.pyplot as plt
import math
def _rotate_matrix(angle,cenx,ceny):
    C=math.cos(angle*math.pi/180)
    S=math.sin(angle*math.pi/180)
    M11=C
    M12=-S
    M13=(1-C)*cenx+S*ceny
    M21=S
    M22=C
    M23=(1-C)*ceny-S*cenx
    return np.array([[M11,M12,M13],[M21,M22,M23],[0,0,1]])
def _scale_matrix(sx,sy,cenx,ceny):
    M11=sx
    M13=(1-sx)*cenx
    M22=sy
    M23=(1-sy)*ceny
    return np.array([[M11,0,M13],[0,M22,M23],[0,0,1]])
def scalebound(scale,Xmin,Xmax,Ymin,Ymax):
    cenx=(Xmin+Xmax)/2
    ceny=(Ymin+Ymax)/2
    return (Xmin-cenx)*scale+cenx,(Xmax-cenx)*scale+cenx,(Ymin-ceny)*scale+ceny,(Ymax-ceny)*scale+ceny
def Rotate_Points(Points,angle,Xmin,Xmax,Ymin,Ymax):
    cenx=(Xmin+Xmax)/2
    ceny=(Ymin+Ymax)/2
    Matrix=_rotate_matrix(angle,cenx,ceny)
    Points=np.insert(Points,2,1,axis=2)
    return np.dot(Points,Matrix.T)[:,:,0:2]
if __name__=='__main__':
    arr=np.array([[0,0],[50,0],[50,50],[0,50],[0,0]])
    plt.plot(arr[:,0],arr[:,1],color='g')
    newa=Rotate_Points(arr,45)
    plt.plot(newa[:,0],newa[:,1],color='r')







