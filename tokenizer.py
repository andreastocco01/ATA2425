from spacy.util import registry, compile_suffix_regex
import re
from spacy.tokenizer import Tokenizer

@registry.callbacks("customize_tokenizer")
def make_customize_tokenizer():
    def custom_tokenizer(nlp):
        prefix_re = re.compile(r'[.,;:?!(\[\'"</]')
        suffix_re = re.compile(r'[.,;:?!)\]\'">■™]')
        infix_re = re.compile(r'[-/+=&]')
        nlp.tokenizer.prefix_search = prefix_re.search
        nlp.tokenizer.suffix_search = suffix_re.search
        nlp.tokenizer.infix_finditer = infix_re.finditer
    return custom_tokenizer
