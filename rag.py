from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

def load_docs():
    loader = TextLoader("data/sample.txt")
    documents = loader.load()

    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(docs, embeddings)

    return db

def retrieve(query, db):
    return db.similarity_search(query, k=3)