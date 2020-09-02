import os
import cv2
import numpy as np

file_names = list(range(0,13))
train = []
train_labels = []
#print(file_names)
for file_name in file_names:
    path = './training_data/' + str(file_name) + '/' # ./training_data/0~9/ 지정
    file_count = len(next(os.walk(path))[2]) # 디렉토리 안에 있는 이미지 파일 개수 저장

    for i in range(1 , file_count+1):
        img = cv2.imread(path + str(i) + '.png') # 이미지 모두 불러오기
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 전처리
        train.append(gray) # 이미지 데이터 저장
        train_labels.append(file_name) # 레이블 저장


# train 데이터 전처리
x = np.array(train)
train  = x[:,:].reshape(-1,400).astype(np.float32) # 이미지 데이터 전처리 - Flatten 작업.
train_labels = np.array(train_labels)[:,np.newaxis] # 레이블 전처리. 배열 형태로 바꾸어 준다.


print(train.shape)
print(train_labels.shape)
np.savez('trained.npz', train=train, train_labels=train_labels) # 데이터 파일 형태로 저장