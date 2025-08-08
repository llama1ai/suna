import fakeredis.aioredis as fakeredis
from typing import List, Any

client: fakeredis.FakeRedis | None = None

REDIS_KEY_TTL = 3600 * 24


async def initialize_async():
    global client
    if client is None:
        client = fakeredis.FakeRedis()
    return client


async def close():
    global client
    if client:
        await client.close()
        client = None


async def get_client():
    global client
    if client is None:
        await initialize_async()
    return client


async def set(key: str, value: str, ex: int = None, nx: bool = False):
    redis_client = await get_client()
    return await redis_client.set(key, value, ex=ex, nx=nx)


async def get(key: str, default: str = None):
    redis_client = await get_client()
    result = await redis_client.get(key)
    return result if result is not None else default


async def delete(key: str):
    redis_client = await get_client()
    return await redis_client.delete(key)


async def publish(channel: str, message: str):
    redis_client = await get_client()
    return await redis_client.publish(channel, message)


async def create_pubsub():
    redis_client = await get_client()
    return redis_client.pubsub()


async def rpush(key: str, *values: Any):
    redis_client = await get_client()
    return await redis_client.rpush(key, *values)


async def lrange(key: str, start: int, end: int) -> List[str]:
    redis_client = await get_client()
    return await redis_client.lrange(key, start, end)


async def keys(pattern: str) -> List[str]:
    redis_client = await get_client()
    return await redis_client.keys(pattern)


async def expire(key: str, seconds: int):
    redis_client = await get_client()
    return await redis_client.expire(key, seconds)
