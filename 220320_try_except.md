# 220320 try~ except~

## Bakjoon OJ 10951번 문제
```
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력은 여러 개의 테스트 케이스로 이루어져 있다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
```

해당 문제는 Baekjoon OJ 내 10951번 문제이다.

위 문제를 풀던 중, 난관에 봉착하였다.

```python
while True:
    a, b = map(int,input().split())
    if a > 0 and b < 10:
        print(a + b)
    else:
        break
```

분명 맞는 답안을 제출하였다 생각했지만, ```EOFERROR``` 라는 알 수 없는 오류로 인해 오답처리가 된 것이다.

## EOFERROR

문제를 다시 읽어본 결과, 해당 문제를 잘못 이해하였음을 알게 되었다.

0 < A, B < 10라는 조건을 보고, 채점 과정에서 자연히 ```A, B = 0, 10```과 같은 예외 사항이 입력되어 while문이 종료되리라 생각했다. 컴퓨터는 스스로 0 >= A, B >= 10를 입력하는 일이 없었다.

결국 컴퓨터는 해당 조건을 만족하는 범위 내에서 연산을 진행하게되고, 더이상 입력받을 값이 없는데도 계속 입력을 요구하니 EOFError가 발생하게 되는 것이다.

EOF는 End of File의 약자로, 정의는 다음과 같다.

_**데이터 소스로부터 터 이상 읽을 수 있는 데이터가 없음을 나타낸다.**_

# 예외처리

그렇다면, 위와 같은 에러 상황을 만나게 되면 어떻게 해야할까? 그 해답은 예외처리에 있다.

```python
while True:
    try:
        a, b = map(int,input().split())
        print(a + b)
    except EOFError:
        break
```

위 오답을 수정한 결과이다. 

```try``` 아래의 code context들을 진행하는 중, ```EOFError```가 발생하면 그 아래에 해당하는 code context를 진행시키라는 명령어이다.

해당 답안에서는 EOFError 상황만을 예외처리하였지만, ```except``` 뒤에 무엇이 오는 지에 따라 다른 상황을 예외로 처리할 수도 있다. `ZeroDivisionError`, `ValueError`, `IndexError` 등이 그 예이다. 더불어 `except`를 여러번 사용하여 여러 예외 사항에 대한 명령어를 입력할 수도 있고, except 뒤에 아무런 예외 사항을 적지 않고 `except:`로 마무리하여 모든 예외 사항을 한번에 처리할 수도 있다.