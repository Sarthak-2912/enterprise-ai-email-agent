from email_agent.gmail.auth_manager import login
from email_agent.gmail.gmail_service import GmailService

from email_agent.tools.intent_extractor import IntentExtractor
from email_agent.tools.database_tool import DatabaseTool
from email_agent.tools.draft_tool import DraftTool


def main():

    print("=" * 60)
    print("Enterprise AI Email Agent")
    print("=" * 60)

    # Login
    session = login()

    print(f"\nLogged in as: {session.email}")

    # Initialize tools
    extractor = IntentExtractor()
    database = DatabaseTool()
    draft_tool = DraftTool()
    gmail = GmailService(session)

    # User input
    prompt = input("\nWhat would you like me to do?\n> ")

    # Step 1 - Intent Extraction
    intents = extractor.extract(prompt)

    print("\nIntent:")
    print(intents)

    # Handle both a single object and a list
    if isinstance(intents, dict):
        intents = [intents]

    for intent in intents:

        print("\n" + "=" * 60)
        print(f"Department: {intent['department']}")

        recipients = database.find_recipients(
        recipient_type="department",
        recipient_value=intent["department"]
       )

        print("Recipients:")
        print(recipients)

        if not recipients:
            print("No recipients found.")
            continue

        draft = draft_tool.draft(
            intent["instruction"]
        )

        print("\nGenerated Email")
        print("-" * 60)
        print("Subject:", draft["subject"])
        print()
        print(draft["body"])
        print("-" * 60)

        choice = input("\nSend this email? (yes/no): ").strip().lower()

        if choice != "yes":
            print("Skipped.")
            continue

        gmail.send_email(
            recipients=recipients,
            subject=draft["subject"],
            body=draft["body"]
        )

        print("Email sent successfully.")

    print("\nAll requests processed.")


if __name__ == "__main__":
    main()