const API_URL = "http://127.0.0.1:8000";

export async function connectGoogleAccount() {
  const response = await fetch(`${API_URL}/auth/login`, {
    method: "POST",
  });

  if (!response.ok) {
    throw new Error("Failed to connect Gmail.");
  }

  return await response.json();
}

export async function getConnectedAccounts() {
  const response = await fetch(`${API_URL}/auth/accounts`);

  if (!response.ok) {
    throw new Error("Failed to load Gmail accounts.");
  }

  return await response.json();
}