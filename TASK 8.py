# -*- coding: utf-8 -*-
"""TASK 8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WYYJUauOMgjQkhSjYIgJDlqcLbp5zZdR

1. Generate a 3 x 3 matrix using random module.
"""

#please provide your answer below this line.
import numpy as np
x = np.arange(2,11).reshape(3,3)
print(x)

"""2. Generate two 4 x 4 matrix using numpy and 

 a) Reshape it to 2 x 8matrix and vertically stack it.

 b) Reshape it to 2 x 8 matrix and horizontally stack it.
"""

#please provide your answer below this line.
import numpy as np
a1 = np.arange(1,17).reshape(4,4)
print(a1)
a1 = np.arange(1,17).reshape(8,2)
print(a1)
a1 = np.arange(1,17).reshape(2,8)
print(a1)