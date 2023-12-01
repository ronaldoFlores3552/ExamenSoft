from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# Simulación de base de datos en memoria
db = {
    'contactos': {
        '21345': {'123': 'Luisa', '456': 'Andrea'},
        '123': {'21345':'Christian'},
        '456': {'21345':'Christian', '123': 'Luisa'}
    },
    'cuentas': {
        '21345': {'saldo': 1000, 'operaciones': []},
        '123': {'saldo': 550, 'operaciones': ['Pago recibido de 100 de Christian', 'Pago realizado de 50 a Andrea']},
        '456': {'saldo': 0, 'operaciones': []}
    }
}

@app.route('/billetera/contactos', methods=['GET'])
def obtener_contactos():
    numero = request.args.get('minumero')
    if numero in db['contactos']:
        return jsonify(db['contactos'][numero])
    else:
        return jsonify({'error': 'Número no encontrado'}), 404

@app.route('/billetera/pagar', methods=['GET'])
def realizar_pago():
    numero_origen = request.args.get('minumero')
    numero_destino = request.args.get('numerodestino')
    valor = int(request.args.get('valor'))

    if numero_origen in db['cuentas'] and numero_destino in db['contactos'][numero_origen]:
        saldo_actual = db['cuentas'][numero_origen]['saldo']
        if saldo_actual >= valor:
            # Realizar la transferencia
            db['cuentas'][numero_origen]['saldo'] -= valor
            db['cuentas'][numero_origen]['operaciones'].append(f'Pago a {numero_destino} por {valor}. Realizado en {datetime.now().strftime("%d/%m/%Y")}')
            db['cuentas'][numero_destino]['saldo'] += valor
            db['cuentas'][numero_destino]['operaciones'].append(f'Recibido de {numero_origen} por {valor}. Realizado en {datetime.now().strftime("%d/%m/%Y")}')
            return jsonify({'mensaje': f'Realizado en {datetime.now().strftime("%d/%m/%Y")}'})
        else:
            return jsonify({'error': 'Saldo insuficiente'}), 400
    else:
        return jsonify({'error': 'Número de cuenta o destino no encontrado'}), 404


@app.route('/billetera/historial', methods=['GET'])
def obtener_historial():
    numero = request.args.get('minumero')
    if numero in db['cuentas']:
        saldo = db['cuentas'][numero]['saldo']
        operaciones = db['cuentas'][numero]['operaciones']
        return jsonify({'saldo': saldo, 'operaciones': operaciones})
    else:
        return jsonify({'error': 'Número no encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
