import numpy as np
import cv2
import utils
import requests
import shutil
import time


FILE_NAME = 'trained.npz'

with np.load(FILE_NAME) as data:
    train = data['train']
    train_labels = data['train_labels']

# knn model
knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels) # cv2.ml.ROW_SAMPLE : 배열의 길이을 전체 길이 1로 간주한다는 것

def check(test, train, train_labels):
    # 가장 가까운 K개의 글자를 찾아 어떤 숫자에 해당하는지.
    ret, result, neighbors, dist = knn.findNearest(test, k=1) # test 데이터와 가장 가까운 데이터 1개를 찾아라. 여기선 모든 숫자가 동일한 크기, 모양을 갖고 있기 때문에 가장 가까운 이미지 1개만 찾아도 분류 가능.
    return result


# 학습된 모델로 테스트 하기(테스트 결과 확인)
def get_result(file_name):
    image = cv2.imread(file_name)
    chars = utils.extract_chars(image)
    result_string = "" # 문자를 저장할 변수

    for char in chars:
        matched = check(utils.resize20(char[1]), train, train_labels) # char[1] : 하나하나의 숫자 이미지 array값.
        if matched < 10: # 숫자인 경우
            result_string += str(int(matched))
            continue # 숫자면 추가하고 다시 체크 반복.
        if matched ==10:
            matched  = '+'
        elif matched ==11:
            matched = '-'
        elif matched == 12:
            matched = '*'
        result_string += matched
    return result_string

print(get_result('2.png')) # 결과 확인



# 답 제출 자동화
host = 'http://localhost:10000'
url = '/start'

 # target_images 라는 폴더 생성
with requests.Session() as s:
    answer = ''

    for i in range(0,30):
      start_time = time.time()
      params = {'ans':answer}

      # 정답을 파라미터에 달아서 전송하여, 이미지 경로를 받아온다.
      response = s.post(host + url, params)
      print('Server Return: ' + response.text)
      if i ==0:
        returned = response.text
        image_url = host + returned
        url = '/check'
      else:
        returned = response.json()
        image_url = host + returned['url']
      print('Problem ' + str(i) + ': ' + image_url)

      # 특정한 폴더에 이미지 파일을 다운로드 받는다.
      response = s.get(image_url, stream = True)
      target_image = './target_images/' + str(i) + '.png'

      with open(target_image, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
      del response

     # 다운로드 받은 이미지 파일을 분석하여 답 도출.
      answer_string = get_result(target_image)
      print('String: ' + answer_string)
      answer_string = utils.remove_first_0(answer_string)
      answer = str(eval(answer_string))
      print('Answer: ' + answer)
      print('--- %s seconds ---' % (time.time() - start_time))


