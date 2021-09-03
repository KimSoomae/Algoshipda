# Algoshipda
SSAFY 6기 광주 2반 알고리즘 스터디(알고쉽다)

**규칙**

- 1일 1 커밋
- 서로의 코드 구경하며 좋은 코드 흡수하기
- 주말에 한번 설명이 필요한 코드 설명 및 refresh 시간

**git사용법**

1. 관리할 로컬 저장소 생성(본인 컴퓨터 어딘가에 폴더 만들기)

2. 콘솔에서(cmd, git bash, 터미널 등) 1번의 폴더로 이동
```console
cd 파일경로명
```

3. git 저장소 생성
```console
git init
```

4. 원격 저장소 연결
```console
git remote add origin https://github.com/KimSoomae/Algoshipda.git
```

5. 잘 연결 되었는지 확인 -> origin 나오면 잘 된거
```console
git remote -v
```

6. 본인 푸시 전에 최종 업뎃 된 다른 사람들 것 받아오기
```console
 git pull origin master
```

7. 파일 올리기
```console
git add "파일명"
```

한꺼번에 다 올려버리기
```console
git add .
```

8. 커밋- 커밋 메세지는 체크하기 쉽게 날짜포함하면 좋을 거 같아요
```console
git commit -m "커밋 메세지"
```

9. 원격 저장소에 푸쉬
```console
git push -u origin master
```

10. 잘 올라갔는지 확인

