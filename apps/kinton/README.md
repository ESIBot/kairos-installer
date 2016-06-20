# Kinton Hub

```bash
docker run -p 1884:1884 kinton/hub
```

You can bind the following volumes:

- `kinton/data`: persistence data.
- `kinton/logs`: logs.

 ```bash
 docker run -p 1884:1884 -v /var/kinton/data:/kinton/data -v /var/kinton/logs:/kinton/logs kinton/hub
 ```
