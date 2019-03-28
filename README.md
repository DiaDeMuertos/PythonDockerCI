# N Queen

## DOCKER

Crear imagen
```
$ docker build -t glen-app .
```

Entrar el contenedor
```
$ docker run --name glen-app -it --rm glen-app
```

Ejecular python del contenedor y lo borra
```
$ docker run --name glen-app -it --rm glen-app python3 main.py
```

Ver el log del test
```
$ docker logs glen-app-test
```

# DOCKER COMPOSE

Crear imagenes
```
$ docker-compose build
```

Ejecutar contenedores
```
$ docker-compose up -d
```

Ver estado de contenedores 
```
$ docker-compose ps
```

Ejecuta (default test) contenedor y lo borra 
```
$ docker-compose run --rm app
```

Ejecuta contenedor y lo borra 
```
$ docker-compose run --rm app python3 main.py
```
