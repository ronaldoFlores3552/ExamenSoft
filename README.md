# ExamenSoft

Examen final del curso:

pregunta 1:
simulación de una bd:
![image](https://github.com/ronaldoFlores3552/ExamenSoft/assets/85258014/2703de69-392c-4d4a-9841-47761cfba549)

resultados de los endpoints:
1.
![image](https://github.com/ronaldoFlores3552/ExamenSoft/assets/85258014/f2b75a4e-1164-4fa7-88f4-5b22be284f0b)

2.
![image](https://github.com/ronaldoFlores3552/ExamenSoft/assets/85258014/ca59c2f6-8ebe-444e-aaa1-4c40562972fb)

3.
![image](https://github.com/ronaldoFlores3552/ExamenSoft/assets/85258014/f24e5986-2ef6-47df-8c72-eecf0cbeeff6)

Pregunta 2:
![image](https://github.com/ronaldoFlores3552/ExamenSoft/assets/85258014/e7db8400-9d05-4c1c-80a7-3b051d51a655)

Pregunta 3:

Los cambios necesarios para soportar un valor máximo de dinero transferido en el día:

1. Agregamos un nuevo campo en la base de datos para cada cuenta que registre la cantidad total de dinero transferido en el día actual.
2. Antes de realizar una transferencia, verificamos la suma del valor a transferir con el total transferido en el día, si en el día actual excede el límite diario se rechaza, si no continua con normalidad.
3. Si la transferencia es exitosa, actualizamos el total transferido en el día actual.

los cambios a las pruebas:
1. Un caso en el que la suma de las transferencias en un día no exceda el límite diario, este caso es de éxito
2. Un caso en el que la suma de las transferencias en un día exceda el límite diario, debe fallar.
