from openai import OpenAI
import numpy as np
from sklearn.decomposition import PCA
import os
from dotenv import load_dotenv
import plotly.graph_objects as go

load_dotenv()
api_key = os.getenv("OPEN_API_KEY")
if not api_key:
  raise ValueError("No API Key Found")
client = OpenAI(api_key=api_key)

def get_embedding(doc, model="text-embedding-ada-002"):
  return client.embeddings.create(input=[doc], model=model).data[0].embedding

documents = [
  "For everyday listeners seeking excellent value, the standard AirPods 4 at $129 are the most affordable AirPods yet while delivering core features like the H2 chip and improved comfort.",
  "They're particularly appealing for users who prefer the open-ear design and don't require noise cancellation.",
  "The AirPods 4 with ANC at $179 offer the sweet spot for many users. They provide almost all of the same key features as the AirPods Pro at a lower price point, making them ideal for commuters and professionals who need noise control without the premium price tag.",
  "The $50 upgrade from the base model brings significant value through ANC and enhanced charging capabilities.",
  "For those seeking the ultimate audio experience, the AirPods Pro 3 at $249 are Apple's premium option. The additional $70 over the AirPods 4 with ANC delivers superior sound quality, longer battery life, health monitoring features, and professional-grade noise cancellation.",
  "Bottom line: your choice should align with your specific needs and budget constraints. The AirPods 4 lineup brings professional features to mainstream pricing, while the Pro 3 represents the pinnacle of Apple's audio engineering. Consider the standard AirPods 4 if you prioritize affordability and comfort over advanced features."  
]

embeddings = [get_embedding(doc) for doc in documents]

embeddings_array = np.array(embeddings)

print(f"Embeddings Shape: {embeddings_array.shape}")

pca = PCA(n_components=3)
reduced_embeddings = pca.fit_transform(embeddings_array)

fig = go.Figure(data=[go.Scatter3d(
    x=reduced_embeddings[:,0],
    y=reduced_embeddings[:,1],
    z=reduced_embeddings[:,2],
    mode='markers+text',
    text=documents,  # Adding document texts for hover
    hoverinfo='text',  # Showing only the text on hover
    marker=dict(
        size=12,
        color=list(range(len(documents))),
        opacity=0.8
    )
)])

# Adding titles and labels to the plot
fig.update_layout(title="3D Plot of Apple Airpods Article Embeddings",
                  scene=dict(
                      xaxis_title='PCA Component 1',
                      yaxis_title='PCA Component 2',
                      zaxis_title='PCA Component 3'
                  ))

fig.show()