import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ViajeService } from '../../services/viaje.service';
import { ReservaService } from '../../services/reserva.service';
import { Viaje, Reserva } from '../../models/models';

@Component({
  selector: 'app-viajes-list',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './viajes-list.component.html',
  styleUrl: './viajes-list.component.css'
})
export class ViajesListComponent implements OnInit {
  viajes: Viaje[] = [];
  filteredViajes: Viaje[] = [];
  
  // Filtros de búsqueda
  searchOrigen: string = '';
  searchDestino: string = '';
  searchFecha: string = '';
  
  // Modal de reserva
  showReservaModal: boolean = false;
  selectedViaje?: Viaje;
  nuevaReserva: Reserva = {
    nombre_pasajero: '',
    email: '',
    telefono: '',
    numero_asientos: 1,
    viaje_id: 0
  };

  constructor(
    private viajeService: ViajeService,
    private reservaService: ReservaService
  ) { }

  ngOnInit(): void {
    this.loadViajes();
  }

  loadViajes(): void {
    this.viajeService.getViajes().subscribe({
      next: (data) => {
        this.viajes = data;
        this.filteredViajes = data;
      },
      error: (error) => console.error('Error loading viajes:', error)
    });
  }

  buscarViajes(): void {
    if (!this.searchOrigen && !this.searchDestino && !this.searchFecha) {
      this.filteredViajes = this.viajes;
      return;
    }

    this.viajeService.buscarViajes(this.searchOrigen, this.searchDestino, this.searchFecha)
      .subscribe({
        next: (data) => this.filteredViajes = data,
        error: (error) => console.error('Error searching viajes:', error)
      });
  }

  openReservaModal(viaje: Viaje): void {
    this.selectedViaje = viaje;
    this.nuevaReserva.viaje_id = viaje.id!;
    this.showReservaModal = true;
  }

  closeReservaModal(): void {
    this.showReservaModal = false;
    this.selectedViaje = undefined;
    this.nuevaReserva = {
      nombre_pasajero: '',
      email: '',
      telefono: '',
      numero_asientos: 1,
      viaje_id: 0
    };
  }

  crearReserva(): void {
    if (!this.nuevaReserva.nombre_pasajero || !this.nuevaReserva.email) {
      alert('Por favor, complete todos los campos requeridos');
      return;
    }

    this.reservaService.createReserva(this.nuevaReserva).subscribe({
      next: (data) => {
        alert('Reserva creada exitosamente!');
        this.closeReservaModal();
        this.loadViajes(); // Recargar para actualizar asientos disponibles
      },
      error: (error) => {
        console.error('Error creating reserva:', error);
        alert('Error al crear la reserva. Por favor, intente de nuevo.');
      }
    });
  }

  formatDate(dateString: string): string {
    const date = new Date(dateString);
    return date.toLocaleString('es-ES');
  }
}
