from keras.preprocessing.image import ImageDataGenerator, img_to_array, array_to_img, load_img
from matplotlib import pyplot

generator = ImageDataGenerator(
    rotation_range=45,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.6,
    channel_shift_range=50,
    zoom_range=0.5,
    fill_mode='nearest',
    horizontal_flip=True
)

img = load_img('cat.jpg')

x = img_to_array(img)
xShape = x.shape
x = x.reshape((1,) + xShape)

i = 0
images = []

for image in generator.flow(x, batch_size=1):
    images.append(image.reshape(xShape))
    i += 1
    if i > 9:
        break

for j in range(9):
    pyplot.subplot(330 + 1 + j)
    pyplot.imshow(array_to_img(images[j]))

pyplot.show()
