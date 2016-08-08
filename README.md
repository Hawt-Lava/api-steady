[![Stories in Ready](https://badge.waffle.io/LavaHq/api-steady.png?label=ready&title=Ready)](https://waffle.io/LavaHq/api-steady)
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


## Interaction
We need to handle the following cases. 

- [ ] `GET` given a user, return a list of entries grouped by prompt: `/entries?user=<user>` 
- [X] `POST` create a user based off of a device 
token `/users`
- [X] `POST` create a grouping of entries in a scoresheet `/scoresheets`
