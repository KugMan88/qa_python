import pytest
class TestBooksCollector:

    def test_add_new_book_adding_a_new_book(self, books_collector):
        books_collector.add_new_book("Красная шапочка")
        assert "Красная шапочка" in books_collector.get_books_genre()

    def test_add_new_book_invalid_name(self,books_collector):
        books_collector.add_new_book("Преступление и наказание" * 20)
        assert "Преступление и наказание" * 20 not in books_collector.get_books_genre()

    @pytest.mark.parametrize("genre", ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_assigning_genre(self,books_collector, genre):
        books_collector.add_new_book("Молчание ягнят")
        books_collector.set_book_genre("Молчание ягнят", genre)
        assert books_collector.get_book_genre("Молчание ягнят") == genre

    def test_set_book_genre_invalid_book(self, books_collector):
        books_collector.set_book_genre("Властелин колец", "Фантастика")
        assert books_collector.get_book_genre("Властелин колец") is None or books_collector.get_book_genre("Властелин колец") == ""

    def test_get_book_genre_getting_genre(self,books_collector):
        books_collector.add_new_book("Оно")
        books_collector.set_book_genre("Оно", "Ужасы")
        assert books_collector.get_book_genre("Оно") == "Ужасы"

    def test_get_book_genre_invalid_name(self,books_collector):
        assert books_collector.get_book_genre("Код да Винчи") is None

    def test_get_books_with_specific_genre_list_specific_genre(self,books_collector):
        books_collector.add_new_book("Убийство на улице Морг")
        books_collector.set_book_genre("Убийство на улице Морг", "Детективы")
        assert "Убийство на улице Морг" in books_collector.get_books_with_specific_genre("Детективы")

    def test_get_books_with_specific_genre_invalid_genre(self,books_collector):
        assert books_collector.get_books_with_specific_genre("Романтика") == []

    def test_get_books_for_children_children_books(self,books_collector):
        books_collector.add_new_book("Простоквашино")
        books_collector.set_book_genre("Простоквашино", "Мультфильмы")
        assert "Простоквашино" in books_collector.get_books_for_children()

    def test_get_books_for_children_invalid_genre(self,books_collector):
        books_collector.add_new_book("Вий")
        books_collector.set_book_genre("Вий", "Ужасы")
        assert "Вий" not in books_collector.get_books_for_children()

    def test_add_book_in_favorites_adding_book(self,books_collector):
        books_collector.add_new_book("Дюна")
        books_collector.add_book_in_favorites("Дюна")
        assert "Дюна" in books_collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_already_added(self,books_collector):
        books_collector.add_new_book("Повелитель мух")
        books_collector.add_book_in_favorites("Повелитель мух")
        books_collector.add_book_in_favorites("Повелитель мух")
        assert books_collector.get_list_of_favorites_books().count("Повелитель мух") == 1

    def test_delete_book_from_favorites(self,books_collector):
        books_collector.add_new_book("Вторая жизнь Уве")
        books_collector.add_book_in_favorites("Вторая жизнь Уве")
        books_collector.delete_book_from_favorites("Вторая жизнь Уве")
        assert "Вторая жизнь Уве" not in books_collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_not_in_favorites(self,books_collector):
        books_collector.delete_book_from_favorites("Мастер и Маргарита")
        assert books_collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books(self,books_collector):
        books_collector.add_new_book("Важные годы")
        books_collector.add_book_in_favorites("Важные годы")
        assert books_collector.get_list_of_favorites_books() == ["Важные годы"]

    def test_get_list_of_favorites_books_empty(self,books_collector):
        assert books_collector.get_list_of_favorites_books() == []