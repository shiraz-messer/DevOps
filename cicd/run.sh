#!/bin/bash
kubectl create -f deploymentfrontend.yaml
kubectl create -f deploymentbackend.yaml
kubectl create -f deploymentlogger.yaml
kubectl create -f servicefrontend.yaml
kubectl create -f servicebackend.yaml
kubectl create -f servicelogger.yaml

