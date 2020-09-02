import cv2
import numpy as np
import re



# 특정한 색상의 모든 단어가 포함된 이미지를 추출하는 함수.
BLUE = 0
GREEN = 1
RED = 2

def get_chars(img, color):
    other_color_1 = (color + 1) % 3
    other_color_2 = (color + 2) % 3 # 다른 색상 값 저장

    c = img[:, :, other_color_1] == 255
    img[c] = [0, 0, 0]

    c = img[:, :, other_color_2] == 255
    img[c] = [0, 0, 0]

    c = img[:, :, color] <170 # 다른 두 색상이 겹치는 부분도 제거
    img[c] = [0, 0, 0]

    c = img[:, :, color] != 0
    img[c] = [255, 255, 255] # 해당 색은 흰색으로 변환

    return img




# 전체 이미지 추출
def extract_chars(img):
    chars = []
    colors = [BLUE, GREEN, RED]

    for color in colors:
        img_from_one_color = get_chars(img.copy(), color)
        img_gray = cv2.cvtColor(img_from_one_color, cv2.COLOR_BGR2GRAY) # threshold 적용을 위한 전처리

        ret, threshold = cv2.threshold(img_gray, 127, 255, 0) # ret =127, threshold : 임계점 처리한 뒤 이미지 픽셀값들.
        contours, b = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # contours = 찾은 x,y 좌표
        # RETR_EXTERNAL 옵션으로 숫자의 외각을 기준으로 분리

        for contour in contours:
            # 추출된 이미지 크기가 50 이상인 경우만 실제 문자 데이터인 것으로 파악
            area = cv2.contourArea(contour)

            if area > 50:
                x, y, width, height = cv2.boundingRect(contour)
                roi = img_gray[y:y + height, x:x + width] # roi = region of interest. Slicing 연산으로 가져옴. 숫자에 해당하는 부분만 가져온다.
                chars.append((x, roi))
    chars = sorted(chars, key = lambda char : char[0]) # 좌표별로 정렬. chars[0]은 x 좌표를 의미함. 따라서 x좌표 순서대로 이미지를 정렬하겠다는 의미.
    return chars




# 이미지를 20 X 20 크기로 정규화.
def resize20(img):
    resize = cv2.resize(img, (20,20))
    return resize.reshape(-1,400).astype(np.float32) # Flatten 작업




# 문자 처리 함수
def remove_first_0(string):
    temp = []
    for i in string:
        if i == '+' or i == '-' or i == '*':
            temp.append(i)
    split = re.split('\*|\+|-', string)  # 정규표현식으로 split
    i = 0
    temp_count = 0
    result = ""
    for a in split:
        a = a.lstrip('0')  # 왼쪽 0 제거
        if a == '':  # 0밖에 없었으면 0으로 저장
            a = '0'
        result += a
        if i < len(split) - 1:  # split된 문자 길이 동안
            result += temp[temp_count]  # split된 문자 하나 끝날때마다 부호 추가
            temp_count += 1
        i += 1  # 다음 문자
    return result

