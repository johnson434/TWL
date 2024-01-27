# 👀 Annotation이란? (어노테이션, 애너테이션)

" **주석처럼 프로그래밍 언어에 영향을 미치지 않으며, 유용한 정보를 제공한다.**



```
@IntRange(1,5)
public void functiom(int num) {
    if (num > 5 || num < 1) {
        throw Exception();
    }
}

main() {
    function(10);
}

```

## 📌 Annotation 역할 

✔️ 컴파일러에게 문법 에러를 체크하도록 정보를 제공한다.

✔️ 프로그램을 빌드할 때 코드를 자동으로 생성할 수 있도록 정보를 제공한다.

✔️ 런타임에 특정 기능을 실행하도록 정보를 제공한다. (Reflection)





## 📌 Annotation 종류(표준 어노테이션, 메타 어노테이션)



✔️ 표준 어노테이션 : 자바에서 기본적으로 제공하는 어노테이션

✔️ 메타 어노테이션 : 어노테이션을 위한 어노테이션, 어노테이션을 개발 시 활용

✔️ 사용자 정의 어노테이션 : 메타 어노테이션을 통해 개발자가 원하는 어노테이션 정의하여 활용





## 📌 Meta Annotation 종류(메타 어노테이션)

## 🔍 @**Target**

✔️ 어노테이션을 적용할 수 있는 대상의 지정에 사용



```java
@Target({TYPE, FIELD, METHOD})
public @interface TestAnnotation() {}
```

### 🔍 @**Retention**

✔️ 어노테이션이 유지(Retention) 되는 기간을 지정하는데 사용



```java
@Retention(RetentionPolicy.RUNTIME)
public @interface FunctionalInterface {}
```



❓ 의문점 : SOURCE 레벨과 CLASS 레벨은 차이가 없어 보인다. 뭘까?



롬복에서 자주 사용하는 @Getter 와 @NotNull 어노테이션이 존재한다.

@Getter 는 SOURCE 레벨로 정의했고, @NotNull은 CLASS 레벨로 정의했다.

두 기능의 공통점은 JAVA파일을 CLASS 파일로 컴파일할 때 특정 코드를 삽입한다는 것이다.



하지만 차이점이 존재하는데, 

SOURCE 레벨은 CLASS 파일에 어노테이션이 남아있지 않다는 것이고

CLASS 레벨은 CLASS 파일에 어노테이션이 그대로 유지된다는 점이다. 

→ CLASS 파일을 디컴파일해보면 확인할 수 있다



추가되는 기능은 같고 그럼 언제 CLASS 레벨을 써야하는걸까?

→ 우리는 개발하면서 다양한 jar 파일, 라이브러리를 포함하여 개발을 진행한다.

라이브러리는 대부분 jar 파일로 관리되고있고, 해당 jar파일엔 java파일이 아니라 class 파일들만 모여있다.



어노테이션을 활용하여 기능을 구현한 라이브러리들을 사용하면서 IDE의 경고메시지, 타입 체크 등을 사용하기 위해서 CLASS 정책이 필요한 것이다.



→ 참고 :  @Retention SOURCE VS CLASS

### 🔍 @**Inherited**

✔️ 자손 클래스에 상속하고자 할 때 사용

```java
@Inherited
public @interface TestAnno() {}

@TestAnno
class Parent {}
class Child extends Parent {} // Child에 어노테이션이 붙은걸로 인식

```

### 🔍 @**Repeatable** 

✔️ 반복해서 붙일 수 있는 어노테이션을 정의할 때 사용

```java
@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
public @interface Todos {
    Todo[] value();
}

@Repeatable(Todos.class)
public @interface Todo {
    String value() default "";
}

@Todo("집 가기")
@Todo("빨래 하기")
class MyClass {}
```

### 🔍 @**Documented**

✔️ javadoc으로 작성한 문서에 포함시키려면 사용





## 📌 사용자 정의 Annotation (RUNTIME)

```java
public class Anno {

    @Target(ElementType.TYPE)
    @Retention(RetentionPolicy.RUNTIME)
    public @interface Todos {
        Todo[] value();
    }

    @Repeatable(Todos.class)
    public @interface Todo {
        String value() default "";
        int num();
    }

    @Todo(value = "집 가기", num = 0)
    @Todo(value = "빨래 하기", num = 1)
    class MyClass {

    }

    public static void main(String[] args) {
        Annotation[] annotations = MyClass.class.getDeclaredAnnotations();
//        Annotation[] annotations = MyClass.class.getAnnotations();

        for (Annotation i : annotations) {
            if (i instanceof Todos) {
                Todos todos = (Todos) i;
                for (Todo todo : todos.value()) {
                    System.out.println(todo.num() + " : " + todo.value());
                }
            }
        }
    }
}
```



```
// 출력
0 : 집 가기
1 : 빨래 하기
```



❓ getDeclaredAnnotations() vs getAnnotations() 

→ getDeclaredAnnotations : 상속 어노테이션(@inherited) 제외하고 가져옴

→ getAnnotations() : 다 가져옴



참고 → getDeclaredAnnotations() vs getAnnotations() 





## 📌 사용자 정의 Annotation (SOURCE, CLASS)

```java
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.SOURCE)
public @interface Override {}
```



@Getter로 예시를 들면 직접 JAVA 파일에는 getter() 메서드를 작성하지 않았지만, 어노테이션을 지정을 통해 자동적으로 추가되어 사용할 수 있다. 해당 원리는 컴파일 시점에 의도된 동작을 삽입하는 것이다.

컴파일시점에 getter메서드를 추가해주기 위해선 Annotation Processor 라는 것을 활용하면 된다.

RUNTIME 레벨이 런타임에 리플렉션을 통해 어노테이션을 핸들링한다면, SOURCE, CLASS는 컴파일 시점에 Annotation Processor를 통해 핸들링하는 것이다.



참고 → Annotation Processor





```
class UserDto {
    @LengthLimit(1,10)
    String name;
}

@UserNameValidation
method(String name) {
    
}
```



# 리플렉션

- 실행 시점(동적)에 객체의 프로퍼티와 메소드에 접근할 수 있게 해주는 방법
- 사용 시점 
  - 1. 타입과 관계 없이 객체를 다뤄야 하는 경우



```kotlin
import kotlin.reflect.full.findAnnotation
import kotlin.reflect.full.memberProperties

@Retention(AnnotationRetention.RUNTIME)
@Target(AnnotationTarget.PROPERTY)
annotation class JsonExclude

@Retention(AnnotationRetention.RUNTIME)
@Target(AnnotationTarget.PROPERTY)
annotation class JsonName

class Person(@JsonExclude val name: String, @JsonName val age: Int)

// { name : dd, age : 1}

fun main() {
    val personKClass = Person::class
    // JsonExclude 어노테이션이 없는 변수들만 리턴.
    personKClass.memberProperties
        .filter { it.findAnnotation<JsonExclude>() == null }
        .forEach { println(it.name) }
}
```



## **어노테이션 스터디**

**날짜 :** 2024-01-13, 1:00 PM

Attendees: [문상후](mailto:sanghoo.moon@gmail.com) [최승복](mailto:sbok1126@gmail.com) [ig h](mailto:ghkddlsrb96@gmail.com) 

**논의 사항**

- [ ] 어노테이션 스터디

