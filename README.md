# DevOps Excrcise - Coin Master

This exercise covers several areas:
* Application deployment
* Automate infrastructure and application provisioning
* Application logging delivery

Along the way you will be going to play around with the following technologies:
* Docker
* Kubernetes
* Terraform
* Elasticsearch 

## Instructions

### Exercise Structure

This exercise is built incrementally with stages so every stage is based on its predecessor.  
You will have to finish the first stage to be able to continue to the second one and so forth.

### Submitting Solutions

1. You will have to upload your solutions to a public git repository
(Github/Gitlab/Whatever you're comfortable with)
2. Every stage solution should exist on a separate matching git tag  
For example - Stage 0 solution should exist on `stage-0` git tag
3. It is not necessary to work with several branches, you can use master
4. Use meaningful git commits
5. Write minimal documentation for what you write - it should be clear enough
for someone who didn't read your code/automation to use and deploy it

Have fun!

## Stage 0 - Background

You are given with an example application
for fetching currencies exchange rate - Coin Master.  
This application provides an API to retrieve the exchange rate between two currencies.  
For this purpose it uses `exchangerate-api.com`.

The application is written in Python and can be deployed with docker.  
You can find the application source code at `coint-master-api` directory in this repository.  
In order to properly deploy this app you will need an API token for `exchangerate-api.com` -
generate a free one on
[https://app.exchangerate-api.com/sign-in](https://app.exchangerate-api.com/sign-in).


## Stage 1 - Application Deployment

In the end of this stage you will have a deployed instance of Coin Master API
on a local/remote Kubernetes cluster.

### Step 1 - Build & Publish a docker image

Go to the `coint-master-api`, build a Docker image and deploy it to Docker Hub.

### Step 2 - Deploy a Kubernetes Cluster

Choose your favorite Kubernetes solution and provision a cluster.  

Recomendations:
* [Local] Kind
* [Local] Minikube
* [Local] Docker Desktop Kubernetes
* [Local] Rancher Desktop
* [Remote] Amazon EKS
* [Remote] Azure AKS
* [Remote] Google Cloud GKE

The cluster should have an ingress controller and storage class.

### Step 3 - Deploy a workload on the Kubernetes cluster

Create YAML manifests for the application:
* The API should be exposed over ingress
* The `exchangerate-api.com` API key should be kept in a Kubernetes secret

## Stage 2 - Automate application provisioning with Terraform

In the end of this stage you will have Terraform module(s)
that deploy the application on a Kubernetes cluster.  
You can use `local` backend for managing Terraform state.  
Write Terraform module to provision `coin-master-api` components over Kubernetes:
* Make the module get everything required as parameters (kube-config, API Key, etc.)
* Make deployment configuration configurable as well (like deployment replicas).  
Use sane default values for this paramters.
* Use the Kubernetes provider for Terraform

## Stage 3 - Deliver application logs to Elasticsearch

In the end of this you will be able to search and analyze
Coin Master logs withing self managed Elasticsearch and Kibana.  
The `coin-master-api` uses structured logging - it prints JSON formatted logs
to its standard output, which can be seen using `kubectl logs`.  
In this stage you will:
1. Deploy Elasticsearch and Kibana for logging storage, indexing and analysis
2. Deploy Banzai Logging Operator for managing application logging pipelines
3. Configure logging pipeline for collecting `coin-master-api`
logs and send them to Elasticsearch

### Step 1 - Deploy Elasticsearch and Kibana

In order to index and analyze logs you will need an up and running
deployments of Elasticsearch and Kibana.  
For this purpose you are going to use ECK (Elastic Cloud for Kubernetes).  
Install the ECK Operator and deploy a minimal instance of Elasticsearch and Kibana.  
Manage the installation of Elasticsearch and Kibana via Terraform module.  
NOTE: You don't have to install the operator using Terraform.

### Step 2 - Deploy Banzai Logging Operator

Banzai Logging Operator is a product that enables one to create and manage logging
pipelines of Kubernetes application to various Logging outputs - in our case Elasticsearch.
Read Banzai documentation and install the Logging Operator on your Kubernetes cluster.  
NOTE: You don't have to install the operator using Terraform.  

### Step 3 - Collect application logs and send to Elasticsearch

Use Banzai Logging Operator objects to configure a logging pipeline:
* Configure logging output to your Elasticsearch deployment
* Configure logging collection and parsing of your `coin-master-api` instance.  
Notice that `coin-master-api` uses JSON formatted structured logging.
