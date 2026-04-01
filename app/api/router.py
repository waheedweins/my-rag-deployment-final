from fastapi import APIRouter, Request
from app.api.schema import QuestionRequest, AnswerResponse

router = APIRouter(prefix="/api")

@router.post("/answer", response_model=AnswerResponse)
async def answer(payload: QuestionRequest, request: Request):
    rag_chain = request.app.state.rag_chain
    result = rag_chain.invoke(payload.question)
    return AnswerResponse(answer=result)
