#open(file,mode:r,w,a,rt,rb,at,ab,wt,wb,UTF8,UTF16)
import sys

try:
    f= open('data.txt',mode='rt',encoding='utf-8')
    print(type(f))
    for line in f:
        sys.stdout.write(line)

finally:
    f.close()