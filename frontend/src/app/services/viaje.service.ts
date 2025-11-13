import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Viaje } from '../models/models';

@Injectable({
  providedIn: 'root'
})
export class ViajeService {
  private apiUrl = 'http://localhost:5000/api/viajes';

  constructor(private http: HttpClient) { }

  getViajes(): Observable<Viaje[]> {
    return this.http.get<Viaje[]>(this.apiUrl);
  }

  getViaje(id: number): Observable<Viaje> {
    return this.http.get<Viaje>(`${this.apiUrl}/${id}`);
  }

  buscarViajes(origen?: string, destino?: string, fecha?: string): Observable<Viaje[]> {
    let params = '';
    if (origen) params += `origen=${origen}&`;
    if (destino) params += `destino=${destino}&`;
    if (fecha) params += `fecha=${fecha}`;
    return this.http.get<Viaje[]>(`${this.apiUrl}/buscar?${params}`);
  }

  createViaje(viaje: Viaje): Observable<Viaje> {
    return this.http.post<Viaje>(this.apiUrl, viaje);
  }

  updateViaje(id: number, viaje: Viaje): Observable<Viaje> {
    return this.http.put<Viaje>(`${this.apiUrl}/${id}`, viaje);
  }

  deleteViaje(id: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}/${id}`);
  }
}
