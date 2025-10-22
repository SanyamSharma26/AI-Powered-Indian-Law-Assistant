from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

def load_summarizer():
    model_name = "sshleifer/distilbart-cnn-12-6"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return pipeline("summarization", model=model, tokenizer=tokenizer)

def chunk_text(text, max_chunk_len=1024):
    words = text.split()
    for i in range(0, len(words), max_chunk_len):
        yield ' '.join(words[i:i + max_chunk_len])

def summarize_text(summarizer, text, max_length=250, min_length=100):
    summaries = []
    for chunk in chunk_text(text):
        result = summarizer(chunk, max_length=max_length, min_length=min_length, do_sample=False)[0]['summary_text']
        summaries.append(result.strip())
    return " ".join(summaries)
