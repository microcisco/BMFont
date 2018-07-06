from PIL import Image
import os

dataPath = './pics/'
s = input("输入原始图片文件夹")
if os.path.isdir(s):
    dataPath = s + '/'
else:
    print("目标不是文件夹将使用当前目录下的pics文件夹")
datas = list()
for i in os.listdir(dataPath):
    datas.append(Image.open(dataPath + str(i)))

maxWidth = 0
maxHeight = 0
for i in datas:
    if i.size[0] > maxWidth:
        maxWidth = i.size[0]
    if i.size[1] > maxHeight:
        maxHeight = i.size[1]

newImg = Image.new("RGBA", (maxWidth * len(datas), maxHeight), (0, 0, 0, 0))

lastPos = 0
for im in datas:
    newImg.paste(im, (lastPos * maxWidth + int(maxWidth / 2 - im.size[0] / 2), int(maxHeight / 2 - im.size[1] / 2)))
    lastPos += 1

newImg.save("./out.png", "PNG")
