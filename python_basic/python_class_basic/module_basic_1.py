"""
모듈(Module)은 파이썬 코드를 논리적으로 묶어서 관리하고 사용할 수 있도록 하는 것으로, 보통 하나의 파이썬 .py 파일이 
하나의 모듈이 된다
모듈 안에는 함수, 클래스, 혹은 변수들이 정의될 수 있으며, 실행 코드를 포함할 수도 있다
"""

import math
n = math.factorial(5)
# 사용 방법: import 모듈1[, 모듈2[,... 모듈N]

# 하나의 모듈 안에는 여러 함수들이 존재할 수 있는데, 이 중 하나의 함수만을 불러 사용하기 위해서는 
# 아래와 같이 "from 모듈명 import 함수명"이라는 표현을 사용할 수 있다

# factorial 함수만 import
from math import factorial  
n = factorial(5) / factorial(3) 

"""
모든 함수를 불러 사용하기 위해서는 "from 모듈명 import *" 와 같이 asterisk(*)를 사용할 수 있다. 
이렇게 from...import... 방식으로 import 된 함수는 호출시 모듈명 없이 직접 함수명을 사용한다.
"""

# 모든 함수를 import
from math import *
n = sqrt(5) + fabs(-12.5) 

"""
파이썬에서 모듈을 import 하면 그 모듈을 찾기 위해 다음과 같은 경로를 순서대로 검색한다.

- 현재 디렉토리
- 환경변수 PYTHONPATH에 지정된 경로
- Python이 설치된 경로 및 그 밑의 라이브러리 경로

이러한 경로들은 모두 취합되어 시스템 경로인 sys.path에 리스트 형태로 저장된다.
따라서, 모듈이 검색되는 검색 경로는 sys.path를 체크하면 쉽게 알 수 있다. 
모듈을 import 하면 sys.path에 있는 경로 순서대로 모듈을 찾아 import하다가 만약 끝까지 찾지 못하면 에러가 발생된다.
"""
import sys
print(sys.path)



