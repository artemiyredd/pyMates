"""Стан застосунку, який отримує кожна команда.

Щоб додати нову колекцію (наприклад, нотатник):
1. додайте поле в ``AppContext``;
2. додайте його завантаження в ``load`` і збереження в ``save``.
"""

from dataclasses import dataclass

from .models import AddressBook, NoteBook
from .storage import data_file, load_data, save_data

ADDRESS_BOOK_FILE = "addressbook.pkl"
NOTES_FILE = "notes.pkl"


@dataclass
class AppContext:
    """Усі дані, з якими працюють команди."""

    book: AddressBook
    notes: NoteBook

    @classmethod
    def load(cls) -> "AppContext":
        """Завантажити всі дані з диска."""
        return cls(
            book=load_data(data_file(ADDRESS_BOOK_FILE), AddressBook),
            notes=load_data(data_file(NOTES_FILE), NoteBook),
        )

    def save(self) -> None:
        """Зберегти всі дані на диск."""
        save_data(self.book, data_file(ADDRESS_BOOK_FILE))
        save_data(self.notes, data_file(NOTES_FILE))
