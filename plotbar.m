%%
% This code is used to plot the bar graph
%{
y1=[15.81292 16.43826 5.696203; 10.91314 8.493151 5.379747; 10.24499 7.945205 8.860759; 12.02673 13.15068 19.62025;...
    5.790646 15.89041 37.34177; 7.349666 9.041096 6.012658; 10.69042 10.13699 3.797468; 16.03563 10.68493 5.696203;...
    11.13586 8.219178 7.594937];
 
b=bar(y1);
grid on;
set(gca, 'xticklabel', {'0-20','20-40','40-60','60-80','80-100','100-120','120-140','140-160','160-180'});
legend('156C','164C','172C');
xlabel('Angle:degree');
ylabel('Percentage:%');
title('Angle');
ylim([-2 2]);
%}


%%
%{
figure;
sAUC = [0.6386 0.6546 0.6439 0.6588; ...
              0.6442 0.6667 0.6614 0.6598]; 
b=bar(sAUC);
grid on;
ylim([0.63 0.72]);
set(gca, 'xticklabel', {'fine-tune on CAT2000','fine-tune on Valid Set'});
legend('SAM-VGG','SAM-ResNet','ML-Net','OpenSALICON');
%xlabel('Angle:degree');
ylabel('sAUC score');
%title('Angle');
set(gca,'FontSize',15);
%line([0:1],[0.68,0.68],'linestyle','--');
line([1:2],[0.7168,0.7168],'linestyle','--','linewidth',4,'color','r');

figure;
CC = [0.7606 0.7730 0.5974 0.5304; ...
              0.7753 0.7822 0.5984 0.5484]; 
b=bar(CC);
grid on;
ylim([0.50 0.95]);
set(gca, 'xticklabel', {'fine-tune on CAT2000','fine-tune on Valid Set'});
%legend('SAM-VGG','SAM-ResNet','ML-Net','OpenSALICON');
%xlabel('Angle:degree');
ylabel('CC score');
%title('Angle');
set(gca,'FontSize',15);
line([1:2],[0.9333,0.9333],'linestyle','--','linewidth',4,'color','r');

figure;
NSS = [2.2692 2.2922 1.9558 1.6223; ...
              2.3444 2.3567 1.9527 1.7108]; 
b=bar(NSS);
grid on;
ylim([1.50 3.20]);
set(gca, 'xticklabel', {'fine-tune on CAT2000','fine-tune on Valid Set'});
%legend('SAM-VGG','SAM-ResNet','ML-Net','OpenSALICON');
%xlabel('Angle:degree');
ylabel('NSS score');
%title('Angle');
set(gca,'FontSize',15);
line([1:2],[3.1273,3.1273],'linestyle','--','linewidth',4,'color','r');

figure;
KL = [1.0122 1.1512 0.8945 0.8691; ...
              0.6673 0.6821 0.7702 0.8134]; 
b=bar(KL);
grid on;
ylim([0.50 1.30]);
set(gca, 'xticklabel', {'fine-tune on CAT2000','fine-tune on Valid Set'});
%legend('SAM-VGG','SAM-ResNet','ML-Net','OpenSALICON');
%xlabel('Angle:degree');
ylabel('KL score');
%title('Angle');
set(gca,'FontSize',15);

figure;
AUCBorji = [0.8681 0.8724 0.8107 0.8205; ...
              0.8766 0.8817 0.8207 0.8469]; 
b=bar(AUCBorji);
grid on;
ylim([0.80 0.90]);
set(gca, 'xticklabel', {'fine-tune on CAT2000','fine-tune on Valid Set'});
%legend('SAM-VGG','SAM-ResNet','ML-Net','OpenSALICON');
%xlabel('Angle:degree');
ylabel('AUC-Borji score');
%title('Angle');
set(gca,'FontSize',15);

figure;
SIM = [0.6317 0.6385 0.5364 0.4778; ...
              0.6584 0.6627 0.5386 0.5018]; 
b=bar(SIM);
grid on;
ylim([0.45 0.68]);
set(gca, 'xticklabel', {'fine-tune on CAT2000','fine-tune on Valid Set'});
%legend('SAM-VGG','SAM-ResNet','ML-Net','OpenSALICON');
%xlabel('Angle:degree');
ylabel('SIM score');
%title('Angle');
set(gca,'FontSize',15);
%}
%%
figure;
sAUC = [0.5790 0.5771 0.5845 0.6080; ...
              0.5751 0.5716 0.5827 0.6017]; 
b=bar(sAUC);
grid on;
ylim([0.55 0.68]);
set(gca, 'xticklabel', {'fine-tune on CAT2000','fine-tune on Invalid Set'});
legend('SAM-VGG','SAM-ResNet','ML-Net','OpenSALICON');
%xlabel('Angle:degree');
ylabel('sAUC score');
%title('Angle');
set(gca,'FontSize',15);
%line([0:1],[0.68,0.68],'linestyle','--');
line([1:2],[0.6754,0.6754],'linestyle','--','linewidth',4,'color','r');

figure;
CC = [0.7551 0.7584 0.5727 0.5379; ...
              0.7268 0.7508 0.5546 0.5341]; 
b=bar(CC);
grid on;
ylim([0.50 0.95]);
set(gca, 'xticklabel', {'fine-tune on CAT2000','fine-tune on Invalid Set'});
%legend('SAM-VGG','SAM-ResNet','ML-Net','OpenSALICON');
%xlabel('Angle:degree');
ylabel('CC score');
%title('Angle');
set(gca,'FontSize',15);
line([1:2],[0.9134,0.9134],'linestyle','--','linewidth',4,'color','r');

figure;
NSS = [1.9231 1.8984 1.4433 1.3662; ...
              1.8291 1.8880 1.3898 1.3434]; 
b=bar(NSS);
grid on;
ylim([1.20 2.30]);
set(gca, 'xticklabel', {'fine-tune on CAT2000','fine-tune on Invalid Set'});
%legend('SAM-VGG','SAM-ResNet','ML-Net','OpenSALICON');
%xlabel('Angle:degree');
ylabel('NSS score');
%title('Angle');
set(gca,'FontSize',15);
line([1:2],[2.2134,2.2134],'linestyle','--','linewidth',4,'color','r');

figure;
KL = [0.9949 1.0745 0.7949 0.7793; ...
              1.6512 1.7643 1.1768 0.7919]; 
b=bar(KL);
grid on;
ylim([0.0 2.00]);
set(gca, 'xticklabel', {'fine-tune on CAT2000','fine-tune on Invalid Set'});
%legend('SAM-VGG','SAM-ResNet','ML-Net','OpenSALICON');
%xlabel('Angle:degree');
ylabel('KL score');
%title('Angle');
set(gca,'FontSize',15);

figure;
AUCBorji = [0.8406 0.8423 0.7652 0.7978; ...
              0.8233 0.8263 0.7594 0.7918]; 
b=bar(AUCBorji);
grid on;
ylim([0.70 0.86]);
set(gca, 'xticklabel', {'fine-tune on CAT2000','fine-tune on Invalid Set'});
%legend('SAM-VGG','SAM-ResNet','ML-Net','OpenSALICON');
%xlabel('Angle:degree');
ylabel('AUC-Borji score');
%title('Angle');
set(gca,'FontSize',15);

figure;
SIM = [0.6507 0.6517 0.5442 0.5194; ...
              0.6316 0.6490 0.5402 0.5065]; 
b=bar(SIM);
grid on;
ylim([0.48 0.68]);
set(gca, 'xticklabel', {'fine-tune on CAT2000','fine-tune on Invalid Set'});
%legend('SAM-VGG','SAM-ResNet','ML-Net','OpenSALICON');
%xlabel('Angle:degree');
ylabel('SIM score');
%title('Angle');
set(gca,'FontSize',15);

