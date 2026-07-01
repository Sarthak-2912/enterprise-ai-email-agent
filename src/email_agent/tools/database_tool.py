from email_agent.database.database_service import (
    get_employee_emails_by_department,
)


class DatabaseTool:

    def find_recipients(self, recipient_type, recipient_value):

        if recipient_type == "department":
            return get_employee_emails_by_department(recipient_value)

        raise ValueError(
            f"Unsupported recipient type: {recipient_type}"
        )