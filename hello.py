from fastapi import FastAPI, Header, Body

# app은 전체 웹 애플리케이션을 나타내는 최상위 FastAPI 객체
app = FastAPI()     

# app.get("/hi")는 '경로 데코레이터'
# 데코레이터는 HTTP GET 동작에만 적용됨
# 또한 다른 HTTP 동작 (PUT, POST 등)와 함께 전송된 "/hi" URL에 응답할 수 있음
@app.get("/hi/{who}")

# 해당 함수는 경로 함수로, HTTP 요청과 응답의 주요 접점
# def greet(who: str = Body(embed=True)):
def greet(who):
    return f"Hello? {who}?"


# reload: hello.py가 변경되면 웹 서버를 다시 시작하도록 uvicorn에 지시

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)
