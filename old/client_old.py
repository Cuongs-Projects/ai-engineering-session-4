import asyncio
from fastmcp import Client

#client = Client("http://localhost:3000/mcp")
client = Client("https://aggressive-emerald-moth.fastmcp.app/mcp")

async def call_tool(name: str):
    async with client:
        result = await client.call_tool("greet", {"name": name})
        print(result)

asyncio.run(call_tool("Chinkka"))