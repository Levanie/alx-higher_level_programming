able File  16 lines (15 sloc)  340 Bytes

#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            else:
                result += (a**b)/i
        except:
            result = b + a
            break
    return result

#import dis
#dis.dis(magic_calculation)
