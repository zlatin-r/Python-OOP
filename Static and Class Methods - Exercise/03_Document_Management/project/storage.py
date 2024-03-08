from typing import List
from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:

    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category: Category) -> None:
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document) -> None:
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str) -> None:
        category = self.categories[category_id - 1]
        category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        topic = self.topics[topic_id - 1]
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_filename: str) -> None:
        document = self.documents[document_id - 1]
        document.edit(new_filename)

    def delete_category(self, category_id: int) -> None:
        curr_category = self.categories[category_id - 1]
        self.categories.remove(curr_category)

    def delete_topic(self, topic_id: int) -> None:
        curr_topic = self.topics[topic_id - 1]
        self.topics.remove(curr_topic)

    def delete_document(self, document_id: int) -> None:
        curr_document = self.documents[document_id - 1]
        self.documents.remove(curr_document)

    def get_document(self, document_id: int) -> Document:
        return self.documents[document_id - 1]

    def __repr__(self) -> str:
        return '\n'.join([str(d) for d in self.documents])
