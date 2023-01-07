from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from transformers import pipeline
from pysbd import Segmenter

app = FastAPI()
segmenter = Segmenter(language='en', clean=False)
task = "text-classification"
model_name = "remzicam/privacy_intent"
privacy_intent_pipe = pipeline(
                               task,
                               model_name
                               )

def doc2sent(text:str)-> dict:
    """
    > It takes a string of text and returns a list of sentences
    
    Args:
      text (str): the text to be segmented
    
    Returns:
      A list of sentences
    """
    sentences = segmenter.segment(text)
    return [sentence.replace("\n", "").strip() for sentence in sentences]


def pipe(text:str) -> list[str]:    
    """
    It takes a string of text and returns a dictionary of sentences and their corresponding privacy
    intent labels.
    
    Args:
      text (str): the text to be classified
    
    Returns:
      A dictionary of sentences and their corresponding labels.
    """
    sentences = doc2sent(text)
    preds = [privacy_intent_pipe(sent)[0]["label"] for sent in sentences]
    return dict(zip(sentences, preds))


@app.get("/infer_intents")
def t5(input):
    return {"output": pipe(input)}


app.mount("/", StaticFiles(directory="static", html=True), name="static")


@app.get("/")
def index() -> FileResponse:
    return FileResponse(path="/app/static/index.html", media_type="text/html")
