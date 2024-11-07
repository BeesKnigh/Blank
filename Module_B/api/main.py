from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model.summarizer import Summarizer

app = FastAPI()
summarizer = Summarizer()

class Article(BaseModel):
    text: str

@app.post("/annotate/")
async def annotate(article: Article):
    if len(article.text) == 0:
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    summary = summarizer.summarize(article.text)
    return {"annotation": summary}
