from typing import Sequence
from PySide2.QtCore import Slot, QCoreApplication
from PySide2.QtCore import Signal
from PySide2.QtWidgets import QListWidget, QHBoxLayout, QVBoxLayout, QPushButton, QWidget, QSpacerItem, QSizePolicy, \
    QInputDialog, QListWidgetItem, QApplication, QDialog


class StringListInput(QWidget):
    """Виджет для ввода списка строк
       (Widget for entering a list of strings)"""

    string_added = Signal(str)
    string_changed = Signal(int)
    string_deleted = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        horizontalLayout = QHBoxLayout(self)

        self.listWidget = QListWidget()
        self.listWidget.setFont(QApplication.instance().font())

        self.listWidget.itemDoubleClicked.connect(self._on_edit_item)
        horizontalLayout.addWidget(self.listWidget)
        horizontalLayout.setMargin(0)

        verticalLayout = QVBoxLayout()

        add_btn = QPushButton("+")
        add_btn.clicked.connect(self._on_add_item)
        verticalLayout.addWidget(add_btn)

        edit_btn = QPushButton("✎")
        edit_btn.clicked.connect(self._on_edit_item)
        verticalLayout.addWidget(edit_btn)

        delete_btn = QPushButton("−")
        delete_btn.clicked.connect(self._on_del_item)
        verticalLayout.addWidget(delete_btn)

        verticalSpacer_2 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)
        verticalLayout.addItem(verticalSpacer_2)

        moveup_btn = QPushButton("⮝")
        moveup_btn.clicked.connect(lambda: self._on_move_item("up"))
        verticalLayout.addWidget(moveup_btn)

        movedown_btn = QPushButton("⮟")
        movedown_btn.clicked.connect(lambda: self._on_move_item("down"))
        verticalLayout.addWidget(movedown_btn)

        verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        verticalLayout.addItem(verticalSpacer)
        horizontalLayout.addLayout(verticalLayout)

    def get_list(self) -> list[str]:
        """Получить список строк (Get list of strings)"""
        extracted_list: list[str] = []
        for i in range(self.listWidget.count()):
            extracted_list.append(self.listWidget.item(i).text())
        return extracted_list

    def set_list(self, lst: Sequence[str]) -> None:
        """Установить список строк (Set list of strings)"""
        self.listWidget.clear()
        self.listWidget.addItems(lst)

    def setToolTip(self, arg__1: str) -> None:
        """Установить всплывающую подсказку (Set tooltip)"""
        self.listWidget.setToolTip(arg__1)

    def toolTip(self) -> str:
        """Вернуть текст всплывающей позсказки (Returns text of tooltip)"""
        return self.listWidget.toolTip()

    def _get_text_dialog(self, title: str, label: str, text: str = "") -> str:
        """ Получить текст, введенный пользователем в диалоговом окне
        (Get the text entered by an user in the dialog box)"""
        dlg = QInputDialog(self)
        dlg.setInputMode(QInputDialog.TextInput)
        dlg.setWindowTitle(title)
        dlg.setLabelText(label)
        dlg.setTextValue(text)
        dlg.resize(600, 0)
        res = dlg.exec()
        if res == QDialog.Accepted:
            return dlg.textValue()
        else:
            return text

    @Slot()
    def _on_add_item(self):
        text = self._get_text_dialog(QCoreApplication.translate("input_widgets", "Add string"),
                                     QCoreApplication.translate("input_widgets", "Enter the line text"))
        if text:
            self.listWidget.addItem(text)
            self.listWidget.setCurrentRow(self.listWidget.count() - 1)
            self.string_added.emit(text)

    @Slot()
    def _on_edit_item(self):
        row = self.listWidget.currentRow()
        if row < 0: return
        item: QListWidgetItem = self.listWidget.item(row)
        prev_text: str = item.text()

        text = self._get_text_dialog(QCoreApplication.translate("input_widgets", "Edit string"),
                                     QCoreApplication.translate("input_widgets", "Edit the line text"),
                                     text=item.text())

        if text and text != prev_text:
            item.setText(text)
            self.string_changed.emit(row)

    @Slot()
    def _on_del_item(self):
        row = self.listWidget.currentRow()
        if row < 0:
            return

        self.string_deleted.emit(self.listWidget.takeItem(row).text())

    @Slot()
    def _on_move_item(self, direction: str):
        row = self.listWidget.currentRow()
        if row < 0:
            return
        count = self.listWidget.count()

        if direction == "up":
            if row > 0:
                item = self.listWidget.takeItem(row)
                self.listWidget.insertItem(row - 1, item)
                self.listWidget.setCurrentRow(row - 1)

        elif direction == "down":
            if row < count - 1:
                item = self.listWidget.takeItem(row)
                self.listWidget.insertItem(row + 1, item)
                self.listWidget.setCurrentRow(row + 1)
