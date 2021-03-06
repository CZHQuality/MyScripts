#coding=utf-8
#The code for local contrast normalization proposed by LeCun

import theano
import theano.tensor as T
import numpy
from theano.tensor.nnet import conv
import matplotlib.pyplot as plt
import pylab
import cv2

#class LecunLCN(object):
class LecunLCN:
    def __init__(self, X, image_shape, threshold=1e-4, radius=9, use_divisor=True):
        """
        Allocate an LCN.
        :type X: theano.tensor.dtensor4
        :param X: symbolic image tensor, of shape image_shape
        :type image_shape: tuple or list of length 4
        :param image_shape: (batch size, num input feature maps,
                             image height, image width)
        :type threshold: double
        :param threshold: the threshold will be used to avoid division by zeros
        :type radius: int
        :param radius: determines size of Gaussian filter patch (default 9x9)
        :type use_divisor: Boolean
        :param use_divisor: whether or not to apply divisive normalization
        """

        # Get Gaussian filter
        filter_shape = (1, image_shape[1], radius, radius)

        self.filters = theano.shared(self.gaussian_filter(filter_shape), borrow=True)

        # Compute the Guassian weighted average by means of convolution
        convout = conv.conv2d(
            input=X,
            filters=self.filters,
            image_shape=image_shape,
            filter_shape=filter_shape,
            border_mode='full'
        )

        # Subtractive step
        mid = int(numpy.floor(filter_shape[2] / 2.))

        # Make filter dimension broadcastable and subtract
        centered_X = X - T.addbroadcast(convout[:, :, mid:-mid, mid:-mid], 1)

        # Boolean marks whether or not to perform divisive step
        if use_divisor:
            # Note that the local variances can be computed by using the centered_X
            # tensor. If we convolve this with the mean filter, that should give us
            # the variance at each point. We simply take the square root to get our
            # denominator

            # Compute variances
            sum_sqr_XX = conv.conv2d(
                input=T.sqr(centered_X),
                filters=self.filters,
                image_shape=image_shape,
                filter_shape=filter_shape,
                border_mode='full'
            )


            # Take square root to get local standard deviation
            denom = T.sqrt(sum_sqr_XX[:,:,mid:-mid,mid:-mid])

            per_img_mean = denom.mean(axis=[2,3])
            divisor = T.largest(per_img_mean.dimshuffle(0, 1, 'x', 'x'), denom)
            # Divisise step
            new_X = centered_X / T.maximum(T.addbroadcast(divisor, 1), threshold)
        else:
            new_X = centered_X

        self.output = new_X
        #print(new_X)


    def gaussian_filter(self, kernel_shape):
        x = numpy.zeros(kernel_shape, dtype=theano.config.floatX)

        def gauss(x, y, sigma=2.0):
            Z = 2 * numpy.pi * sigma ** 2
            return  1. / Z * numpy.exp(-(x ** 2 + y ** 2) / (2. * sigma ** 2))

        mid = numpy.floor(kernel_shape[-1] / 2.)
        for kernel_idx in xrange(0, kernel_shape[1]):
            for i in xrange(0, kernel_shape[2]):
                for j in xrange(0, kernel_shape[3]):
                    x[0, kernel_idx, i, j] = gauss(i - mid, j - mid)

        return x / numpy.sum(x)


#img = cv2.imread('/media/ubuntu/CZHhy/TestImg/ts1.jpg') # 3 dims
img = cv2.imread('/media/ubuntu/CZHhy/TestImg/ts2.jpg') # 3 dims
img_ = img
#sp = img.shape
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sp = img.shape
row = sp[0]
col = sp[1]
dim = sp[2]
print("row,col,dim are:", row,col,dim)
#patch_batch = []
#patch_batch.append(img) 
#patch_batch.append(img) # 4 dims
img = numpy.array(img,dtype='float32')/256
img = img.transpose(2,0,1).reshape(1,3,row,col)

shape = (1,dim,row,col)
#obj1 = Foo('chengd', 18)

obj1 =  LecunLCN(img, shape, 1e-4, 9, True)
#out = obj1.output
#print(out)
out = obj1.output.eval()[0][0] #This command execute the theano 
cv2.imshow('original.jpg',img_)
cv2.imshow('result.jpg',out)
cv2.waitKey(0)






