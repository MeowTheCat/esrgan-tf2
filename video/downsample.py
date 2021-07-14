from modules.utils import imresize_np
import os
import cv2

def create_lr_hr_pair(raw_img_path, scale, hr_path, lr_path):
    for img_name in os.listdir(raw_img_path):
        if not img_name.endswith('.png'):
            continue
        raw_img = cv2.imread(os.path.join(raw_img_path, img_name))
        lr_h, lr_w = raw_img.shape[0] // scale, raw_img.shape[1] // scale
        hr_h, hr_w = lr_h * scale, lr_w * scale
        hr_img = raw_img[:hr_h, :hr_w, :]
        lr_img = imresize_np(hr_img, 1 / scale)
        cv2.imwrite(os.path.join(hr_path, img_name), hr_img)
        cv2.imwrite(os.path.join(lr_path, img_name), lr_img)


create_lr_hr_pair("/Users/miaowu/Downloads/720pp", 4, "/Users/miaowu/Downloads/hr", "/Users/miaowu/Downloads/lr" )