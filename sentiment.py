# from sentiment import sentiment_analysis
# comment='This law is not usefull for muslims'
# senti=sentiment_analysis(comment)
# r=senti.score()
# print(r) --> ['very opposing',1] --> sentiment and rating 1/5



from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
class sentiment_analysis:
    
    def __init__(self,text):
        self.text=text       
    def score(self):
        global sc
        # access_token='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'
        tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
        model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
        tokens = tokenizer.encode(self.text, return_tensors='pt')
        result = model(tokens)
        sentiment=['Very Opposing','Slightly Negative','Needs improvement','Slightly positive','Complete Grant']
        print(result.logits)
        sc=sentiment[int(torch.argmax(result.logits))]
        return [sc,int(torch.argmax(result.logits))+1]