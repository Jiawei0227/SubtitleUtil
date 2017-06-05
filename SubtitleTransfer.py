# *_* coding:utf-8 *_*
import sys


class SubtitleTransfer:
    def __init__(self):
        pass

    def is_chinese(self, uchar):
        """判断一个unicode是否是汉字"""
        if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
            return True
        else:
            return False

    def transfer(self, filename):
        newfilename = filename.split('.')[0] + "_new.ass"
        file = open(filename, 'r')
        newfile = open(newfilename, 'w')

        for line in file.readlines():
            # print line.decode('utf-8')
            if line.startswith("Dialogue"):
                for char in line.decode('utf-8'):
                    if self.is_chinese(char):
                        line = line.replace(char.encode('utf-8'), '')
                newfile.write(line)

            else:
                newfile.write(line)

        print "Transfer Successfully."


if __name__ == '__main__':
    filename = sys.argv[1]
    s = SubtitleTransfer()
    s.transfer(filename)
