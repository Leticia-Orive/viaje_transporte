import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ViajeService } from '../../services/viaje.service';
import { TransporteService } from '../../services/transporte.service';
import { ReservaService } from '../../services/reserva.service';
import { Viaje, Transporte, Reserva } from '../../models/models';

@Component({
  selector: 'app-admin',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './admin.component.html',
  styleUrl: './admin.component.css'
})
export class AdminComponent implements OnInit {
  activeTab: string = 'transportes';
  
  // Transportes
  transportes: Transporte[] = [];
  nuevoTransporte: Transporte = {
    tipo: '',
    nombre: '',
    capacidad: 0
  };
  
  // Viajes
  viajes: Viaje[] = [];
  nuevoViaje: Viaje = {
    origen: '',
    destino: '',
    fecha_salida: '',
    fecha_llegada: '',
    precio: 0,
    asientos_disponibles: 0,
    transporte_id: 0
  };
  
  // Reservas
  reservas: Reserva[] = [];

  constructor(
    private viajeService: ViajeService,
    private transporteService: TransporteService,
    private reservaService: ReservaService
  ) { }

  ngOnInit(): void {
    this.loadData();
  }

  loadData(): void {
    this.loadTransportes();
    this.loadViajes();
    this.loadReservas();
  }

  loadTransportes(): void {
    this.transporteService.getTransportes().subscribe({
      next: (data) => this.transportes = data,
      error: (error) => console.error('Error loading transportes:', error)
    });
  }

  loadViajes(): void {
    this.viajeService.getViajes().subscribe({
      next: (data) => this.viajes = data,
      error: (error) => console.error('Error loading viajes:', error)
    });
  }

  loadReservas(): void {
    this.reservaService.getReservas().subscribe({
      next: (data) => this.reservas = data,
      error: (error) => console.error('Error loading reservas:', error)
    });
  }

  setActiveTab(tab: string): void {
    this.activeTab = tab;
  }

  // Transportes CRUD
  crearTransporte(): void {
    this.transporteService.createTransporte(this.nuevoTransporte).subscribe({
      next: () => {
        alert('Transporte creado exitosamente');
        this.loadTransportes();
        this.nuevoTransporte = { tipo: '', nombre: '', capacidad: 0 };
      },
      error: (error) => {
        console.error('Error creating transporte:', error);
        alert('Error al crear el transporte');
      }
    });
  }

  eliminarTransporte(id: number): void {
    if (confirm('¿Está seguro de que desea eliminar este transporte?')) {
      this.transporteService.deleteTransporte(id).subscribe({
        next: () => {
          alert('Transporte eliminado exitosamente');
          this.loadTransportes();
        },
        error: (error) => {
          console.error('Error deleting transporte:', error);
          alert('Error al eliminar el transporte');
        }
      });
    }
  }

  // Viajes CRUD
  crearViaje(): void {
    this.viajeService.createViaje(this.nuevoViaje).subscribe({
      next: () => {
        alert('Viaje creado exitosamente');
        this.loadViajes();
        this.nuevoViaje = {
          origen: '',
          destino: '',
          fecha_salida: '',
          fecha_llegada: '',
          precio: 0,
          asientos_disponibles: 0,
          transporte_id: 0
        };
      },
      error: (error) => {
        console.error('Error creating viaje:', error);
        alert('Error al crear el viaje');
      }
    });
  }

  eliminarViaje(id: number): void {
    if (confirm('¿Está seguro de que desea eliminar este viaje?')) {
      this.viajeService.deleteViaje(id).subscribe({
        next: () => {
          alert('Viaje eliminado exitosamente');
          this.loadViajes();
        },
        error: (error) => {
          console.error('Error deleting viaje:', error);
          alert('Error al eliminar el viaje');
        }
      });
    }
  }

  eliminarReserva(id: number): void {
    if (confirm('¿Está seguro de que desea eliminar esta reserva?')) {
      this.reservaService.deleteReserva(id).subscribe({
        next: () => {
          alert('Reserva eliminada exitosamente');
          this.loadReservas();
        },
        error: (error) => {
          console.error('Error deleting reserva:', error);
          alert('Error al eliminar la reserva');
        }
      });
    }
  }

  formatDate(dateString: string): string {
    const date = new Date(dateString);
    return date.toLocaleString('es-ES');
  }
}
