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
# AWS Step Functions - Workflow de Pedido

Este projeto foi desenvolvido como parte do desafio da DIO para consolidar o uso do AWS Step Functions.

## Descrição
O fluxo automatiza a validação e processamento de um pedido, usando estados `Choice`, `Task` e `Fail`.

## Estrutura do Workflow
- **Start** → `IsOrderValida`
- **Choice** → verifica `$.status`
- **Se OK** → vai para `ProcessOrder`
- **Faz backup → `Backup-Order`
- **Senão** → vai para `Permance-order`

## Ferramentas
- AWS Step Functions
- Amazon States Language (ASL)
- Interface visual do console AWS

## Arquivos
- `stepfunction-definition.json` → definição exportada da máquina de estados.
- `workflow-diagram.png` → diagrama visual do fluxo.
- `insights.md` → anotações sobre o processo.

## 🚀 Como visualizar
1. Acesse o [AWS Step Functions Console](https://eu-north-1.console.aws.amazon.com/states/home?region=eu-north-1#/v2/statemachines/getStarted)
2. Clique em **Criar máquina de estado**.
3. Escolha **Importar definição** e cole o conteúdo do arquivo `stepfunction-definition.json`.

# ProjetoCloudCamila - Pilha AWS CloudFormation

Este projeto contém um template AWS CloudFormation para provisionamento automatizado de recursos essenciais em nuvem, utilizando o conceito de pilhas (stacks).

## Recursos criados

- S3 Bucket: Armazenamento de arquivos, backups e logs. O bucket criado tem nome exclusivo.
- IAM Group & User: Grupo de administração (GPO-ADMIN-LAB) e usuário IAM chamado cgl.
- EC2 Instance: Máquina virtual Amazon Linux, pronta para testes e aplicações.
- Security Group: Libera acesso SSH (porta 22) para a instância EC2.
- Outputs: Retorna identificadores dos principais recursos ao final da criação.

## Processo realizado

1. **Definição do template YAML**
   - O arquivo 04-EC2_S3_UserGroup.yaml especifica todos os recursos necessários e seus parâmetros conforme boas práticas do AWS CloudFormation.
   - Foram corrigidos problemas comuns consultando mensagens de erro do Console AWS, como nomes de bucket duplicados, AMI inválida, VPC inexistente e tipo de instância incompatível.

2. **Validação e ajustes**
   - Busquei no painel AWS o VPC ID válido, um AMI público para a região selecionada e um Key Pair existente para acesso à EC2.
   - Ajustei nomes e referências dos recursos para o padrão do AWS CloudFormation, evitando conflitos e erros de sintaxe.

3. **Implantação da pilha**
   - Fiz upload do template no serviço CloudFormation, preenchendo os parâmetros solicitados.
   - Acompanhei o progresso da criação dos recursos, resolvendo as falhas encontradas.
   - Após sucesso, conferi que todos os itens foram criados conforme esperado, incluindo EC2, S3, usuário e grupo IAM.

4. **Permissões do IAM**
   - A política de permissões foi atribuída **manualmenteno console AWS**, depois da criação da pilha.
   - Escolhi a política `ReadOnlyAccess` para o grupo IAM (`GPO-ADMIN-LAB`), garantindo que todos os usuários do grupo herdem esse acesso.

5. **Acesso e validação**
   - Realizei o acesso SSH usando o Key Pair gerado, corrigindo as permissões do arquivo (`chmod 400 modelo.pem`).
   - Validei no Console AWS (EC2, IAM, S3) e salvei prints de cada etapa importante para evidenciar resultados.

## Problemas enfrentados e soluções

- **Erro de SSH (Permission denied):**
  - Correção de permissões da chave (`chmod 400`) e uso do usuário certo (`ec2-user` para Amazon Linux).
  - Testes necessários até encontrar a combinação ideal de IP da instância e Key Pair correto.
- **Chave PEM não encontrada ou inválida:**
  - Checagem do diretório correto, ajuste do caminho e conferência do Key Pair vinculado à instância.
- **Bucket S3 com nome duplicado:**
  - Alteração do nome para garantir sua exclusividade global e uso de letras minúsculas conforme exigido.
- **Grupo IAM sem permissão:**
  - Inclusão de política `ReadOnlyAccess` de forma manual pelo Console após a criação da pilha.

## Como usar

- Clone este repositório.
- No Console AWS CloudFormation, selecione "Criar Pilha com novo recurso (com template)".
- Faça upload do arquivo YAML disponível neste repositório.
- Preencha os parâmetros necessários (tipo da instância, VPC ID, chave SSH).
- Aguarde a criação dos recursos.
- Valide a criação dos recursos no Console AWS (EC2, IAM, S3).
- Atribua permissões ao grupo IAM manualmente, se necessário.

## Prints/documentação visual

Acesse a pasta `/images` para capturas do processo:
- Console EC2 mostrando recursos criados.
- Página do IAM evidenciando usuário, grupo e permissões.
- Terminal de SSH bem-sucedido e correções aplicadas.

## Pré-requisitos

- Conta AWS ativa e permissões para EC2, IAM e S3.
- Par de chave SSH criado (Key Pair) para acesso à instância EC2.
- VPC ID válido (obtido no Console AWS).
- AMI válida para a região (obtida no Console AWS).

## Id da Pilha

[Link direto à sua pilha CloudFormation](https://us-east-1.console.aws.amazon.com/go/view?arn=arn%3Aaws%3Acloudformation%3Aus-east-1%3A160927904891%3Astack%2Fcloudfcamia1%2F2ad98500-b58d-11f0-84d3-0ee4edc8c2cf&source=cloudformation)

# AWS Lambda + S3: Processamento Automatizado

Este repositório contém o laboratório de automação de tarefas usando AWS Lambda e S3, desenvolvido como desafio prático para consolidar conhecimentos em computação sem servidor (serverless) e armazenamento de arquivos.

## Objetivo

Automatizar o processamento e movimentação de arquivos entre buckets S3 usando uma função Lambda disparada por eventos S3. O repositório traz anotações, código fonte e insights obtidos durante o desenvolvimento para servir como material de apoio em futuros estudos.

## Arquitetura

- **Bucket de origem**: Armazena arquivos enviados, que disparam eventos S3.
- **AWS Lambda**: Função que processa o evento e copia o arquivo recebido para o bucket de destino.
- **Bucket de destino** (`bucketdestinoprocessamentocamila`): Recebe arquivos que foram processados pela Lambda.
- **IAM Role**: Permissões configuradas para a Lambda acessar ambos os buckets e enviar logs para o CloudWatch.

## Passo a passo de implementação

1. **Crie os buckets S3**  
   - Origem: recebe uploads para disparar o fluxo.  
   - Destino: armazena arquivos processados.

2. **Configure IAM Role**  
   - AmazonS3FullAccess para ler e gravar arquivos.  
   - CloudWatchLogsFullAccess para monitorar logs de execução.

3. **Desenvolva a Lambda**  
   - Use Python.  
   - Código responsável por receber o evento S3, identificar o arquivo e copiar para o bucket destino.

4. **Configure gatilho no bucket de origem**  
   - Adicione trigger do tipo S3 (ObjectCreated) para acionar a Lambda ao enviar arquivos.

5. **Teste a automação**  
   - Envie arquivos ao bucket de origem e confira no bucket destino e nos logs do CloudWatch se o processo ocorreu com sucesso.
## Código principal

import json
import boto3

def lambda_handler(event, context):
record = event['Records']
bucket_name = record['s3']['bucket']['name']
object_key = record['s3']['object']['key']
bucket_destino = 'bucketdestinoprocessamentocamila'



## Teste

- Manualmente simule eventos S3 com o formato correto para testes no console da Lambda.  
- Recomenda-se testar o fluxo real enviando arquivos para o bucket de origem.

## Insights e boas práticas

- Documente todo o fluxo, incluindo permissões e arquitetura.  
- Utilize logs no CloudWatch para depuração.  
- Mantenha permissões restritas e seguras na IAM Role.  
- Sempre teste com arquivo real para garantir que não ocorram erros de inexistência (404).


---

## Acesso e Avaliação

Para avaliar este projeto, compartilho o código fonte da função Lambda e instruções completas para replicação do ambiente. O avaliador poderá:
- Revisar o código em `lambda_function.py`.
- Criar os buckets S3 e IAM Role conforme descrito.
- Configurar o disparo do Lambda via S3.
- Testar o fluxo automatizado enviando arquivos reais.

Este material garante transparência, replicabilidade e compreensão completa do trabalho realizado.




