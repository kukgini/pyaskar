import asyncio
import logging
import os
import sys
import time

from aries_askar import Store

logging.basicConfig(level=os.getenv("LOG_LEVEL", "").upper() or None)

async def main():
    store = await Store.open(
        uri="postgres://postgres:mysecretpassword@localhost:5432/acapy",
        key_method="kdf:argon2i",
        pass_key="acapy")

    categories = ["connection","credential_exchange_v10"]
    records = 0
    scan_start = time.perf_counter()
    for category in categories:
        async for row in store.scan(category, {}):
            records += 1
            print(f"category={category} name={row.name}, tags={row.tags}")
    dur = time.perf_counter() - scan_start
    print(f"scan duration ({records} records): {dur:0.2f}s")

if __name__ == "__main__":
    asyncio.run(main());