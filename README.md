🛠 Docker 기반 비디오 분석 실행 가이드

이 가이드는 Docker 이미지를 다운로드하고 실행하는 방법을 설명합니다.별도의 Git 클론 없이도 Docker만 설치되어 있다면 즉시 실행 가능합니다! 🚀

✅ 1. Docker 설치 (필요 시)

📌 Ubuntu (리눅스)

sudo apt update && sudo apt install -y docker.io

또는 공식 스크립트로 설치:

sudo wget -qO- http://get.docker.com/ | sh

📌 Windows & Mac

Docker 공식 다운로드

Docker Desktop을 설치하고 실행하면 됩니다.


# 서버_우분투
설정_서버_도커


# 서버 접속
```bash
ssh ubuntu@서버_IP
```

### Ubuntu 서버에서 Git 설치 (이미 설치되어 있으면 생략)

```bash
sudo apt update && sudo apt install -y git
```


### ubuntu 서버에 필요한 docker 설치
```bash
sudo wget -qO- http://get.docker.com/ | sh
```

## Docker PUll
Docker Hub에 있는 이미지를 pull 받는법
```bash
docker pull leehakjin/sym:latest
```


### 디렉토리 이동 
```bash
cd ~/Server_ubuntu/hpe_project
```


## 실행 방법
동영상 분석 실행방법


### Docker 이미지 빌드 (필요 시 실행)
docker build -t sym .

### Docker 실행 (비디오 분석)
웹서버에서 저장시키면되는 파일경로는  

```bash
docker run --rm -it -v /home/ubuntu/hpe_project/sym/data/output/:/app/sym/data/output/ sym --vid_path "./sym/data/동영상이름.mp4"
```

호스트(Ubuntu)의 /home/ubuntu/hpe_project/sym/data/에 있는 동영상을 분석    
- 컨테이너 내부에서 동영상을 처리하여 JSON 파일을 생성
- JSON 파일이 Ubuntu(호스트)에 저장됨
- 컨테이너가 종료되더라도 JSON 파일은 유지됨!

```bash
ls -lh /home/ubuntu/hpe_project/sym/data/output/
```
여기에 동영상이름.json이 존재하게됨
## 동영상 업로드 방법
# 동영상을 저장할 경로: /home/ubuntu/hpe_project/sym/data/
로컬 컴퓨터에서 서버로 동영상을 업로드하려면 아래 명령어를 사용하세요. (PowerShell 추천)



### 프로젝트 다운
```bash
git clone git@github.com:dlgkrwls/Server_ubuntu.git
```

```bash
scp local_video.mp4 ubuntu@IP:~/hpe_project/data/
```

- local_video.mp4 → 내 컴퓨터에 있는 동영상 파일 이름
- ubuntu@IP → 서버 로그인 정보
- ~/hpe_project/sym/data/ → 서버에서 저장할 폴더 경로
