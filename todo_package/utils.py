# 할 일 저장, 불러오기, 필터링 도우미 함수
import json

from .core import Task
from .subclass import RecurringTask


def save_tasks(tasks, filename):
    """할 일 목록을 JSON 파일로 저장한다.

    :param tasks: 저장할 Task 또는 RecurringTask 객체 목록
    :param filename: 저장할 파일 이름 (예: "tasks.json")
    :return: 없음

    >>> import os
    >>> from todo_package.core import Task
    >>> save_tasks([Task("테스트", "2025-06-30", "보통")], "temp.json")
    >>> os.path.exists("temp.json")
    True
    >>> os.remove("temp.json")
    """
    data = []
    for task in tasks:
        # 각 Task 객체를 딕셔너리로 변환
        task_dict = task.to_dict()
        data.append(task_dict)

    # JSON 파일로 저장 (한글 깨짐 방지: ensure_ascii=False)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_tasks(filename):
    """JSON 파일에서 할 일 목록을 불러온다.

    딕셔너리에 "interval_days" 키가 있으면 RecurringTask로,
    없으면 일반 Task로 복원한다.

    :param filename: 불러올 파일 이름 (예: "tasks.json")
    :return: Task 또는 RecurringTask 객체 목록

    >>> import os
    >>> from todo_package.core import Task
    >>> save_tasks([Task("테스트", "2025-06-30", "보통")], "temp2.json")
    >>> loaded = load_tasks("temp2.json")
    >>> loaded[0].title
    '테스트'
    >>> os.remove("temp2.json")
    """
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    tasks = []
    for item in data:
        # "interval_days" 키가 있으면 RecurringTask로 복원
        if "interval_days" in item:
            task = RecurringTask(
                item["title"],
                item["due_date"],
                item["priority"],
                item["interval_days"],
                item["tags"]
            )
            task.repeat_count = item["repeat_count"]
        else:
            task = Task(
                item["title"],
                item["due_date"],
                item["priority"],
                item["tags"]
            )
        # 완료 여부 복원
        task.done = item["done"]
        tasks.append(task)

    return tasks


def filter_by_priority(tasks, priority):
    """우선순위로 할 일 목록을 필터링한다.

    :param tasks: 전체 Task 객체 목록
    :param priority: 필터링할 우선순위 ("높음", "보통", "낮음")
    :return: 해당 우선순위의 Task 목록

    >>> from todo_package.core import Task
    >>> t1 = Task("운동", "2025-06-30", "높음")
    >>> t2 = Task("독서", "2025-06-30", "보통")
    >>> result = filter_by_priority([t1, t2], "높음")
    >>> len(result)
    1
    """
    # 리스트 컴프리헨션으로 해당 우선순위의 할 일만 추출
    return [task for task in tasks if task.priority == priority]