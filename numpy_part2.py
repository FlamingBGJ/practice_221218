import pandas
import numpy as np

# 색인과 슬라이싱 기초
data_2 = np.random.randn(3,10,5)
print(data_2.shape)
print(data_2[:,:,1:2].shape)

arr_1 =  np.arange(10)
print(arr_1)
print(arr_1[5])
print(arr_1[5:8])
print(arr_1[:-1])
print(arr_1[-1:])

arr_1[1] = 122222
print(arr_1)

arr_1[:] = 10
print(arr_1)

arr_1 = 10
print(arr_1)

# copy
arr_2 = arr_1
print(arr_2)

arr_1[1] = 122222
print(arr_1)
print(arr_2)

arr_3 = arr_1.copy()
print(arr_3)

arr_1[2] = 1
print(arr_1)
print(arr_2)
print(arr_3)

# id 비교
print(id(arr_1))
print(id(arr_2))
print(id(arr_3))


# 블리언 값으로 선택
names = np.array(["A", "B", "C", "D", "E"])

## 정규분포에서 값을 뽑아 (5,4) 의 shape으로 만들어 준다. 
data = np.random.randn(5,4)
print(data)
## - 각각의 이름은 data배열의 각 row에 대응한다고 가정하자.
print(names == "A")
print(data[names == "A"])

bool_1 = names == "A"
print(data[~bool_1])


# data에서 0보다 작은 값들만 필터링
print(data[data < 0])

# data에서 0보다 작은 값들을 0으로 치환
data[data < 0] = 0 
print(data)


# 팬시 색인
arr_4 = np.empty((8,4))
print(arr_4)
print(arr_4[0])

for i in range(8):
    arr_4[i] = i 
print(arr_4)

# 과정을 제대로 이해할 것
print(arr[[1,2,3,4]])
print(arr[[2,1,5,4]])
print(arr[[2,-1,5,4]])

arr_5 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
])
print(arr_5.shape)
print(arr_5[:])
print(arr_5[:,1:])
print(arr_5[...,1:])


arr_6 = np.empty((10,3,5,8,4))
print(arr_6)
print(arr[..., -1:])

# 메모 : 특정한 row 를 선택하고 싶다면 그냥 원하는 순서가 명시된 정수가 담긴 ndarray 나 list를 넘기면 된다.


# 벡터화 연산 적용하기
mat_1 = np.array(range(1,10))
print(mat_1)

mat_2 = mat_1.reshape(3,3)
add_10 = lambda i: i+10
vec_add_10 = np.vectorize(add_10)
print(vec_add_10(mat_2))
print(mat_2 + 10)


# 배열 전치와 축 바꾸기
## 참고 arr_7 = np.array(range(12)) 이상태에서는 transpose 가 되지 않는다. 바꿔줄 행과 열이 없다. 
arr_7 = np.array(range(12)).reshape(12,1)
print(arr_7.shape)
print(arr_7.T.shape)
print(arr_7)

arr_8 = np.array(range(12)).reshape(3,4)
print(arr_8)

