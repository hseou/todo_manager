# Task, RecurringTask 클래스 단위 테스트
import pytest
from todo_package import Task, RecurringTask


# ── 정상 케이스 ──────────────────────────────

def test_task_creation():
    # Task가 올바르게 생성되는지 확인
    t = Task("운동하기", "2025-06-30", "높음", ["건강"])
    assert t.title == "운동하기"
    assert t.due_date == "2025-06-30"
    assert t.priority == "높음"
    assert t.tags == ["건강"]
    assert t.done is False


def test_task_complete():
    # complete() 호출 후 done이 True가 되는지 확인
    t = Task("독서", "2025-07-01", "보통")
    t.complete()
    assert t.done is True


def test_task_to_dict():
    # to_dict()가 올바른 딕셔너리를 반환하는지 확인
    t = Task("공부", "2025-07-01", "높음", ["학교"])
    result = t.to_dict()
    assert result["title"] == "공부"
    assert result["priority"] == "높음"
    assert result["done"] is False


def test_task_display():
    # display()가 제목과 우선순위를 포함하는지 확인
    t = Task("청소", "2025-06-30", "낮음")
    result = t.display()
    assert "청소" in result
    assert "낮음" in result


def test_recurring_task_creation():
    # RecurringTask가 부모 속성과 자식 속성 모두 갖는지 확인
    t = RecurringTask("매일 운동", "2025-06-30", "높음", 1, ["건강"])
    assert t.title == "매일 운동"
    assert t.interval_days == 1
    assert t.repeat_count == 0


def test_recurring_task_reset():
    # reset() 후 done이 False, repeat_count가 1 증가하는지 확인
    t = RecurringTask("주간 보고서", "2025-06-30", "보통", 7)
    t.complete()
    assert t.done is True
    t.reset()
    assert t.done is False
    assert t.repeat_count == 1


def test_recurring_task_to_dict():
    # RecurringTask의 to_dict()에 interval_days가 포함되는지 확인
    t = RecurringTask("운동", "2025-06-30", "높음", 3)
    result = t.to_dict()
    assert result["interval_days"] == 3
    assert result["repeat_count"] == 0


# ── 엣지 케이스 ──────────────────────────────

def test_task_invalid_priority():
    # 잘못된 우선순위 입력 시 ValueError가 발생하는지 확인
    with pytest.raises(ValueError):
        Task("테스트", "2025-06-30", "엄청높음")


def test_task_default_tags_is_empty_list():
    # tags를 넣지 않으면 빈 리스트가 기본값인지 확인
    t = Task("메모", "2025-06-30", "낮음")
    assert t.tags == []


def test_task_empty_title():
    # 제목이 빈 문자열이어도 오류 없이 생성되는지 확인
    t = Task("", "2025-06-30", "보통")
    assert t.title == ""