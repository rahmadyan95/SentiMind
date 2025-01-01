import os,sys
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

from transformers import BertTokenizer, BertConfig, BertForSequenceClassification, logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import torch
import torch.nn.functional as F
from app.controllers.DatabaseController import DatabaseController
import pandas as pd

logging.set_verbosity_error()

class Model:
    def __init__(self):
        model_name = "indobenchmark/indobert-base-p1"
        self.tokenizer = BertTokenizer.from_pretrained(model_name)
        self.config = BertConfig.from_pretrained(model_name)
        self.config.num_labels = 6  # Match the checkpoint label count
        self.model = BertForSequenceClassification.from_pretrained(model_name, config=self.config)

        # Load model state
        state_dict = torch.load(
            "C:\\Users\\Rahmadyan\\Documents\\Project\\sentimind\\app\\models\\trained_model.pth",
            map_location=torch.device("cpu"),
            weights_only=True,
        )
        self.model.load_state_dict(state_dict)
        self.model.eval()  # Set model to evaluation mode

        

    def process_text(self, text):
        inputs = self.tokenizer(text, return_tensors="pt")
        logits = self.model(**inputs).logits

        label = torch.argmax(logits, dim=-1).item()
        confidence = F.softmax(logits, dim=-1).squeeze()[label] * 100
        label_name = {
            0: "sadness",
            1: "anger",
            2: "love",
            3: "fear",
            4: "happy",
            5: "disgust",
        }[label]

        return {
            "text": text,
            "emotions": label_name,
            "confidence": confidence.item(),
        }

    def process_comments(self, comments):
        results = []
        for comment in comments:
            try:
                result = self.process_text(comment)
                results.append(result)
            except Exception as e:
                results.append({
                    "text": comment,
                    "error": str(e),
                })
        return results
    
    def ToDataset(self,result):
        return pd.DataFrame(result)



if __name__ == "__main__":
    tlf = Model()
    DB = DatabaseController()

    commentsdata = DB.GetAllDataByScrapID('qsZGKbT4C_s')['comments']
    commentsdata = tlf.process_comments(commentsdata)
    commentsdata = tlf.ToDataset(commentsdata)
    
    print(commentsdata)
