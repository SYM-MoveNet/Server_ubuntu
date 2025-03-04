# Ubuntu 서버에서 Docker를 사용한 비디오 분석 실행 매뉴얼

이 문서는 **Ubuntu 서버에서 Docker를 설치하고, Docker 이미지를 다운로드하여 실행하는 방법**을 안내합니다.  
Docker를 사용하여 비디오를 분석하고, 분석 결과(JSON 파일)를 Ubuntu(호스트) 서버에 저장하는 방법을 설명합니다.

---

## **1. Ubuntu 서버에서 Docker 설치**
Ubuntu 서버에서 Docker가 설치되어 있지 않다면, 다음 명령어를 실행하여 설치합니다.

```bash
sudo wget -qO- https://get.docker.com/ | sh
```
설치가 완료되면 Docker 버전을 확인하여 정삭적으로 설치되었는지 확인

```bash
docker --version
```
## 출력예시
```bash
Docker version 27.2.0, build 3ab4256
```

## **2  Docekr Hub 에서 이미지 다운로드**
Docker Hub에 업로드된 leehakjin/sym:latest 이미지를 다운로드하려면 다음 명령어를 실행합니다.
```bash
sudo docker pull leehakjin/sym:latest
```
이미지가 정상적으로 다운로드되었는지 확인하려면
## 출력예시
```bash
REPOSITORY      TAG       IMAGE ID       CREATED      SIZE
leehakjin/sym   latest    5f7f6e9cd07a   3 days ago   8.04GB
```


## **3. 비디오 분석 실행**
# 컨테이너 실행(비디오분석)
호스트(Ubuntu 서버)에서 분석할 비디오가 위치한 경로를 컨테이너 내부로 마운트하여 실행합니다.
- 호스트(Ubuntu) 비디오 파일 경로: ex) /home/leehakjin/output/
- 컨테이너 내부에서 사용할 경로 :/app/sym/data/output/
```bash
sudo docker run --rm -it \
  -v /home/leehakjin/output:/app/sym/data/output \
  leehakjin/sym:latest --vid_path "/app/sym/data/output/동영상이름.mp4"
```











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

## 실행 방법
동영상 분석 실행방법

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
