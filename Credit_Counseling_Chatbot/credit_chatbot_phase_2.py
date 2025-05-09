# # Credit Counseling Chatbot (Phase 2 - Free Typing Input)
print("\nWelcome your Credit Counseling Chatbot!")
print("You can type your question or concern below.\n")

# Ask user to describe their issue
user_input = input("What's on your mind? (credit score, debt, goodwill letter, budgeting): ").lower()
# .lower() makes the input case insensitive

# Check keywords and respond
if "credit score" in user_input or "fix my credit" in user_input or "improve" in user_input:
       print("\nCredit Score Tips:")
       print("- Pay at least the minimum on time — every month.")
       print("- Keep your credit usage below 30%.")
       print("- Don’t open too many new accounts at once.")
       print("- Dispute errors on your report if needed.")
elif "debt" in user_input or "collections" in user_input or "pay off" in user_input:
       print("\nDebt Payoff Tips:")
       print("- Try the 'Avalanche' method: Pay high interest first.")
       print("- Or the 'Snowball' method: Pay small debts first to gain momentum.")
       print("- Avoid only making minimum payments.")
       print("- Call lenders to negotiate payment plans or settlements.")
elif "goodwill" in user_input or "late payment" in user_input:
       print("\n📝 Goodwill Letter Advice:")
       print("- A goodwill letter politely asks a creditor to remove a late payment.")
       print("- Mention any hardship (like illness or job loss).")
       print("- Be honest, brief, and respectful.")
       print("- Always follow up and keep a copy.")
elif "budget" in user_input or "money plan" in user_input or "save" in user_input:
       print("\nBudgeting Basics:")
       print("- Use the 50/30/20 rule: Needs/Wants/Savings.")
       print("- Track every dollar for 1 month to find leaks.")
       print("- Use apps like Mint or YNAB to manage your spending.")
       print("- Build an emergency fund, even if slowly.")
else:
       print("\nSorry, I didn't recognize that topic.")
       print("Try asking about: credit score, debt, goodwill letters, or budgeting.")

# Motivational message
print("\nYou're doing great just by asking questions. Keep going, you're not alone.\n")