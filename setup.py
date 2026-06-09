# pip install . 명령으로 설치할 수 있게 해주는 설정 파일
from setuptools import setup, find_packages

setup(
    name="todo_package",
    version="1.0.0",
    author="홍서우",          
    author_email="hongsw070427@gmail.com",   
    description="우선순위와 태그로 할 일을 관리하는 Python 패키지",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[],
)