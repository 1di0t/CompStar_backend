# 1. 베이스 이미지 설정
# 공식 Python 3.10 슬림 버전을 기반으로 이미지를 생성합니다.
# 'slim' 버전은 운영에 불필요한 파일을 제외하여 이미지 크기를 줄여줍니다.
FROM python:3.10-slim

# 2. 환경 변수 설정
# Python이 출력을 버퍼링하지 않고 바로 터미널에 표시하도록 설정하여,
# Cloud Run의 로그를 실시간으로 확인할 수 있게 합니다.
ENV PYTHONUNBUFFERED True

# 애플리케이션 코드가 위치할 디렉토리 경로를 환경 변수로 설정합니다.
ENV APP_HOME /app
WORKDIR $APP_HOME

# 3. 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 소스 코드 복사
# 프로젝트의 모든 소스 코드를 컨테이너의 작업 디렉토리로 복사합니다.
COPY . .

# 5. 프로덕션 서버 실행
# Django 개발 서버(runserver) 대신, 프로덕션 환경에 적합한 Gunicorn을 사용합니다.
# - "config.wsgi:application": Django 프로젝트의 WSGI 애플리케이션 경로입니다.
# - "--bind :8080": Cloud Run이 요청을 수신하는 기본 포트인 8080에 서버를 바인딩합니다.
# - "--workers 2 --threads 4": 서버의 성능을 조절하는 옵션입니다. (환경에 따라 조절 가능)
# - "--timeout 0": Cloud Run 환경에서는 이 옵션을 0으로 설정하여 타임아웃을 비활성화하는 것이 좋습니다.
CMD exec gunicorn --bind :8080 --workers 2 --threads 4 --timeout 0 config.wsgi:application

