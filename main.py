from fastapi import FastAPI

app = FastAPI()

courses = {
    1: {
        "title": "PHP Advanced",
        "lessons": 112,
        "hours": 58,
    },
    2: {
        "title": "Java How To Program",
        "lessons": 87,
        "hours": 67,
    },
}


@app.get('/test')
async def test():
    return {"msg": "Route ok"}


@app.get('/courses')
async def get_courses():
    return courses


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
