import cv2
import os


def resizeImage(img, desiredSize):
    newImg = cv2.resize(img, (desiredSize, desiredSize))
    return newImg


def resizeImageKeepRatio(img, desiredSize):
    oldSize = img.shape[:2]  # wysokosc x szerokosc

    ratio = float(desiredSize) / max(oldSize)
    newSize = tuple([int(x * ratio) for x in oldSize])

    img = cv2.resize(img, (newSize[1], newSize[0]))  # szerokosc x wysokosc

    deltaX = desiredSize - newSize[1]
    deltaY = desiredSize - newSize[0]

    top = deltaY // 2
    bottom = deltaY - (deltaY // 2)
    left = deltaX // 2
    right = deltaX - (deltaX // 2)

    color = [0, 0, 0]

    newImg = cv2.copyMakeBorder(img, top, bottom, left, right,
                                cv2.BORDER_CONSTANT, value=color)
    return newImg


outputDir = "dataset"
desiredSize = 150


path = os.getcwd()
directories = [d for d in os.listdir(path) if os.path.isdir(d)]

# tworzenie folderów dla obrazów wyjściowych
if not os.path.exists(outputDir):
    os.makedirs(outputDir)
    for directory in directories:
        os.makedirs(f"{outputDir}/{directory}")

i = 0

for directory in directories:
    for file in os.listdir(f"{path}/{directory}/"):
        if file.endswith((".jpg", ".png")):
            img = cv2.imread(f"{path}/{directory}/{file}", cv2.IMREAD_COLOR)
            img = resizeImage(img, 100)
            cv2.imwrite(f"{outputDir}/{directory}/{directory}_{i}.jpg",
                        img, [cv2.IMWRITE_JPEG_QUALITY, 90])
            i += 1
print("Koniec")
