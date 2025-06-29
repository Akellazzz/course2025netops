# напишите функцию api_request, которая принимает:
#  - method = только "GET", "POST", "DELETE"
#  - url = строка
#  - data = опциональный словарь, разрешен только для "POST"
# для "POST" data обязателен, для других методов data запрещен
# в написании поможет Literal + @overload. Нужно обеспечить следующий результат работы mypy:
#  - api_request("GET", "/user")                      ---> mypy без ошибок
#  - api_request("POST", "/user", {"name": "admin"})  ---> mypy без ошибок
#  - api_request("POST", "/user")                     ---> mypy выводит ошибку на эту строку
#  - api_request("GET", "/user", {"name": "admin"})   ---> mypy выводит ошибку на эту строку

from typing import Any, Literal, overload

Method = Literal["GET", "POST", "DELETE"]

@overload
def api_request(method: Literal["POST"], url: str, data: dict[str, Any] ) -> None: ...

@overload
def api_request(method: Literal["GET", "DELETE"], url: str) -> None: ...

def api_request(method: Method, url: str, data: dict[str, Any] | None = None) -> None: 
    if data:
        if method == "POST":
            print(f"send request: {method=} {url=} {data=}")
        else:
            raise ValueError("Параметр data допустим только в POST запросах")
    else:
        print(f"send request: {method=} {url=}")

if __name__ == "__main__":
    api_request("GET", "/user")  # mypy - OK
    api_request("POST", "/user", {"name": "admin"})  # mypy - OK
    api_request("POST", "/user")  # mypy - FAIL
    api_request("GET", "/user", {"name": "admin"})  # mypy - FAIL