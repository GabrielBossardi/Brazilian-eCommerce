To create the stack, execute the commands below:

```
docker-compose --env-file .env -f infra/docker-compose.yaml up -d
```

```
cd extraction/script__kaggle/;./build.sh
```

```
docker run --rm -e DB_ROOT_USER=postgres -e DB_ROOT_PASSWORD=postgres -e DB_HOST="172.16.0.2" --network=infra_stack_net extractor/kaggle python main.py
```
