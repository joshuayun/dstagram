from django.shortcuts import render

# Create your views here.
# 뷰: 사용자에게 화면을 보여주거나, 혹은 보여주지 않거나 하는 동작을 수행하는 단위
"""
1. 로그인 페이지로 이동
2. 아이디 패스워드 입력화면이 나타남
3. 로그인 과정 진행
4. 메인페이지로 이동
"""

# 뷰: 함수형, 클래스형
# 장고에서 함수형 뷰의 첫번쨰 매개변수는 request여야 한다.
from django.http import HttpResponse
# 뷰 완성
# 뷰에 접속할 때 필요한 URl을 설정해야 한다.

# 1. 뷰와 html  코드가 공존
# 2. 템플릿 파일 별도로 만들기
"""
템플릿 ? : html 내부에 템플릿 문법이 약간 혼용된 형태
템플릿 파일을 어디에 둬야 하나? app/templates/app
"""
"""
템플릿에 파이썬 데이터 집어 넣기
1. 템플릿 파일에 변수가 출력될 공간 설정하기 - format, %, f
2. 파이썬 변수를 템플릿에 전달하기
"""
# + 데이터베이스와의 연동


def index(request):
    title = "메인 페이지"
    content = "내용 입니다."
    return render(request, 'photo/index.html',{'title':title, 'content':content})

def bmi(request):
    height = request.GET.get('height')
    weight = request.GET.get('weight')
    bmi = 0

    if height and weight:
        height = float(height)
        weight = float(weight)
        bmi = weight / (height/100) ** 2

    return render(request, 'photo/bmi.html', {'bmi':bmi})