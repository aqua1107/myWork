![20241228_174349](https://github.com/user-attachments/assets/31d584e8-7f6d-4d8d-b10b-34b8432c004c)

- JVM(Java Virtual Machine): 자바 가상 머신
- JRE(Java Runtime Environment): 자바 실행 환경
- JDK(Java Development Kit): 자바 어플리케이션을 개발하기 위한 환경을 지원하는 도구

## JVM 메모리 구조

![20241229_124515](https://github.com/user-attachments/assets/b6f14b1f-2332-4bb5-9a73-7f20232aea8c)


참고: 자바소스파일은 자바 컴파일러에 의해 바이트코드 형태인 클래스 파일이 된다. <br>
이 클래스 파일은 클래스 로더가 읽어들이면서 JVM이 수행됨.

## JVM 작동 원리 개념 정리
1. Class Loader: JVM내로 클래스 파일을 불러오고, 링크를 통해 배치하는 작업을 수행하는 모듈
2. Execution Engine: Class Loader를 통해 JVM 안의 Runtime Data Area에 배치된 바이트코드들을 명령어 단위로 읽어 실행.
3. Garbage Collector: Heap Memory Area에 만들어진 객체들 중에 참조되지 않은 객체들을 탐색 후 제거하는 역할을 함.
4. Runtime Data Area: JVM의 메모리 영역. 자바 실헹 시 사용되는 데이터들을 쌓는 영역.
- I. Static Area: 모든 스레트가 공유하는 메모리 영역(class, interface, method, field, static variable 등의 바이트코드를 보관.
- II. Heap Area: 객체와 배열아 생성되는 영역
- III. Stack Area: method 호출할 때마다 Stack Frame 생성.(즉, method 안의 값들을 저장) method 수행 종료 시 Frame별로 삭제.
- IV. PC Register: 스레드 시작 시 생성. 스레드 관련 기록함.(수행중인 JVM 명령의 주소를 갖음.)
- V. Native Method Stack: 다른 언어로 작성된 코드를 위한 메모리 영역

## JVM의 주요 특징
-->자바의 메모리 관리를 자동으로 해줌.

## 인터페이스
인터페이스: 소프트웨어 간 접촉, 공통되는 부분(접속, 연결)

## Java의 간략한 소개
### 자바 언어 플랫폼

1. JAVA SE(표준 에디션): JAVA 앱 개발
2. JAVA ME(휴대용 에디션): 소형 디바이스에서의 사용 목적으로 개발(스마트폰 등장 이후 소멸)
3. JAVA EE(기업용 에디션): 기업 솔루션 개발

## 자바 언어의 특징
1. JVM(가상머신)이 있어 운영체제와 독립
2. 메모리 관리 불필요(Garbage Collector)
3. OOP: 유지보수 & 개발 효율적 진행과 캡슐화, 상속, 다형성 등을 지원

## Method

method: 특정한 작업을 수행하는 코드의 묶음


시각화:
![20241229_131346](https://github.com/user-attachments/assets/05bb01f6-8334-41bb-8bd0-c0ee8020ce71)



보충: 파이썬에 input 입력값 내장함수가 있으면, 자바에는 Scanner라는 입력 클래스가 있다.


키보드 버퍼: 프로세스 실행 전, keystroke input을 임시저장하는 메모리 영역

## 변수
변수: 하나의 값이나 객체를 저장할 수 있는 메모리에 특정 번지에 붙여진 이름(Stack memory가 메모리 주소 할당)
<br> * 변수 타입이 필요한 이유: 메모리 할당과 확보
<br> * 변수는 선언만 하면 메모리 공간을 할당받지 못하기 때문에 반.드.시. 초기화 해야함.
<br> 로컬 변수: method 내에서 선언된 변수(실행 종료시 Stack Memory에서 pop됨. 즉, 로컬변수는 해당 method 내에서만 사용가능.)
<br> 리터럴: 변수의 초가값
<br> 큰따옴표: 문자열(String class(참조타입)), 작은따옴표: 문자 리터럴(문자 변수의 초기값)

## 상수
상수: 불변의 값(final)
사용이유
- 고정값이 필요할 때
- (관례)전체에서 하나의 값을 일관적으로 사용할때

## Overflow
- Overflow: 선언된 데이터 타입의 값보다 클 때
- Underflow: 선언된 데이터 타입의 값보다 작을 때

## 타입분류

![image](https://github.com/user-attachments/assets/5980497f-d708-409d-be5f-27085ce58190)
