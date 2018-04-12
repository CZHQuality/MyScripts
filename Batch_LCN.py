#coding=utf-8
#The code for batch local contrast normalization

import theano
import theano.tensor as T
import numpy
from theano.tensor.nnet import conv
import matplotlib.pyplot as plt
import pylab
import cv2
import LocalNor as LN
import os

def Norto255(input):
    #temp = numpy.array(input)
    #temp = input.reshape((256*256, 1))
    temp = input
    #print("temp is:", temp)
    da = temp.max()
    xiao = temp.min()
    #da = numpy.maximum(temp)
    #xiao = numpy.maximum(temp)
    #print("max and min are", da, xiao)
    temp = (temp - xiao) / (da - xiao)
    #print("temp is:", temp)
    #temp = temp.astype(numpy.int8)
    temp = temp * 255
    #temp = temp.astype(numpy.int8)
    return temp


list_path = "/media/ubuntu/CZHhy/BarcodeQA/TIEcode/DATAMultiLabel/list.txt"
read_space = "/media/ubuntu/CZHhy/BarcodeQA/TIEcode/DATAMultiLabel/Aug/"
save_space = "/media/ubuntu/CZHhy/BarcodeQA/TIEcode/DATAMultiLabelLCN/"

index = 1
for filename in os.listdir(read_space):
    #index += 1
    #if(index>3):
     #   break
    temp_path = read_space + filename
    print temp_path
    img = cv2.imread(temp_path) # 3 dims

    sp = img.shape
    row = sp[0]
    col = sp[1]
    dim = sp[2]
    img = numpy.array(img,dtype='float32')/256
    img = img.transpose(2,0,1).reshape(1,3,row,col)
    shape = (1,dim,row,col)
    obj1 =  LN.LecunLCN(img, shape, 1e-4, 9, True)
    out = obj1.output.eval()[0][0] #This command execute the theano 
    out2 = Norto255(out)
    temp_sv = save_space + filename
    cv2.imwrite(temp_sv, out2)


'''
def Norto255(input):
    #temp = numpy.array(input)
    #temp = input.reshape((256*256, 1))
    temp = input
    #print("temp is:", temp)
    da = temp.max()
    xiao = temp.min()
    #da = numpy.maximum(temp)
    #xiao = numpy.maximum(temp)
    #print("max and min are", da, xiao)
    temp = (temp - xiao) / (da - xiao)
    print("temp is:", temp)
    #temp = temp.astype(numpy.int8)
    temp = temp * 255
    #temp = temp.astype(numpy.int8)
    return temp

img = cv2.imread('/media/ubuntu/CZHhy/TestImg/ts2.jpg') # 3 dims
#print(img)
sp = img.shape
row = sp[0]
col = sp[1]
dim = sp[2]
img = numpy.array(img,dtype='float32')/256
img = img.transpose(2,0,1).reshape(1,3,row,col)
shape = (1,dim,row,col)
obj1 =  LN.LecunLCN(img, shape, 1e-4, 9, True)
out = obj1.output.eval()[0][0] #This command execute the theano 
#out2 = Norto255(out)
#print(out2)
print(out.shape)
#out2 = out.astype(numpy.int8)
#print(out2)
out2 = Norto255(out)
print(out2)
temp_sv = '/media/ubuntu/CZHhy/BarcodeQA/TIEcode/DATAMultiLabelLCN/shan.jpg'
cv2.imwrite(temp_sv, out2)

cv2.imshow('result1.jpg',out)
jieguo = cv2.imread('/media/ubuntu/CZHhy/BarcodeQA/TIEcode/DATAMultiLabelLCN/shan.jpg')
cv2.imshow('result2.jpg',jieguo)
cv2.waitKey(0)
'''