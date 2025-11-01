# LlamaPen-Search

Self-hostable search integration for [LlamaPen](https://github.com/ImDarkTom/LlamaPen), using SearXNG for search and MarkItDown for url-to-markdown conversions.

## Setup

### Prerequisites

- Ensure both **Docker** and **Docker Compose** are installed and functional.
- No other app/service is already running on port `8000`.

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
>  ✔ Network llamapen-search_searxnet  Created
>  ✔ Container searxng                 Started
>  ✔ Container url2md                  Started
> ```
>
> After which, navigating to `http://localhost:8000` will open a short guide page. If you see this page, you are ready for use inside LlamaPen.

## Configuration

A SearXNG config is available at `config/settings.yml`, it remains mostly the same as the default config with the exception of allowing JSON requests. It will not be directly accessible by you as it is only interally used within your Docker `searxnet` network, and any search requests are forwarded by `url2md`. 

## Credits

- **Search results**: [SearXNG](https://github.com/searxng/searxng/)
- **Original site as markdown code**: [url-to-markdown](https://github.com/iw4p/url-to-markdown) by iw4p

## License

*LlamaPen-Search* is AGPL-3.0.