import spacy

nlp = spacy.load("en_core_web_sm")

def process_user_input(text):
    doc = nlp(text)
    intents = []
    entities = []
    
    for ent in doc.ents:
        entities.append((ent.text, ent.label_))
    
    if "customize" in text.lower():
        intents.append("START_CUSTOMIZATION")
    elif "feature" in text.lower():
        intents.append("SELECT_FEATURE")
    
    return intents, entities
