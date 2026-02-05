import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { User } from '../models/user';

@Injectable({
  providedIn: 'root'
})
export class UserService {

private apiUrl = 'http://k8s-my3tier-mybacken-5c2cb5adbb-651084299.ap-south-1.elb.amazonaws.com/api/register';

  constructor(private http: HttpClient) {}

  register(user: User): Observable<any> {
    return this.http.post(this.apiUrl, user);
  }
}