import { Component } from '@angular/core';
import { UserService } from '../services/user.service';
import { User } from '../models/user';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {

  user: User = {
    name: '',
    email: '',
    password: ''
  };

  successMessage = '';
  errorMessage = '';
  loading = false;

  constructor(private userService: UserService) {}

  register() {
    this.successMessage = '';
    this.errorMessage = '';
    this.loading = true;

    this.userService.register(this.user).subscribe({
      next: () => {
        this.loading = false;
        this.successMessage = 'Registration successful 🎉';
        this.user = { name: '', email: '', password: '' };
      },
      error: () => {
        this.loading = false;
        this.errorMessage = 'Registration failed. Try again.';
      }
    });
  }
}