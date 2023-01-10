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

    rc = 0
    tags = 0
    scan_start = time.perf_counter()
    async for row in store.scan("credential_exchange_v10", {}):
        rc += 1
        tags += len(row.tags)
        print(f"{row}")
    dur = time.perf_counter() - scan_start
    print(f"scan duration ({rc} rows, {tags} tags): {dur:0.2f}s")

if __name__ == "__main__":
    asyncio.run(main());