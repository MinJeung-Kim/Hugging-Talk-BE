from typing import Union


from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from model.translation import translate_text, translate_sentences


app = FastAPI()

# CORS 미들웨어 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인 허용, 필요시 수정
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


# 번역 API 예시 엔드포인트
@app.get("/translate")
def translate(text: str):
    result = translate_text(text)
    return {"translated": result}



# 문장 단위 번역 API 엔드포인트
class TextRequest(BaseModel):
    text: str

@app.post("/translate/sentences")
def translate_sentences_api(request: TextRequest):
    results = translate_sentences(request.text)
    return {"translated_sentences": results}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q2": q}
