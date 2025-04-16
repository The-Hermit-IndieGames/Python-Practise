import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index  # 區塊編號
        self.previous_hash = previous_hash  # 前一個區塊的雜湊值
        self.timestamp = timestamp or time.time()  # 區塊生成時間
        self.data = data  # 區塊中存放的資料（可為交易清單）
        self.hash = self.calculate_hash()  # 此區塊的雜湊值
    
    def calculate_hash(self):
        # 將區塊內容串接並進行 SHA-256 雜湊
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}"
        return hashlib.sha256(block_string.encode()).hexdigest()

# 建立一個區塊示範
genesis_block = Block(0, "0", "Genesis Block")
print(f"Block Hash: {genesis_block.hash}")
