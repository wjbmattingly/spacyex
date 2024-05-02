# spaCyEx
[![PyPI version](https://badge.fury.io/py/spacyex.svg)](https://pypi.org/project/spacyex/)
[![GitHub stars](https://img.shields.io/github/stars/wjbmattingly/spacyex.svg?style=social&label=Star&maxAge=2592000)](https://github.com/wjbmattingly/spacyex/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/wjbmattingly/spacyex.svg?style=social&label=Fork&maxAge=2592000)](https://github.com/wjbmattingly/spacyex/network)


`spaCyEx` is a powerful extension for spaCy, designed to make pattern matching as flexible and easy as using regular expressions. It builds upon the existing capabilities of spaCy's `Matcher`, enhancing it with a more accessible syntax for defining complex patterns. `spaCyEx` allows for intuitive and detailed text pattern specifications, perfect for extracting detailed linguistic features from texts.

## Installation

You can install `spaCyEx` via pip:

```bash
pip install spacyex
```

## Features

- **Dynamic Pattern Creation**: Create complex token matching patterns using a simple string-based syntax.
- **Integration with spaCy**: Leverage spaCy's Matcher capabilities to find sequences in text that match defined patterns.
- **Customizable Matching Rules**: Define token attributes including text characteristics, lexical attributes, and grammatical properties.

### Creating Patterns

Define patterns using a string syntax where each token and its attributes are encapsulated by parentheses. Token attributes are specified by key-value pairs, separated by an equals sign (`=`), and multiple attributes are divided by a pipe (`|`).

#### Syntax Examples

- **Single Attribute**: `(pos=NOUN)`
- **Multiple Attributes**: `(pos=NOUN|lemma=run)`
- **Using List Values**: `(lemma=in[run,walk])`
- **Using Operators**: `(ent_type=person|op={2,3})`

### Pattern Matching

Once a pattern is defined, it can be used to search text for matches.


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