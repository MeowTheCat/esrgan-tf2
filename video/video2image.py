import cv2
vidcap = cv2.VideoCapture('/Users/miaowu/Downloads/3guo_2.mp4')
success, image = vidcap.read()
count = 0
while success:
  count += 1
  success, image = vidcap.read()
  if count % 100 !=0 :
    continue
  cv2.imwrite("/Users/miaowu/Downloads/3guo_img_2/frame%d.jpg" % count, image)     # save frame as JPEG file
  print('Read a new frame: ', success)
