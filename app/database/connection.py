"""
数据库连接池模块
"""
from databases import Database
from sqlalchemy import create_engine, MetaData
# from sqlalchemy.orm import sessionmaker # 不再需要
from sqlalchemy.ext.declarative import declarative_base
from pathlib import Path
import os

from app.config.config import settings
from app.log.logger import get_database_logger

logger = get_database_logger()

# 确保数据库文件目录存在
DB_DIR = Path(os.path.dirname(settings.SQLITE_DATABASE))
DB_DIR.mkdir(exist_ok=True)

# 数据库URL - 使用SQLite
DATABASE_URL = f"sqlite:///{settings.SQLITE_DATABASE}"

# 创建数据库引擎
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# 创建元数据对象
metadata = MetaData()

# 创建基类
Base = declarative_base(metadata=metadata)

# 创建数据库连接池
database = Database(DATABASE_URL)


async def connect_to_db():
    """
    连接到数据库
    """
    try:
        await database.connect()
        logger.info("Connected to database")
    except Exception as e:
        logger.error(f"Failed to connect to database: {str(e)}")
        raise


async def disconnect_from_db():
    """
    断开数据库连接
    """
    try:
        await database.disconnect()
        logger.info("Disconnected from database")
    except Exception as e:
        logger.error(f"Failed to disconnect from database: {str(e)}")
