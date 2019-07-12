# conding: utf-8
import hashlib
from abc import ABCMeta, abstractmethod
from injector import Injector, inject

# インターフェースを定義(なぜインターフェースを定義しているかは考えてみて)
# インターフェースは，引数と返り値だけ持つ抽象クラス
class EncrypterInterface(metaclass=ABCMeta):
    # パスワードハッシュ化用のメソッド
    @abstractmethod
    def hashed_password(self, password: str) -> str:
        pass
    # ハッシュ化された文字列と対象が等価か評価するメソッド
    @abstractmethod
    def check_hashed(self, hashed: str, password: str) -> bool:
        pass

# 実際に暗号化を行う本体
# コンストラクタで，インターフェースをインジェクション
class Encrypter():
    @inject
    def __init__(self, i: EncrypterInterface):
        if not isinstance(i, EncrypterInterface):
            raise Exception("i is not Interface of Encrypter")
    
    def hashed_password(self, password: str) -> str:
        bin_password = password.encode()
        hashed_pass = hashlib.sha256(bin_password).hexdigest() 
        return hashed_pass
    
    def check_hashed(self, hashed: str, password: str) -> bool:
        bin_password = password.encode()
        hashed_pass = hashlib.sha256(bin_password).hexdigest() 
        if hashed == hashed_pass: return True
        else: return False