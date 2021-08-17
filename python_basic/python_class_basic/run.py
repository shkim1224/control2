"""
이 프로그램을 커맨드 창에서 수행하려면 터미널에서 현재 폴더로 이동하고 
PS F:\2021_2_lecture\control2\python_basic\python_class_basic> python run.py google.com
만일 python 명령을 사용하지 않으려면 
#! f:/anaconda3/envs/control2/python.exe  => linux 에서
"""

#! f:/anaconda3/envs/control2/python.exe
# run.py
import sys
def openurl(url):
    #..본문생략..
    print(url)
 
if __name__ == '__main__':
    openurl(sys.argv[1])  