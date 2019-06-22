from operator import truediv

from django.db import models

# Create your models here.
"""
모델: 데이터를 데이터베이스에 어떤 형식으로 저장할 것인지 묘사하는 도구
데이터베이스에는 보통 데이터가 엑셀 파일과 비슷한 형태로 저장됩니다.
로우(줄) 당 컬럼(열) 에 어떤 데이터 형식으로 저장할 것이냐?

username, password, 이름, 주민번호,
admin        11111   jake 123123

"""

"""
ORM 
"""
"""
함수: 새로운 명령
def 함수이름([매개변수]):
    실행하고 싶은 코드
클래스: 새로운 변수 타입
class 클래스이름([부모클래스]):
    [필드]
    [함수-메서드]
    def __?__(self)
    
"""
"""
def __?__(self)
매직메서드, dunder메서드
"""
# 1. 모델을 만들었다 -> DB에 저장될 데이터 구조를 설계했다.
# 2. makemigrations -> DB에 반영될 변경 내역을 추적
# python manage.py makemigrations photo
# 3. migrate -> 변경 내역을 반영
# python manage.py migrate photo
class BMI(models.Model):
    # 어떤 데이터를 저장할지 변수들을 설정: 필드 설정
    name = models.CharField(max_length=50, blank=True)
    weight = models.FloatField()
    height = models.FloatField()
    bmi = models.FloatField(blank=True, null=True) # null