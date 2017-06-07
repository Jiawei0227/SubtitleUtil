# -*- coding:utf-8 -*-
import sys
import urllib2
import hashlib
import os


class SubtitleDownloader:
    """
    this class is to help with the Subtitle Downloader
    """
    _url = "http://api.thesubdb.com/?"
    _headers = {'User-Agent': 'SubDB/1.0 (SubtitleUtil/1.0; https://github.com/WJerry0227/SubtitleUtil)'}


    def __init__(self, fileName, language = "default"):
        self.fileName = fileName
        self.language = language
        self.hash = self.__get_hash()

    def __get_hash(self):
        """
        this hash function receives the name of the file and returns the hash code
        """
        readSize = 64 * 1024
        with open(self.fileName, 'rb') as f:
            data = f.read(readSize)
            f.seek(-readSize, os.SEEK_END)
            data += f.read(readSize)
            return hashlib.md5(data).hexdigest()

    def get_available_subtitle(self):
        """
        this function helps you get the available subtitle for your video
        """
        searchUrl = SubtitleDownloader._url + "action=search&hash=" + self.hash + "&versions"
        req = urllib2.Request(searchUrl, "", SubtitleDownloader._headers)
        try:
            res_data = urllib2.urlopen(req)
            res = res_data.read()
            if self.language == "default":
                print "These are all subtitles you can download: { " + res + " }"
                type = raw_input("Input the type you want: ")
                self.__download_subtitle(type)
            else:
                self.__download_subtitle(self.language)
        except:
            print "Sorry, none subtitle has been found for this video."
            return

    def __download_subtitle(self, language):
        """
        this function helps you download the subtitle for your video
        """
        fileName, extension = os.path.splitext(self.fileName)
        newFileName = fileName + ".srt"
        downloadUrl = SubtitleDownloader._url + "action=download&hash=" + self.hash + "&language=" + language
        req = urllib2.Request(downloadUrl, "", SubtitleDownloader._headers)
        res_data = urllib2.urlopen(req)
        res = res_data.read()
        newFile = open(newFileName, "w")
        newFile.write(res)
        print "Download Successfully! The subtitle file path is in \"" + newFileName + "\""

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("This program requires your video path.")
        sys.exit(1)
    elif len(sys.argv) == 2:
        filePath = sys.argv[1]
        s = SubtitleDownloader(filePath)
        s.get_available_subtitle()
    elif len(sys.argv) == 3:
        filePath = sys.argv[1]
        language = sys.argv[2]
        s = SubtitleDownloader(filePath,language)
        s.get_available_subtitle()

