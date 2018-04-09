from tqdm import tqdm
import numpy as np
import os
from random import shuffle
import cv2

TRAIN_PATH='train'
LR=1e-3

def label_img(img):
    word_label = img.split('_')
    word_label = word_label[0]
    if word_label == 'cat' : return [1, 0]
    elif word_label == 'dog' : return [0, 1]

def crate_train():
    train_data = []
    for img in tqdm(os.listdir(TRAIN_PATH)):
        label = label_img(img)
        path = os.path.join (TRAIN_PATH, img)
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        train_data.append([np.array(img), np.array(label)])       
    shuffle(train_data)
    np.save('train_data.npy', train_data)
    return train_data

train_data=crate_train()
print (data[0])

#if load
#train_data=np.load('train_data.npy')
