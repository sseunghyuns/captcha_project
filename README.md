# captcha_project
## Opencv 라이브러리를 활용하여 이미지 속의 수식 추출하기


captcha_project는  유튜버 '동빈나'님의 [Python 데이터 분석과 이미지 처리] 영상을 참고하여 진행했습니다. `OpenCV`를 사용하여 이미지 처리하는 방법들을 공부했습니다.   
* 이미지 속의 숫자들을 정확히 분류하기 위해 KNN모델을 적용
* 이미지 속의 수식을 문자열 형태로 추출하여 자동으로 연산하는 알고리즘을 구성


# 파일 설명
## 1. utils.py
이미지 및 이미지 속에서 추출한 문자를 처리하는 함수들이 포함되어있습니다. 


## 2. make_train_data.py
이미지를 추출하여 train data를 직접 만들어내는 함수가 포함되어있습니다.

## 3. knn_trainer.py
knn모델을 적용하기 위해 데이터를 전처리하는 함수가 포함되어있습니다. 전처리된 데이터는 trained.npz에 저장했습니다.

## 4. run.py
knn모델 학습, 새로운 데이터에 적용하여 수식을 풀어내는 함수, 도출된 답을 사이트에 자동으로 제출하게 하는 자동화 함수가 포함되어있습니다. 마지막 단계에서 실행하는 파일입니다.

# 참고
나동빈 - [Python 데이터 분석과 이미지 처리]

https://www.youtube.com/watch?v=V8Lpf3WCZ4g&list=PLRx0vPvlEmdBx9X5xSgcEk4CEbzEiws8C
