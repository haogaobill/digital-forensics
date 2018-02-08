import sys

filename = sys.argv[1]
offset = 0
with open(filename, 'rb') as f:

    def print_able(x):
        if (x >= 0x20 and x <= 0x7E) and chr(x) != '\n':
            return chr(x)
        else:
            return '.'

    while 1:
        byte_set = f.read(16)
        if not byte_set:
            if(offset != 0):
                print('{:08x}'.format(offset))
            break
        
        offset_hex = '{:08x}'.format(offset)
        hex_1 = ' '.join(['{:02x}'.format(x) for x in byte_set[0:8]])
        hex_2 = ' '.join(['{:02x}'.format(x) for x in byte_set[8:16]])
        hex = '  '.join([hex_1, hex_2])
        if(len(hex) < 48):
            hex = hex.ljust(48)
        printable =''.join(list(map(print_able, byte_set)))
        printable = '|' + printable + '|'
        line = '  '.join([offset_hex, hex, printable])
        print(line)
        offset = offset + len(byte_set)


