#encoding: utf-8
'''
Getting started Keras
'''

'''
Kerasには2つのレイヤー構成方法がある。
それらは、SequentialとGraphと呼ばれる。
順番にモジュールを見ていこう。
'''
from keras.models import Sequential
model = Sequential()

'''
Sequentialのモデルには、レイヤーを簡単に追加できる
'''
from keras.layers.core import Dense, Activation
model.add(Dense(output_dim=64, input_dim=100, init="glorot_uniform"))
