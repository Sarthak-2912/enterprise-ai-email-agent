export default function LoginCard({ onConnect }) {
  return (
    <div>
      <h1>Enterprise Email Assistant</h1>

      <p>
        Generate professional emails using AI and send them
        from your connected Gmail account.
      </p>

      <button onClick={onConnect}>
        Connect Gmail
      </button>
    </div>
  );
}