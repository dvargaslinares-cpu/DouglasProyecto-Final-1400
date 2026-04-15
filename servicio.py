import json
from datetime import datetime

COSTO_POR_HORA = 25
ARCHIVO = "datos.json"


class ServicioTecnico:

    def iniciar(self):
        while True:
            try:
                opcion = self.menu()

                if opcion == "1":
                    self.revisar()
                elif opcion == "2":
                    self.reparar()
                elif opcion == "3":
                    self.donar()

            except Exception as e:
                print("[Bot]: Error inesperado:", e)

            salir = input("\n[Bot]: ¿Deseas continuar? (s/n): ")
            if salir.lower() != "s":
                print("[Bot]: Gracias por usar el servicio  ")
                break

    # MENÚ TIPO WHATSAPP
    def menu(self):
        print("\n📱 WhatsApp Bot")
        print("[Bot]: Hola  ¿Qué deseas hacer?")
        print("1️⃣ Revisar dispositivo")
        print("2️⃣ Reparar dispositivo")
        print("3️⃣ Donar dispositivo")

        return self.pedir_opcion("[Tú]: ", ["1", "2", "3"])

    # VALIDACIÓN DE OPCIONES
    def pedir_opcion(self, mensaje, opciones):
        while True:
            try:
                opcion = input(mensaje)
                if opcion not in opciones:
                    raise ValueError("Opción inválida")
                return opcion
            except ValueError as e:
                print(f"[Bot]: {e}")

    # VALIDAR NÚMEROS
    def pedir_entero(self, mensaje):
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("[Bot]: Debes ingresar un número válido")

    # REVISAR
    def revisar(self):
        print("\n[Bot]: Vamos a revisar tu dispositivo 🔍")

        tipo = input("[Bot]: Tipo (Laptop/PC/Teléfono): ")
        marca = input("[Bot]: Marca: ")
        modelo = input("[Bot]: Modelo: ")
        año = self.pedir_entero("[Bot]: Año: ")
        problema = input("[Bot]: Describe el problema: ")

        horas = 1
        costo = horas * COSTO_POR_HORA

        datos = self.crear_registro(
            "Revisión", tipo, marca, modelo, año, problema, horas, costo
        )

        self.guardar(datos)
        self.informe(datos)

    # EPARAR
    def reparar(self):
        print("\n[Bot]: ¿Qué deseas reparar? 🔧")
        print("1. Pantalla")
        print("2. Batería")
        print("3. Sistema lento")
        print("4. Virus")
        print("5. No enciende")

        opcion = self.pedir_opcion("[Tú]: ", ["1", "2", "3", "4", "5"])

        problemas = {
            "1": ("Pantalla", 2),
            "2": ("Batería", 1.5),
            "3": ("Sistema lento", 2),
            "4": ("Virus", 1),
            "5": ("No enciende", 3),
        }

        problema, horas = problemas[opcion]
        costo = horas * COSTO_POR_HORA

        datos = self.crear_registro(
            "Reparación", "-", "-", "-", "-", problema, horas, costo
        )

        self.guardar(datos)
        self.informe(datos)

    # DONAR
    def donar(self):
        print("\n[Bot]: Gracias por donar  ")

        tipo = input("[Bot]: Tipo de dispositivo: ")
        estado = input("[Bot]: Estado (Bueno/Regular/Malo): ")
        funciona = input("[Bot]: ¿Funciona? (Sí/No): ")

        datos = {
            "id": self.generar_id(),
            "fecha": self.fecha_actual(),
            "servicio": "Donación",
            "tipo": tipo,
            "estado": estado,
            "funciona": funciona
        }

        self.guardar(datos)
        self.informe(datos)

    # CREAR REGISTRO
    def crear_registro(self, servicio, tipo, marca, modelo, año, problema, horas, costo):
        return {
            "id": self.generar_id(),
            "fecha": self.fecha_actual(),
            "servicio": servicio,
            "tipo": tipo,
            "marca": marca,
            "modelo": modelo,
            "año": año,
            "problema": problema,
            "horas": horas,
            "costo": costo
        }

    # ID AUTOMÁTICO
    def generar_id(self):
        return datetime.now().strftime("%Y%m%d%H%M%S")

    # FECHA
    def fecha_actual(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M")

    # GUARDAR JSON (CON ERRORES CONTROLADOS)
    def guardar(self, datos):
        try:
            with open(ARCHIVO, "r") as f:
                contenido = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            contenido = []

        contenido.append(datos)

        try:
            with open(ARCHIVO, "w") as f:
                json.dump(contenido, f, indent=4)
        except Exception as e:
            print("[Bot]: Error al guardar:", e)

    # INFORME FINAL
    def informe(self, datos):
        print("\n📄 ----- INFORME DE SERVICIO -----")
        for clave, valor in datos.items():
            print(f"{clave}: {valor}")