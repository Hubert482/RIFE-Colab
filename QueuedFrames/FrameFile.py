import cv2


class FrameFile:
    filePath: str = None
    imageData = None

    def __init__(self, filePath: str):
        self.filePath = filePath

    def __str__(self):
        return self.filePath

    def setImageData(self, imageData):
        self.imageData = imageData

    def getImageData(self):
        return self.imageData

    def saveImageData(self):
        cv2.imwrite(self.filePath, self.imageData)

    def loadImageData(self):
        self.imageData = cv2.imread(self.filePath)