# pycode — OpenAI example (compatible with Python 3.14)

This small project demonstrates calling the OpenAI Chat Completions API without using LangChain, so it remains compatible with Python 3.14.

## Why this change
LangChain (and some of its dependencies like Pydantic v1 and tiktoken) are not yet fully compatible with Python 3.14. This project uses the official `openai` client directly to avoid those compatibility issues.

## Setup (macOS)
1. Ensure you have Python 3.14 installed and active for the project (this repo is set to `python_version = "3.14"` in `Pipfile`).
2. Create the pipenv environment and install dependencies:

```bash
pipenv --rm || true
pipenv install
```

3. Set your API key (do NOT hardcode it in source):

```bash
export OPENAI_API_KEY="sk-REPLACE_WITH_YOUR_KEY"
```

4. Run the script:

```bash
pipenv run python main.py
```

## If you previously leaked an API key
If a key was committed to source (a secret has been removed from `main.py`), revoke it and create a new key in the OpenAI dashboard: https://platform.openai.com/account/api-keys

## Notes
- If you need LangChain features, consider using a Python 3.11/3.12 environment until downstream packages add full 3.14 support.
- For transient rate limits, the script prints a helpful message with a link to the billing page.
