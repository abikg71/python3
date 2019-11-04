clc
clear all
close all
% Abinet Kenore
%Friday October 25, 2019 10:45 to 1159PM
%%%%%%%%%%%%%%%% enhancement %%%%%%%%%%%%%%%%%%%%%%
 %im_pro =imread('./Dataset/enrolling/ID01_001.bmp');
 %im_en=histeq(im_pro);
%%%%%%%%%%%%%%%%%%%%% TRAINING %%%%%%%%%%%%%%%%%%%%
imlist=dir('./Dataset/enrolling/*.bmp');
im =imread(['./Dataset/enrolling/',imlist(1).name]);

[r,c]=size(im);
num_im=length(imlist);
num_p=num_im/5;
x=zeros((r*c),num_p);
im_vector=zeros(r*c,num_im);
Mec=zeros(r*c,1);
index=zeros;
index2=zeros;
match=zeros(1,30); %Changed from 10 to 30
match2=zeros(1,30);
cmc=zeros(0,30);
cmc2=zeros(1,30);
%%%%%% convert all images to vector %%%%%%
for i=1:num_im
    im =imread(['./Dataset/enrolling/',imlist(i).name]);
    im_vector(:,i)=reshape(im',r*c,1);
end
%%%%%%%%%%%%%% to get xi and Me%%%%%%%%%%%%%%%%
j=1; %xi for five images # Modification
for i=1:5:(num_im-4)
x(:,j)=(im_vector(:,i)+im_vector(:,i+1)+im_vector(:,i+2)+im_vector(:,i+3)+im_vector(:,i+4))/5;
Mec(:,1)=Mec(:,1)+im_vector(:,i)+im_vector(:,i+1)+im_vector(:,i+2)+im_vector(:,i+3)+im_vector(:,i+4);
j=j+1;
end
Me=Mec(:,1)./num_im;
%%%%%%%%%%%%%% to get big A %%%%%%%%%%%%%%%%%%%%
for i=1:num_p
a(:,i)=x(:,i)-Me;
end
%%%%%%%%%%%%%% to get eig of A'*A (P2) %%%%%%%%%
ata = a'*a;
[V, D] = eig(ata);
p2 = [];
for i = 1 : size(V,2)
    if( D(i,i)>1 )
        p2 = [p2 V(:,i)];
    end
end
%%%weight of the training data projected into eigen space%%%%%
wta=p2'*ata; % A*P2= P;  P'*A =Wt_A

%%%%%%%%%%%%%% to get the Eigenfaces %%%%%%%%%%%%
ef =a*p2;  %here is the P you need to use in matching
[rr,cc]=size(ef);
for i=1:cc
eigim_t=ef(:,i);
eigface(:,:,i)=reshape(eigim_t,r,c);
figure,imagesc(eigface(:,:,i)');
axis image;axis off; colormap(gray(256));
title('Eigen Face Image','fontsize',10);
end
%%%%%%%%%%%%%%%%%%%%%%%  TESTING  %%%%%%%%%%%%%%%%%%%%%%%%
imlist2=dir('./Dataset/testing/*.bmp');
num_imt=length(imlist2);
imt_vector=zeros(r*c,num_imt);
%%%%%% convert all test images to vector %%%%%%
for i=1:num_imt
im =imread(['./Dataset/testing/',imlist2(i).name]);
imt_vector(:,i)=reshape(im',r*c,1);
%%%%% get B=y-me %%%%%%%
b(:,i)=imt_vector(:,i)-Me;  %% bi=imt_vector(i)-Me;
wtb=ef'*b(:,i);  %%wtb=P'*bi;
for ii=1:num_p   %% weight compare wtb and wta(i)
 eud(ii)=sqrt(sum((wtb-wta(:,ii)).^2));
end
[cdata, index(i)]=min(eud);  %% find minimum eud's index
%%%%%%%%%%%%%%%%%%%%%%%  RESULT  %%%%%%%%%%%%%%%%%%%%%%%%
%%% right result by observation is 1 1 2 3 4 %%%%%
% see the pattern
rresult=[1 1 1 1 1 2 2 2 2 2 3 3 3 3 3 4 4 4 4 4 5 5 5 5 5 6 6 6 6 6 7 7 7 7 7 8 8 8 8 8 9 9 9 9 9 ...
    10 10 10 10 10 11 11 11 11 11 12 12 12 12 12 13 13 13 13 13 14 14 14 14 14 15 15 15 15 15 16 16 16 16 16 17 17 17 17 17 18 18 18 18 18 ...
    19 19 19 19 19 20 20 20 20 20 21 21 21 21 21 22 22 22 22 22 23 23 23 23 23 24 24 24 24 24 25 25 25 25 25 26 26 26 26 26 27 27 27 27 27 ...
    28 28 28 28 28 29 29 29 29 29 30 30 30 30 30 31 31 31 31 31 32 32 32 32 32 33 33 33 33 33 34 34 34 34 34 35 35 35 35 35 36 36 36 36 36 ...
    37 37 37 37 37 38 38 38 38 38 39 39 39 39 39 40 40 40 40 40 41 41 41 41 41 42 42 42 42 42 43 43 43 43 43];
%%%%%%%%%%%%%%% CMC calculation %%%%%%%
if index(i)==rresult(i)
    match(1)=match(1)+1;%%%%%%%first rank matching number
else
        [svals,idx]=sort(eud(:));
        index2(i)=idx(2);
        if index2(i)==rresult(i)
            match(2)=match(2)+1;%%%%%%%second rank matching number
        end
        % Copy past for 29X
        if idx(3)==rresult(i)
            match(3)=match(3)+1;
        end
        if idx(4)==rresult(i)
            match(4)=match(4)+1;
        end
        if idx(5)==rresult(i)
            match(5)=match(5)+1;
        end
        if idx(6)==rresult(i)
            match(6)=match(6)+1;
        end
        if idx(7)==rresult(i)
            match(7)=match(7)+1;
        end
        if idx(8)==rresult(i)
            match(8)=match(8)+1;
        end
        if idx(9)==rresult(i)
            match(9)=match(9)+1;
        end
        if idx(10)==rresult(i)
            match(10)=match(10)+1;
        end
        if idx(11)==rresult(i)
            match(11)=match(11)+1;
        end
        if idx(12)==rresult(i)
            match(12)=match(12)+1;
        end
        if idx(13)==rresult(i)
            match(13)=match(13)+1;
        end
        if idx(14)==rresult(i)
            match(14)=match(14)+1;
        end
        if idx(15)==rresult(i)
            match(15)=match(15)+1;
        end
        if idx(16)==rresult(i)
            match(16)=match(16)+1;
        end
        if idx(17)==rresult(i)
            match(17)=match(17)+1;
        end
        if idx(18)==rresult(i)
            match(18)=match(18)+1;
        end
        if idx(19)==rresult(i)
            match(19)=match(19)+1;
        end
        if idx(20)==rresult(i)
            match(20)=match(20)+1;
        end
        if idx(21)==rresult(i)
            match(21)=match(21)+1;
        end
        if idx(22)==rresult(i)
            match(22)=match(22)+1;
        end
        if idx(23)==rresult(i)
            match(23)=match(23)+1;
        end
        if idx(24)==rresult(i)
            match(24)=match(24)+1;
        end
        if idx(25)==rresult(i)
            match(25)=match(25)+1;
        end
        if idx(26)==rresult(i)
            match(26)=match(26)+1;
        end
        if idx(27)==rresult(i)
            match(27)=match(27)+1;
        end
        if idx(28)==rresult(i)
            match(28)=match(28)+1;
        end
        if idx(29)==rresult(i)
            match(29)=match(29)+1;
        end
        if idx(30)==rresult(i)
            match(30)=match(30)+1;
        end
end
end
for i=1:30  %% The CMC of the 1st to 10th rank matching number
cmc(i)=sum(match(1:i))/num_imt;
end
figure,plot(cmc);title('CMC curve');
