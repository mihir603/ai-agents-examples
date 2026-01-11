from openai import OpenAI
from dotenv import load_dotenv
import os
import chromadb

load_dotenv()
api_key = os.getenv("OPEN_API_KEY")

if not api_key:
  raise ValueError("api key not found")

client = OpenAI(api_key=api_key)

def get_embedding(doc):
  doc = doc.replace("\n", " ")
  return client.embeddings.create(input=[doc], model="text-embedding-ada-002").data[0].embedding


documents = [
  "For everyday listeners seeking excellent value, the standard AirPods 4 at $129 are the most affordable AirPods yet while delivering core features like the H2 chip and improved comfort.",
  "They're particularly appealing for users who prefer the open-ear design and don't require noise cancellation.",
  "The AirPods 4 with ANC at $179 offer the sweet spot for many users. They provide almost all of the same key features as the AirPods Pro at a lower price point, making them ideal for commuters and professionals who need noise control without the premium price tag.",
  "The $50 upgrade from the base model brings significant value through ANC and enhanced charging capabilities.",
  "For those seeking the ultimate audio experience, the AirPods Pro 3 at $249 are Apple's premium option. The additional $70 over the AirPods 4 with ANC delivers superior sound quality, longer battery life, health monitoring features, and professional-grade noise cancellation.",
  "Bottom line: your choice should align with your specific needs and budget constraints. The AirPods 4 lineup brings professional features to mainstream pricing, while the Pro 3 represents the pinnacle of Apple's audio engineering. Consider the standard AirPods 4 if you prioritize affordability and comfort over advanced features."  
]

embeddings = [get_embedding(doc) for doc in documents]
ids = [f"id{i}" for i in range(len(documents))]

chroma_client = chromadb.Client()
collection = chroma_client.create_collection("airpods_documents")

collection.add(
  embeddings=embeddings,
  documents=documents,
  ids=ids
)

def query_db(query, n=2):
  query_embedding = get_embedding(query)
  results = collection.query(query_embeddings=[query_embedding], n_results=n)
  return [(id, score, text) for id, score, text in zip(results['ids'][0], results['distances'][0], results['documents'][0])]



while True:
  query = input("Enter what you want to search for airpods ('exit' for exit):")
  if query.lower() == 'exit':
    break
  n = int(input("Enter how many top matches do you want ?"))
  search_results = query_db(query, n)

  print("Top matched documents:")
  for id, score, text in search_results:
    print("-"*20)
    print(f"ID: {id}, TEXT: {text}, SCORE: {score}")
    print("="*20)
