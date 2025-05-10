# ATA2425
Advanced Text Analytics Project

## BioASQ - Task GutBrainIE - Subtask 6.1 - Named Entity Recognition

## Models

Use of alignment = "strict" in every model

- Base: default tokenizer in document creation and during training (1118 non recognized entities)
- Tok: custom tokenizer in document creation and during training (all the entities are recognized)
- No Tags: HTML tags removal during preprocessing (365 non recognized entities)

## Models Score

| Model | TOK | NER P | NER R | NER F |
| ----- | --- | ----- | ----- | ----- |
| Base | 100.00 | 83.25 | 74.19 | 78.46 |
| Tok | 100.00 | 75.75 | 74.66 | 75.20 |
| No Tags | 100.00 | 77.58 | 73.64 | 75.56

## Create Models

Run the `gutbrainie_ner.ipynb` to generate all the models examined in this task.

## Running Predictions

To generate predictions on the test data using the trained model, run the script `submission.py`.
For simplicity, the trained model is already included in the repository.

**Important**: Before running the script, make sure to update the path to your test data inside `submission.py`.
