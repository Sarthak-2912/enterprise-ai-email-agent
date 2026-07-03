export default function DraftEditor({
  draft,
  setDraft,
}) {
  return (
    <div className="bg-white rounded-xl shadow p-6">

      <h2 className="text-xl font-semibold mb-4">
        Email Draft
      </h2>

      <input
        className="w-full border rounded-lg p-3 mb-4"
        value={draft.subject}
        onChange={(e) =>
          setDraft({
            ...draft,
            subject: e.target.value,
          })
        }
        placeholder="Subject"
      />

      <textarea
        rows={10}
        className="w-full border rounded-lg p-3 mb-4"
        value={draft.body}
        onChange={(e) =>
          setDraft({
            ...draft,
            body: e.target.value,
          })
        }
        placeholder="Email Body"
      />

      <button className="bg-blue-700 text-white px-5 py-3 rounded-lg hover:bg-blue-800">
        Send Email
      </button>

    </div>
  );
}