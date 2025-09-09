# LlamaPen-Search

Add search integration to LlamaPen using SearXNG.

## Setup

### Prerequisites

- Ensure **Docker** and **Docker Compose** are installed and functional.
- No other app/service is already running on port 8080.

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
> [+] Running 2/2
>  ✔ Network searxng_default  Created
>  ✔ Container searxng        Started
> ```
>
> After which, navigating to `http://127.0.0.1:8080` will open a SearXNG search page.

## Configuration

By default, the `config/settings.yml` file is setup to allow requests from all origins and to allow response format to be in JSON, meaning you should be ready to go right after installing and running.
