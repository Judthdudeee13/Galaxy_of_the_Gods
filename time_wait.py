import math
import numpy as np
for x in np.arange(0, 10.1, 0.1):
    y=math.sqrt((10*10)-(x*x))
    print(f"({x}, {y})")
    
for x in np.arange(0, 10.1, 0.1):
    y=math.sqrt((10*10)-(x*x))
    print(f"({x}, -{y})")

for x in np.arange(0, 10.1, 0.1):
    y=math.sqrt((10*10)-(x*x))
    print(f"(-{x}, {y})")
    
for x in np.arange(0, 10.1, 0.1):
    y=math.sqrt((10*10)-(x*x))
    print(f"(-{x}, -{y})")
    
