# 서버_우분투
설정_서버_도커

## 프로젝트 개요
이 프로젝트는 JSON 형식의 데이터를 분석하여 비디오에서 **사람의 자세(Human Pose)**를 출력하는 시스템입니다.  
Docker를 사용하여 분석하며, 결과는 JSON 파일로 저장됩니다.

## 실행 방법
서버에 접속한 후, 프로젝트 디렉토리로 이동하여 Docker를 실행합니다.

```bash
# 서버 접속
ssh ubuntu@3.37.3.170

# 프로젝트 디렉토리 이동
cd ./hpe_project

# Docker 이미지 빌드 (필요 시 실행)
docker build -t sym .

# Docker 실행 (비디오 분석)
docker run --rm -it sym
docker run --rm -it sym --vid_path "sym/data/비디오.mp4"
```

---
## 동영상 업로드 방법
로컬 컴퓨터에서 서버로 동영상을 업로드하려면 아래 명령어를 사용하세요. (PowerShell 추천)
```bash
scp local_video.mp4 ubuntu@3.37.3.170:~/hpe_project/sym/data/
```
local_video.mp4 → 내 컴퓨터에 있는 동영상 파일 이름

ubuntu@3.37.3.170 → 서버 로그인 정보

~/hpe_project/sym/data/ → 서버에서 저장할 폴더 경로
