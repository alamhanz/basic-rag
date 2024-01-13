# source: https://github.com/langchain-ai/langchain/issues/3016

from langchain.schema import Document
import json
from typing import Iterable


def save_docs_to_jsonl(array: Iterable[Document], file_path: str) -> None:
    with open(file_path, "w") as jsonl_file:
        for doc in array:
            try:
                jsonl_file.write(doc.json() + "\n")
            except:
                jsonl_file.write(json.dumps(doc) + "\n")


def load_docs_from_jsonl(file_path, document_object=True) -> Iterable[Document]:
    array = []
    with open(file_path, "r") as jsonl_file:
        for line in jsonl_file:
            obj = json.loads(line)
            if document_object:
                obj = Document(**obj)
            array.append(obj)
    return array
