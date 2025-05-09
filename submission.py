from bs4 import BeautifulSoup
import spacy
import json

nlp = spacy.load("out/no_tags/model-best")

# Load evaluation data
with open("gutbrainie2025/Test_Data/articles_test.json", "r") as f:
    evaluation_data = json.load(f)

# Process and collect outputs
results = {}

for doc_id, content in evaluation_data.items():
    entities = []
    for field in ["title", "abstract"]:
        text = content.get(field)
        if not text:
            continue  # Skip if the field is missing or empty

        # Remove all HTML tags from the main text
        soup = BeautifulSoup(text, "html.parser")
        clean_text = soup.get_text()

        doc = nlp(clean_text)
        for ent in doc.ents:
            entities.append({
                "start_idx": ent.start_char,
                "end_idx": ent.end_char - 1,
                "location": field,
                "text_span": ent.text,
                "label": ent.label_
            })
    results[doc_id] = {"entities": entities}

# Save results to JSON file
with open("model_predictions.json", "w") as f:
    json.dump(results, f, indent=4)
