terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    helm = {
      source  = "hashicorp/helm"
      version = "~> 2.12"
    }
  }
}

# 1. Настраиваем провайдер AWS
provider "aws" {
  region = "ca-central-1" # ОБЯЗАТЕЛЬНО проверь и впиши свой регион (us-east-1, eu-central-1 и т.д.)
}

# 2. Получаем данные о твоем существующем кластере
data "aws_eks_cluster" "eks" {
  name = "lagman-cluster"
}

data "aws_eks_cluster_auth" "eks" {
  name = "lagman-cluster"
}

# 3. Настраиваем провайдер Helm для связи с твоим K8s кластером
provider "helm" {
  kubernetes {
    host                   = data.aws_eks_cluster.eks.endpoint
    cluster_ca_certificate = base64decode(data.aws_eks_cluster.eks.certificate_authority[0].data)
    token                  = data.aws_eks_cluster_auth.eks.token
  }
}

# 4. Устанавливаем ArgoCD через Helm-чарт
resource "helm_release" "argocd" {
  name             = "argocd"
  repository       = "https://argoproj.github.io/argo-helm"
  chart            = "argo-cd"
  namespace        = "argocd"
  create_namespace = true 

  set {
    name  = "server.service.type"
    value = "ClusterIP"
  }
}