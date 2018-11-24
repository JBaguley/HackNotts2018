from PIL import Image

pa = Image.open("test_tile.jpg").load()

for y in range(2):
    for x in range(2):
        print(pa[x,y])

c = ord('c')
print(bin(c))

r =c >> 6
g =(c & 0b0110000)>>4
b =(c & 0b0001100)>>2
r2 =(c & 0b0000011)

print(r)
print(b)
print(g)

pa[0,0] = ((pa[0,0][0]&0b11111100)+r,(pa[0,0][1]&0b11111100)+g,(pa[0,0][2]&0b11111100)+b)

print(pa[0,0])