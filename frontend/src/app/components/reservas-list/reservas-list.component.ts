import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReservaService } from '../../services/reserva.service';
import { Reserva } from '../../models/models';

@Component({
  selector: 'app-reservas-list',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './reservas-list.component.html',
  styleUrl: './reservas-list.component.css'
})
export class ReservasListComponent implements OnInit {
  reservas: Reserva[] = [];

  constructor(private reservaService: ReservaService) { }

  ngOnInit(): void {
    this.loadReservas();
  }

  loadReservas(): void {
    this.reservaService.getReservas().subscribe({
      next: (data) => this.reservas = data,
      error: (error) => console.error('Error loading reservas:', error)
    });
  }

  cancelarReserva(id: number): void {
    if (confirm('¿Está seguro de que desea cancelar esta reserva?')) {
      this.reservaService.updateReserva(id, { estado: 'cancelada' } as Reserva).subscribe({
        next: () => {
          alert('Reserva cancelada exitosamente');
          this.loadReservas();
        },
        error: (error) => {
          console.error('Error canceling reserva:', error);
          alert('Error al cancelar la reserva');
        }
      });
    }
  }

  formatDate(dateString: string): string {
    const date = new Date(dateString);
    return date.toLocaleString('es-ES');
  }
}
