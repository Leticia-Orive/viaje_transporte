export interface Transporte {
  id?: number;
  tipo: string;
  nombre: string;
  capacidad: number;
  activo?: boolean;
}

export interface Viaje {
  id?: number;
  origen: string;
  destino: string;
  fecha_salida: string;
  fecha_llegada: string;
  precio: number;
  asientos_disponibles: number;
  transporte_id: number;
  transporte?: Transporte;
}

export interface Reserva {
  id?: number;
  nombre_pasajero: string;
  email: string;
  telefono?: string;
  numero_asientos: number;
  fecha_reserva?: string;
  estado?: string;
  viaje_id: number;
}
