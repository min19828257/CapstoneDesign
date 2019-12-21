import cv2
from fire_detection import test
from PIL import Image


# 화면 감지 하기위한 사각형 범위 결
def cut_rectangle(cnt1,cnt2,cnt3,cnt4,img):
    img = cv2.rectangle(img, (cnt1, cnt2), (cnt3, cnt4), (0, 255, 0), 3)
    height = img.shape[0]
    width = img.shape[1]

    return img

# 이미지 resize()
def resize(img,cnt1,cnt2,cnt3,cnt4):

    dst = img.copy()
    dst = img[cnt4:cnt2,cnt3:cnt1]
    return dst

# 화재 확률값 측정
def calculate(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)

    result = test(img)
    return result

def start(image):
    img = image

    #cnt1,cnt3 (사각형 기준 오른쪽 왼쪽 선)
    #cnt2,cnt4 (사각형 기준 밑쪽 위쪽 선)
    cnt1 = 200 ;cnt3=0;cnt2=200;cnt4=0

    #화재 감지된 수
    count =  0
    
    while True:

        # 화면 detection 하기위한 사전 작업
        img = cut_rectangle(cnt1,cnt2,cnt3,cnt4,img)
        # 네트워크 들어가기 위한 사전 작업
        resize_img = resize(img,cnt1,cnt2,cnt3,cnt4)
        # 검사 화면 결과를 확률값으로 나타
        result = calculate(resize_img)

        if(result >0.5):
            cv2.imshow("df",resize_img)
            count +=1
            #cv2.waitKey(0)
        cv2.imshow('loop',image)


        # ESC키를 누를시 작업 종료
        k = cv2.waitKey(1)
        if k == 27:  # wait for ESC key to exit
            cv2.destroyAllWindows()
            break

        # 탐지사각형을 오른쪽으로 이동
        cnt3+=340;cnt1+=340

        if(cnt1 == 1900 and cnt3 == 1700 and cnt2 ==1000 and cnt4==800):
            print("끝났습니다.")
            return count
            

        if(cnt1 == 1900 and cnt3 == 1700):
            cnt1 = 200; cnt3=0; cnt2+=200; cnt4+=200
