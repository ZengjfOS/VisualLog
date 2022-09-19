# MatplotlibZoom

Matplotlib绘制可缩放、平移可视化数据

# API

* Show：静态绘图
  * callback: matplotlib绘图回调函数
  * rows：当前绘制多少行图
  * cols：当前绘制多少列图
* Live：实时绘图
  * callback: matplotlib绘图回调函数
  * rows：当前绘制多少行图
  * cols：当前绘制多少列图
  * interval：动态绘图每帧图间隔时间，单位ms

```python
class Show:
    def __init__(self, callback = None, rows = 1, cols = 1):
        pass

class Live:
    def __init__(self, callback, rows = 1, cols = 1, interval = 1000 / 1):
        pass
```

# 完整使用示例

* [BatteryZCV.py](/tests/BatteryZCV.py)
