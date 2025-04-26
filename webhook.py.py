from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/tradingview', methods=['POST'])
def receive_signal():
    data = request.json
    print(f"Señal recibida: {data}")

    # Responder para confirmar que la señal fue recibida
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)