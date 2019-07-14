import cv2
import time
from fire_opencv import start

# ip 카메라로부터 영상받을 준비
def Setting():
    rtsp_url = 'rtsp://210.119.87.226:554/video1'
    video = cv2.VideoCapture(rtsp_url)
    time.sleep(0.25)
    video.set(cv2.CAP_PROP_FPS, 10)

    return video

# 카메라로 부터 받은 자원free
def free():
    capture.release()  
    cv2.destroyAllWindows()

#화재 규모 판단
def confirm_scale(result):

    #return 1은 화재규모가 큼
    #return 0은 화재규모가 작음
    if(result > 5):
        return 1
    else:
        return 0

#def trans_to_server(result):
    #서버로 화재규모 알림 전송
#    url="http://210.119.87.228:3000"
#    data={'msg':result}
#    headers={'Content-type':'application/json','Accept':'text/plain'}
#    requests.post(url,data=json.dumps(data),headers=headers)

# 화면 스트리밍
def Streaming(video):
    while(True):
        #영상으로부터 화면 불러오기
        _, frame = video.read()

        #frame을 딥러닝 통해 화재여부 검사
        result = start(frame)
        #화재 규모 판단
        result =confirm_scale(result)
        #서버로 전송
       # trans_to_server(result)

        # 영상띄우기
        cv2.imshow('HA-20SW', frame)
        cv2.waitKey(1) 

#1. 화면영상 세팅
#2. 스트리밍 서비스
#3. 자원 해제
def main():
    video = Setting()
    Streaming(video)
    free()

# Main실행
if __name__ == "__main__":
    main()
    
