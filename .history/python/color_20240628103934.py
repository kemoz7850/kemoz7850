import getpixelcolor
while True:
    color= getpixelcolor.pixel(700, 408)
    print(color)
    if(color == (0, 172, 193) or color == (24, 193, 219)):
        break