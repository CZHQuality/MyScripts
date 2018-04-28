# This script is from CSDN blog: https://blog.csdn.net/lijiancheng0614/article/details/77727445
# test the prediction for single image

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import math
import tensorflow as tf

from nets import nets_factory
from preprocessing import preprocessing_factory

slim = tf.contrib.slim

tf.app.flags.DEFINE_string(
    'master', '', 'The address of the TensorFlow master to use.')

tf.app.flags.DEFINE_string(
    # 'checkpoint_path', '/media/ubuntu/CZHhy/BarcodeQA/ResNet/Dataset/model/mobilenetv1/model.ckpt-10442',
    # 'checkpoint_path', '/media/ubuntu/CZHhy/BarcodeQA/ResNet/Dataset/model/mobilenetnew/model.ckpt-29497', # For TaskA
    'checkpoint_path', '/media/ubuntu/CZHhy/BarcodeQA/ResNet/Dataset/model/mobilenetTaskB/model.ckpt-29136', # For TaskB
    'The directory where the model was written to or an absolute path to a '
    'checkpoint file.')

tf.app.flags.DEFINE_string(
   'test_path', '/media/ubuntu/CZHhy/BarcodeQA/ResNet/Dataset/TaskA/flower_photos/5/0-5-0-0-0-0-0-0-0-390_3.jpg', 'Test image path.')

tf.app.flags.DEFINE_integer(
    'num_classes', 6, 'Number of classes.')

tf.app.flags.DEFINE_integer(
    'labels_offset', 0,
    'An offset for the labels in the dataset. This flag is primarily used to '
    'evaluate the VGG and ResNet architectures which do not use a background '
    'class for the ImageNet dataset.')

tf.app.flags.DEFINE_string(
    'model_name', 'mobilenet_v1', 'The name of the architecture to evaluate.')

tf.app.flags.DEFINE_string(
    'preprocessing_name', None, 'The name of the preprocessing to use. If left '
    'as `None`, then the model_name flag is used.')

tf.app.flags.DEFINE_integer(
    'test_image_size', None, 'Eval image size')

FLAGS = tf.app.flags.FLAGS


#def main(_):
def main():
    #if not FLAGS.test_list:
     #   raise ValueError('You must supply the test list with --test_list')

    tf.logging.set_verbosity(tf.logging.INFO)
    with tf.Graph().as_default():
        tf_global_step = slim.get_or_create_global_step()

        ####################
        # Select the model #
        ####################
        network_fn = nets_factory.get_network_fn(
            FLAGS.model_name,
            num_classes=(FLAGS.num_classes - FLAGS.labels_offset),
            is_training=False)

        #####################################
        # Select the preprocessing function #
        #####################################
        preprocessing_name = FLAGS.preprocessing_name or FLAGS.model_name
        image_preprocessing_fn = preprocessing_factory.get_preprocessing(
            preprocessing_name,
            is_training=False)

        test_image_size = FLAGS.test_image_size or network_fn.default_image_size

        if tf.gfile.IsDirectory(FLAGS.checkpoint_path):
            checkpoint_path = tf.train.latest_checkpoint(FLAGS.checkpoint_path)
        else:
            checkpoint_path = FLAGS.checkpoint_path
        '''
        tf.Graph().as_default()
        with tf.Session() as sess:
            image = open(FLAGS.test_path, 'rb').read()
            image = tf.image.decode_jpeg(image, channels=3)
            processed_image = image_preprocessing_fn(image, test_image_size, test_image_size)
            processed_images = tf.expand_dims(processed_image, 0)
            logits, _ = network_fn(processed_images)
            predictions = tf.argmax(logits, 1)
            saver = tf.train.Saver()
            saver.restore(sess, checkpoint_path)
            np_image, network_input, predictions = sess.run([image, processed_image, predictions])
            print('{} {}'.format(FLAGS.test_path, predictions[0]))
        '''

        root_path = '/media/ubuntu/CZHhy/BarcodeQA/AlexNet/list2.txt' #image and path list of Validation Set 
        linestrlist = []
        fh = open(root_path, 'r')
        for line in fh.readlines():
            # print(line)
            linestr = line.strip()
            # print(linestr)
            linestrlist.append(linestr)
        fh.close()
        list = linestrlist
        #batchhh = list[0:1]
        batchhh = list[25:35]
        #batchhh = list[2:3]
        #batchhh = list[3:4]
        #batchhh = list[4:5]

        tf.Graph().as_default()
        '''
        saver = tf.train.Saver()
        for imgname in batchhh:
            with tf.Session() as sess:
            # for imgname in batchhh:
                #saver = tf.train.Saver()
                #saver.restore(sess, checkpoint_path)
                temp = imgname[0:-2]
                print("temp is:", temp)
                # temp = '/media/ubuntu/CZHhy/BarcodeQA/TIEcode/DATAMultiLabel/Aug/0-5-0-0-0-0-0-0-0-390_3.jpg'
                FLAGS.test_path = temp
                image = open(FLAGS.test_path, 'rb').read()
                image = tf.image.decode_jpeg(image, channels=3)
                processed_image = image_preprocessing_fn(image, test_image_size, test_image_size)
                processed_images = tf.expand_dims(processed_image, 0)
                logits, _ = network_fn(processed_images) # can not be repeatly loaded, just for single test image
                predictions = tf.argmax(logits, 1)
                saver = tf.train.Saver()
                saver.restore(sess, checkpoint_path)
                np_image, network_input, predictions = sess.run([image, processed_image, predictions])
                print('{} {}'.format(FLAGS.test_path, predictions[0]))
        '''  
        '''
        saver = tf.train.Saver()
        for imgname in batchhh:
            with tf.Session() as sess:
            # for imgname in batchhh:
                #saver = tf.train.Saver()
                #saver.restore(sess, checkpoint_path)
                temp = imgname[0:-2]
                print("temp is:", temp)
                # temp = '/media/ubuntu/CZHhy/BarcodeQA/TIEcode/DATAMultiLabel/Aug/0-5-0-0-0-0-0-0-0-390_3.jpg'
                FLAGS.test_path = temp
                image = open(FLAGS.test_path, 'rb').read()
                image = tf.image.decode_jpeg(image, channels=3)
                processed_image = image_preprocessing_fn(image, test_image_size, test_image_size)
                processed_images1 = tf.expand_dims(processed_image, 0)

                image2 = open('/media/ubuntu/CZHhy/BarcodeQA/ResNet/Dataset/TaskA/flower_photos/4/3-4-1-4-4-4-4-4-0-1295_10.jpg', 'rb').read()
                image2 = tf.image.decode_jpeg(image2, channels=3)
                processed_image2 = image_preprocessing_fn(image2, test_image_size, test_image_size)
                processed_images2 = tf.expand_dims(processed_image2, 0)
                
                images = []
                images.append(image)
                images.append(image2)
                processed_images = tf.concat([processed_images1, processed_images2], 0) # 0 means batch dimension
                

                logits, _ = network_fn(processed_images) # can not be repeatly loaded, just for single test image
                predictions = tf.argmax(logits, 1)
                saver = tf.train.Saver()
                saver.restore(sess, checkpoint_path)
                # np_image, network_input, predictions = sess.run([image, processed_image, predictions])
                np_image, network_input, predictions = sess.run([images, processed_images, predictions])
                print('{} {}'.format(FLAGS.test_path, predictions[0]))    
                print('{} {}'.format(FLAGS.test_path, predictions))   
        '''
        saver = tf.train.Saver()

        
        # for imgname in batchhh:
        with tf.Session() as sess:
            image2 = open('/media/ubuntu/CZHhy/BarcodeQA/ResNet/Dataset/TaskA/flower_photos/4/3-4-1-4-4-4-4-4-0-1295_10.jpg', 'rb').read()
            image2 = tf.image.decode_jpeg(image2, channels=3)
            processed_image2 = image_preprocessing_fn(image2, test_image_size, test_image_size)
            processed_images2 = tf.expand_dims(processed_image2, 0)
            processed_images = processed_images2
            images = []
            ori_labels = []
            print("temp is: /media/ubuntu/CZHhy/BarcodeQA/ResNet/Dataset/TaskA/flower_photos/4/3-4-1-4-4-4-4-4-0-1295_10.jpg") # to generate processed_images

            for imgname in batchhh:
                #saver = tf.train.Saver()
                #saver.restore(sess, checkpoint_path)
                temp = imgname[0:-2]
                print("temp is:", temp)
                temp_label = int(imgname[57:58]) # Task_B
                ori_labels.append(temp_label)
                # temp = '/media/ubuntu/CZHhy/BarcodeQA/TIEcode/DATAMultiLabel/Aug/0-5-0-0-0-0-0-0-0-390_3.jpg'
                FLAGS.test_path = temp
                image = open(FLAGS.test_path, 'rb').read()
                image = tf.image.decode_jpeg(image, channels=3)
                processed_image = image_preprocessing_fn(image, test_image_size, test_image_size)
                processed_images1 = tf.expand_dims(processed_image, 0)

                

                
                # images = []
                images.append(image)
                # images.append(image2)
                processed_images = tf.concat([processed_images, processed_images1], 0) # 0 means batch dimension
                

            logits, _ = network_fn(processed_images) # can not be repeatly loaded, just for single test image
            predictions = tf.argmax(logits, 1)
            saver = tf.train.Saver()
            saver.restore(sess, checkpoint_path)
            # np_image, network_input, predictions = sess.run([image, processed_image, predictions])
            np_image, network_input, predictions = sess.run([images, processed_images, predictions])
            print('{} {}'.format(FLAGS.test_path, predictions[0]))    
            print('{} {}'.format("Batch Logits are: ", predictions[1:-1]))   
            print("Original Labels are: ", ori_labels)
           

if __name__ == '__main__':
    #tf.app.run()
    main()
