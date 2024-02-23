from motor.motor_asyncio import AsyncIOMotorClient

mongo_client = AsyncIOMotorClient(MONGO_DB_URI)
mongodb = mongo_client.TXT
sudoersdb = mongodb.sudoers

async def get_sudoers() -> list[int]:
    try:
        sudoers_doc = await sudoersdb.find_one({"sudo": "sudo"})
        if sudoers_doc:
            return sudoers_doc.get("sudoers", [])
        else:
            return []
    except Exception as e:
        print(f"Error fetching sudoers: {str(e)}")
        return []

async def add_sudo(user_id: int) -> bool:
    try:
        sudoers = await get_sudoers()
        if user_id in sudoers:
            return False  # User is already a sudoer
        sudoers.append(user_id)
        await sudoersdb.update_one(
            {"sudo": "sudo"}, {"$set": {"sudoers": sudoers}}, upsert=True
        )
        return True
    except Exception as e:
        print(f"Error adding sudo: {str(e)}")
        return False

async def remove_sudo(user_id: int) -> bool:
    try:
        sudoers = await get_sudoers()
        if user_id not in sudoers:
            return False  # User is not a sudoer
        sudoers.remove(user_id)
        await sudoersdb.update_one(
            {"sudo": "sudo"}, {"$set": {"sudoers": sudoers}}, upsert=True
        )
        return True
    except Exception as e:
        print(f"Error removing sudo: {str(e)}")
        return False