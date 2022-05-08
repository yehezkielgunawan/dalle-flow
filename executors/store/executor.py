from jina import Executor, requests, DocumentArray


class MyStore(Executor):

    def __init__(self, store_path: str, **kwargs):
        super().__init__(**kwargs)
        self.storage = DocumentArray(storage='sqlite', config={'connection': store_path, 'table_name': f'dallemega'})

    @requests(on='/')
    def store(self, docs: DocumentArray, **kwargs):
        docs[...].blobs = None  # remove all blobs from anywhere to save space
        self.storage.extend(docs)
        print(f'total: {len(self.storage)}')
