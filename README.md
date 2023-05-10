# Local lab to POC SSTI on Mako templates

Ce repot est un projet constituant à POC une SSTI (Server Side Template Injection) dans le moteur de templates [Mako](https://www.makotemplates.org/), utilisant python. 


### Docker - How to run 

Requierement: 
    [docker-compose](https://docs.docker.com/compose/)

```sh
docker-build up --build
```

### From source - Lancer le lab sur son local

Requierement: 
    `python3-venv`

```sh
chmod +x setup.sh
./setup.sh
```