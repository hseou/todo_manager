# 할 일 관리 도구의 핵심 클래스 정의

class Task:
    """할 일을 표현하는 클래스

    :ivar title: 할 일 제목
    :ivar due_date: 마감일 (예: "2025-06-30")
    :ivar priority: 우선순위 ("높음", "보통", "낮음")
    :ivar tags: 태그 목록 (예: ["공부", "운동"])
    :ivar done: 완료 여부

    >>> t = Task("운동하기", "2025-06-30", "높음", ["건강"])
    >>> t.title
    '운동하기'
    """

    # 사용 가능한 우선순위 목록
    VALID_PRIORITIES = ["높음", "보통", "낮음"]

    def __init__(self, title, due_date, priority, tags=None):
        """Task 객체를 초기화한다.

        :param title: 할 일 제목
        :param due_date: 마감일 (예: "2025-06-30")
        :param priority: 우선순위 ("높음", "보통", "낮음")
        :param tags: 태그 목록, 기본값은 빈 리스트

        >>> t = Task("독서", "2025-07-01", "보통")
        >>> t.done
        False
        """
        self.title = title
        self.due_date = due_date
        self.priority = self._validate_priority(priority)  # 검증 후 저장
        self.tags = tags if tags is not None else []
        self.done = False

    def _validate_priority(self, priority):
        """우선순위 값이 유효한지 검증한다. (비공개 메서드)

        :param priority: 검증할 우선순위 문자열
        :return: 유효하면 그대로 반환
        :raises ValueError: 유효하지 않은 값이면 오류 발생
        """
        if priority not in self.VALID_PRIORITIES:
            raise ValueError(
                f"우선순위는 {self.VALID_PRIORITIES} 중 하나여야 합니다."
            )
        return priority

    def complete(self):
        """할 일을 완료 처리한다.

        :return: 없음

        >>> t = Task("청소", "2025-06-30", "낮음")
        >>> t.complete()
        >>> t.done
        True
        """
        self.done = True

    def to_dict(self):
        """할 일 정보를 딕셔너리로 변환한다. (저장용)

        :return: 할 일 정보가 담긴 딕셔너리

        >>> t = Task("공부", "2025-06-30", "높음", ["학교"])
        >>> t.to_dict()['title']
        '공부'
        """
        return {
            "title": self.title,
            "due_date": self.due_date,
            "priority": self.priority,
            "tags": self.tags,
            "done": self.done,
        }

        def display(self):
            """할 일 정보를 보기 좋은 문자열로 반환한다.

            :return: 할 일 요약 문자열

            >>> t = Task("운동하기", "2025-06-30", "높음")
            >>> "운동하기" in t.display()
            True
            """
    # 완료 여부를 이모지로 표시
        status = "✅" if self.done else "⬜"
        return f"{status} [{self.priority}] {self.title} (마감: {self.due_date})"