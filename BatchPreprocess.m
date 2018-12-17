%%
% This code is used to prepare the 2D barcode dataset as 64X64 and .png
% format, to satisfied the function which transfers these images into
% "MNIST" format
clear;clc;
% input_path = 'D:\Study\code\Pytorch-AdvExm\JPG-PNG-to-MNIST-NN-Format-master\training-images-bmp\';
% sv_path = 'D:\Study\code\Pytorch-AdvExm\JPG-PNG-to-MNIST-NN-Format-master\training-images\';
input_path = 'D:\Study\code\Pytorch-AdvExm\JPG-PNG-to-MNIST-NN-Format-master\test-images-bmp\';
sv_path = 'D:\Study\code\Pytorch-AdvExm\JPG-PNG-to-MNIST-NN-Format-master\test-images\';

for i = 0 : 5
    temp_1 = strcat(input_path, num2str(i), '\');
    temp_2 = strcat(sv_path, num2str(i), '\');
    %  temp_1
    fpath = temp_1;  %这里是文件夹的名字
    img_path_list = dir(strcat(fpath,'*.bmp'));%获取该文件夹中所有bmp格式的图像  
    for j = 1 : length(img_path_list)
        img = imread(strcat(temp_1, img_path_list(j).name));
        img = imresize(img, [64, 64]);
        img = rgb2gray(img);
        name = img_path_list(j).name(1:length(img_path_list(j).name)-4);
        imwrite(img, strcat(temp_2,  name, '.png'));
    end
end

    
