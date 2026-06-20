# todo_package

우선순위·기한·태그로 할 일을 관리하는 Python 패키지

---

## 1. 프로젝트 개요

`todo_package`는 할 일(Task)을 추가·완료·저장·불러오기할 수 있는 Python 패키지입니다.
일반 할 일(`Task`)과 반복 할 일(`RecurringTask`)을 지원하며, JSON 파일로 데이터를 저장합니다.

- Python 패키지 구조 및 객체지향 설계 실습 프로젝트
- GitHub: https://github.com/hseou/todo_manager

---

## 2. 설치 방법

```bash
# 저장소 복제
git clone https://github.com/hseou/todo_manager.git
cd todo_manager

# 가상환경 생성 및 활성화
python -m venv .venv
.venv\Scripts\activate

# 패키지 설치
pip install .
```

---

## 3. 실행 예시

```python 파일 생성 후 아래 코드 붙여넣기
from todo_package import Task, RecurringTask
from todo_package.utils import save_tasks, load_tasks, filter_by_priority

# 할 일 생성
t1 = Task("파이썬 공부", "2025-07-01", "높음", ["학교"])
t2 = Task("방 청소", "2025-07-02", "낮음")
t3 = RecurringTask("매일 운동", "2025-07-01", "보통", 1)

# 완료 처리
t1.complete()
print(t1.display())
# ✅ [높음] 파이썬 공부 (마감: 2025-07-01)

# 우선순위 필터링
high = filter_by_priority([t1, t2, t3], "높음")
print(len(high))  # 1

# JSON 저장 및 불러오기
save_tasks([t1, t2, t3], "tasks.json")
loaded = load_tasks("tasks.json")
print(loaded[0].title)  # 파이썬 공부
```

---

## 4. 주요 기능

### Task (기본 할 일)

| 메서드 | 설명 |
|---|---|
| `Task(title, due_date, priority, tags)` | 할 일 생성 |
| `complete()` | 완료 처리 |
| `to_dict()` | 딕셔너리로 변환 (저장용) |
| `display()` | 요약 문자열 반환 |

### RecurringTask (반복 할 일)

| 메서드 | 설명 |
|---|---|
| `RecurringTask(..., interval_days)` | 반복 할 일 생성 |
| `next_due_date()` | 반복 주기 안내 문자열 반환 |
| `reset()` | 미완료로 초기화, 반복 횟수 1 증가 |

### 도우미 함수 (utils)

| 함수 | 설명 |
|---|---|
| `save_tasks(tasks, filename)` | JSON 파일로 저장 |
| `load_tasks(filename)` | JSON 파일에서 불러오기 |
| `filter_by_priority(tasks, priority)` | 우선순위로 필터링 |

### 불러오기

| python 파일명.py |

---

## 5. 테스트 실행 방법

```bash
pip install pytest
pytest
```

### 테스트 결과

```
platform win32 -- Python 3.14.3, pytest-9.0.3
collected 15 items

tests\test_core.py ..........   [ 66%]
tests\test_utils.py .....       [100%]

15 passed in 0.15s
```

### PEP 8 스타일 검사 결과

```bash
pycodestyle todo_package/
```

```
(경고 없음)
```

---

## 6. 작성자 정보

- 이름: 홍서우
- 학번: 202620902
- 이메일: hongsw070427@gmail.com