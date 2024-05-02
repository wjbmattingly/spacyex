# spaCyEx

![spacy ex logo](/images/spacyex-logo.png)

`spaCyEx` is a powerful extension for spaCy, designed to make pattern matching as flexible and easy as using regular expressions. It builds upon the existing capabilities of spaCy's `Matcher`, enhancing it with a more accessible syntax for defining complex patterns. `spaCyEx` allows for intuitive and detailed text pattern specifications, perfect for extracting detailed linguistic features from texts.

## Installation

You can install `spaCyEx` via pip:

```bash
pip install spacyex
```

## Features

- Create complex matching patterns using a simple syntax.
- Supports all dictionary properties that are used by spaCy's `Matcher`.
- Easy integration with existing spaCy pipelines.

## Usage

Here is a simple example to get started with `spaCyEx`:

```python
import spacyex as se
import spacy

nlp = spacy.load("en_core_web_sm")
text = "John Smith runs fast, but Jacob Smith walks slowly."
pattern = "(ent_type=person|op={2}) (lemma=in[run,walk]) (pos=ADV)"

results = se.search(pattern, text, nlp)
for match in results:
    print(match[0].text, "Start:", match[1], "End:", match[2])
```

This code will match sequences in the text based on the defined pattern, using named entities, lemmas, and parts of speech.

## Roadmap

- [ ] Support for all dictionary properties in patterns.
- [ ] Additional utilities and helper functions for more complex pattern scenarios.