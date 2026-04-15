def menu(self):
    print("\n=== Servicio Técnico Pro ===")
    print(f"[Servicio Técnico]: Bienvenido {self.cliente}")
    print(f"[Servicio Técnico]: {self.cliente}, seleccione una opción")
    print("1️⃣ Revisar")
    print("2️⃣ Reparar")
    print("3️⃣ Donar")
    return input(f"[{self.cliente}]: ")
