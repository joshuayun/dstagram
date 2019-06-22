"""
어떤 웹 사이트를 만든다!

어떤 도구를 사용해서 만들것인가?
1. 파이썬, 자바, PHP 언어를 선택
2. 프레임워크 : Django, Spring, Laravel

장고로 웹 사이트를 만들자
1. 프로젝트를 만든다. - 파이참에서 파이썬 신규프로젝트 만들기
2. 장고를 설치
$ pip install django
3. 장고 프로젝트 만들기
$ django-admin startproject config .
- config 폴더: 프로젝트를 구성하는 설정 파일들이 저장된 폴더
- setting.py: 추가 설정을 기입하는 파일
- urls.py: 웹 서비스의 URL 라우팅 테이블(주소에 대한 설계)를 기록하는 파일
- wsgi.py: 웹 서비스 애플리케이션 실행 파일
- manage.py: 장고에 명령을 전달하는 파일


장고 프로젝트를 만든 후
$ python manage.py runserver
1. 셋팅(데이터베이스 정보 입력, 이미지 서버나 파일서버 정보 입력)

2. 데이터베이스 초기화(회원 정보가 기록되는 테이블 생성)
$ python manage.py migrate
2-1. 관리자 계정 생성
$ python manage.py createsuperuser

3. 앱 생성(기능 뷰(페이지)를 만들기 위해서)
$ python manage.py startapp [앱이름]
- migrations 폴더: 데이터베이스 변경 사항 기록 파일들이 담기는 폴더
- __init__.py: 파이썬 2 와의 호환을 위한 파일
- admin.py: 관리자 페이지 커스터마이징
- apps.py: 해당 앱에 관한 정보와 설정
- models.py: Model을 기록하는 파일
- tests.py: 테스트 세트를 기록하는 파일
- views,py: 실제 로직과 기능이 동작하는 뷰를 기록하는 파일


4. 뷰를 만들기
4-1. 데이터베이스가 필요한 뷰라면 모델을 만든다.
4-2. 사용자에게 보여줄 화면을 구성하는 코드(html, css, javascript) 템플릿
MVC 패턴 - 디자인 패턴(설계상 발생하는 문제를 해결하기 위한 해결책)
장고에서는 MVC를 MTV라고 부른다

Model(Model): 데이터베이스에 필요한 내용을 반영
Template(View): 화면에 보여질 내용
View(Controller): 서버 애플리케이션에서 동작하는 로직


"""