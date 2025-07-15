# 📘 Sample Prompt Instructions — Synthetic Loan Data MCP

This guide helps you write prompts for AI agents that use the `loan_application_mcp.json` protocol. These instructions are meant for **humans**, not the AI agent itself.

---

## ✅ General Prompting Guidelines

| Rule            | Description                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| 📅 Use ISO dates | Convert Excel serial dates to ISO format (e.g., `2025-07-01`)              |
| 🚫 No guessing   | If data is missing or irrelevant, reply with `"I am unsure"`               |
| ✅ Clear output  | Ask for responses in markdown tables or JSON fenced blocks (` ```json `)   |
| 🛡️ Stay scoped   | Only answer using fields from the MCP; do not rely on external knowledge   |

---

## 🧠 Example Prompt Patterns

### 🔹 1. Ask about disbursed loans
> *List all applications where `Application Status` is `"Disbursed"`. Show `ID`, `Branch Name`, and `Loan Amount`.*

### 🔹 2. Ask about aging
> *Which top 3 applications have the highest `Aging` values?*

### 🔹 3. Check pending disbursement aging
> *For applications with `Application Status = "Pending Disbursement"`, show their `ID` and `Pending Disbursement Aging`.*

### 🔹 4. Invalid query
> *What is the applicant’s name for `APP100006`?*  
> (✅ Expected response: `"I am unsure"` — no applicant name in MCP)

---

## 🧩 Field Reference (from MCP)

- `ID`: Loan application ID  
- `BRANCH NAME`: Where application originated  
- `CREATED AT`, `UPDATED AT`, `Sanction Date`: Excel serial dates — convert to ISO  
- `LOAN AMOUNT`: Amount requested  
- `Application Status`: Enum (e.g., Disbursed, Declined, Pending Disbursement...)  
- `Aging`: Days since last update  
- `Pending Disbursement Aging`: Only present for "Pending Disbursement" entries

---

## 🔍 Tips

- Start with summary queries before asking for filters
- Avoid vague phrasing like “What’s going on with this app?”
- Prefer explicit conditions (`"Application Status = Draft: Query"` instead of `"not final"`)

---

