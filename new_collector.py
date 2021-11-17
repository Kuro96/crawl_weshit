from typing import TypeVar, Type

import yaml
from pymongo import MongoClient

T = TypeVar('T', bound='NewsCollector')


class NewsCollector:

    def __init__(
        self,
        client: MongoClient,
    ) -> None:
        self.client = client
        self.db = client.news

    @classmethod
    def from_file(
        cls: Type[T],
        cfg_fp: str = 'config.yml',
    ) -> T:
        with open(cfg_fp) as f:
            cfg = yaml.load(f, Loader=yaml.SafeLoader)
        client = MongoClient(
            host=cfg.get('host', '127.0.0.1'),
            port=cfg.get('port', 27017),
            username=cfg.get('username'),
            password=cfg.get('password'),
        )
        return cls(client)


if __name__ == '__main__':
    def fmt_result(result):
        return 'successed' if result.acknowledged else 'failed'

    cc = NewsCollector.from_file()

    result = cc.db.yjjr.insert_one({'name': 'aaa'})
    print(f'Write {fmt_result(result)}!')
    print(f'Total count: {cc.db.yjjr.count_documents(filter={})}')
    result = cc.db.yjjr.delete_one({'name': 'aaa'})
    print(f'Delete {fmt_result(result)}!')

    import pdb
    pdb.set_trace()
