""" 
파이썬에서의 클래스:
http://pythonstudy.xyz/python/article/19-%ED%81%B4%EB%9E%98%EC%8A%A4
상기의  블로그 내용 
"""

"""
메서드는 클래스의 행위를 표현하는 것으로 클래스 내의 함수로 볼 수 있다. 
파이썬에서 메서드는 크게 인스턴스 메서드(instance method), 클래스 메서드(class method), 정적 메서드(static method)가 있다. 
가장 흔히 쓰이는 인스턴스 메서드는 인스턴스 변수에 엑세스할 수 있도록 메서드의 첫번째 파라미터에 항상 객체 자신을 의미하는 
"self"라는 파라미터를 갖는다.
"""

class Rectangle:
    count = 0  # 클래스 변수: 해당 클래스를 사용하는 모두에게 공용으로 사용되는 변수(class의 global variable)
               # 클래스 변수는 클래스 내외부에서 "클래스명.변수명" 으로 엑세스 할 수 있다.
    # 초기자(initializer)
    def __init__(self, width, height): # width, height는 객체 생성시 사용되는 파라미터임
        # self.* : 인스턴스변수 => 인스턴스 변수는 __init__() 생성자에서 정의됨 => 인스턴스 변수는 각 객체 인스턴스마다 별도로 존재한다
        # 클래스 밖에서는 "객체이름.인스턴스변수"와 같이 엑세스 
        self.width = width
        self.height = height
        Rectangle.count += 1 # Rectangle 객체가 생성될 때 마다 하나씩 증가
 
    # 메서드 => Python 클래스는 기본적으로 모든 멤버가 public이라고 할 수 있다
    def calcArea(self):
        area = self.width * self.height
        return area
    
    # private 메서드 => 만약 특정 변수명이나 메서드를 private으로 만들어야 한다면 두개의 밑줄(__)을 이름 앞에 붙이면 된다
    def __internalRun(self):
        pass
    
    # 정적 메서드
    @staticmethod
    def isSquare(rectWidth, rectHeight):
        return rectWidth == rectHeight   
 
    # 클래스 메서드
    @classmethod
    def printCount(cls):
        print(cls.count)   
        
    # 테스트
square = Rectangle.isSquare(5, 5)        
print(square)   # True        
 
rect1 = Rectangle(5, 5)
rect2 = Rectangle(2, 5)
rect1.printCount()  # 2         

"""
클래스 인스턴스의 생성과 사용
"""

# 인스턴스 생성
r = Rectangle(2, 3)

# 메서드 호출
area = r.calcArea()
print("area = ", area)

# 인스턴스 변수 엑세스
r.width = 10
print("width = ", r.width)
 
# 클래스 변수 엑세스
print(Rectangle.count)
print(r.count)