# Python 3.12 이미지 사용
FROM python:3.12
RUN apt-get update && apt-get install -y libgl1-mesa-glx
# 작업 디렉토리 설정
WORKDIR /app

# 필수 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 코드 및 데이터 복사
COPY . .
ENTRYPOINT ["python","sym/mk_json_3D_json.py"]







