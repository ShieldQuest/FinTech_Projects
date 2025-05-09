# Credit Counseling Chatbot (Phase 1)
print("\nWelcome your Credit Counseling Chatbot!")
print("I'm here to help you get your credit life together\n")

# User choices
print("What do you need help with today?")
print("1. Improving my Credit Score")
print("2. Paying off debt")
print("3. Writting a goodwill letter")
print("4. Budgeting Advice")

# Get User Input
choice = input("\nPlease enter the number of your choice (1-4): ")

# Give realistic advised based on choice
if choice == "1":
    print("\nCredit Score Tips:")
    print("- Pay at least the minimum on time - every month.")
    print("- Keep your credit usage below 30%.")
    print("- Don't open too many new accounts at once.")
    print("- Dispute error on you credit report if needed.")
elif choice == "2":
    print("\nDebt Payoff Tips:")
    print("- Try the 'Avalanche' method: Pay high interest first.")
    print("- Or the 'Snowball' method: Pay small debts first to gain momentum.")
    print("- Avoid only paying the minimum payments.")
    print("- Call lenders to negotiate payment plans or settlements.")
elif choice == "3":
    print("\nGoodwill Letter Advice:")
    print("- A goodwill letter politley asks a creditor to remove a late payment.")
    print("- Mention any hardship (like illness or job loss).")
    print("- Be honest, brief, and respectful.")
    print("- Always follow up and keep a copy.")
elif choice == "4":
    print("\nBudgeting Basics:")
    print("- Use the 50/30/20 rule: Needs/Wants/Savings.")
    print("- Track every dollar for 1 month to find leaks.")
    print("- Use apps like Mint or YNAB to manage your spending.")
    print("- Build an emergency fund, evenn if slowly.")
else:
    print("\nSorry, that's not a valid option. Please run the program again.")

# Goodbye message
print("\nYou've taken a  great first step! Keep learning and building your credit future.\n")
