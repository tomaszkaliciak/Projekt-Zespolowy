from keras.preprocessing.image import img_to_array, load_img
from keras.models import load_model
import numpy as np

model = load_model('./model.h5')

paths = ['bocian.jpg', 'kot.jpg', 'pies.jpg']

for path in paths:
    image = load_img(path, target_size=(224, 224))
    image = img_to_array(image)
    image = image / 255
    image = np.expand_dims(image, axis=0)

    result = model.predict(image)
    print(result)  # 1 - ptak, 2 - kot, 3 - pies
