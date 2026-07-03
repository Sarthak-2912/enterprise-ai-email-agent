export default function RecipientSelector() {
  return (
    <div className="bg-white rounded-xl shadow p-6 mb-6">

      <h2 className="text-xl font-semibold mb-4">

        Recipient

      </h2>

      <select className="w-full border rounded-lg p-3 mb-4">

        <option>Department</option>

      </select>

      <input
        className="w-full border rounded-lg p-3"
        placeholder="Marketing"
      />

    </div>
  );
}