# SmartDesk — Kubernetes k3s local (Notebook 09)

## Âmbito
Apenas uma replica FastAPI no k3s do Notebook 08. Preservar `compose.k3s.yaml`, `headlamp-lab.yaml`, o MVP, a API, os testes e o PostgreSQL `db` do `compose.yaml`, incluindo o volume Docker `postgres_data`. Nao criar PostgreSQL no Kubernetes. Nao publicar credenciais.

## Ficheiros
- `k8s/01_postgres_externo.yaml`: Service sem selector e EndpointSlice para a BD existente.
- `k8s/02_smartdesk.yaml`: Deployment (uma replica) e Service ClusterIP.
- Segredos locais: Secret Kubernetes `smartdesk-db` com `DATABASE_URL` e `SMARTDESK_SESSION_SECRET`, criado no cluster; nunca em Git.

## Verificacoes preliminares
Na raiz do repositorio:
```bash
docker compose up -d db
docker compose -f compose.k3s.yaml up -d k3s
docker compose ps -q db
docker inspect "$(docker compose ps -q db)" --format '{{json .NetworkSettings.Networks}}'
```
Identificar a rede Docker real do contentor `db` e o seu IPv4. Ligar o contentor k3s a essa rede, se ainda nao estiver ligado:
```bash
docker network connect NOME_REAL_DA_REDE smartlearning-k3s
```
Substituir `SUBSTITUIR_PELO_IP_REAL_DO_DB` no primeiro manifesto. O IP pode mudar ao recriar a BD. Esta topologia requer **teste de conectividade real de um pod para db:5432**, tanto em Linux como em Docker Desktop/Windows. Partilhar a rede Docker, por si so, nao comprova acesso a partir da rede dos pods. Se o teste falhar, parar e corrigir a topologia; nao declarar o laboratorio funcional.

## Imagem
```bash
docker build -t smartdesk:k3s-lab .
docker save smartdesk:k3s-lab | docker exec -i smartlearning-k3s k3s ctr images import -
docker exec smartlearning-k3s k3s ctr images list
```
A imagem no manifesto e `docker.io/library/smartdesk:k3s-lab`, com `imagePullPolicy: Never`. Confirmar que aparece no containerd do k3s antes do Deployment.

## Secret local
Criar o Secret no k3s, com valores recolhidos localmente do ambiente ja configurado, **sem colocar valores reais em ficheiros versionados**. A URL deve apontar para `postgres-compose:5432` e para a base existente; reutilizar a mesma chave de sessao do Compose. Evitar colocar passwords em historico de shell, logs ou screenshots. O comando Kubernetes usa sempre:
```bash
docker compose -f compose.k3s.yaml exec k3s kubectl ...
```
Por exemplo, depois de preparar os valores num ambiente seguro dentro do contentor k3s:
```bash
kubectl create secret generic smartdesk-db --from-literal=DATABASE_URL="$DATABASE_URL" --from-literal=SMARTDESK_SESSION_SECRET="$SMARTDESK_SESSION_SECRET"
```
O comando anterior e executado **dentro** do contentor k3s; no anfitriao usar o prefixo `docker compose -f compose.k3s.yaml exec k3s kubectl` quando nao sao necessarias variaveis de shell do contentor. Nunca publicar o Secret.

## Aplicacao
```bash
docker cp k8s/01_postgres_externo.yaml smartlearning-k3s:/tmp/01_postgres_externo.yaml
docker cp k8s/02_smartdesk.yaml smartlearning-k3s:/tmp/02_smartdesk.yaml
docker compose -f compose.k3s.yaml exec k3s kubectl apply -f /tmp/01_postgres_externo.yaml
docker compose -f compose.k3s.yaml exec k3s kubectl apply -f /tmp/02_smartdesk.yaml
docker compose -f compose.k3s.yaml exec k3s kubectl get deployments,pods,services,endpointslices
docker compose -f compose.k3s.yaml exec k3s kubectl rollout status deployment/smartdesk --timeout=120s
```
A porta 8089 ja esta publicada no `compose.k3s.yaml` fechado. Num terminal aberto:
```bash
docker compose -f compose.k3s.yaml exec k3s kubectl port-forward --address 0.0.0.0 service/smartdesk 8089:80
```
Abrir `http://localhost:8089/login`. No Headlamp ja configurado no Notebook 08, observar o namespace `default`, Deployment, Pod e Service SmartDesk. O endpoint `/health` nao verifica a BD.

## Ensaio obrigatorio antes de tres replicas
1. Confirmar login e criar um ticket na interface da porta 8089.
2. Anotar ID, titulo e estado; confirmar na listagem e na mesma BD PostgreSQL do Compose.
3. Reiniciar o pod sem eliminar o volume:
```bash
docker compose -f compose.k3s.yaml exec k3s kubectl delete pod -l app=smartdesk
docker compose -f compose.k3s.yaml exec k3s kubectl rollout status deployment/smartdesk --timeout=120s
```
4. Restabelecer o port-forward se tiver terminado, voltar ao browser e confirmar mesmo ID e estado.
5. Registar evidencia do browser, pod novo e consulta PostgreSQL. **Nao aumentar replicas sem esta demonstracao e aprovacao.**

## Limites
Nao foram executados testes Kubernetes nem de conectividade nesta proposta. `src/services.py` faz verificacao e atualizacao de estado em passos distintos; concorrencia entre varias replicas nao esta validada. `initialize(db)` corre no arranque; inicializacao simultanea numa BD vazia nao foi validada. Nao expor este laboratorio a redes externas.
