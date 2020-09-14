import pandas as pd  
import numpy as np  
from random import randint

#Series 연산 
#=> Numpy Array에서 사용한 연산자들을 활용할 수 있다.
A = pd.Series([2,4,6], index = [0,1,2])
B = pd.Series([1,3,5], index = [1,2,3])

#index끼리 덧셈을 한다.
print(A + B)

#맞지 않는 index여서 값이 비어있는 곳은 NaN으로 처리가 되는데
#맞지 않는 값을 0으로 해서 더한다.
print(A.add(B, fill_value = 0))


#DataFrame 연산
C = pd.DataFrame(np.random.randint(0,10,(2,2)), columns = list("AB"))
D = pd.DataFrame(np.random.randint(0,10,(3,3)), columns = list("BAC"))

print(C + D)

print(C.add(D, fill_value = 0))

#집계함수 적용가능
data = {"A" : [i + 5 for i in range(3)],
"B" : [i ** 2 for i in range(3)]}

df = pd.DataFrame(data)

print(df['A'].sum())

print(df.sum())

print(df.mean())

