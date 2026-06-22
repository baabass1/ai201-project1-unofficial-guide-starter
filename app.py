import os
import chromadb
import gradio as gr
from groq import Groq
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

load_dotenv()

groq_client = Groq()

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = []

for filename in os.listdir("documents"):
    if filename.endswith(".txt"):
        filepath = os.path.join("documents", filename)

        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()

        documents.append({
            "filename": filename,
            "text": text
        })

texts = [doc["text"] for doc in documents]
embeddings = model.encode(texts).tolist()

client = chromadb.Client()

collection = client.create_collection(
    name="python_tutorials"
)

collection.add(
    documents=texts,
    embeddings=embeddings,
    ids=[str(i) for i in range(len(texts))]
)

def answer_question(query):
    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    context = "\n\n".join(results["documents"][0])

    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "Answer only using the provided context. If the answer is not in the context, say you do not know."
            },
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion: {query}"
            }
        ]
    )

    return response.choices[0].message.content

demo = gr.Interface(
    fn=answer_question,
    inputs=gr.Textbox(label="Ask a Python Question"),
    outputs=gr.Textbox(label="Answer"),
    title="Python Tutorial RAG Assistant"
)

demo.launch()
