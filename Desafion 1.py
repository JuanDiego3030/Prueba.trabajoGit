#DESAFIO N3
import random

# Requerimiento 1: Asignar valores literales a variables
nombre_empleado = "Raulymar De Abreu"
salario_base = 1500  # Ejemplo de salario base

# Requerimiento 2: Asignar valores aleatorios a variables
tarifa_por_hora = random.randint(20, 50)
horas_trabajadas = random.randint(5, 40)

# Requerimiento 3: Calcular el monto total por horas trabajadas
monto_por_horas = tarifa_por_hora * horas_trabajadas

# Requerimiento 4: Calcular el salario total del empleado
salario_total = salario_base + monto_por_horas

# Requerimiento 5: Mostrar el "recibo de pago"
print("------------Recibo de Pago------------")
print("--Nombre del Empleado:", nombre_empleado)
print("--Salario Base:", salario_base)
print("--Horas Trabajadas:", horas_trabajadas)
print("--Tarifa por Hora:", tarifa_por_hora)
print("--Monto por Horas Trabajadas:", monto_por_horas)
print("Salario Total:", salario_total)