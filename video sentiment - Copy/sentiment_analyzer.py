import cv2
from deepface import DeepFace


def analyze_video(video_path):
    cap=cv2.VideoCapture(video_path)
    emotions_count={'angry':0,'disgust':0,'fear':0,'happy':0,'sad':0,'surprise':0,'neutral':0}
    frame_count=0


    while cap.isOpened():
        ret,frame=cap.read()
        print("Frame captured")
        if not ret:
            break

        if frame_count % 30==0:
            try:
                print("calling deepface")
                result=DeepFace.analyze(frame,actions=['emotion'],enforce_detection=False,detector_backend='retinaface')
                print(result)

               
                if isinstance(result, list) and len(result) > 0:
                    dom = result[0]['dominant_emotion']
                    emotions_count[dom] += 1
                elif isinstance(result, dict):
                    dom = result['dominant_emotion']
                    emotions_count[dom] += 1
                else:
                    continue
            except Exception as e:
                print("DeepFace Error:", e)
        frame_count = frame_count+1
    cap.release()


    total_analyzed=sum(emotions_count.values())
    if total_analyzed ==0:
            return"no faces found"
    report="video Sentiment Breakdown:\n\n"
    for emotions, count in emotions_count.items():
        if count>0:
                percentage=(count/ total_analyzed)*100
                report +=f"-{emotions.capitalize()}:{percentage:.2f}%\n"
    return report


