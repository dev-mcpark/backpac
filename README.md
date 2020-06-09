# backpac

#### homework

django 서버 실행
```angular2
docker-compose up
```
---
관리자 계정 만들기
```angular2
docker-compose run backpac python manage.py createsuperuser
```

---
#### api 문서
> localhost:8000/docs/

#### 주요 api 정리
- 회원가입
> POST /rest-auth/registration/
>   > Request Body parameter
>   > * username* : 이름
>   > * email* : 이메일
>   > * password1* : 패스워드
>   > * password2* : 패스워드 확인
>   > * nickname* : 별명
>   > * gender : 성별
- 로그인
> POST /rest_auth/login/
>   > Request Body parameter
>   > * username* : 이름
>   > * email* : 이메일
>   > * password1* : 패스워드
- 로그아웃
> POST /rest_auth/logout/
>   > header
>   > * Authorization : Token {token}
- 회원 목록
> GET /users
>   > header
>   > * Authorization : Token {token}

>   > Query parameter
>   > * username : 이름
>   > * email : 이메일
- 회원 상세
> GET /users/{id}/
>   > header
>   > * Authorization : Token {token}
- 회원 주문 목록
> GET /users/{id}/orders/
>   > header
>   > * Authorization : Token {token}
- 주문 추가
> POST /orders/
>   > header
>   > * Authorization : Token {token}

>   > Request Body parameter
>   > * product : 제품명
