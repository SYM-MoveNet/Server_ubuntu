# 서버_우분투
설정_서버_도커


# 서버 접속
```bash
ssh ubuntu@3.37.3.170
```

### Ubuntu 서버에서 Git 설치 (이미 설치되어 있으면 생략)

```bash
sudo apt update && sudo apt install -y git
```

### 프로젝트 다운
```bash
git clone https://github.com/dlgkrwls/Server_ubuntu.git
```

### ubuntu 서버에 필요한 docker 설치
```bash
sudo wget -qO- http://get.docker.com/ | sh
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

```bash
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
