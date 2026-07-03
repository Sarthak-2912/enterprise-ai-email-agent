export default function Navbar() {
  return (
    <nav className="bg-white shadow">

      <div className="max-w-6xl mx-auto px-6 py-4 flex justify-between items-center">

        <h1 className="text-2xl font-bold text-blue-700">
          Enterprise Email Assistant
        </h1>

        <div className="text-right">

          <p className="font-semibold">
            Not Connected
          </p>

          <p className="text-gray-500 text-sm">
            Connect Gmail to continue
          </p>

        </div>

      </div>

    </nav>
  );
}