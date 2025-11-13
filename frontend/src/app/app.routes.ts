import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { ViajesListComponent } from './components/viajes-list/viajes-list.component';
import { ReservasListComponent } from './components/reservas-list/reservas-list.component';
import { AdminComponent } from './components/admin/admin.component';

export const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'viajes', component: ViajesListComponent },
  { path: 'reservas', component: ReservasListComponent },
  { path: 'admin', component: AdminComponent },
  { path: '**', redirectTo: '' }
];
