from email_agent.tools.intent_extractor import IntentExtractor

agent = IntentExtractor()

result = agent.extract(

    "Send an email to everyone in Marketing saying tomorrow is Work From Home."

)

print(result)