# backend/db.py
from prisma import Prisma

prisma = Prisma()

async def get_prisma():
    return prisma
