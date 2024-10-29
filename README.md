# branching-startegy

```
docker build -t python-web:1 .
```

```
docker run -d --name python -p 5000:5000 -e ENV_NAME=dev python-web:1
```



```
helm install branching-strategy ./ -f env/dev.yaml --namespace dev --create-namespace
```

```
helm upgrade --install "$HELM_RELEASE_NAME" . -f env/dev.yaml --namespace dev --create-namespace --set image.repository="$DOCKER_IMAGE" --set image.tag="$IMAGE_TAG"
```

