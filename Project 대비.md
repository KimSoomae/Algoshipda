# Project 대비



## 1. 5주차 - Web

 - ### HTML / CSS

    - HTML 기본구조 및 속성 (tag), 시멘틱 태그 (37P~)
       - HTML 문서 구조화(66P~)
    - CSS 입문, 선택자 및 단위, 자손/자식 결합자 (81P~)
    - CSS BOX MODEL (132P~)
       - margin, padding, box sizing
       - Display 속성
       - fixed, absolute positioning

 - ### 그리드 시스템/ 반응형 웹

    - Flex box control (20P~)
       - flex item에 대한 정렬 수행
       - container, justify, flex, start, end, align, direction 등
   - BOOTSTRAP (54P)
     - css를 Bootstrap 스타일로 어떻게 바꾸는지( 예: mx-auto)
   - 반응형 그리드 웹(93P~)
     - Breakpoint
     - 사용자 경험 향상에 도움
     
     

## 2. 9주차 - Django start

 - ### Template, View, Routing / django-share, 00이전내용들에 django-01있음

    - Web Framework(4P)
      - 기본개념, MTV패턴
      - 요청과 응답, templates
      - 변수 및 태그 적용
    - HTML Form(63P)
      - input, label, for, id 등에 대한 개념
      - Throw & Catch
      - Django에서 URL을 관리하는 법

 - ### Model 

    - Database와 Model ( 5P ~)
       - modelField설정 ~ Migrate까지의 과정, sqlmigrate, 
    - Django CRUD실습(53P~)
       - 이후 과정에서 완성된 템플릿 사용하는것을 추천
       - 개념정리 차원에서 이용



## 3. 10주차 - Django 심화1

 - ### Form / ModelForm

   -  ModelForm (16P~)
      - ModelForm을 왜쓰는지
      - 여러 세부사항(위젯) 적용하기
   -  Bootstarp과 함께 사용하기(42P~)
      - Bootstarp을 html에 적용하는 방법
      - Django에서 HttpMethod를 처리하는 방법, decorator




 - ### STATIC, MEDIA files

    - STATIC 파일 및 Media 파일을 어떻게 넣을것인가(5P~)
    
      - STATIC ROOT, URL 등 
      - Media ROOT, 그외 자잘한 세팅 가이드
    
    - 이미지 업로드 ( 28P~ ) 
    
      - 이미지 업로드, 수정까지의 과정, django view.py에서 file 객체 처리
    
        

## 4. 11주차 - Django 심화 2

 - ### 사용자 인증 권한

    - 로그인 / 로그아웃(5P~)
      - Authentication form, 쿠키와 세션, 접근제한, 관련 데코레이터
    - 회원가입 / 회원탈퇴 (70P~)
      - 회원가입, UserCreationForm, 회원정보 수정, 비밀번호 수정

## 5. 16주차 - DB

 - ### 1:N DB관계(월)

    - Foreign Key: 한명이 여러 댓글 작성 / 
    - **Comment(32P~)** : CRUD
    - Custom UserModel 적용하기
    - User-Article(67P~), User-Comment(80P~)

 - ### M:N DB관계(수)

    - ManyToManyField(37P~)
    - Like구현(54P~), Profile Page(67P~), Follow(74P~)
    
    

## 6. 17주차 - REST API, JS start

 - ### REST API

    - RESTFUL API(4P~)
      - HTTP(5P~), 
      - RESTful API(20P~)
      - JSON response(28P~)
    - Single Model, Serializer, ModelSerializer(53P~)
      - POSTMan 사용 및 CRUD
      - 1:N Relation 적용
      - 예제별로 예시코드 수록(게시글에 작성된 댓글 목록 출력)

 - ### JS기초

   	- DOM(28P~)
   	
   	  - 선택, 생성, 삭제, 추가 관련 조작
   	
   	- EVENT(68P~)
   	
   	  - 이벤트 추가, 정지등 동적 페이지를 위한 조작
   	
   	  

## 7. 18주차 - JS 심화,  VUE CDN

 - ### JS심화

    -  AJAX(8P~)
    -  Asynchronous JS(14P~)
       -  동기 및 비동기식 처리에 대한 개념정리 
       -  Callback Function(50P~)
       -  Promise(.then, .catch 등)
    -  Axios
       -  Axios적용해보기

 - ### VUE CDN

    - Vue.js 소개(5P~)
      - SPA, CSR, SSR
      - MVVM Pattern
      - 기본 적용법(44P~)
    - Vue.js 기본(52P~)
      - if, for, vind 등 세부 method에 대한 조작
      - computed, watch, method 비교
    - Lifecycle Hook, Lodash(78P~)
    
    

## 8. 19주차 - VUE 심화

 - ### VUE CLI와 VUE ROUTER

    -  Vue Cli(16P~)
       -  Vue 구조 소개
    -  Pass Props & Emit Events(43P~)
       -  Props/Emit 개념 및 실제 적용 코드
    -  Vue Router(65P~)
       -  프로그래밍 방식 네비게이션
       -  컴포넌트와 view 비교, 
    -  Youtube Project(88P~)
       -  youtube API를 이용하여 동영상 정보를 가져오는 방법
       -  검색 및 출력까지의 과정

 - ### 컴포넌트간 데이터 통신과 VUEX

    - Vuex(5P~)
      - state, actions, mutations, getters에 대한 개념 소개 및 Vuex cycle 소개
      - 개념정리 차원
    - Set Project & component(39P) : 기본설정 적용하기
    - Todo CRUD 작성(48P)
      - Getters(71P)
      - mapState(78P)

