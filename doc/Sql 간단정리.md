업무를 하게 되면서 헷갈렸던 부분 혹은 자주 마주쳤던 부분들에 대한 간단한 정리

# 서브 쿼리의 종류

## 1.스칼라 (서브) 쿼리 → SELECT절에 사용되는 쿼리

장점1. 내부적으로 서브쿼리에 대한 결과를 캐싱

장점2. NULL을 반환하여 아우터 조인처럼 실행 

스칼라 쿼리의 경우 평균값이나 단일값을 반환하는 쿼리를 의미한다.

```sql
SELECT  AVG(Salary) 
FROM    Employee;

// 생일이 NOT NULL일 때는 가능하지만.. NULL인 경우 조회되지 않는 로우가 생긴다?
select (select name 
          from emp 
         where emp = 1)
  from ORDER A
     , RECEVIER B
     , BIRTHDAY C
 where A.CUST_NO = B.CUST_NO
   and B.CUST_NO = C.CUST_NO;

// 기본적으로 스칼라쿼리는 조인할 때 부재 시, NULL을 반환하여 아우터 조인처럼 실행됨.
// 고객 생일, 조회되게 해주세요... 아우터 조인 
select (select name 
          from emp 
         where emp = 1),
       (SELECT BDAY
          FROM BIRTHDAY C
         WHERE B.CUST_no = C.CUST_NO)
  from ORDER A
     , RECEVIER B
 where A.CUST_NO = B.CUST_NO; // 100만 건 조회

SELECT A.1
     , A.2, B.1, B.2
  FROM A
  LEFT OUTER JOIN B
    ON A.1 = B.1
```



## 2.인라인 뷰 → FROM

1. 서브쿼리가 중첩되어 있는 경우 인라인 뷰를 사용하면 좀 더 이해하기 쉽게 가능하다.

 2.  인라인 뷰 부분만 수정하면 되어 재사용성이 좋다.

 

```sql
select *
  from emp A
     , (select name 
          from dept
         where dept_no = '20') B 
```



서브 쿼리 성능에 대해서는 아래 링크 참조

 [https://12bme.tistory.com/299](https://12bme.tistory.com/299)



## WITH절의 경우

복잡한 쿼리를 더 작은 부분으로 나누고 이름을 붙여 가독성을 향상시킬 수 있다.

인라인 뷰 부분만 수정하면 되어 재사용성이 좋다.

 

```sql
// WITH절 사용 시
WITH SalesEmp AS  (
                  SELECT EmpID
                   ,  SUM(Price) AS TotalSales
                  FROM Employee 
                  )
SELECT  Products.ProductName
     ,  SalesEmp.TotalSales
FROM    Products
WHERE   Products.ProductID = SalesEmp.EmpID;

//  WITH절 미 사용 시
SELECT  Products.ProductName
     ,  SalesEmp.TotalSales
FROM    Products
   , (
      SELECT EmpID
       ,  SUM(Price) AS TotalSales
      FROM Employee 
      ) AS SalesEmp 
WHERE   Products.ProductID = SalesEmp.EmpID
```



## UNION

집합 연산 쿼리로 통계쿼리 나 당일 건수비교할때 많이들 사용한다. 

### UNION과 UNION ALL 차이점

두개의 쿼리 결과를 집합으로 합치는데 UNION의 경우 중복된 행을 제거하고 유일한 결과만 집합으로 생성한다.



## 자주하는 실수? 

ORA-00918 열의 정의가 애매합니다.

 

```sql
// 문제 코드
SELECT  empName
   ,    empNum
FROM    Employee
   ,    Dept
WHERE   Employee.empName = Dept.empName;

// 정답
SELECT  Employee.empName
   ,    Employee.empNum
FROM    Employee
   ,    Dept
WHERE   Employee.empName = Dept.empName;
```





ORA-01722 수치가 부적합합니다.

>> 문자열을 숫자로 변환할때 발생하는 오류로 데이터 타입을 잘확인할것..!
>> [https://lnsideout.tistory.com/entry/ORACLE%EC%98%A4%EB%9D%BC%ED%81%B4-ORA-01722-%EC%88%98%EC%B9%98%EA%B0%80-%EB%B6%80%EC%A0%81%ED%95%A9%ED%95%A9%EB%8B%88%EB%8B%A4-%ED%95%B4%EA%B2%B0%EC%99%84%EB%A3%8C](https://lnsideout.tistory.com/entry/ORACLE%EC%98%A4%EB%9D%BC%ED%81%B4-ORA-01722-%EC%88%98%EC%B9%98%EA%B0%80-%EB%B6%80%EC%A0%81%ED%95%A9%ED%95%A9%EB%8B%88%EB%8B%A4-%ED%95%B4%EA%B2%B0%EC%99%84%EB%A3%8C)

