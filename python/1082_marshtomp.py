'''
遍历一趟，若以字母m(M)开头的子字符串与marshtomp不区分大小写相同，
则记录下其位置，最后将相应子字符串用fjxmlhx替换。
'''
import sys

def isSame(str1, str2):
    for i in xrange(len(str1)):
        # 不区分大小写相同
        sub = ord(str1[i]) - ord(str2[i])
        if sub not in {-32, 0, 32}:
            return False
    return True

ori = "marshtomp"
rep = "fjxmlhx"

for line in sys.stdin:
    line = line[:-1]

    if len(line) < len(ori):
        print(line)
    else:
        l = []
        i = 0
        while i < len(line)-len(ori)+1:
            if line[i] == 'm' or line[i] == 'M':
                if isSame(line[i:i+len(ori)], ori):
                    # 记录下起始位置
                    l.append(i)
                    i += len(ori)
                else:
                    i += 1
            else:
                i += 1

        if len(l) == 0:
            print(line)
        else:
            repLine = ""
            for j in xrange(len(l)):
                # 其余字符，包括开头，中间，结尾
                if j == 0:
                    repLine += line[:l[j]]
                else:
                    repLine += line[l[j-1]+len(ori):l[j]]
                repLine += rep
                if j == len(l)-1:
                    repLine += line[l[j]+len(ori):]
            print(repLine)
