# minishop-using-flask-microservices 

# Containerized Flask microservices using Docker,, Kubernetes,  CI/CD and GitHub Actions

# 🧱 Flask Microservices Architecture

A simple containerized microservices architecture using **Flask**, **Docker**, **Kubernetes**, and **CI/CD with GitHub Actions**. Includes user and product services with API gateway routing and database integration.

---

## 🚀 Project Overview

This project demonstrates:
- ✅ Flask-based microservices
- 🐳 Docker containers for each service
- ☸️ Kubernetes orchestration (Minikube or local cluster)
- 🛠️ CI/CD pipeline using GitHub Actions
- 🗃️ MongoDB and PostgreSQL databases

---

## 🧩 Microservices Structure

.
├── api-gateway/         # Routes requests to other services
├── user-service/        # Handles user data (MongoDB)
├── product-service/     # Handles product data (PostgreSQL)
├── k8s/                 # Kubernetes deployment files
└── .github/workflows/   # GitHub Actions CI/CD workflow


⚙️ Technologies Used

Python 3.10

Flask

Docker & Docker Compose

Kubernetes (Minikube or Docker Desktop)

MongoDB (for user service)

PostgreSQL (for product service)

GitHub Actions (CI/CD)
