import hashlib
import time

#區塊結構
class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index                          #區塊編號
        self.previous_hash = previous_hash          #前一個區塊的雜湊值
        self.timestamp = timestamp or time.time()   #區塊生成時間
        self.data = data                            #區塊中存放的資料（可為交易清單）
        self.hash = self.calculate_hash()           #此區塊的雜湊值
    
    def calculate_hash(self):
        #將區塊內容串接並進行 SHA-256 雜湊
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}"
        return hashlib.sha256(block_string.encode()).hexdigest()

#建立一個區塊示範
genesis_block = Block(0, "0", "Genesis Block")
print(f"Block Hash: {genesis_block.hash}")



#hash示範
def hash_data(data):
    #對任意資料進行 SHA-256 雜湊
    return hashlib.sha256(data.encode()).hexdigest()

#展示: 1、2 改變尾碼  2、3 改變首字母大小寫
print(hash_data("Hello Blockchain 001"))    #回傳 2652636848ec74ec09faa3e09b08362f1fcccaffa426c6b6d6aa22cd0e0d8f01
print(hash_data("Hello Blockchain 002"))    #回傳 cee75c795f3547678491cdc7c910689ac0a6ec981bcc0eac4248a7494384f878
print(hash_data("hello Blockchain 002"))    #回傳 302050d94739cbfbf3ff74abde0efeb35c34568bee2cdd3c6463cb11c2ff3479

