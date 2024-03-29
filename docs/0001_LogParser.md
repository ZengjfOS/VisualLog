# LogParser

Kernel、Logcat、文本数据提取

# API

* file：需要解析的文件
* regex：被解析的文件每行数据才用这个正则表达式进行匹配
* callback：如果regex找到了数据，调用这个回调函数
* fileEncode：解析file的时候才用的编码格式
  * `utf-8`
  * `ISO-8859-1`
  * `GB2312`
  * `gbk`

```python
def logFileParser(file = None, regex = None , callback=defaultLineCallback, fileEncode = "utf-8"):
```

# 示例

```python
from VisualLog.LogParser import logFileParser

def dateLineCallback(lineInfo, col = 1):
    lineInfoFixed = []
    today_year = str(datetime.date.today().year)

    for index in range(len(lineInfo)):
        if index == 0:
            continue

        if index == col:
            timeString = today_year + "-" + lineInfo[0] + " " + lineInfo[index]
            currentDate = datetime.datetime.strptime(timeString, "%Y-%m-%d %H:%M:%S.%f")
            lineInfoFixed.append(currentDate)
            continue

        lineInfoFixed.append(lineInfo[index])
    
    return lineInfoFixed

# 06-29 09:37:46.551252  2283  2283 I DebugLoggerUI/MainActivity: onPause
lineInfos = logFileParser(
        "default/AndroidSystemWakeup.curf", 
        r'(\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2}\.\d*)\s+\d+\s+\d+\s+\w+\s+(.*)',
        callback=dateLineCallback
        )
for info in lineInfos:
    print(info)
```

# 正则表达式示例

## kernel

* [BatteryInfoDischarge.py](/tests/BatteryInfoDischarge.py)

```python
# 15932.513576 : 1138-android.bg      : AP_Launch: com.android.settings/.FallbackHome 756ms
r'(\d+.\d+)\s+:(.*):\s+(\w*):\s*(.*)'

# <5>[  313.509051]  (0)[235:battery_thread]car[-30,251,-251,50,-259] tmp:30 soc:100 uisoc:97 vbat:4297 ibat:-2762 algo:0 gm3:0 0 0 0,boot:0
r'\[\s*(\d*\.\d*)\].*\d*\:battery_thread.*tmp:(\d*) soc:(\d*) uisoc:(\d*) vbat:(\d*) ibat:([-]?\d*)'
```

## ZCV

* [BatteryZCV.py](/tests/BatteryZCV.py)

```python
# 2705    42248   1025
r'(\d+)\s+(\d+)\s+(\d+)'
```

## logcat

* [MonotoneCubicSpline.py](/tests/MonotoneCubicSpline.py)
* [AmbienteLight.py](/tests/AmbienteLight.py)

```python
# 06-29 09:37:46.551252  2283  2283 I DebugLoggerUI/MainActivity: onPause
r'(\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2}\.\d*)\s+\d+\s+\d+\s+\w+\s+(.*)'

# 09-19 14:19:17.183  1027  1110 I DisplayPowerController[0]: No longer ignoring proximity [1]
r'(\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2}\.\d*)\s+\d+\s+\d+\s+\w+\s+.*: No longer ignoring proximity \[(\d)\]'

# 09-09 18:24:12.680436   571   628 I Light   : event->word[0]=400,  event->word[1]=0,event->word[2]=0
r'(\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2}\.\d*)\s+\d+\s+\d+\s+\w+\s+Light\s*:\s.*=(\d*),\s*.*=(\d*),\s*.*=(\d*)'
```

## 数据帧

* [SecImageFile.py](/tests/SecImageFile.py)

```python
# Signed image is stored at /home/zengjf/zengjf/android/xxxxxx/xbl.elf
# Processing 1/25: /home/zengjf/zengjf/android/xxxxxx/xbl.elf
r'(Signed image is stored at (.*)|Processing \d*/\d*: (.*))',
```

# callback示例

```python
# 直接添加
def defaultLineCallback(lineInfo):
    lineInfoFixed = []

    for index in range(len(lineInfo)):
        lineInfoFixed.append(lineInfo[index])
    
    return lineInfoFixed

# 转float
def floatLineCallback(lineInfo):
    lineInfoFixed = []

    for index in range(len(lineInfo)):
        lineInfoFixed.append(float(lineInfo[index]))
    
    return lineInfoFixed

# 转日期
def dateLineCallback(lineInfo, col = 1):
    lineInfoFixed = []
    today_year = str(datetime.date.today().year)

    for index in range(len(lineInfo)):
        if index == 0:
            continue

        if index == col:
            timeString = today_year + "-" + lineInfo[0] + " " + lineInfo[index]
            currentDate = datetime.datetime.strptime(timeString, "%Y-%m-%d %H:%M:%S.%f")
            lineInfoFixed.append(currentDate)
            continue

        lineInfoFixed.append(lineInfo[index])
    
    return lineInfoFixed

# 多个正则表达式匹配获取组合数据帧，配合类使用
def frameLineCallback(self, lineInfo, col = 1):
    if lineInfo[0].startswith("Signed image is"):
        self.currentInfo.append(lineInfo[1].split("/sectools/")[1])
        return self.currentInfo

    if lineInfo[0].startswith("Processing "):
        self.currentInfo = []
        self.currentInfo.append(lineInfo[2].split("/xxxxxx/")[1])
        return None

    return None
```
