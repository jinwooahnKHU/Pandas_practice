import pandas as pd  

#Series : Numpy Array 가 보강된 형태(Array + index). Data와 Index로 이루어져 있음

#Series 만들기

data = pd.Series([1,2,3,4])

print(data)


#index를 가지고 있고, index로 접근 가능하다.

data_1 = pd.Series([1,2,3,4], index = ['a','b','c','d'])

print(data_1)

print(data_1['b'])


#dictionary로도 series를 만들 수 있다.

pop_dict = {'korea' : 123, 'japan': 1584, 'america': 4546}

pop = pd.Series(pop_dict)

print(pop)

#이 때 key => index, values => data 로 변환된다.

#array로 출력해줌.
print(pop.values)