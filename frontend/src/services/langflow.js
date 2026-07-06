const LANGFLOW_URL = import.meta.env.VITE_LANGFLOW_URL;

const DRAFT_FLOW_ID = import.meta.env.VITE_DRAFT_FLOW_ID;
const SEND_FLOW_ID = import.meta.env.VITE_SEND_FLOW_ID;

const LANGFLOW_API_KEY = import.meta.env.VITE_LANGFLOW_API_KEY;

// --------------------
// Generate Draft
// --------------------
export async function generateDraft(instruction) {
  const response = await fetch(
    `${LANGFLOW_URL}/api/v1/run/${DRAFT_FLOW_ID}?stream=false`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "x-api-key": LANGFLOW_API_KEY,
      },
      body: JSON.stringify({
        input_request: {
          input_value: instruction,
          input_type: "chat",
          output_type: "chat",
          session_id: window.crypto.randomUUID(),
        },
      }),
    }
  );

  if (!response.ok) {
    throw new Error(await response.text());
  }

  const result = await response.json();

  let text =
    result.outputs[0].outputs[0].results.message.text;

  text = text
    .replace(/```json/g, "")
    .replace(/```/g, "")
    .trim();

  return JSON.parse(text);
}

// --------------------
// Send Email
// --------------------
export async function sendEmail({
  sender,
  recipients,
  subject,
  body,
}) {
  const prompt = `
Sender Email:
${sender}

Recipients:
${JSON.stringify(recipients)}

Subject:
${subject}

Body:
${body}
`;

  const response = await fetch(
    `${LANGFLOW_URL}/api/v1/run/${SEND_FLOW_ID}?stream=false`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "x-api-key": LANGFLOW_API_KEY,
      },
      body: JSON.stringify({
        input_request: {
          input_value: prompt,
          input_type: "chat",
          output_type: "chat",
          session_id: window.crypto.randomUUID(),
        },
      }),
    }
  );

  if (!response.ok) {
    throw new Error(await response.text());
  }

  const result = await response.json();

  // Print the complete response so we can inspect it
  console.log("Send Flow Response:");
  console.log(result);

  return result;
}