# *_* coding:utf-8 *_*
from SubtitleTransfer import SubtitleTransfer

if __name__ == '__main__':
    s = SubtitleTransfer("test.ass","Chinese")
    s.transfer()
    ss = SubtitleTransfer("test.srt","Chinese")
    s.transfer()