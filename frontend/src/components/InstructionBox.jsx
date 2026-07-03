export default function InstructionBox({
  instruction,
  setInstruction,
  onGenerate,
}) {
  return (
    <div className="bg-white rounded-xl shadow p-6 mb-6">

      <h2 className="text-xl font-semibold mb-4">
        Instruction
      </h2>

      <textarea
        rows={5}
        className="w-full border rounded-lg p-3"
        value={instruction}
        onChange={(e) => setInstruction(e.target.value)}
        placeholder="Example: Tomorrow is Work From Home for Marketing."
      />

      <button
        onClick={onGenerate}
        className="mt-5 bg-green-600 text-white px-5 py-3 rounded-lg hover:bg-green-700"
      >
        Generate Draft
      </button>

    </div>
  );
}