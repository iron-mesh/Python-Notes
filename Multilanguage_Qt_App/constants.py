from PySide2.QtCore import QCoreApplication as QA

class LangConstants:
    ''' Класс с языковыми константами'''
    @classmethod
    def retranslate(cls):
        ''' Метод переводит языковые константы, используя установленные в приложении словари'''
        cls.route_status = QA.translate("языковые константы", "Маршрут проложен: {0}")
        cls.destination_point = QA.translate("языковые константы", "Пункт назначения: {0}")
        cls.status_success = QA.translate("языковые константы", "успешно")
        cls.status_failed = QA.translate("языковые константы", "произошла ошибка")
        cls.start= QA.translate("языковые константы", "Поехали!")
        cls.start_title_info = QA.translate("заголовки окон", "Сообщение от ЦУП")
        cls.test_text = QA.translate("заголовки окон", "Случайный текст", "комментарий от разработчика")
