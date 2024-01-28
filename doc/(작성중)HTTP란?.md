## **HTTP(Hyper-Text Transfer Protocol)란?**

1. 클라이언트와 서버 간의 통신을 위한 규칙을 정의
2. HTML , 이미지, 동영상 등의 하이퍼미디어 문서를 전송하고, 웹 브라우저와 웹 서버 간의 상호작용을 지원



## **HTTP의 동작방식**

- Stateless(무상태성)

   1. 각 요청은 서버에 저장된 상태 정보를 사용하지 않고 독립적으로 처리된다.
   2. 각 요청은 이전 요청과 관련이 없으며 서버는 클라이언트의 상태를 유지하지 않습니다.



>> **무상태성을 지키지 않은 경우(서버 사이드 렌더링(SSR)을 통해 구현)**

사용자 컴퓨터 ←→ 주문 API서버(서버)

API 서버 : 세션 체크 및 로그인 등 체크가 필요하므로 순수한 무상태성이라고 보긴 힘듬?

>> **무상태성을 엄격하게 지킨 경우(클라이언트 사이드 렌더링(CSR)을 통해 구현)**

사용자 컴퓨터 ←→ 프론트서버(서버) ←→ 주문 API서버(서버)

프론트 서버 : 세션 체크 및 로그인 관리

API 서버 : 프론트 서버를 통해 세션 체크 및 로그인 등 체크가 끝났으므로 순수한 API 요청만 검증하면 됨.





[https://sanghoo.tistory.com/54](https://sanghoo.tistory.com/54)



**1. 장점**

>> 확장성

독립적이기 때문에 서버는 각 요청을 개별적으로 처리 가능

>> 간단한 구현 및 유지보수

서버가 클라이언트의 상태를 유지하지 않기 때문에 서버 측에서의 복잡한 세션 관리가 필요하지않음



**2.단점**

>> 상태유지의 부재

각각의 요청이 독립적으로 처리되기 때문에 클라이언트의 상태를 서버가 기억하지 않으므로 일부 불편할수 있음

>> 세션관리의 어려움

특정 작업의 진행 상태를 유지하거나 사용자 세션을 효과적으로 관리하기 위해서는 클라이언트와 서버 간의 추가적인 처리가 필요



- Request-Response

   1. 클라이언트는 서버에게 요청을 보내고, 서버는 이에 대한 응답을 반환한다.



## 메서드

>> GET

   1. 특정한 리소스를 가져오도록 요청하며 데이터를 가져올때만 사용해야한다.

```java
GET /index.html HTTP/1.1
Host: www.google.com
```



>> POST

   1. 서버로 데이터를 전송하며 유형은 Content-Type 헤더로 나타난다.

```java
POST /submit HTTP/1.1
Host: www.google.com
Content-Type: application/x-www-form-urlencoded

username=seungbok&password=1234
```



OPTIONS / PUT / DELETE / PATCH

```
url : www.google.com/user
GET(조회) : 유저를 가져온다.
DELETE(삭제) : 유저를 지운다.
PATCH(수정) : 유저를 수정한다.
PUT(덮어쓰기) : 유저를 덮어쓴다.
```

## HTTP응답코드

# [수신 성공(200)](https://developer.mozilla.org/ko/docs/Web/HTTP/Status)

### 1. 200 OK

- 정상적으로 수행되었을때 

### 2. 301 Moved Permanently

- 해당 URI이 다른 주소로 바뀌었을때

```java
HTTP/1.1 301 Moved Permanently
Location: http://www.example.org/index.asp
```

### 3. 400 Bad Request

- 해당 요청이 잘못된 요청일때 보내는 코드.
- 주로 요청에 포함된 input 값들이 잘못된 값들로 보내졌을때

### 4.  401 Unauthorized

- 유저가 해당 요청을 진행 할때 먼저 로그인을 하거나 회원 가입을 하는등 사전권한이 필요할 때

### 5. 403 Forbidden

- 유저가 해당 요청에 대한 권한이 없음
- 예를 들어 권한이 존재하는 유저만 볼 수 있는 데이터를 요청 할때

### 6. 404 Not Found

- 요청된 URL이 존재 하지 않을때

## 참조 사이트

HTTP 상태 코드 : [https://developer.mozilla.org/ko/docs/Web/HTTP/Status](https://developer.mozilla.org/ko/docs/Web/HTTP/Status)

HTTP : [https://developer.mozilla.org/ko/docs/Web/HTTP](https://developer.mozilla.org/ko/docs/Web/HTTP)

