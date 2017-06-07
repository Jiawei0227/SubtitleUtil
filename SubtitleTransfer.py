# *_* coding:utf-8 *_*
import sys
import re
import chardet
import os


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
        self.file = open(filename)

        fileName, extension = os.path.splitext(filename)
        self.extension = extension
        code = chardet.detect(self.file.read())
        self.encoding = code['encoding']
        print "Encoding Type : " + self.encoding + ", Confidence : " + str(code['confidence'])

        self.newFileName = fileName+ "_new_no" + type + extension
        self.type = type

    def is_chinese(self, uchar):
        """
        judge whether unicode is Chinese
        """
        if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
            return True
        else:
            return False

    def is_alphabet(self,uchar):
        """judge whether unicode is an alphabet"""
        if (uchar >= u'\u0041' and uchar <= u'\u005a') or (uchar >= u'\u0061' and uchar <= u'\u007a'):
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
            if line.startswith("Dialogue"):
                lineSplits = line.split(",")
                content = ""
                prefix = ""
                i = 0
                while i < len(lineSplits):
                    if i < 9:
                        prefix += lineSplits[i]
                        prefix += ","
                    elif i < len(lineSplits) - 1:
                        content += lineSplits[i]
                        content += ","
                    else:
                        content += lineSplits[i]
                    i += 1

                matchTags = re.findall("\{.*\}", line)

                for matchTag in matchTags:
                    content = content.replace(matchTag, "")
                contentSplits = content.split("\N")
                for contentSplit in contentSplits:
                    for char in contentSplit.decode(self.encoding, 'ignore'):
                        if self.is_chinese(char):
                            line = line.replace(contentSplit, "")
                            break

                newfile.write(line)
            else:
                newfile.write(line)
        print "Delete Chinese Subtitle Successfully."

    def del_English_Ass(self):
        """
        del ass English subtitle
        """
        file = open(self.filename, 'r')
        newfile = open(self.newFileName, 'w')
        for line in file.readlines():
            if line.startswith("Dialogue"):
                lineSplits = line.split(",")
                content = ""
                prefix = ""
                i = 0
                while i < len(lineSplits):
                    if i < 9:
                        prefix += lineSplits[i]
                        prefix += ","
                    elif i < len(lineSplits)-1:
                        content += lineSplits[i]
                        content += ","
                    else:
                        content += lineSplits[i]
                    i += 1

                matchTags = re.findall("\{.*\}", line)

                for matchTag in matchTags:
                    content = content.replace(matchTag, "")
                contentSplits = content.split("\N")
                for contentSplit in contentSplits:
                    isChineseLine = False
                    for char in contentSplit.decode(self.encoding, 'ignore'):
                        if self.is_chinese(char):
                            isChineseLine = True
                            break
                    if not isChineseLine:
                        line = line.replace(contentSplit,"")
                if not line.endswith("\n"):
                    line += "\n"
                newfile.write(line)
            else:
                newfile.write(line)
        print "Delete English Subtitle Successfully."



    def del_Chinese_Srt(self):
        """
        del srt Chinese subtitle
        """
        file = open(self.filename, 'r')
        newFile = open(self.newFileName, 'w')

        for line in file.readlines():
            isChineseLine = False
            for char in line.decode(self.encoding,'ignore'):
                if self.is_chinese(char):
                    isChineseLine = True
                    break
            if not isChineseLine:
                newFile.write(line)
        print "Delete Chinese Subtitle Successfully."

    def del_English_Srt(self):
        """
        del srt English subtitle
        """
        file = open(filename, 'r')
        newFile = open(self.newFileName, 'w')

        for line in file.readlines():
            isChineseLine = False
            isEnglishLine = False
            matchTags = re.findall("\{.*\}", line)
            oldline = line
            for matchTag in matchTags:
                line = line.replace(matchTag, "")

            for char in line.decode(self.encoding, 'ignore'):
                if self.is_chinese(char):
                    isChineseLine = True
                    break
                if self.is_alphabet(char):
                    isEnglishLine = True
            if isChineseLine:
                newFile.write(oldline)
                continue
            if isEnglishLine:
                continue
            newFile.write(oldline)

        print "Delete English Subtitle Successfully."


    def transfer(self):
        """
        Transfer Main
        """
        if self.filename.endswith(".ass"):
            if self.type == "Chinese":
                self.del_Chinese_Ass()
            elif self.type == "English":
                self.del_English_Ass()

        elif self.filename.endswith(".srt"):
            if self.type == "Chinese":
                self.del_Chinese_Srt()
            elif self.type == "English":
                self.del_English_Srt()


if __name__ == '__main__':
    filename = sys.argv[1]
    type = sys.argv[2]
    s = SubtitleTransfer(filename,type)
    s.transfer()
