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
>  ✔ Container caddy           Started
> ```
>
> After which, navigating to `https://localhost` will open a SearXNG search page.

## Configuration

By default, the `config/settings.yml` file is setup to allow requests from all origins and to allow response format to be in JSON, meaning you will be ready to go right after installing and running (although you may need to visit https://localhost/ in your browser first to allow connecting).

## Why port 443?
Setting up on port 443 allows us to connect to our local SearXNG instance via HTTPS. This is important because modern web browsers enforce security rules that cause HTTPS websites like the [official LlamaPen instance](https://llamapen.app/) to not able to send requests to non-HTTPS websites. This configuration addresses that and lets you use web search on both the official and any self-hosted LlamaPen instances, while not requiring any 3rd party dns/domain.

## Credits
- **Search results**: [SearXNG](https://github.com/searxng/searxng/)
- **Original site as markdown code**: [url-to-markdown](https://github.com/iw4p/url-to-markdown) by iw4p