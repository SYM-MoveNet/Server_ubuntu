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

### 프로젝트 다운
```bash
git clone git@github.com:dlgkrwls/Server_ubuntu.git
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
웹서버에서 저장시키면되는 파일경로는  

```bash
docker run --rm -it -v /home/ubuntu/hpe_project/sym/data/output/:/app/sym/data/output/sym --vid_path "./sym/data/동영상이름.mp4"
```

호스트(Ubuntu)의 /home/ubuntu/hpe_project/sym/data/에 있는 동영상을 분석    
컨테이너 내부에서 동영상을 처리하여 JSON 파일을 생성
분석이 끝나면, 결과 JSON 파일이 Ubuntu(호스트)에 저장됨
컨테이너가 종료되더라도 JSON 파일은 유지됨!

동영상 실행시 data/out/비디오.json 파일 생성
```bash
ls -lh /home/ubuntu/hpe_project/sym/data/output/
```
여기에 동영상이름.json이 존재하게됨
## 동영상 업로드 방법
# 동영상을 저장할 경로: /home/ubuntu/hpe_project/sym/data/
로컬 컴퓨터에서 서버로 동영상을 업로드하려면 아래 명령어를 사용하세요. (PowerShell 추천)

```bash
scp local_video.mp4 ubuntu@3.37.3.170:~/hpe_project/data/
```

- local_video.mp4 → 내 컴퓨터에 있는 동영상 파일 이름
- ubuntu@3.37.3.170 → 서버 로그인 정보
- ~/hpe_project/sym/data/ → 서버에서 저장할 폴더 경로
