# 오늘 배웠던 내용에 대해 md 파일로 작성해보는 시간

## git의 기초

### git, github는 왜 해야하는가?

- 버전 관리의 목적 : 백업, 복구, 협업
- 포트폴리오 관리

### CLI

`touch`, `pwd`, `cd`, `mkdir`, `rm`, `rm -r` 등등

### git의 세 공간

*workind directory* -> *staging area* -> *commits*

## git 이용 방법

### 작성자 이름, 메일 등록 (최초 1번만 실행)

```bash
git config --global user.name "github username"
git config --global user.email "github email"
```
- 이후 username 변경하고 싶다면 다시 입력하면 되지만, url 등도 수정해야한다.
- `git config --global core.editor “code --wait”`
    - 입력 시 code 이후 띄어쓰기 주의


### config 정보 출력

```bash
git config --global --list
```

### 일반 폴더 -> 로컬 저장소

```bash
git init
```

### 버전 상태 출력

```bash
git status
```

### Working Directory -> Staging Area

```bash
git add [File]
git add .  # 모든 파일 add
```

### Staging Area -> Commits

```bash
git commit -m "commit message"
```

### commits 목록 출력

```bash
git log
git log --oneline  # 한줄로 보기 옵션
git log -p  # 커밋마다 차이 보기 옵션
```
- `git log` 입력 이후, 열이 초과되어 입력이 되지 않는 이슈가 발생하면? 
    - Q 키로 종료 가능
    - Z 키로 다음 내용 확인 가능

### commit 이후 원격 저장소에 저장하기
```bash
git remote add origin [원격 저장소 url]
git push origin master
```
```git remote -b 는 remote가 어떻게 연결됐는지 확인하는 명령어 ```
