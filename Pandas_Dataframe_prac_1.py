import pandas as pd  

#DataFrame 이론
#여러개의 Series가 모여서 행과 열을 이룬 데이터

#Series 2개로 Dataframe 만들기
population = pd.Series({"china":141500, 'japan' : 12718, 'korea' : 5180, 'usa' : 32676})

gdp_dict = {'korea' : 169320000, 'japan': 516700000, 'china' : 1409250000, 'usa':2041280000}

gdp = pd.Series(gdp_dict)

country = pd.DataFrame({'population': population, 'gdp': gdp})

print(country)


#DataFrame 요소 파악
print(country.index)

print(country.columns)


print(country['gdp']) #-> Series로 나오게 된다.


#DataFrame에 새로운 변수(Series) 추가
gdp_per_capita = country['gdp'] / country['population']

country['gdp_per_capita'] = gdp_per_capita
#=> country['새 column 이름'] = 기존에 정의한 변수 

print(country)


#저장과 불러오기

#저장
country.to_csv('country.csv')

country.to_excel('country.xlsx')

#불러오기
country = pd.read_csv('country.csv')

country = pd.read_excel('country.xlsx')