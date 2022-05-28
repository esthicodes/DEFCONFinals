import zlib

s = b'toorganizersd'
# using zlib.crc32() method
t = zlib.crc32(s)
  
print(t)

def all_combinations(x, len ):
    for char in range(65, 71):
        x[len] = chr(char)
        if (len>0):
            all_combinations( x, len - 1 );
        else:
            yield x

x = list(chr(65))*10
for y in all_combinations(x, 9):
    print(y)

#CRC32(the_intended_answer) == CRC32(your_string)
