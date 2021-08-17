# 정보제어공학설계 입문 
본 강좌는 정보제어공학전공 학생들이 수강하는 과목입니다.

본 강좌에서는 visual studio code 및 pycharm을 이용하여 1학기에 학습한 aruduino에 장착된 다양한 인터페이스(서보모터, led, 초음파 센서 등)을 python 프로그래밍언어를 활용하여 제어하는 방법에 대해 학습합니다.

본 강좌 수강을 위한 준비사항:

1) 여러분 컴퓨터에 아나콘다를 설치한 후 conda prompt를 열고 하나의 가상환경을 아래의 명령을 사용하여 생성함
 (base) c:\Users\shkim> conda create -n control python=3.8 # 이 명령은 아나콘다에 control이라는 가상환경을 만들고 그 가상환경의 기본 python 인터프리터 버젼을 3.8로 설정하는 것임
                                               # 가상환경이 생성되면 ananconda3이 설정된 디렉토리로 가면 envs라는 폴더에 tensorflow1이라는 폴더가 생성되고 그 폴더내에
                                               # python.exe(version 3.8)이 설치되어 있음을 확인할 수 있음
                                               # 이러한 가상환경에서 특정용도로 사용되는 패키지를 설치할 수 있으며 이 가상환경을 위해 설치되는 패키지는 anaconda3/envs/control/Lib/site-
                                                 packages/ 아래에 설치됨
(2) 생성된 가상환경을 활성화시킴
(base) c:\Users\shkim> conda activate control

(3) 가상환경으로 진입된 상태에서 필요로 되는 패키지(pyfirmata)를 설치함
(control) c:\Users\shkim> pip install pyfirmata

(4) 가상환경에 설치된 패키지를 확인하는 방법
(control) c:\Users\shkim> pip list  or pip freeze 
=> 리스트 결과가 화면에 표시됨

(5) 자신의 컴퓨터에 git을 설치함( 또는 https://github.com/shkim1224/control2 를 브라우저 창에 입력하여 github로 가서 Code의 download zip을 선택하여 자신의 컴퓨터에 download 받음)

(6) VSC를 수행시키고 파일-> 폴더열기 에서 git clone 한 위치에 만들어진 control2를 선택하던지 아니면 압축을 푼 폴더를 선태하면 됨

(7) Control 폴더에는 python 소스로 되어 있기 때문에 VSC에서 python extension을 설치해야 함
(8) 폴더의 파이선 소스(xxx.py)를 선택하면 edit 창에 파일내용이 나오고 vsc 하단에 이 파이선 프로그램의 수행시 필요로 되는 python 인터프리터를 찾게 됨
    => Select Python Interpreter를 클릭하면 현재 자신의 컴퓨터에 설치된 여러 python 인터프리터가 리스트업되고 우리가 conda 환경에서 만든 control:conda가 보이면 이를 선택함
    => 만일 보이지 않는다면 "Enter interpreter path..."를 선택하고 설치된 가상환경으로 가서 python.exe(인터프리터)를 선택함

(9) 상기와 같이 설정이 완료되면 프로그램의 수행이 가능함
