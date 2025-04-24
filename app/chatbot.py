from langchain_community.embeddings import HuggingFaceEmbeddings  # ✅
from langchain_community.vectorstores import FAISS  # ✅
from langchain.text_splitter import CharacterTextSplitter

# Load knowledge base
with open("app/data/knowledge.txt") as f:
    text = f.read()
texts = CharacterTextSplitter().split_text(text)
embeddings = HuggingFaceEmbeddings()
db = FAISS.from_texts(texts, embeddings)

def rag_chat(question):
    docs = db.similarity_search(question)
    context = "\n".join([d.page_content for d in docs])
    prompt = f"Context: {context}\nQuestion: {question}"
    return chat(prompt)