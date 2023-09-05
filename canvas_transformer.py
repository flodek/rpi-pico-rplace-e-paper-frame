import sys

def pictureEncoder(input, output, x, y, height, width):
    real_w = width
    f = open(input, 'rb')
    res = open(output, 'w')
    r = f.read(54)
    f.read(x * real_w * 3 + y * 3)
    print('read picture')
    for i in range (0, height):
        for j in range (0, width):
            r = f.read(3)
            if(r[0] == 239):
                res.write('0')
            elif(r[0] == 183):
                res.write('1')
            elif(r[0] == 74):
                res.write('2')
            elif(r[0] == 33):
                res.write('3')
            else:
                print("This isn't right: " + str(r[0]))
        f.read((real_w - (y + width)) * 3 + y *3)
    f.close()
    res.close()

if __name__=='__main__':
    if(len(sys.argv) != 5):
        print("please specify the following args: input_bmp_file output_hex_file height width")
    else:
        pictureEncoder(str(sys.argv[1]), str(sys.argv[2]), 0, 0, int(sys.argv[3]), int(sys.argv[4]))
