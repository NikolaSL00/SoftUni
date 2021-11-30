from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def __get_object_by_id(self, objects: list, object_id: int):
        for object in objects:
            if object.id == object_id:
                return object

    def add_category(self, category: Category):
        if category in self.categories:
            return
        self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic in self.topics:
            return
        self.topics.append(topic)

    def add_document(self, document: Document):
        if document in self.documents:
            return
        self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = self.__get_object_by_id(self.categories, category_id)
        category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.__get_object_by_id(self.topics, topic_id)
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        document = self.__get_object_by_id(self.documents, document_id)
        document.edit(new_file_name)

    def delete_category(self, category_id):
        category_to_delete = self.__get_object_by_id(self.categories, category_id)
        self.categories.remove(category_to_delete)

    def delete_topic(self, topic_id):
        topic_to_delete = self.__get_object_by_id(self.topics, topic_id)
        self.topics.remove(topic_to_delete)

    def delete_document(self, document_id):
        document_to_delete = self.__get_object_by_id(self.documents, document_id)
        self.documents.remove(document_to_delete)

    def get_document(self, document_id):
        return self.__get_object_by_id(self.documents, document_id)

    def __repr__(self):
        result_string = [str(document) for document in self.documents]
        return '\n'.join(result_string)
