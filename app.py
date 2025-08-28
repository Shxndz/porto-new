from flask import Flask, request, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Kalkulator Flask</title>
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gradient-to-r from-gray-900 via-gray-800 to-gray-900 text-white flex items-center justify-center min-h-screen">
  <div class="bg-gray-800 p-6 rounded-2xl shadow-xl w-96 border border-gray-700">
    <h1 class="text-3xl font-bold mb-6 text-center text-blue-400">🧮 Kalkulator</h1>

    <form method="POST" action="/" class="space-y-4">
      <input type="number" step="any" name="num1" placeholder="Masukkan angka pertama"
             class="w-full px-4 py-2 rounded-lg text-black focus:ring-2 focus:ring-blue-500" required>

      <input type="number" step="any" name="num2" placeholder="Masukkan angka kedua"
             class="w-full px-4 py-2 rounded-lg text-black focus:ring-2 focus:ring-blue-500" required>

      <select name="operation" class="w-full px-4 py-2 rounded-lg text-black focus:ring-2 focus:ring-blue-500">
        <option value="add">➕ Tambah</option>
        <option value="subtract">➖ Kurang</option>
        <option value="multiply">✖ Kali</option>
        <option value="divide">➗ Bagi</option>
      </select>

      <button type="submit" class="w-full bg-blue-600 hover:bg-blue-700 py-2 rounded-lg font-semibold shadow-md transition">
        Hitung
      </button>
    </form>

    {% if result is not none %}
    <div class="mt-6 text-center bg-gray-700 py-3 rounded-lg">
      <h2 class="text-xl font-semibold text-green-400">Hasil: {{ result }}</h2>
    </div>
    {% endif %}
  </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operation = request.form["operation"]

            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                result = num1 / num2 if num2 != 0 else "Error: Bagi 0"
        except Exception as e:
            result = f"Error: {str(e)}"

    return render_template_string(html, result=result)

if __name__ == "__main__":
    app.run(debug=True)
