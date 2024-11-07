import re
import torch
from transformers import BartForConditionalGeneration, BartTokenizer

class Summarizer:
    def __init__(self):
        self.model_name = "facebook/bart-large-cnn"
        self.tokenizer = BartTokenizer.from_pretrained(self.model_name)
        self.model = BartForConditionalGeneration.from_pretrained(self.model_name)

    def preprocess_text(self, text):
        # Очистка текста от лишних символов и пробелов
        text = re.sub(r'\s+', ' ', text)  # Удаление лишних пробелов и переносов строк
        text = re.sub(r'[^\w\s.,]', '', text)  # Удаление всех символов, кроме слов, пробелов, точек и запятых
        text = re.sub(r'([.,])\1+', r'\1', text)  # Удаление повторяющихся знаков препинания
        text = re.sub(r'(\s[.,])', '', text)  # Удаление одиночных знаков препинания
        text = text.strip()  # Удаление пробелов в начале и конце строки
        return text

    def summarize(self, text, max_length=150):
        # Предобработка текста перед отправкой в модель
        clean_text = self.preprocess_text(text)
        
        inputs = self.tokenizer([clean_text], max_length=1024, return_tensors="pt", truncation=True)
        summary_ids = self.model.generate(inputs["input_ids"], max_length=max_length, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
        return self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)