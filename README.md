# 서버_우분투
설정_서버_도커

# 이미지를 다운받고 사용하는법

### ubuntu 서버에 필요한 docker 설치
```bash
sudo wget -qO- http://get.docker.com/ | sh
```

## Docker PUll
Docker Hub에 있는 이미지를 pull 받는법
```bash
sudo docker pull leehakjin/sym:lastest
```
image pull확인방법
```bash
docker images
```


### 디렉토리 이동 
```bash
cd ~/Server_ubuntu/hpe_project
```


## 실행 방법
동영상 분석 실행방법


### Docker 이미지 빌드 (필요 시 실행)
docker build -t sym .ac

### Docker 실행 (비디오 분석)
호스트(리눅스서버)경로: 서버에 맞게 파일에 맞춰서
컨테이너 내부경로:/app/sym/data/output/

예시
```bash
sudo docker run --rm -it   -v /home/leehakjin/output:/app/sym/data/output   leehakjin/sym:latest --vid_path "./sym/data/동영상이름.mp4"
```

호스트(Ubuntu)의 /home/leehakjin/output/에 있는 동영상을 분석    
- 컨테이너 내부에서 동영상을 처리하여 JSON 파일을 생성
- JSON 파일이 Ubuntu(호스트)에 저장됨
- 컨

```bash
ls -lh /home/ubuntu/hpe_project/sym/data/output/
```
여기에 동영상이름.json이 존재하게됨


## 개발자
코드적으로 확인
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
