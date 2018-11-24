import base64, io

def incPos(i, j, s):
    j = (j + 1) % s[1]
    if j % s[1] == 0:
        return (i + 1, j)
    return (i, j)

# dataToImage - takes user data and puts it into the image data
# imgdata - base64 jpg image data
# data - list of data to encode
def dataToImage(imgData, userData):
    # imgData -> pixel colour values
    pic = Image.open(io.BytesIO(imgData))
    pa = pic.load()
    paSize = pic.size

    i = 0
    j = 0
    count = 0

    # loop through userData
    for item in userData:
        # loop through data item
        for x in item:
            # int value of character
            c = ord(x)

            c1 = c >> 6
            c2 = (c & 0b0110000) >> 4
            c3 = (c & 0b0001100) >> 2
            c4 = (c & 0b0000011)

            cs = [c1, c2, c3, c4]

            if count == 0:
                pa[i,j] = ((pa[i,j][0] & 0b11111100) + c1,
                           (pa[i,j][1] & 0b11111100) + c2,
                           (pa[i,j][2] & 0b11111100) + c3)

                (i, j) = incPos(i, j, paSize)

                pa[i,j] = ((pa[i,j][0] & 0b11111100) + c4,
                           pa[i,j][1],
                           pa[i,j][2])
            

            elif count == 1:
                pa[i,j] = (pa[i,j][0],
                           (pa[i,j][1] & 0b11111100) + c1,
                           (pa[i,j][2] & 0b11111100) + c2)

                (i, j) = incPos(i, j, paSize)

                pa[i,j] = ((pa[i,j][0] & 0b11111100) + c3,
                           (pa[i,j][1] & 0b11111100) + c4,
                           pa[i,j][2])
            

            elif count == 2:
                pa[i,j] = (pa[i,j][0],
                           pa[i,j][1],
                           (pa[i,j][2] & 0b11111100) + c1)

                (i, j) = incPos(i, j, paSize)

                pa[i,j] = ((pa[i,j][0] & 0b11111100) + c2,
                           (pa[i,j][1] & 0b11111100) + c3,
                           (pa[i,j][2] & 0b11111100) + c4)

