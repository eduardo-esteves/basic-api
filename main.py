from typing import Optional

from fastapi import FastAPI, HTTPException, status, Query
from fastapi.responses import JSONResponse

from models import Course


app = FastAPI()

courses = [
    {
        "title": "PHP Advanced",
        "lessons": 112,
        "hours": 58,
        "price": 120.45,
    },
    {
        "title": "Java How To Program",
        "lessons": 87,
        "hours": 67,
        "price": 200.05,
    },
    {
        "title": "Learn Python Programming",
        "lessons": 65,
        "hours": 50,
        "price": 220.05,
    },
]


@app.get('/test')
async def test():
    return {"msg": "Route ok"}


@app.get('/courses')
async def get_courses():
    return courses


@app.get('/courses/{id}')
async def get_course(id: int):
    idx = id - 1
    try:
        return courses[idx]
    except KeyError:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail='Course Not Found')


@app.post('/courses', status_code=status.HTTP_201_CREATED)
async def post_course(course: Course):
    if course.title is not None:
        courses.append(course)
        del course.id
        return course
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'Already exists a course with ID {course.id}')


@app.put('/courses/{id}')
async def update_course(id: int, course: Course):
    idx = id - 1
    if courses[idx]:
        courses[idx] = course
        del course.id
        return course
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Course informed Not Found')


@app.delete('/courses/{id}')
async def delete_course(id: int):
    idx = id - 1
    if not 0 <= idx < len(courses):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Course not exists')
    title = courses[idx]['title']
    del courses[idx]
    return JSONResponse({
        "msg": f"deleted {title} with success",
        "status": status.HTTP_200_OK,
    }, status.HTTP_200_OK)


@app.get('/sum')
async def sum(n1: int = Query(default=None, gt=0), n2: int = Query(default=None, ge=1), n3: Optional[int] = 0):
    return {"result": (n1 + n2 + n3)}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
