package com.example.register.controller;

import org.springframework.web.bind.annotation.*;
import com.example.register.entity.User;
import com.example.register.repository.UserRepository;

@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "*")
public class UserController {

    private final UserRepository repo;

    public UserController(UserRepository repo) {
        this.repo = repo;
    }

    @PostMapping("/register")
    public User register(@RequestBody User user) {
        return repo.save(user);
    }
}