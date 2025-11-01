# LlamaPen-Search 🌐

Add self-hosted search integration to [LlamaPen](https://github.com/ImDarkTom/LlamaPen) using SearXNG and Caddy.

## Setup

### Prerequisites

- Ensure **Docker** and **Docker Compose** are installed and functional.
- No other app/service is already running on port `443` (local HTTPS).

### Downloading

```bash
git clone https://github.com/ImDarkTom/LlamaPen-Search
cd ./LlamaPen-Search
```

### Running

```bash
docker compose up -d
```

> If everything goes well, you should see something along the lines of:
> 
> ```bash
> [+] Running 3/3
>  ✔ Network searxng_searxnet  Created
>  ✔ Container searxng         Started
>  ✔ Container url2md          Started
> ```
>
> After which, navigating to `http://localhost:8080` will open a guide page.

## Configuration

By default, the `config/settings.yml` file is setup to allow requests from all origins and to allow response format to be in JSON, meaning you will be ready to go right after installing and running (although you may need to visit https://localhost/ in your browser first to allow connecting).

## Credits
- **Search results**: [SearXNG](https://github.com/searxng/searxng/)
- **Original site as markdown code**: [url-to-markdown](https://github.com/iw4p/url-to-markdown) by iw4p