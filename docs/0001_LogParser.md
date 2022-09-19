# LogParser

Kernel、Logcat、文本数据提取

# API

* file：需要解析的文件
* regex：被解析的文件每行数据才用这个正则表达式进行匹配
* callback：如果regex找到了数据，调用这个回调函数
* fileEncode：解析file的时候才用的编码格式

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

kernel

```python
# 15932.513576 : 1138-android.bg      : AP_Launch: com.android.settings/.FallbackHome 756ms
r'(\d+.\d+)\s+:(.*):\s+(\w*):\s*(.*)'
```

ZCV

```python
# 2705    42248   1025
r'(\d+)\s+(\d+)\s+(\d+)'
```

logcat

```python
# 06-29 09:37:46.551252  2283  2283 I DebugLoggerUI/MainActivity: onPause
r'(\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2}\.\d*)\s+\d+\s+\d+\s+\w+\s+(.*)',
```

# callback示例

```python
def defaultLineCallback(lineInfo):
    lineInfoFixed = []

    for index in range(len(lineInfo)):
        lineInfoFixed.append(lineInfo[index])
    
    return lineInfoFixed


def floatLineCallback(lineInfo):
    lineInfoFixed = []

    for index in range(len(lineInfo)):
        lineInfoFixed.append(float(lineInfo[index]))
    
    return lineInfoFixed

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
```
