import plotly.graph_objects as go
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

docs = [
  "Chemistry is the study of matter and its interactions with other matter and energy.",
  "Matter is anything that has mass and takes up space.",
  "Physical properties and chemical properties of matter can change.",
  "Combinations of different substances are called mixtures.",
  "Elements can be described as metals, nonmetals, and semimetals.",
  "Science is broken down into various fields, of which chemistry is one.",
  "Science is a process of knowing about the natural universe through observation and experiment.",
  "Science, including chemistry, is both qualitative and quantitative.",
  "Matter is composed of elements and compounds."
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(docs)

cosine_similarities = cosine_similarity(X)
while True:
  selected_doc_index = input(f"Enter Doc No. between (0 - {len(docs) - 1}) or 'exit' to quit: ").strip()
  if selected_doc_index.lower() == "exit":
    break
  if not selected_doc_index.isdigit() or not 0 <= int(selected_doc_index) <= len(docs):
    print("Invalid input..")
  selected_doc_index = int(selected_doc_index)
  selected_doc_similarities = cosine_similarities[selected_doc_index]

  x_axis_labels = [doc[:50] + "..." if len(doc) > 50 else doc for doc in docs]

    
  fig = go.Figure([go.Bar(x=x_axis_labels, 
                            y=selected_doc_similarities)])

  fig.update_layout(title=f"Cosine Similarities of '{docs[selected_doc_index][:50] + '...' if len(docs[selected_doc_index]) > 50 else docs[selected_doc_index]}' with Others",
                      xaxis_title="Document",
                      yaxis_title="Cosine Similarity",
                      xaxis={'tickangle': 45})

  fig.show()



