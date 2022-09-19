# ShellCmd

获取shell命令数据

# API

* 构造函数：
  * callback：每行处理回调函数
* run：
  * cmd：执行的命令
* reset：
  * callback：重置callback
* stop：
  * 停止处理

```python
class Shell:
    def __init__(self, callback = None):
        pass

    def run(self, cmd):
        pass
    
    def reset(self, callback):
        pass

    def stop(self):
        pass
```

# 完整使用示例

* [ShellCmd.py](/tests/ShellCmd.py)
