from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import Response
from markitdown import MarkItDown, UnsupportedFormatException, FileConversionException
from urllib.parse import unquote
import asyncio
import logging
import requests

SEARX_URL = "http://searxng:8080"

app = FastAPI(
    title="URL to Markdown API",
    description="API service to convert urls to markdown using MarkItDown",
    version="1.0.0",
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.get("/healthz")
async def healthz():
    return Response(content="ok", media_type="text/plain")

@app.get("/search")
async def search(q: str, limit: int = 5):
    def format_result(result):
        return {
            "url": result.get("url", ""),
            "title": result.get("title", ""),
            "content": result.get("content", ""),
            "published": result.get("publishedDate", "")
        }
    
    limit = max([limit, 1])

    response = requests.get(f"{SEARX_URL}/search?q={q}&format=json", verify=False)

    data = response.json()

    results = data.get("results", [])[:limit]
    results = list(map(format_result, results))

    return {
        "query": q,
        "results": results
    }


@app.get("/open")
async def convert_url(url: str, request: Request):
    if not url:
        return Response(
            content=f"Usage: {request.base_url}open?url=<url>",
            media_type="text/plain",
        )

    decoded_url = unquote(url)
    logger.info("Decoded URL: %s", decoded_url)

    try:
        if not decoded_url.startswith(("http://", "https://")):
            if decoded_url.startswith("www."):
                decoded_url = "https://" + decoded_url
            else:
                decoded_url = "https://www." + decoded_url

        try:

            async def _convert() -> str:
                def _run():
                    instance = MarkItDown()
                    conversion_result = instance.convert(decoded_url)
                    return conversion_result.text_content

                return await asyncio.to_thread(_run)

            text_content = await asyncio.wait_for(_convert(), timeout=25)
            return Response(content=text_content, media_type="text/plain")
        except UnsupportedFormatException as e:
            raise HTTPException(
                status_code=415, detail=f"Unsupported URL format: {str(e)}"
            )
        except FileConversionException as e:
            raise HTTPException(
                status_code=400, detail=f"URL conversion failed: {str(e)}"
            )
        except asyncio.TimeoutError:
            raise HTTPException(
                status_code=504, detail="Conversion timed out. Please try again later."
            )
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Internal server error: {str(e)}"
            )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"URL processing failed: {str(e)}")