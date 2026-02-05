package com.example.register.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.example.register.entity.User;

public interface UserRepository extends JpaRepository<User, Integer> {
}