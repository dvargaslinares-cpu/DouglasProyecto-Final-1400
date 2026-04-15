import json
import time
import sys

COSTO_POR_HORA = 25
ARCHIVO = "datos.json"


class ServicioTecnico:

    def __init__(self):
        self.cliente = ""

    def iniciar(self):
        self.cliente = input("[Servicio Técnico]: Ingrese su nombre: ")

        while True:
            try:
                opcion = self.menu()

                if opcion == "1":
                    self.revisar()
                elif opcion == "2":
                    self.reparar()
                elif opcion == "3":
                    self.donar()
                else:
                    print("[Servicio Técnico]: Opción no válida")

            except Exception as e:
                print("[Servicio Técnico]: Error controlado:", e)

    def continuar(self):
        opcion = input(f"\n[Servicio Técnico]: {self.cliente}, ¿desea algo más? (s/n): ")
        if opcion.lower() != "s":
            print(f"[Servicio Técnico]: Gracias por su visita, {self.cliente}")
            return False
        return True

    def menu(self):
        print("\n=== Servicio Técnico Pro ===")
        print(f"[Servicio Técnico]: Bienvenido {self.cliente}")
        print(f"[Servicio Técnico]: {self.cliente}, seleccione una opción")
        print("1️⃣ Revisar")
        print("2️⃣ Reparar")
        print("3️⃣ Donar")
        return input(f"[{self.cliente}]: ")

    def pedir_año(self):
        while True:
            try:
                return int(input(f"{self.cliente}, ingrese el año: "))
            except ValueError:
                print("[Servicio Técnico]: Ingrese un número válido")

    # 🔹 REVISAR
    def revisar(self):
        print(f"\n[Servicio Técnico]: {self.cliente}, vamos a revisar su dispositivo")

        tipo = input(f"{self.cliente}, ingrese el tipo de dispositivo: ")
        marca = input(f"{self.cliente}, ingrese la marca: ")
        modelo = input(f"{self.cliente}, ingrese el modelo: ")
        año = self.pedir_año()
        problema = input(f"{self.cliente}, describa el problema: ")

        datos = {
            "id": int(time.time()),
            "cliente": self.cliente,
            "servicio": "Revisión",
            "tipo": tipo,
            "marca": marca,
            "modelo": modelo,
            "año": año,
            "problema": problema,
            "horas": 1,
            "costo_total": COSTO_POR_HORA
        }

        self.informe(datos)

        print(f"\n[Servicio Técnico]: {self.cliente}, se recomienda proceder con la reparación.")
        print(f"[Servicio Técnico]: El costo puede variar según el diagnóstico final.")

        continuar = input(f"{self.cliente}, ¿desea continuar con la reparación? (s/n): ")

        if continuar.lower() == "s":
            self.reparar()
        else:
            print(f"[Servicio Técnico]: Puede retirar su equipo cuando lo desee, {self.cliente}")

        if not self.continuar():
            sys.exit()

    # 🔹 REPARAR
    def reparar(self):
        print(f"\n[Servicio Técnico]: {self.cliente}, seleccione el tipo de reparación")
        print("1. Pantalla")
        print("2. Batería")
        print("3. Sistema")
        print("4. No enciende")

        while True:
            opcion = input(f"{self.cliente}, seleccione una opción: ")
            if opcion in ["1", "2", "3", "4"]:
                break
            else:
                print("[Servicio Técnico]: Opción inválida")

        if opcion == "1":
            problema, horas = "Pantalla", 2
        elif opcion == "2":
            problema, horas = "Batería", 1.5
        elif opcion == "3":
            problema, horas = "Sistema", 2
        else:
            problema, horas = "No enciende", 3

        print(f"\n[Servicio Técnico]: {self.cliente}, seleccione el método de entrega")
        print("1. Llevar equipo (Gratis)")
        print("2. Recogida a domicilio ($10)")
        print("3. Servicio urgente ($20)")

        while True:
            traslado = input(f"{self.cliente}, seleccione una opción: ")
            if traslado in ["1", "2", "3"]:
                break
            else:
                print("[Servicio Técnico]: Opción inválida")

        if traslado == "1":
            tipo_traslado = "Cliente lleva el equipo"
            costo_traslado = 0
        elif traslado == "2":
            tipo_traslado = "Recogida a domicilio"
            costo_traslado = 10
        else:
            tipo_traslado = "Servicio urgente"
            costo_traslado = 20

        costo_total = (horas * COSTO_POR_HORA) + costo_traslado

        datos = {
            "id": int(time.time()),
            "cliente": self.cliente,
            "servicio": "Reparación",
            "problema": problema,
            "horas": horas,
            "traslado": tipo_traslado,
            "costo_estimado": costo_total
        }

        self.informe(datos)

        print(f"\n[Servicio Técnico]: {self.cliente}, el monto final puede variar.")

        confirmar = input(f"{self.cliente}, ¿desea continuar? (s/n): ")
        if confirmar.lower() != "s":
            print(f"[Servicio Técnico]: Operación cancelada, {self.cliente}")
            return

        if traslado == "1":
            fecha = input(f"{self.cliente}, ¿cuándo traerá el equipo?: ")
            ticket = int(time.time())

            print(f"\n[Servicio Técnico]: {self.cliente}, su número de ticket es: {ticket}")

            datos["ticket"] = ticket
            datos["fecha"] = fecha

            self.guardar(datos)

            finalizar = input(f"\n[Servicio Técnico]: {self.cliente}, ¿es todo por hoy? (s/n): ")
            if finalizar.lower() == "s":
                print(f"[Servicio Técnico]: Gracias por su visita, {self.cliente}")
                sys.exit()

        else:
            fecha = input(f"{self.cliente}, indique la fecha de recogida: ")
            datos["fecha"] = fecha
            self.guardar(datos)

        if not self.continuar():
            sys.exit()

    # 🔹 DONAR
    def donar(self):
        print(f"\n[Servicio Técnico]: Gracias {self.cliente} por su donación")

        tipo = input(f"{self.cliente}, ingrese el tipo de dispositivo: ")
        estado = input(f"{self.cliente}, ingrese el estado: ")

        datos = {
            "id": int(time.time()),
            "cliente": self.cliente,
            "servicio": "Donación",
            "tipo": tipo,
            "estado": estado
        }

        self.guardar(datos)
        self.informe(datos)

        if not self.continuar():
            sys.exit()

    # 🔹 GUARDAR
    def guardar(self, datos):
        try:
            with open(ARCHIVO, "r") as f:
                contenido = json.load(f)
        except:
            contenido = []

        contenido.append(datos)

        with open(ARCHIVO, "w") as f:
            json.dump(contenido, f, indent=4)

    # 🔹 INFORME
    def informe(self, datos):
        print("\n--- INFORME ---")
        for clave, valor in datos.items():
            print(f"{clave}: {valor}")
