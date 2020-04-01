from keras.models import load_model
from keras.optimizers import Adam
from keras.preprocessing import image
import  numpy as np
model =  load_model('data//epochs_049-val_acc_0.999.hdf5')
import cv2
model.summary()
opt =Adam(lr = 1e-3,decay=1e-3/25)
model.compile(loss='binary_crossentropy',metrics=['accuracy'],optimizer=opt)

def predict_image(img):
#img = image.load_img('005591af-575a-422a-a457-720d9d3b0283___CREC_HLB 7298.jfif', target_size=(64, 64))
    print("Inside")
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    images = np.vstack([x])
    classes = model.predict_classes(images, batch_size=10)
    print (classes)
    labels = np.load('data//labels.npy')
    final = labels[classes]
    final = final[0]
    if(final[-7:]=='healthy'):
        output = 'Healthy Leaf'
    else:
        output = final
    print(output)
    return output