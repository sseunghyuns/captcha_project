import os
import numpy as np
import cv2
import utils



# training_data 폴더 생성 및 그 내부에 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 폴더 생성
# 파이참에서 코드 돌려서 직접 레이블링 하는 과정

image = cv2.imread("2.png")
chars = utils.extract_chars(image) # 이미지 내의 모든 숫자들을 추출

for char in chars:
        cv2.imshow('Image', char[1])
        input = cv2.waitKey(0)
        resized = cv2.resize(char[1], (20, 20))

        if input >= 48 and input <= 57: # 0~9 아스키코드 참고
                name = str(input - 48) # 파일 이름 지정하기
                file_count = len(next(os.walk('./training_data/' + name + '/'))[2]) # ('./training_data/5/', [], ['4.png', '2.png', '3.png', '1.png']) -> 이런 식으로 반환됨. [2] 인덱스 값은 현재 디렉토리에 저장된 이미지들
                cv2.imwrite('./training_data/' + str(input - 48) + '/' + str(file_count + 1) + '.png', resized) # 지정된 디렉토리에 이미지 저장
        elif input == ord('a') or input == ord('b') or input == ord('c'): # + : a, - : b, x : c를 입력. ord('a') = 97.
                name = str(input - ord('a') + 10) # 차례대로 10, 11, 12에 들어감.
                file_count = len(next(os.walk('./training_data/' + name + '/'))[2])
                cv2.imwrite('./training_data/' + name + '/' + str(file_count + 1) + '.png', resized)


