import cv2
vidcap = cv2.VideoCapture('/Users/miaowu/Downloads/old_sanguo.mp4')
frame_per_second = vidcap.get(cv2.CAP_PROP_FPS)
print(frame_per_second)
success, image = vidcap.read()
count = 0
while success:
    count += 1
    success, image = vidcap.read()
    if count % 100 != 0:
        continue
    cv2.imwrite(f"/Users/miaowu/Downloads/360pp/ss{count//100}.png", image)
    print(count//100)