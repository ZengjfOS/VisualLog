# SameLines

比较两个文本数组

# API

* old：被对比数组
* new：对比数组
* callback：提取对比数据
* 返回值：sameLines, oldIndexs, newIndexs
  * sameLines：相同的文本数组
  * oldIndexs：相同文本在old数组中的索引数组
  * newIndexs：相同文本的new数组中的索引数组

```python
def diffList(old, new, callback = defaultCallback):
```

# 完整使用示例

* [SameLines.py](/tests/SameLines.py)
