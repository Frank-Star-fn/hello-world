# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

a=np.array([1,2,3])
type(a)

print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)
print(a.itemsize)

b=np.array([[1,2,3],[4,5,6]])
print(b.ndim)
print(b.shape)
print(b.size)
print(b.dtype)
print(b.itemsize)

c=np.array([[1,2,3],[4,5,6]],dtype=np.int64)
print(c.dtype)

