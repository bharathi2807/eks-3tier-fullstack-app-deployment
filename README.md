# EKS Fargate Flask App with ALB Ingress

This project demonstrates deploying a **Python Flask application** on **Amazon EKS using Fargate (serverless Kubernetes)** and exposing it to the internet using an **Application Load Balancer (ALB)** via **Kubernetes Ingress**.

No EC2 worker nodes were used.

---

## Architecture Overview

Client  
→ ALB (AWS Load Balancer Controller)  
→ Kubernetes Ingress  
→ ClusterIP Service  
→ Flask Pods (running on Fargate)

---

## Tech Stack

- AWS EKS (Kubernetes)
- AWS Fargate
- AWS Load Balancer Controller
- Application Load Balancer (ALB)
- Docker
- Python Flask

---

## Project Structure
├── app.py # Flask application
├── requirements.txt # Python dependencies
├── Dockerfile # Container image definition
├── flask-eks.yml # Kubernetes manifests (Deployment, Service, Ingress)
├── iam_policy.json # IAM policy for ALB controller


---

## Key Kubernetes Concepts Used

- Fargate-only EKS cluster
- ALB Ingress with `target-type: ip`
- ClusterIP Service
- Kubernetes Ingress resources
- Real-world ingress debugging (HTTP vs browser behavior)

---

## How to Run (High Level)

1. Build and push Docker image to ECR
2. Create EKS Fargate cluster
3. Install AWS Load Balancer Controller
4. Apply Kubernetes manifests
5. Access app via ALB DNS

---

## What I Learned

- How ALB actually integrates with Kubernetes
- Why Fargate requires `target-type: ip`
- How traffic flows from ALB → Service → Pods
- Debugging ingress issues instead of blindly trusting YAML

---

## Author

**Bharathi**  
Automation / DevOps Engineer  