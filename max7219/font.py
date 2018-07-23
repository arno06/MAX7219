
class HeightPixelFont:
    chars = {
        'a':[46,42,28],
        'b':[62,10,12],
        'c':[6,10, 10],
        'd':[14,10,60],
        'e':[28,42,58],
        'f':[30,40,40],
        'g':[26,42,60],
        'h':[62,8,6],
        'i':[46],
        'j':[1,47],
        'k':[62,8,22],
        'l':[60,2],
        'm':[30,16,12,16,14],
        'n':[30,16,14],
        'o':[30,18,14],
        'p':[15, 20, 8],
        'q':[8,20,15],
        'r':[14,16],
        's':[18,42,36],
        't':[60,10,10],
        'u':[28,2,30],
        'v':[28,2,28],
        'w':[28,2,4,2,28],
        'x':[54,8,54],
        'y':[29,5,30],
        'z':[38,42,42,50],
        '1':[66,254,2],
        '2':[70,138,146,98],
        '3':[68,146,146,108],
        '4':[48,80,144,254],
        '5':[114,146,146,140],
        '6':[124,146,146,12],
        '7':[142,144,160,192],
        '8':[108,146,146,108],
        '9':[96,146,146,124],
        '0':[124,130,130,124],
        ':':[40],
        ' ':[0]
    }

    bit_values = [1,2,4,8,16,32,64,128]


    def from_string(str):
        canvas = []
        for i, c in enumerate(str):
            if i > 0:
                canvas.append([0 for j in range(8)])
            d = HeightPixelFont.chars[c]
            if d is None:
                print("HeightPixelFont missing char : "+c)
                continue
            for k in d:
                row=[]
                for value in HeightPixelFont.bit_values:
                    v=0
                    if k&value==value:
                        v=1
                    row.append(v)
                canvas.append(row)
        return canvas
