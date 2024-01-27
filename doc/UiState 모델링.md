https://velog.io/@vov3616/Android-State-Modeling-%EC%96%B4%EB%96%A4%EA%B2%8C-%EC%A2%8B%EC%9D%84%EA%B9%8C-6l780eug

안드로이드 MVVM 구조에서 ViewModel이 가지는 State를 어떻게 표현하면 좋을지 작성한 글입니다.

저도 늘 고민했던 주제였고, 어떤 방법이 좋을까 생각을 했었는데 위의 글은 각각 코드의 장단점을 쉽게 작성했습니다.

MVVM 구조에 대해서 모르는 분을 위해 사전 지식을 먼저 설명하겠습니다.

# MVVM 구조란?





MVC(Model-View-Controller) 패턴의 경우, View에서 Input을 받고 Controller에서 Model에 데이터를 요청합니다. 후에 Contoller는 Model에서 받은 데이터와 함께 View를 리턴합니다.

MVVM(Model-View-ViewModel)은 여기서 ViewModel이 Controller의 역할을 합니다.

하지만, MVVM은 ViewModel에서 View에 데이터를 전달하지 않습니다. 그렇다면 어떻게 View에서 데이터를 받느냐? View는 ViewModel의 데이터를 관찰하면서 업데이트 되는 걸 기다립니다. 그리고 업데이트가 일어나면 View를 수정합니다.

이러한 특징을 **UDF(Undirectional Data Flow : 단방향 데이터 플로우)**라고 합니다.

이처럼 MVVM에선 ViewModel와 View가 독립적이므로 테스트에 용이합니다.



아래 코드들은 의사 코드라 실제로 동작하지 않을 수도 있어요.

```kotlin
// View의 코드
fun MainScreen(viewModel: MainViewModel) {
    Text(
        content = viewModel.uiData
    )

    Button(
        onClick = viewModel.performAction()
    ) {
        Text(content = "Button Name")
    }
}

// ViewModel의 코드
class MainViewModel {
    val repository = Repository()
    val uiData = mutableStateFlow("empty")
    
    fun performAction() { 
        val data = repository.getData()    
        uiData.value = data
    }
}
```

# UiState란 뭐냐?

UiState란 ViewModel에서 데이터를 담고 있을 곳을 말합니다.

UiState를 쓰지 않을 시 코드는 아래와 같습니다.

```kotlin
class MainViewModel {
    val bookNames = mutableStateFlow{ listOf("book1", "book2") }
    val userNames = mutableStateFlow{ listOf("user1", "user2") }
    val isLoading = mutableStateFlow { false }
    val ...
    val ...
    val ...
    val ...
}

```



이를 편리하게 만드는 것이 UiState입니다.  UiState를 사용한 코드는 아래와 같습니다.

```kotlin
class UiState {
    val bookNames
    val userNames
    val isLoading
}

class MainViewModel {
    val uiState = mutableStateFlow { UiState() }
}
```

그러나, 위의 코드는 사용자가 isLoading을 초기화하지 않으면, 로딩 화면이 사라지지 않는다는 문제가 있습니다.



이를 해결하는 방법이 서로 다른 State를 정의하는 것입니다.

```kotlin
sealed class UiState {
    object LoadingState(): UiState()
    object LoginState(val userNames, val bookNames): UiState()
}
```

그러나, 위처럼 서로 다른 State를 정의하면 State가 바뀔 때마다 이전 데이터를 모두 잃습니다.

예를 들어, 화면엔 userNames와 bookNames가 표시된 상태에서 LoadingState로 상태가 변경되면 화면에 userNames와 bookNames가 사라집니다.

# 결론이 그래서 뭔데?

결국 정답인 방법은 없습니다. 얻는 게 있으면 잃는 게 있습니다. 상황에 맞춰서 유도리 있게 씁시다.













