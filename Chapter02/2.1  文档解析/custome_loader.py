#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/9/29 16:09
# @Author  : yongjie.su
# @File    : custome_loader.py
# @Software: PyCharm
import logging
from typing import List, Optional
from langchain_core.documents import Document
from langchain_community.document_loaders import TextLoader

logger = logging.getLogger(__name__)


class CustomTextLoader(TextLoader):
    """Load text file.


    Args:
        file_path: Path to the file to load.

        encoding: File encoding to use. If `None`, the file will be loaded
        with the default system encoding.

        autodetect_encoding: Whether to try to autodetect the file encoding
            if the specified encoding fails.
    """

    def __init__(self, file_path: str, encoding: Optional[str] = None,
                 autodetect_encoding: bool = False):
        """Initialize with file path."""
        super().__init__(file_path, encoding, autodetect_encoding)

    def load(self) -> List[Document]:
        """Load from file path."""

        try:
            with open(self.file_path, encoding=self.encoding) as f:
                lines = f.readlines()
        except Exception as e:
            raise RuntimeError(f"Error loading {self.file_path}") from e
        if not lines:
            return []
        docs = []
        for idx, line in enumerate(lines):
            metadata = {"source": self.file_path, "index": idx}
            docs.append(Document(page_content=line, metadata=metadata))
        return docs
