# *_* coding:utf-8 *_*
import sys
import re


class SubtitleTransfer:
    """
        Transfer Subtitle
    """

    def __init__(self, filename, type):
        """
        filename: filepath
        type: Chinese/English/...

        """
        self.filename = filename
        spilts = filename.split('.')
        self.newFileName = spilts[0] + "_new." + filename.split('.')[len(spilts)-1]
        self.type = type

    def is_chinese(self, uchar):
        """
        judge whether unicode is Chinese
        """
        if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
            return True
        else:
            return False

    def del_Chinese_Ass(self):
        """
        del ass Chinese subtitle
        """
        file = open(self.filename, 'r')
        newfile = open(self.newFileName, 'w')

        for line in file.readlines():
            # print line.decode('utf-8')
            if line.startswith("Dialogue"):
                for char in line.decode('utf-8'):
                    if self.is_chinese(char):
                        line = line.replace(char.encode('utf-8'), '')
                newfile.write(line)

            else:
                newfile.write(line)
        print "Delete Chinese Subtitle Successfully."


    def del_Chinese_Srt(self):
        """
        del srt Chinese subtitle
        """
        file = open(filename, 'r')
        newFile = open(self.newFileName, 'w')

        for line in file.readlines():
            isChineseLine = False
            for char in line.decode("utf-8"):
                if self.is_chinese(char):
                    isChineseLine = True
                    break
            if not isChineseLine:
                newFile.write(line)
        print "Delete Chinese Subtitle Successfully."


    def transfer(self):
        """
        Transfer Main
        """
        if self.filename.endswith(".ass"):
            if self.type == "Chinese":
                self.del_Chinese_Ass()

        elif self.filename.endswith(".srt"):
            if self.type == "Chinese":
                self.del_Chinese_Srt()




if __name__ == '__main__':
    filename = sys.argv[1]
    type = sys.argv[2]
    s = SubtitleTransfer(filename,type)
    s.transfer()
