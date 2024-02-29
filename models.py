from typing import Optional, List
from pydantic import BaseModel


class Course(BaseModel):
    id: Optional[int] = None
    title: str = ""
    lessons: int = 0
    hours: int = 0
    price: float = 0.0

    _all_courses: List['Course'] = []

    @classmethod
    def courses_to_dict(cls, courses: List['Course']) -> List[dict]:
        return [course.dict() for course in courses]

    def get_courses(self) -> List['Course']:
        if len(self._all_courses) < 1:
            self._all_courses = [
                Course(id=1, title='PHP Advanced', lessons=112, hours=58, price=120.45),
                Course(id=2, title='Java How To Program', lessons=87, hours=67, price=200.05),
                Course(id=3, title='Learn Python Programming', lessons=65, hours=50, price=220.05),
            ]

        return self._all_courses
