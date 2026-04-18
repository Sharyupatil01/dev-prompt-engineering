## 🎭 Technique #2: Role Prompting

Role prompting is a powerful prompt engineering technique where you assign a **specific role or persona** to ChatGPT to control the tone, style, and depth of its responses.

---

## 🤔 What is Role Prompting?

Role prompting means instructing the AI to behave like a particular expert or persona.

👉 Instead of asking:
```
Write a review of a pizza place
```

👉 You assign a role:
```
You are a food critic. Write a review of a pizza place
```

This small change can significantly improve the **quality, tone, and structure** of the output.

---

## 🎯 Why Use Role Prompting?

- Controls tone (formal, casual, persuasive)
- Improves clarity and depth
- Makes outputs more realistic and domain-specific
- Helps in professional communication

---

## ✍️ Application #1: Styling Text

### 🟢 Example: Food Review

| Prompt Type | Output Style |
|------------|-------------|
| Basic Prompt | Generic and simple |
| Food Critic | Detailed and descriptive |
| Michelin Reviewer | Professional and refined |

👉 Insight: Assigning a stronger role = richer output

---

### 🟢 Example: Writing Emails

Role prompting changes **tone and intention**:

- **Communications Specialist** → Clear, professional, direct
- **Marketing Expert** → Persuasive, engaging, positive
- **Customer Support** → Empathetic, solution-focused

👉 Same task, different roles → completely different communication styles

---

## 🧮 Application #2: Improving Accuracy

Role prompting can sometimes improve **logical reasoning and correctness**, especially in structured tasks.

### Example

```
You are a brilliant mathematician. Solve:
100 × 100 ÷ 400 × 56
```

Correct Answer: **1400**

👉 Without role prompting, models may sometimes make calculation mistakes.

---

## 🧠 Pro Tips for Developers

- Combine role + task + constraints

### 🔥 Powerful Prompt Structure
```
You are a [ROLE].
Your task is to [TASK].
Constraints: [RULES]
Output format: [FORMAT]
```

### Example
```
You are a senior software engineer.
Explain REST APIs with real-world examples.
Keep it beginner-friendly.
```

---

## ⚠️ Limitations

- Newer models already perform well without roles
- Overusing roles may not always improve results
- Role should match the task (don’t overcomplicate)

---

## 🧭 When to Use Role Prompting?

| Scenario | Use Role Prompting? |
|--------|--------------------|
| Writing emails | ✅ Yes |
| Content creation | ✅ Yes |
| Coding explanations | ✅ Yes |
| Simple questions | ❌ Not necessary |

---

## 🏁 Key Takeaway

💡 Role prompting is one of the **simplest yet most powerful techniques** in prompt engineering.

👉 If your output feels generic → add a role.
👉 If your output lacks depth → refine the role.

---

