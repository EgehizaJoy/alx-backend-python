#!/bin/bash

# kurbeScript.sh
# Script to start Kubernetes locally with Minikube and check status

# Function to check if a command exists
command_exists () {
    command -v "$1" >/dev/null 2>&1
}

# Check if minikube is installed
if ! command_exists minikube; then
    echo "Minikube is not installed. Please install it from: https://minikube.sigs.k8s.io/docs/start/"
    exit 1
fi

# Start Minikube
echo "Starting Minikube..."
minikube start

# Verify cluster info
echo "Verifying Kubernetes cluster..."
kubectl cluster-info

# List available pods (all namespaces)
echo "Listing pods..."
kubectl get pods --all-namespaces
