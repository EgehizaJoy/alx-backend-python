import asyncio
import aiosqlite

DB_NAME = "example.db"

async def async_fetch_users():
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute("SELECT * FROM users")
        result = await cursor.fetchall()
        await cursor.close()
        print("All users:")
        for row in result:
            print(row)
        return result

async def async_fetch_older_users():
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute("SELECT * FROM users WHERE age > 40")
        result = await cursor.fetchall()
        await cursor.close()
        print("\nUsers older than 40:")
        for row in result:
            print(row)
        return result

async def fetch_concurrently():
    await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )

