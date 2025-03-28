import asyncio
import time
import aiohttp
import os
from datetime import datetime

async def download_file(session, url):
    timedata = datetime.now().strftime("%Y%m%d%H%M%S%f")[:-1]
    original_filename = os.path.basename(url)
    filename = f"{timedata}_{original_filename}"
    print(timedata, filename, original_filename)
    print(f"Downloading {filename} from {url}...")

    async with session.get(url) as response:
        with open(filename, "wb") as file:
            while True:
                chunk = await response.content.read(1024)
                if not chunk:
                    break
                file.write(chunk)
    print(f"Downloaded {filename}")
    return filename
async def main():
    urls = [
        "https://www.example.com/file1.txt",
        "https://www.example.com/file2.txt",
        "https://www.example.com/file3.txt",
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [download_file(session, url) for url in urls]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    print(f"Downloaded files in {end_time - start_time:.2f} seconds")