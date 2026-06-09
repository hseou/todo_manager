# 도우미 함수(저장, 불러오기, 필터링) 단위 테스트
import os
import pytest
from todo_package import Task, RecurringTask
from todo_package.utils import save_tasks, load_tasks, filter_by_priority

# 테스트용 임시 파일 이름
TEMP_FILE = "test_tasks_temp.json"


def test_save_and_load_tasks():
    # 저장 후 불러왔을 때 데이터가 일치하는지 확인
    t = Task("운동", "2025-06-30", "높음", ["건강"])
    save_tasks([t], TEMP_FILE)
    loaded = load_tasks(TEMP_FILE)
    assert loaded[0].title == "운동"
    assert loaded[0].priority == "높음"
    os.remove(TEMP_FILE)


def test_save_and_load_recurring_task():
    # RecurringTask도 저장/불러오기가 올바르게 되는지 확인
    t = RecurringTask("매일 운동", "2025-06-30", "높음", 1)
    save_tasks([t], TEMP_FILE)
    loaded = load_tasks(TEMP_FILE)
    assert loaded[0].interval_days == 1
    assert loaded[0].repeat_count == 0
    os.remove(TEMP_FILE)


def test_filter_by_priority():
    # 우선순위 필터링이 올바르게 동작하는지 확인
    tasks = [
        Task("운동", "2025-06-30", "높음"),
        Task("독서", "2025-06-30", "보통"),
        Task("청소", "2025-06-30", "높음"),
    ]
    result = filter_by_priority(tasks, "높음")
    assert len(result) == 2


def test_filter_empty_list():
    # 빈 리스트를 필터링하면 빈 리스트가 반환되는지 확인
    result = filter_by_priority([], "높음")
    assert result == []


def test_filter_no_match():
    # 해당 우선순위가 없으면 빈 리스트가 반환되는지 확인
    tasks = [Task("운동", "2025-06-30", "보통")]
    result = filter_by_priority(tasks, "높음")
    assert result == []