# from openai import OpenAI
from google import genai
from llama_index.readers.file import PDFReader
from llama_index.core.node_parser import SentenceSplitter
from dotenv import load_dotenv

load_dotenv()

# client = OpenAI()
client = genai.Client()


reader = PDFReader()
# EMBED_MODEL = "text-embedding-3-large"
EMBED_MODEL = "gemini-embedding-001"
EMBED_DIM = 3072


splitter = SentenceSplitter(
  chunk_size=1000, # Maximum number of tokens in each chunk. If the text is longer, it will be split into multiple chunks of this size.
  chunk_overlap=200, # Number of tokens to repeat from the end of one chunk at the start of the next chunk. 0 means no overlap.
)

def load_and_chunk_pdf(path:str):
  docs = reader.load_data(file=path)
  texts = [d.text for d in docs if getattr(d, "text", None)]
  chunks = []
  for t in texts:
    chunks.extend(splitter.split_text(t))
  return chunks

# def embed_texts(texts: list[str]) -> list[list[float]]:
#   response = client.embeddings.create(
#     model=EMBED_MODEL,
#     input=texts
#   )

#   return [item.embedding for item in response.data]

def embed_texts(texts: list[str]) -> list[list[float]]:
  response = client.models.embed_content(
    model=EMBED_MODEL,
    contents=texts
  )

  return [embedding.values for embedding in response.embeddings]