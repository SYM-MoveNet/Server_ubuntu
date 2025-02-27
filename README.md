# 서버_우분투
설정_서버_도커

## 프로젝트 개요
이 프로젝트는 JSON 형식의 데이터를 분석하여 비디오에서 **사람의 자세(Human Pose)**를 출력하는 시스템입니다.  
Docker를 사용하여 분석하며, 결과는 JSON 파일로 저장됩니다.

##서버구축완료 도커설치
ubuntu 서버를 구축한다음 하는 서버구축 

# 서버 접속
```bash
ssh ubuntu@3.37.3.170
```

## 1️⃣ Ubuntu 서버에서 Git 설치 (이미 설치되어 있으면 생략)

```bash
sudo apt update && sudo apt install -y git
```

프로젝트 다운
```bash
git clone https://github.com/dlgkrwls/Server_ubuntu.git
```

docker 설치
```bash
sudo wget -qO- http://get.docker.com/ | sh
```

디렉토리 이동 
```bash
cd ~/Server_ubuntu/hpe_project
```


## 실행 방법
동영상 분석 실행방법


# Docker 이미지 빌드 (필요 시 실행)
docker build -t sym .

# Docker 실행 (비디오 분석)
docker run --rm -it sym
docker run --rm -it sym --vid_path "sym/data/비디오.mp4"
```

동영상 실행시 data/out/비디오.json 파일 생성

## 동영상 업로드 방법
로컬 컴퓨터에서 서버로 동영상을 업로드하려면 아래 명령어를 사용하세요. (PowerShell 추천)

```bash
scp local_video.mp4 ubuntu@3.37.3.170:~/hpe_project/sym/data/
```

- local_video.mp4 → 내 컴퓨터에 있는 동영상 파일 이름
- ubuntu@3.37.3.170 → 서버 로그인 정보
- ~/hpe_project/sym/data/ → 서버에서 저장할 폴더 경로
