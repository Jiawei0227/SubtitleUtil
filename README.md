#Subtitle Util

Subtitle Util has a list of functions below
 - [1 Subtitle Transfer](https://github.com/WJerry0227/SubtitleUtil#1-subtitle-transfer)
 - [2 Subtitle Downloader](https://github.com/WJerry0227/SubtitleUtil#2-subtitle-downloader)
See each util for more details.

**Requirement**:
 - python 2
 - python  ->  urllib2

**Installation**:
```
git clone https://github.com/WJerry0227/SubtitleUtil.git
cd SubtitleUtil
python [Subtitle Util Type].py [Usage]
```
**Contact**:
>wjerry227@gmail.com

**About**:
Developed by WJerry0227

## 1 Subtitle Transfer

### Intro
It is a small python program to **remove Chinese or English** characters in your subtitle file

When I was watching *This is us* on my computer. I hate the Chinese subtitle mixed with English subtitle.

Therefore, this python program came to mind.

### Usage

```
python SubtitleTransfer.py [YOUR SUBTITLE FILE PATH] [TYPE]
```
> - TYPE: The type that you want to delete from your subtitle.
> - [Chinese] [English] are available only
> - FILE PATH :*.ass* and *.srt* are available only

It will create a new file in your old path with the new postfix.

### Encoding

The encoding of your subtitle will be automatically detected.



## 2 Subtitle Downloader

### Intro
It is a small python program to **download subtitle** for your vedio

I always found the subtitle download from Internet does not fit with my vedio. Then I search this website [SubDB](http://thesubdb.com/). Thanks to the API it provides.

### Usage
```
python SubtitleDownloader.py [YOUR VEDIO FILE PATH] [LANGUAGE]
```
> - [LANGUAGE] is optional.
> - It only supports [English, Español, Français, Italiano, Nederlands, Polski, Português (Brazil), Român, Svenska, Türkçe] now

It will automatically download a [vedioname.srt] file in your vedio path


