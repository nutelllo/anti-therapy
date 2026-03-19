Нурсултан, хороший `README.md` — это 50% успеха твоего проекта на GitHub. Это «лицо» твоего кода, которое первым делом смотрят лиды и рекрутеры.

Я составил его так, чтобы сразу было понятно: ты не просто «запустил скрипт», а построил **Enterprise-ready** архитектуру.

Скопируй этот текст в файл `README.md` в корне твоего репозитория:

---

# 🤖 Anti-Therapy AI: Hybrid Microservices Platform

**Anti-Therapy AI** — это демонстрационный микросервисный проект, который превращает жалобы пользователя в "агрессивно-поддерживающие" ответы от ИИ. Проект построен на современных DevOps практиках: инфраструктура как код (IaC), GitOps-доставка и гибридная облачная архитектура.

## 🏗 Архитектура

Проект разделен на три уровня:

1. **Infrastructure Level:** Развернут в **AWS (EKS)** с использованием **Terraform**.
2. **Application Level:** Два микросервиса (Frontend на Nginx и Backend на FastAPI), упакованные в **Docker** и управляемые через **Helm**.
3. **AI Level (Hybrid):** Внешний инференс нейросети **Ollama (Mistral)** в Google Colab/Kaggle, проброшенный в кластер через **Cloudflare Tunnel**.

## 🛠 Технологический стек

* **Облако:** AWS (EKS, VPC, ELB, IAM).
* **IaC:** Terraform (модульная структура).
* **CI/CD:** GitOps через ArgoCD.
* **Оркестрация:** Kubernetes (Services, Deployments, ConfigMaps).
* **Пакетный менеджер:** Helm v3.
* **Реестр образов:** GitHub Container Registry (GHCR).
* **ИИ:** Ollama API (Dolphin-Mistral).

## 🚀 Как это развернуто

### 1. Инфраструктура (Terraform)

Кластер EKS разворачивается одной командой, создавая изолированную сеть VPC и необходимые роли.

```bash
cd terraform
terraform init
terraform apply

```

### 2. Приложение (Helm + ArgoCD)

Управление деплоем происходит через декларативный манифест ArgoCD. Любое изменение в папке `charts/` автоматически синхронизируется с кластером.

```bash
kubectl apply -f argocd-app.yaml

```

## 🔌 Гибридное подключение к LLM

Особенность проекта — использование **Hybrid Cloud**. Бэкенд в AWS не тратит дорогие ресурсы на GPU, а обращается к Ollama, запущенной в Google Colab/Kaggle, через зашифрованный туннель:

1. Запуск Ollama в Colab.
2. Проброс порта 11434 через `cloudflared`.
3. Динамическое обновление `ollamaUrl` в `values.yaml` через GitOps.

## 🎓 Чему я научился (Lessons Learned)

В ходе реализации проекта были решены критические задачи:

* **State Management:** Опыт ручного восстановления ресурсов через AWS CLI после потери `.tfstate`.
* **Network Debugging:** Настройка CORS и Security Groups для взаимодействия микросервисов.
* **Resource Optimization:** Перенос весов нейросети между провайдерами (Colab -> Kaggle) при достижении лимитов GPU.

---

### 💡 Как связаться со мной

**Nursultan (Gem)**

* **Position:** System Administrator / Junior DevOps Engineer
* **Location:** Bishkek, Kyrgyzstan
* **GitHub:** [nutelllo](https://www.google.com/search?q=https://github.com/nutelllo)

