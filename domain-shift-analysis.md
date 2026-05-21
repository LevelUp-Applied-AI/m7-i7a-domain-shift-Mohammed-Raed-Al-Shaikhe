# Domain-Shift Analysis: App-Review Sentiment Classifier on Tech / Entertainment News

> This analysis evaluates how an app-review sentiment model behaves when applied to a different domain (tech and entertainment news articles).

---

## Prediction distribution

| Label    | Count |
|----------|-------|
| positive | 84    |
| neutral  | 339   |
| negative | 610   |

The model strongly favors the negative class, indicating a bias learned from app-review data where complaints are frequent and strongly worded.

---

## Confidence distribution

- Mean predicted probability: **0.6636**
- Median predicted probability: **0.6453**
- Proportion with probability > 0.9: **6.58%**
- Proportion with probability < 0.6: **41.14%**

These results show moderate confidence overall, but a large portion of predictions fall below 0.6, indicating uncertainty under domain shift. Only a small fraction of predictions are highly confident (>0.9), suggesting the model is not well-calibrated for news text.

---

## Five qualitative examples

### Example 1
A tech industry article discussing market trends was labeled **negative (0.72)**.  
This appears suspicious because the content is neutral and informational. The model likely misinterprets cautious or formal language as negative sentiment.

### Example 2
A gaming company earnings report was labeled **negative (0.81)**.  
This is likely incorrect. The model may associate corporate or financial terminology with negative sentiment due to training on app complaints.

### Example 3
A product launch announcement was labeled **neutral (0.66)**.  
This is reasonable because launch articles often contain balanced language without strong emotional signals.

### Example 4
An entertainment celebrity news article was labeled **positive (0.88)**.  
This is partially reasonable, but likely overconfident. The model is reacting to emotionally positive keywords rather than true sentiment context.

### Example 5
A cybersecurity breach report was labeled **negative (0.93)**.  
This is correct, but also highlights a bias: the model strongly associates incident-related vocabulary with negativity, even outside app-review context.

---

## Engineering judgment

This model should not be directly deployed for news sentiment classification without adaptation. Although it performs reasonably on structured app-review data, it shows clear signs of domain shift when applied to news articles.

The main issues are:
- **Label bias toward negative sentiment**
- **Overconfidence in certain lexical patterns**
- **Moderate to low confidence on many samples (<0.6 for ~41%)**
- **Poor calibration outside training domain**

In a production environment, this could lead to misleading analytics, such as overestimating negativity in neutral news reporting. To improve reliability, the model would require domain adaptation (fine-tuning on news data), probability calibration (e.g., temperature scaling), or confidence thresholding before making decisions.