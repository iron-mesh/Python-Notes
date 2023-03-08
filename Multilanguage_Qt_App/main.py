import sys, os, random

from PySide2.QtWidgets import QMainWindow, QApplication, QAbstractItemView, QMessageBox
from PySide2.QtCore import QStringListModel
from PySide2.QtCore import QTranslator
from ui_spaceship_control_panel2 import Ui_MainWindow
from constants import LangConstants as LC

TRANSLATE_DIR = "./Translates" # папка в которой находятся словари

class MainWindow (QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow() # создаем поле с экземпляром класса интерфейса
        self.ui.setupUi(self) # инициализируем интерфейс
        self._init_lang()  # инициализируем список доступных языков
        self.ui.comboBox_language.currentTextChanged.connect(self.on_lang_changed) #привязываем обработчик изменения языка через выпадающий список
        self.ui.compute_pushButton.clicked.connect(self.on_calc_route)#привязываем обработчик на кнопку "построить маршрут"
        self.ui._pushButton_2.clicked.connect(self.on_start)#привязываем обработчик на кнопку "запустит ..."
        self.model = QStringListModel() # модель данных
        self.ui.listView.setModel(self.model) #установить модель в представление
        self.ui.listView.setEditTriggers(QAbstractItemView.NoEditTriggers) #запретить редактирование

    def _init_lang(self):
        dir_list = [i for i in os.listdir(TRANSLATE_DIR) if os.path.isdir(os.path.join(TRANSLATE_DIR, i))] #получаем список папок со словарями
        self.ui.comboBox_language.addItems(dir_list) # добавляем список папок в список
        self._translators = [] #здесь будут храниться установленные словари
        self.ui.comboBox_language.setCurrentText("Русский")  #хочу чтобы текущий язык был русский
        self.on_lang_changed() #запускаем процедуру обновления перевода интерфейса

    def on_lang_changed(self):
        '''Выполнить обновление языка интерфейса'''
        def set_tranlators():
            '''установить словари в приложение'''
            for e in self._translators:
                app.installTranslator(e)

        def del_tranlators():
            '''удалить словари из приложения'''
            for e in self._translators:
                app.removeTranslator(e)

        del_tranlators() # удалить текущие словари из приложения
        self._translators.clear() # очистить список со словарями

        current_lang:str = self.ui.comboBox_language.currentText() # прочитать выбранный язык
        file_list:list[str] = [os.path.join(TRANSLATE_DIR, current_lang, e) for e in os.listdir(os.path.join(TRANSLATE_DIR, current_lang))] # получить список папок, содержащих словари

        for f in file_list: # добавить словари в список
            self._translators.append(QTranslator())
            self._translators[-1].load(f)

        set_tranlators() # установить словари в приложение
        self.ui.retranslateUi(self) # перевесть текст в элементах интерфейса
        LC.retranslate() # в классе с языковыми константами

    def on_calc_route(self):
        is_successful:bool = random.random()>0.5
        successful_status:str = LC.status_success if is_successful else LC.status_failed
        self.model.setStringList(
            [LC.destination_point.format(self.ui.destination_comboBox.currentText()),
            LC.route_status.format(successful_status)])

    def on_start(self):
        QMessageBox.information(self, LC.start_title_info, LC.start, buttons=QMessageBox.YesToAll)



app = QApplication(sys.argv)
app.setStyle("Fusion")
window = MainWindow()
window.show()
sys.exit(app.exec_())



