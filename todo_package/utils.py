# 자식 클래스: 반복되는 할 일을 표현하는 클래스
from .core import Task


class RecurringTask(Task):
    """반복되는 할 일을 표현하는 클래스. Task를 상속받는다.

    예를 들어 '매일 운동', '매주 보고서 작성' 같은
    주기적으로 반복되는 할 일을 관리한다.

    :ivar interval_days: 반복 주기 (일 단위, 예: 7이면 매주)
    :ivar repeat_count: 지금까지 반복 완료한 횟수

    >>> t = RecurringTask("매일 운동", "2025-06-30", "높음", 1)
    >>> t.interval_days
    1
    """

    def __init__(self, title, due_date, priority, interval_days, tags=None):
        """RecurringTask 객체를 초기화한다.

        :param title: 할 일 제목
        :param due_date: 첫 마감일 문자열 (예: "2025-06-30")
        :param priority: 우선순위 ("높음", "보통", "낮음")
        :param interval_days: 반복 주기 (일 단위)
        :param tags: 태그 목록, 기본값은 빈 리스트

        >>> t = RecurringTask("주간 보고서", "2025-06-30", "보통", 7)
        >>> t.repeat_count
        0
        """
        # 부모 클래스(Task)의 초기화를 먼저 실행
        super().__init__(title, due_date, priority, tags)
        self.interval_days = interval_days
        self.repeat_count = 0  # 반복 완료 횟수

    def next_due_date(self):
        """다음 반복 주기 정보를 문자열로 반환한다.

        :return: 반복 주기 안내 문자열

        >>> t = RecurringTask("운동", "2025-06-30", "높음", 3)
        >>> "3" in t.next_due_date()
        True
        """
        return f"마감일 {self.due_date} 기준, 매 {self.interval_days}일마다 반복"

    def reset(self):
        """할 일을 미완료 상태로 초기화하고 반복 횟수를 1 늘린다.

        반복 할 일을 완료한 뒤 다음 주기를 시작할 때 사용한다.

        :return: 없음

        >>> t = RecurringTask("운동", "2025-06-30", "높음", 1)
        >>> t.complete()
        >>> t.reset()
        >>> t.done
        False
        >>> t.repeat_count
        1
        """
        self.done = False
        self.repeat_count += 1

    def to_dict(self):
        """반복 할 일 정보를 딕셔너리로 변환한다. (저장용)

        부모의 to_dict()를 활용하고 반복 관련 정보를 추가한다.

        :return: 반복 할 일 정보가 담긴 딕셔너리

        >>> t = RecurringTask("운동", "2025-06-30", "높음", 1)
        >>> t.to_dict()['interval_days']
        1
        """
        # 부모의 to_dict() 결과를 가져온 뒤 반복 정보 추가
        task_dict = super().to_dict()
        task_dict["interval_days"] = self.interval_days
        task_dict["repeat_count"] = self.repeat_count
        return task_dict

    def display(self):
        """반복 할 일 정보를 보기 좋은 문자열로 반환한다.

        :return: 반복 정보가 포함된 요약 문자열

        >>> t = RecurringTask("운동", "2025-06-30", "높음", 1)
        >>> "매" in t.display()
        True
        """
        # 부모의 display() 결과에 반복 주기 정보를 추가
        base = super().display()
        return f"{base} | 반복: 매 {self.interval_days}일"