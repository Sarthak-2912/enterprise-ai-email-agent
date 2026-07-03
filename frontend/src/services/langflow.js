const LANGFLOW_URL = "http://localhost:7860";
const DRAFT_FLOW_ID = "a597a795-655c-4080-bc50-e8ee3263607e";

const LANGFLOW_API_KEY = "sk-y7PFgQG_MZzlVbm-gwY2YheGuZQU468K9jHHjCbLLA0";

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
        },
      }),
    }
  );

  console.log("Status:", response.status);

  const text = await response.text();

  console.log("Raw Response:");
  console.log(text);

  return text;
}