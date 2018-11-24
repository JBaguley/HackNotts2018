import base64, io
from PIL import Image

usrdat = ["first_name", "last_name", "email", "dob"]

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
    pic = Image.open(io.BytesIO(base64.b64decode(imgData)))
    pa = pic.load()
    paSize = pic.size

    for i in range(1):
        for j in range(16):
            print(pa[i,j])
    print()


    i = 0
    j = 0
    count = 0

    # loop through userData
    for key in userData:
        item = userData[key]
        # loop through data item
        for x in item:
            # int value of character
            c = ord(x)

            c1 = c >> 6
            c2 = (c & 0b0110000) >> 4
            c3 = (c & 0b0001100) >> 2
            c4 = (c & 0b0000011)
            print (str(c1) + " " + str(c2) + " " + str(c3) + " " + str(c4))

            if count == 0:
                print("i: "+str(i)+" j: " +str(j) + " count: " + str(count))
                pa[i,j] = ((pa[i,j][0] & 0b11111100) + c1,
                           (pa[i,j][1] & 0b11111100) + c2,
                           (pa[i,j][2] & 0b11111100) + c3)
                print(pa[i,j])

                (i, j) = incPos(i, j, paSize)

                pa[i,j] = ((pa[i,j][0] & 0b11111100) + c4,
                            pa[i,j][1],
                            pa[i,j][2])

                count += 1
            

            elif count == 1:
                print("i: "+str(i)+" j: " +str(j) + " count: " + str(count))
                pa[i,j] = (pa[i,j][0],
                           (pa[i,j][1] & 0b11111100) + c1,
                           (pa[i,j][2] & 0b11111100) + c2)
                print(pa[i,j])

                (i, j) = incPos(i, j, paSize)

                pa[i,j] = ((pa[i,j][0] & 0b11111100) + c3,
                           (pa[i,j][1] & 0b11111100) + c4,
                            pa[i,j][2])
                count += 1
            

            else:
                print("i: "+str(i)+" j: " +str(j) + " count: " + str(count))
                pa[i,j] = (pa[i,j][0],
                           pa[i,j][1],
                           (pa[i,j][2] & 0b11111100) + c1)
                print(pa[i,j])
                (i, j) = incPos(i, j, paSize)

                pa[i,j] = ((pa[i,j][0] & 0b11111100) + c2,
                           (pa[i,j][1] & 0b11111100) + c3,
                           (pa[i,j][2] & 0b11111100) + c4)
                (i, j) = incPos(i, j, paSize)
                count = 0


    
    buffered = io.BytesIO()
    pic.save(buffered, format="BMP", icc_profile=pic.info.get('icc_profile'), quality=100, subsampling=0, progressive=True)
    pic.save("out.bmp", format="BMP", icc_profile=pic.info.get('icc_profile'), quality=100, subsampling=0, progressive=True)
    return base64.b64encode(buffered.getvalue())




def imageToData(imgData):
    pic = Image.open(io.BytesIO(base64.b64decode(imgData)))
    pa = pic.load()
    paSize = pic.size

    print()
    for i in range(1):
        for j in range(16):
            print(pa[i,j])

    userData = {}
    dataIndex = 0
    ch = 0
    st = ""
    dollars = 0
    count = 0
    
    for i in range(paSize[0]):
        for j in range(paSize[1]):
            for k in range(3):
                
                ch += (pa[i,j][k] & 0b11) << ((3-(count % 4)) * 2)
                if count < 16:
                    print("i: "+str(i)+" j: "+str(j)+" k: "+str(k))
                    print("bits: "+str(bin(ch)))

                if count % 4 == 3:          # end of char
                    if count < 16:
                        print("char: "+str(chr(ch)))
                        print()
                    if chr(ch) != '$':
                        if dollars != 0:    # not $$
                            dollars = 0
                            st += "$"
                        st += str(chr(ch))
                        
                    else:
                        if (dollars == 2):
                            userData[usrdat[dataIndex]] = st
                            st = ""
                            if dataIndex == 3:
                                return userData
                        else:
                            dollars += 1
                    ch = 0
                        
                count += 1

    return userData





