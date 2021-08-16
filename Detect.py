# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 14:44:19 2021

@author: Adarsh
"""

from tensorflow.keras.models import load_model
import tensorflow as tf
import autokeras as ak
import numpy as np

model = load_model("Path_to_pretrained_model", custom_objects=ak.CUSTOM_OBJECTS)

testing_image = data #Load Single Image or a dataset 
testing_image = np.asarray(testing_image)

if testing_image.ndim == 4:
    pred = model.predict(testing_image)
    
elif testing_image.ndim == 3:
    testing_image = tf.expand_dims(testing_image, axis= 0)
    pred = model.predict(testing_image)
    
 
pred = np.rint(pred)
pred[pred<0] = 0
pred[pred == -0] = 0 

pred = np.array(["%.f" % x for x in pred.reshape(pred.size)])
pred = pred.reshape(pred.shape)

for items in pred:
    if items[0] == '0' :
        items[0] = 'P'
    elif items[0] == '1':
        items[0] = 'R'
        
print(pred)



