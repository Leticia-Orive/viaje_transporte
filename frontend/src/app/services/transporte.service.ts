import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Transporte } from '../models/models';

@Injectable({
  providedIn: 'root'
})
export class TransporteService {
  private apiUrl = 'http://localhost:5000/api/transportes';

  constructor(private http: HttpClient) { }

  getTransportes(): Observable<Transporte[]> {
    return this.http.get<Transporte[]>(this.apiUrl);
  }

  getTransporte(id: number): Observable<Transporte> {
    return this.http.get<Transporte>(`${this.apiUrl}/${id}`);
  }

  createTransporte(transporte: Transporte): Observable<Transporte> {
    return this.http.post<Transporte>(this.apiUrl, transporte);
  }

  updateTransporte(id: number, transporte: Transporte): Observable<Transporte> {
    return this.http.put<Transporte>(`${this.apiUrl}/${id}`, transporte);
  }

  deleteTransporte(id: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}/${id}`);
  }
}
