from spacy.util import registry, compile_suffix_regex
import re
from spacy.tokenizer import Tokenizer
import spacy.util

@registry.tokenizers("custom_tokenizer")
def make_custom_tokenizer():
    def custom_tok(nlp):
        prefix_re = re.compile(r'[.,;:?!(\[\'"</]')
        suffix_re = re.compile(r'[.,;:?!)\]\'">■™]')
        infix_re = re.compile(r'[-/+=&]')

        '''prefix_re = spacy.util.compile_prefix_regex(list(nlp.Defaults.prefixes) + [prefix.pattern])
        suffix_re = spacy.util.compile_suffix_regex(list(nlp.Defaults.suffixes) + [suffix.pattern])
        infix_re = spacy.util.compile_infix_regex(list(nlp.Defaults.infixes) + [infix.pattern])'''

        tokenizer = Tokenizer(
            nlp.vocab,
            prefix_search=prefix_re.search,
            suffix_search=suffix_re.search,
            infix_finditer=infix_re.finditer
        )

        return tokenizer
    return custom_tok
