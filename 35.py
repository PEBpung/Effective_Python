

# # Exception을 상속받은 MyError class


## -- 1번 --
# class MyError(Exception): 
#     pass

# def my_generator():
#     yield 1
#     yield 2
#     yield 3

# it = my_generator()
# print(next(it))  # 1을 내놓음
# print(next(it))  # 2를 내놓음
# # 에러를 주입
# print(it.throw(MyError('test error'))) # MyError 예외 발생

## -- 2번 --
# class MyError(Exception): 
#     pass
# def my_generator():
#     yield 1
#     try:
#         yield 2 # 여기까지 진행된 상태
#     except MyError:
#         print('MyError 발생!') # throw 로 받았음
#     else:
#         yield 3 # except에 들어 갔으니 패스
#     yield 4

# it = my_generator()
# print(next(it))  # 1을 내놓음
# print(next(it))  # 2를 내놓음
# print(it.throw(MyError('test error')))  # 4를 내놓음


## -- 3번 --
## throw 메서드에 의존하는 제네레이터를 통해 타이머를 구현
## 수동 예외처리를 위해 Exception 을 상속하는 클래스 생성
class Reset(Exception):
    pass

def timer(period):
    current = period
    while current:
        current -= 1
        try:
            yield current
        # --- 예외 준비 부분 ----
        # yield 식에서 Reset 예외가 발생할 때마다
        # current 카운터가 period 로 재설정 되도록 구현
        except Reset:            
            current = period     

RESETS = [
    False, False, False, True, False, True, False,
    False, False, False, False, False, False, False]

def check_for_reset():
     # RESETS 리스트에서 idx 0 하나씩 꺼냄
    return RESETS.pop(0)

def announce(remaining):
    print(f'{remaining} 틱 남음')

# timer 제너레이터를 구동시키는 run 함수 작성
def run():
    it = timer(4)
    while True:
        try:
            # ---- 에외 발생 부분 ----
            if check_for_reset():
                # throw 를 사용해 Reset 예외를 주입 
                current = it.throw(Reset())  
            else:
                current = next(it)
        except StopIteration:
            break
        else:
            # 제너레이터 출력에 대해 announce 함수 호출
            announce(current)                

run()

## 문제점!!
## throw를 사용를 사용하면 가독성이 나빠진다. 예외를 잡아내고 
## 다시 발생시키는 데 준비 코드가 필요하며 코드가 깊어지기 때문.

## -- 4번 --

class Timer:
    def __init__(self, period):
        self.current = period
        self.period = period

    def reset(self):
        self.current = self.period

    #__iter__ 메서드를 통해 이터러블 컨테이너 객체로 생성
    def __iter__(self):            
        while self.current:
            self.current -= 1
            yield self.current     # 제너레이터로 iter 객체 정의

RESETS = [
    False, False, False, True, False, True, False,
    False, False, False, False, False, False, False]

def check_for_reset():
     # RESETS 리스트에서 idx 0 하나씩 꺼냄
    return RESETS.pop(0)

def announce(remaining):
    print(f'{remaining} 틱 남음')

def run():
    timer = Timer(4)
    # for를 사용하여 timer에 대해 간결하게 이터레이션 수행 가능
    # __iter__ 매직매서드가 정의되어 있기 때문에 가능!
    for current in timer:       
        if check_for_reset():
            timer.reset()
        announce(current)

run()

# 가독성이 더 좋아졌다.

## -- 추가 --
## __iter__ 과 __next__ 비교!

class Test:
    def __init__(self, current):
        self.current = current    # 현재 숫자 유지, 0부터 지정된 숫자 직전까지 반복
        self.stop = 0    # 반복을 끝낼 숫자
 
    def __iter__(self):
        print('__iter__ 호출')
        return self         # 현재 인스턴스를 반환
 
    def __next__(self):
        print('__next__ 호출')
        if self.current > self.stop:    # 현재 숫자가 반복을 끝낼 숫자보다 작을 때
            r = self.current            # 반환할 숫자를 변수에 저장
            self.current -= 1           # 현재 숫자를 1 증가시킴
            return r                    # 숫자를 반환
        else:                           # 현재 숫자가 반복을 끝낼 숫자보다 크거나 같을 때
            raise StopIteration         # 예외 발생


# class Test:
#     def __init__(self, current):
#         self.current = current 
#         self.stop = 0

#     #__iter__ 메서드를 통해 이터러블 컨테이너 객체로 생성
#     def __iter__(self):      
#         print('__iter__ 호출')      
#         while self.current:
#             print('반복')
#             self.current -= 1
#             yield self.current



# it = iter(Test(3))

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it, 10))

test = Test(3)
print(next(test))
# - iter : 반복 가능한 객체에서 이터레이터를 반환
# - next : 이터레이터에서 값을 차례대로 꺼냄

# __iter__ : 객체를 반복 가능한 객체로 만들어준다.
# __next__ : 차례대로 호출된다.