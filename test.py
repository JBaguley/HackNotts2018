from PIL import Image

pa = Image.open("door.jpg")
pic = pa.load()



c = ord('c')
print(pa.size)

r =c >> 6
g =(c & 0b0110000)>>4
b =(c & 0b0001100)>>2
r2 =(c & 0b0000011)


pic[0,0] = ((pic[0,0][0] & 0b11111100) + r,
           (pic[0,0][1] & 0b11111100) + g,
           (pic[0,0][2] & 0b11111100) + b)

