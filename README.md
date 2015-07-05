# NEXTLAB-Python-Tutorial
Python Tutorial을 위한 예제 소스 및 과제

1.simple_webserver
flask 프레임워크가 얼마나 간단하게 웹프로그래밍이 가능한지를 보여주는 예제임

[실행방법]
cmd창에서 아래 명령으로 웹서버를 실행하고 웹브라우저에서 "http://192.168.0.1:5000"으로 접속함
>python 1.flask.py

[과제]
웹브라우저에서 "http://192.168.0.1:5000"으로 접속하면 아래와 같이 현재 시각 정보를 표시함
"2015-07-04 10:50:29"
[힌트]
- time 라이브러리 이용

2.icon_cralwer
유명 아이콘 웹페이지의 HTML을 분석하여 원하는 아이콘 이미지의 URL을 보여주는 예제임

[과제]
아이콘 이미지의 URL을 이용하여 로컬 저장소에 아이콘 이미지를 저장함
[힌트]
- urllib 라이브러리를 이용하여 URL로부터 이미지 파일을 저장함
- os.path.join 을 이용하여 폴더 경로와 파일명을 붙여서 저장 경로를 생성

3.curve_fitting
안드로이드 스마트폰 터치 입력 데이터를 그래프로 표시하는 예제
- touchdata.csv : 안드로이드를 통해 생성된 터치 데이터
- touch_smooth.py : 예제 소스
- smooth.py : smooth한 곡선을 만드는 savitzky_golay 알고리즘 구현 모듈 (로봇 동작을 위한 smooth 곡선 생성용)
- smooth_test.py : smooth 모듈 이용 예제

[과제]
- smooth_test.py 소스를 참고해서 touch_smooth.py에 savitzky_golay 알고리즘을 적용한 곡선 추가로 표시함
