import cv2


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

    newImg = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT,
                                value=color)
    return newImg
