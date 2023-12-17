Docker commands

Create image:
docker build -t password-generator-api .

Validate images:
```
dokcer images
```

Run image console interactivr:
```
docker run -it password-generator-api /bin/sh
```

Run image app interactive:
```
docker run -it -p 8000:5000 password-generator-api
```

Run image app:
```
docker run -it -p 8000:5000 -d password-generator-api
```

Check containers:
```
docker container ls
```

Stop container:
```
docker stop eef
```