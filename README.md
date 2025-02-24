# ATA2425
Advanced Text Analytics Project

## BioASQ - Task GutBrainIE - Subtask 6.1 - Named Entity Recognition

## Models

- Base: default tokenizer. alignment = "strict", then alignment = "expand". a lot of entities contain extra characters ("expand" is very used)
- Tok: custom tokenizer. alignment = "strict", then alignment = "expand". only 10 entities contain extra characters ("expand" is used only 10 times). misinterpreted entities:
    - Span: Ruminococcusgnavusgroup, Text: Ruminococcusgnavus
    - Span: TAMs, Text: TAM
    - Span: Intestinal tissues, Text: Intestinal tissue
    - Span: SGMs, Text: SGM
    - Span: cisgender heterosexuals, Text: cisgender heterosexual
    - Span: SGMs, Text: SGM
    - Span: cisgender-heterosexuals, Text: cisgender-heterosexual
    - Span: patients, Text: patient
    - Span: IBS symptoms, Text: IBS symptom
- Tok Special: custom tokenizer + 3 special cases. alignment = "strict", then alignment = "expand". only 5 entities contain extra characters. misinterpreted entities:
    - Span: Intestinal tissues, Text: Intestinal tissue
    - Span: cisgender heterosexuals, Text: cisgender heterosexual
    - Span: cisgender-heterosexuals, Text: cisgender-heterosexual
    - Span: patients, Text: patient
    - Span: IBS symptoms, Text: IBS symptom
- Tok Config: custom tokenizer + dade's configuration file
- Tok In: custom tokenizer used also during model training

## Models Score

| Model | TOK | NER P | NER R | NER F |
| ----- | --- | ----- | ----- | ----- |
| Base | 100.00 | 82.24 | 74.22 | 78.02 |
| Tok | 90.71 | 81.76 | 75.02 | 78.24 |
| Tok Special | 90.71 | 80.76 | 74.40 | 77.45 |
| Tok Config | 90.71 | 81.08 | 76.72 | 78.84 |
| Tok In | 99.52 | 81.29 | 71.17 | 75.89 |

The special cases are not useful, it is better to use "expand".
