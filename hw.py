def hi(name, age):
    print('hi!')
    print(f"{name} my name is hw and i'm {age}")
    print('hii!!!')

hi('Hi', 30)

def mul(x):
    return x * x

cal = mul(3)
print(mul(5) * mul(6))

# 나머지
print(7.0 % 3)
# 거듭제곱
print(2.0 ** 3)
# 나눗셈은 무조건 소수형으로 나옴
print(7/3)
# 버림 나눗셈
print(7//3)
# 버리고 소숫점으로 표현
print(7.0//2)
# 반올림
print(round(3.141592, 3))
# Type casting
print(int(3.8))
print(float(3))
print(float("2.5") + float("4.7"))
print(str(2) + str(5))
# format 사용
year = 21
month = 11
day = 27
print(f"오늘은 {year}년 {month}월 {day}일이다.")