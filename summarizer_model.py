from transformers import AutoModelWithLMHead, AutoTokenizer
from transformers import pipeline
class summarize:
    def __init__(self,text,max,min):
        self.text=text
        self.max=max
        self.min=min
        
    def get(self):
        summarizer = pipeline("summarization")
        return summarizer(self.text, max_length=self.max, min_length=self.min, do_sample=False)[0]['summary_text']