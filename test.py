import unittest
from run import app
import json
from datetime import datetime

class TestBilletera(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_pago_exitoso(self):
        response = self.app.get('/billetera/pagar?minumero=21345&numerodestino=123&valor=100')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        try:
            datetime.strptime(data['mensaje'], 'Realizado en %d/%m/%Y')
        except ValueError:
            self.fail("La fecha no tiene el formato correcto")

    def test_pago_sin_saldo(self):
        response = self.app.get('/billetera/pagar?minumero=21345&numerodestino=123&valor=2000')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), {'error': 'Saldo insuficiente'})

    def test_pago_sin_contacto(self):
        response = self.app.get('/billetera/pagar?minumero=21345&numerodestino=789&valor=100')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.data), {'error': 'Número de cuenta o destino no encontrado'})

    def test_pago_sin_cuenta(self):
        response = self.app.get('/billetera/pagar?minumero=789&numerodestino=123&valor=100')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.data), {'error': 'Número de cuenta o destino no encontrado'})

if __name__ == '__main__':
    unittest.main()
    