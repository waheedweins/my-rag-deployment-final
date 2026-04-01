from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from app.core.config import settings

def create_rag_chain(retriever):

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    prompt = ChatPromptTemplate.from_template(
        "Answer strictly from context:\n\n{context}\n\nQuestion: {question}"
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=settings.GOOGLE_API_KEY,
        temperature=0
    )

    chain = (
        {
            "question": RunnablePassthrough(),
            "context": retriever | RunnableLambda(format_docs),
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain
