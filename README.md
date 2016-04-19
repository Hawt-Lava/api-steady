# API
A custom API that supports https://github.com/Hawt-Lava/app-steady

## Model Relationship

One `ScoreSheet` contains multiple entries, and each entry contains one prompt
```
Scoresheet
      |_entry
             |_prompt
      |_entry
             |_prompt
      |_entry
             |_prompt
```

We will be re-using prompts in multiple entries.
