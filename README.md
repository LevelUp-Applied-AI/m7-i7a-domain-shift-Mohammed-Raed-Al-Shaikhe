# Module 7 Week A — Integration Task: Domain-Shift Analysis

Apply your fine-tuned classifier (from Lab 7A, hosted on Hugging Face Hub) to the tech / entertainment news corpus and analyze the domain-shift behavior.

Full instructions: see the **Integration Task 7A guide** linked in TalentLMS.

## Quick start

```bash
pip install -r requirements.txt
cp .env.example .env       # then edit MODEL_HUB_ID
make smoke                 # CI substitute model on 5-row fixture
make apply                 # your real model on full 1,033-row tech-news corpus
```

## TODO for learner — fill these in before submitting

## Submission Details

- **Hugging Face Hub model URL:**  
  https://huggingface.co/MohammedRaed/m7-app-review-sentiment

- **Reproducibility command:**
  ```bash
  cp .env.example .env
  # set MODEL_HUB_ID=MohammedRaed/m7-app-review-sentiment
  pip install -r requirements.txt
  make apply
  ```

## Reproducibility

To reproduce results locally:

cp .env.example .env

# set MODEL_HUB_ID=MohammedRaed/m7-app-review-sentiment

pip install -r requirements.txt
python apply.py

## What the model was trained on

This model was fine-tuned on an app-review sentiment dataset containing thousands of user-written reviews across multiple mobile applications. Each review is labeled as one of three sentiment classes: negative (0), neutral (1), or positive (2). The training data consists primarily of short, subjective, opinionated text where sentiment is often explicitly expressed through emotional language such as “great,” “terrible,” or “love/hate”.

Because the training domain is app reviews, the model learns patterns tied to consumer opinions, usability feedback, and emotionally charged expressions rather than factual reporting or neutral informational text.

## Why we apply it to news data (domain shift)

In this task, we apply the same sentiment classifier to a completely different domain: tech and entertainment news articles. Unlike app reviews, news articles are typically more formal, factual, and less emotionally explicit. This creates a domain shift, meaning the statistical patterns in the input text differ significantly from what the model saw during training.

We expect performance degradation because sentiment cues in news are often subtle or absent, and many sentences are descriptive rather than opinionated. As a result, the model may incorrectly map neutral statements to sentiment classes based on superficial word associations learned from review data.

This experiment demonstrates a key limitation of machine learning models: strong in-domain performance does not guarantee robustness when the input distribution changes.

## Submission

Open a PR from `integration-7a-domain-shift` into `main`. Paste the PR URL into TalentLMS → Module 7 → Integration Task 7A.

---

## License

This repository is provided for educational use only. See [LICENSE](LICENSE) for terms.

You may clone and modify this repository for personal learning and practice, and reference code you wrote here in your professional portfolio. Redistribution outside this course is not permitted.
