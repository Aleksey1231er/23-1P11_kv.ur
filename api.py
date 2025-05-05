from fastapi import FastAPI
from main import treesome

app = FastAPI(title="Квадратное уравнение")

@app.get("/")
async def solve_quadratic_get(a: float, b: float, c: float):
    result = treesome(a, b, c)
    return format_response(a, b, c, result)