# Arquitetura Cloud AWS - Plataforma de Viagens Online (3-Camadas)

## Visão Geral do Projeto

Este projeto demonstra a arquitetura completa de uma plataforma de vendas de pacotes de viagens online, focando em **Alta Disponibilidade**, **Escalabilidade** e **Segurança** na Nuvem AWS.

A solução foi projetada para atender a requisitos de tráfego intenso (site institucional e reservas dinâmicas) e proteger dados sensíveis de clientes e transações.

---

## Cenário de Negócio e Requisitos

A arquitetura foi criada para resolver as seguintes necessidades críticas de negócio:

| Requisito de Negócio | Solução de Arquitetura |
| :--- | :--- |
| **Plataforma de Reservas** | Aplicação rodando em **EC2** por trás de um **ALB**. |
| **Site Institucional/Imagens** | Uso de **CloudFront** e **S3** para baixa latência global (CDN). |
| **Banco de Dados** | **RDS (PostgreSQL/MySQL)** para dados de clientes, pacotes e transações. |
| **Alta Disponibilidade** | Uso de **Application Load Balancer (ALB)** e **EC2 Multi-AZ** (simulado com 2 instâncias). |
| **Segurança e Acesso** | **IAM** para controle de permissões e **WAF/Security Groups** como firewall de rede. |
| **Monitoramento/Backup** | **CloudWatch** para observabilidade e **S3** para backups automáticos do RDS. |

---

## Fluxograma

A solução utiliza um modelo de **Arquitetura 3-Camadas** para separar o acesso público do processamento e dos dados.

### Diagrama de Fluxo de Tráfego

O diagrama a seguir (localizado em [**./diagramas/viagens-online-aws.png**]) ilustra o caminho da requisição do usuário e a interação entre os serviços:

1.  **Acesso:** O usuário entra via **Route 53 (DNS)**.
2.  **Distribuição Global:** O **CloudFront (CDN)** gerencia o tráfego. Conteúdo estático (imagens, CSS) é servido diretamente do **S3**.
3.  **Aplicação Dinâmica:** Requisições de reserva são inspecionadas pelo **WAF/Security Groups** e enviadas ao **Application Load Balancer (ALB)**.
4.  **Processamento:** O ALB distribui a carga para duas instâncias **EC2** (onde a aplicação de reservas roda).
5.  **Dados:** O **RDS** hospeda o banco de dados principal.

### Detalhes Técnicos da Camada de Controle

* **Controle de Permissões:** O **IAM** é o centro de controle, gerenciando o acesso seguro de administradores e serviços (ex: permissão do EC2 para acessar o RDS).
* **Observabilidade:** O **CloudWatch** coleta métricas e logs de todas as camadas críticas (ALB, EC2, RDS), garantindo a detecção rápida de problemas.
* **Resiliência de Dados:** O **RDS** é configurado para realizar backups automáticos para um bucket **S3** dedicado.

---

## Tecnologias Utilizadas

| Categoria | Serviço AWS / Ferramenta | Função no Projeto |
| :--- | :--- | :--- |
| **Networking/Entrega** | Route 53, CloudFront, WAF | DNS, CDN e Proteção de Borda. |
| **Computação/Escalabilidade** | EC2, Application Load Balancer (ALB) | Hospedagem da aplicação e distribuição de carga. |
| **Dados** | RDS (PostgreSQL/MySQL), S3 | Banco de dados transacional e armazenamento de objetos (backup/estático). |
| **Gerenciamento** | IAM, CloudWatch | Gerenciamento de acessos, monitoramento e alarmes. |

---

## Próximos Passos (Evolução da Arquitetura)

Para evoluir este projeto e atingir um nível de produção (DevOps), o próximo foco será:

1.  **Implementação de IaC:** Escrever o código **Terraform** (ou CloudFormation) para provisionar toda a infraestrutura descrita.
2.  **CI/CD:** Configurar um *pipeline* (ex: GitHub Actions) para implantar automaticamente o código da aplicação nas instâncias EC2.
3.  **Otimização de Custos:** Analisar o uso de **EC2 Spot Instances** ou migração de partes da aplicação para **Lambda** (Serverless).

---



