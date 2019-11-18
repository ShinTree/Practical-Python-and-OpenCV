import tensorflow as tf

data_train, data_test = tf.keras.datasets.mnist.load_data()
(image_train, labels_train) = data_train
(image_test, labels_test) = data_test

#from keras.datasets import mnist

#(X_train, y_class_train), (X_test, Y_class_test) = mnist.load_data()

#print("학습셋 이미지 수: %d 개" % (X_train.shape[0]))
#print("테스트셋 이미지 수: %d 개" % (X_test.shape[0]))
