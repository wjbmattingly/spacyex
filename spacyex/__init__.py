import spacy
from spacy.matcher import Matcher


def create_pattern(text_input):
    """
    Process the input string to generate patterns for the spaCy Matcher.

    Args:
    text_input (str): The input string defining the patterns.

    Returns:
    list: A list of dictionaries containing token attributes for matching.
    """
    base_patterns = ["orth", "text", "norm", "lower", "lemma"]
    grammar_patterns = [
        "pos", "tag", "morph", "dep", "shape", "ent_type", "ent_iob", "ent_id", "ent_kb_id"
    ]
    full_sequence = []

    for part in text_input.split():
        if "(" in part and ")" in part:
            token, rules = part[:-1].split("(")
            rules = rules.split("|")
            token_attributes = {}

            for rule in rules:
                key, _, value = rule.partition("=")
                key_lower = key.lower()

                if key_lower in base_patterns:
                    if "in" in value:
                        list_data = value.split("[")[1].split("]")[0].split(",")
                        nested = {"IN": list_data}
                        token_attributes[key.upper()] = nested
                    
                    else:
                        token_attributes[key.upper()] = token.lower() if key_lower == "lower" else token

                elif key_lower in grammar_patterns:
                    if "in" in value:
                        list_data = value.split("[")[1].split("]")[0].split(",")
                        nested = {"IN": list_data}
                        token_attributes[key.upper()] = nested
                    else:
                        token_attributes[key.upper()] = value.upper()

                elif key_lower == "op":
                    token_attributes[key.upper()] = value

            if token_attributes:
                full_sequence.append(token_attributes)
        else:
            full_sequence.append({"TEXT": part})
            print(f"Using the raw text of: {part}")
    return full_sequence


def search(pattern, string, nlp):
    """
    
    """
    matcher_pattern = create_pattern(pattern)

    matcher = Matcher(nlp.vocab)
    matcher.add("spacex", [matcher_pattern])

    doc = nlp(string)
    results = matcher(doc)
    doc_results = []
    for result in results:
        _, start, end = result
        doc_results.append([doc[start:end], start, end])

    return doc_results