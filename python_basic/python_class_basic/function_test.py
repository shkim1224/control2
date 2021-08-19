"""def sum(a, b):
    s = a + b
    return s
 
total = sum(4, 7)
print("result = ",total)"""

# def f(i, mylist):
#     i = i + 1
#     mylist.append(0)
 
# k = 10       # k는 int (immutable)
# m = [1,2,3]  # m은 리스트 (mutable)
# a = ["AB", 10, False] # mutable 
# f(k, a)      # 함수 호출
# print(k, a)  # 호출자 값 체크


# def calc(i, j, factor = 1):
#     return i * j * factor
 
# result = calc(10, 20)
# print(result)

# def report(name, age, score):
#     print(name, score)

# #report("sunghokim", 60, 100) 
# #report(10, "Kim", 80)
# report(age=10, score=80,name="Kim")


"""def total(*numbers):
    tot = 0
    for n in numbers:
        tot += n
    return tot
 
t = total(1,2)
print(t)
t = total(1,5,2,6)
print(t)"""

def calc(*numbers):
    count = 0
    tot = 0
    for n in numbers:
        count += 1
        tot += n
    return count, tot
 
xcon, _= calc(10,1,5,2,6)  # (count, tot) 튜플을 리턴
print(xcon)