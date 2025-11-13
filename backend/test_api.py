import requests
import json

BASE_URL = "http://127.0.0.1:5000"

def test_home():
    """Probar la página de bienvenida"""
    print("🏠 Probando página de bienvenida...")
    response = requests.get(f"{BASE_URL}/")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")

def init_database():
    """Inicializar la base de datos con datos de ejemplo"""
    print("🗄️ Inicializando base de datos...")
    response = requests.post(f"{BASE_URL}/api/init-db")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")

def test_transportes():
    """Probar endpoint de transportes"""
    print("🚌 Probando endpoint /api/transportes...")
    response = requests.get(f"{BASE_URL}/api/transportes")
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Total transportes: {len(data)}")
    for t in data:
        print(f"  - {t['tipo']}: {t['nombre']} (Capacidad: {t['capacidad']})")
    print()

def test_viajes():
    """Probar endpoint de viajes"""
    print("✈️ Probando endpoint /api/viajes...")
    response = requests.get(f"{BASE_URL}/api/viajes")
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Total viajes: {len(data)}")
    for v in data:
        print(f"  - {v['origen']} → {v['destino']} | Precio: ${v['precio']} | Asientos: {v['asientos_disponibles']}")
    print()

def test_reservas():
    """Probar endpoint de reservas"""
    print("📋 Probando endpoint /api/reservas...")
    response = requests.get(f"{BASE_URL}/api/reservas")
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Total reservas: {len(data)}\n")

def create_test_reserva():
    """Crear una reserva de prueba"""
    print("➕ Creando reserva de prueba...")
    nueva_reserva = {
        "nombre_pasajero": "Juan Pérez",
        "email": "juan@example.com",
        "telefono": "123456789",
        "numero_asientos": 2,
        "viaje_id": 1
    }
    response = requests.post(f"{BASE_URL}/api/reservas", json=nueva_reserva)
    print(f"Status: {response.status_code}")
    if response.status_code == 201:
        print(f"✅ Reserva creada exitosamente!")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    else:
        print(f"❌ Error: {response.json()}")
    print()

if __name__ == "__main__":
    print("="*60)
    print("🧪 PROBANDO API DE VIAJES Y TRANSPORTE")
    print("="*60 + "\n")
    
    try:
        # 1. Probar página de bienvenida
        test_home()
        
        # 2. Inicializar base de datos
        init_database()
        
        # 3. Probar transportes
        test_transportes()
        
        # 4. Probar viajes
        test_viajes()
        
        # 5. Probar reservas
        test_reservas()
        
        # 6. Crear una reserva de prueba
        create_test_reserva()
        
        # 7. Verificar reservas nuevamente
        test_reservas()
        
        print("="*60)
        print("✅ TODAS LAS PRUEBAS COMPLETADAS")
        print("="*60)
        
    except requests.exceptions.ConnectionError:
        print("❌ Error: No se puede conectar al servidor.")
        print("   Asegúrate de que el backend esté corriendo en http://127.0.0.1:5000")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
