import spacy
from spacy.matcher import Matcher

class SpacyEx:
    def __init__(self, nlp):
        """
        Initialize the SpacyMatcher with a spaCy language model.

        Args:
        nlp (spacy.Language): A spaCy language model.
        """
        self.nlp = nlp
        self.matcher = Matcher(nlp.vocab)

    def create_pattern(self, text_input):
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
                        token_attributes[key.upper()] = token.lower() if key_lower == "lower" else token

                    elif key_lower in grammar_patterns:
                        token_attributes[key.upper()] = value.upper()

                    elif key_lower == "op":
                        token_attributes[key.upper()] = value

                if token_attributes:
                    full_sequence.append(token_attributes)
            else:
                print(f"Error in part format: {part}")

        return full_sequence

    def add_patterns(self, pattern_name, patterns):
        """
        Add the specified patterns to the matcher.

        Args:
        pattern_name (str): The identifier for these patterns.
        patterns (list): The patterns to add to the matcher.
        """
        self.matcher.add(pattern_name, [patterns])

    def query_docs(self, docs):
        """
        Match patterns against a sequence of documents.

        Args:
        docs (Iterable[spacy.tokens.Doc]): Documents to match against.

        Returns:
        list: Match results for each document.
        """
        matches = []
        for doc in docs:
            for item in self.matcher(doc):
                _, start, end = item
                matches.append([start, end, doc[start:end]])
        return matches