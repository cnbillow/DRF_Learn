# 现在有一个包含 N 个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给 N 个变量？

"""
    >>> a = (1, 2)
    >>> x, y = a
    >>> x
    1
    >>> y
    2
    >>> data = ['qinglin', 2018, 8, 6, (2018-8-6)]
    >>> name, year, month, day = data
    Traceback (most recent call last):
      File "<console>", line 1, in <module>
    ValueError: too many values to unpack (expected 4)
    >>> name, year, month, day, date = data
    >>> name, year, month, day, date
    ('qinglin', 2018, 8, 6, 2004)
    >>> name = 'xql'
    >>> f,m,l = name
    >>> f,m,l
    ('x', 'q', 'l')

    # 解压一部分，丢弃其他的值。使用任意变量名去占位。
    # 获取部分，使用占位符
    >>> _,year, month, day, _ = data
    >>> year, month, day
    (2018, 8, 6)
    >>>
"""
