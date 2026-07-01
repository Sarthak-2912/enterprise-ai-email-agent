from email_agent.tools.draft_tool import DraftTool

draft = DraftTool()

email = draft.draft(
    "Tomorrow is Work From Home."
)

print(email)