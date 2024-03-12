# 測試過程文件

## ffmpeg
### Extract wav from mp4 
```ffmpeg -i {INPUT}.mp4 -vn -ar 16000 -ac 1 -f wav {OUTPUT}.wav```

## wenet
### 辨識
#### 中文
```wenet --language chinese {INPUT}.wav```
