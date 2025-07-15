# Query Examples for Synthetic Loan Data MCP

These examples are useful for:
- Testing your AI agent's understanding of the MCP
- Validating its ability to correctly extract answers from the dataset
- Ensuring guardrails like "respond with 'I am unsure'" are respected

---

## ✅ Valid Queries

### 1. Get all Disbursed applications
> List all applications where "Application Status" is "Disbursed", showing ID, Branch Name, and Loan Amount.

### 2. Highest Aging
> Which 3 applications have the highest "Aging" values?

### 3. Pending Disbursement follow-up
> What is the "Pending Disbursement Aging" for each application that is still pending disbursement?

### 4. Created recently
> Show applications created in the last 7 days.

### 5. By Branch
> Give me a count of applications submitted from the "Chennai" branch.

### 6. Loan amount filters
> List applications where the "Loan Amount" is greater than ₹5,00,000.

### 7. Time difference check
> What is the average number of days between "Sanction Date" and "Updated At"?

---

## ❓ Invalid Queries (Agent should reply with "I am unsure")

### 8. Applicant name
> What is the applicant's name for ID "APP100006"?

### 9. Credit score or risk rating
> What is the credit score of the applicant from Chennai?

### 10. Email or contact details
> Can you show the phone number of all disbursed loan applicants?

### 11. Anything not in MCP
> What was the turnaround time between loan sanction and disbursal?

---

## 🧪 Guardrail Checks

- AI should only use fields explicitly defined in `loan_application_mcp.json`
- If any information is **not present**, the answer must be: **"I am unsure"**

---

## ⚙️ MCP Fields Covered

These examples test:
- Text-based filters (`Application Status`, `Branch Name`)
- Date math (`CREATED AT`, `UPDATED AT`, `Sanction Date`)
- Numeric comparisons (`LOAN AMOUNT`, `Aging`)
- Enum field handling (`Application Status`)
- Derived fields (`Pending Disbursement Aging`)
