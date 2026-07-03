export default function GmailSelector({
  accounts,
  selectedAccount,
  onSelect,
  onConnect,
}) {
  return (
    <div className="bg-white rounded-xl shadow p-6 mb-6">
      <h2 className="text-xl font-semibold mb-4">
        Connected Gmail
      </h2>

      <select
        className="w-full border rounded-lg p-3 mb-4"
        value={selectedAccount}
        onChange={(e) => onSelect(e.target.value)}
      >
        {accounts.length === 0 ? (
          <option>No Gmail Connected</option>
        ) : (
          accounts.map((account) => (
            <option key={account} value={account}>
              {account}
            </option>
          ))
        )}
      </select>

      <button
        onClick={onConnect}
        className="bg-blue-600 text-white px-5 py-3 rounded-lg hover:bg-blue-700"
      >
        Connect Gmail
      </button>
    </div>
  );
}