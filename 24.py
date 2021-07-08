########
# None과 독스트링을 사용해 동적인 디폴트 인자를 지정하라.
########

from time import sleep
from datetime import datetime
import json
from typing import Optional

# # -- 1번 --
# def log(message, when=datetime.now()):
#     print(f'{when}: {message}')

# log('안녕!')
# sleep(0.1)
# log('다시 안녕!')

# -- 2번 --

# 독스트링(docstring)은 함수 시작 부분에서 함수 인터페이스를 
# 설명하는 문자열이다(“doc”은 “documentation”의 줄임말이다).

# def log(message, when=None):
#     """메시지와 타임스탬프를 로그에 남긴다.
#     Args:
#         message: 출력할 메시지.
#         when: 메시지가 발생한 시각(datetime).
#             디폴트 값은 현재 시간이다.
#     """
#     if when is None:
#         when = datetime.now()
#     print(f'{when}: {message}')

# log('안녕!')
# sleep(0.1)
# log('다시 안녕!')

# 함수가 정의되는 시점에 호출!!

# # # -- 3번 --
# 인자가 가변적인 경우 특히 중요!
# 단 한번만 평가
# def decode(data, default={}):
#     try:
#         return json.loads(data)
#     except ValueError:
#         return default

# foo = decode('~/id.json')
# foo['stuff'] = 5
# bar = decode('또 잘못된 데이터')
# bar['meep'] = 1
# print('Foo:', foo)
# print('Bar:', bar)

# print(id(foo))
# print(id(bar))

# assert foo is bar

# # # -- 4번 --
# def decode(data, default=None):
#     """문자열로부터 JSON 데이터를 읽어온다.
#     Args:
#         data: 디코딩할 JSON 데이터.
#         default: 디코딩 실패시 반환할 값이다.
#             디폴트 값은 빈 딕셔너리다.
#     """
#     try:
#         return json.loads(data)
#     except ValueError:
#         # 위의 함수에서는 return default
#         if default is None:
#             default = {}
#         return default


# foo = decode('잘못된 데이터')
# foo['stuff'] = 5
# bar = decode('또 잘못된 데이터')
# bar['meep'] = 1
# print('Foo:', foo)
# print('Bar:', bar)
# assert foo is not bar

# print(id(foo))
# print(id(bar))

# # # -- 5번 --

def log_typed(message: str,
              when: Optional[dict]=None) -> None:
    """메시지와 타임스탬프를 로그에 남긴다.
    Args:
        message: 출력할 메시지.
        when: 메시지가 발생한 시각(datetime).
            디폴트 값은 현재 시간이다.
    """
    if when is None:
        when = datetime.now()
    print(f'{when}: {message}')

log_typed('타입 에러')