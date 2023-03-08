
from .ui_InputStringListDesigned import Ui_Form
from .StringListInput import StringListInput
from PySide2.QtWidgets import QApplication

class StringListInputDesigned(StringListInput):
    """Виджет для ввода списка строк 2
    (Widget for entering a list of strings 2)"""
    def __init__(self, parent = None):
        super(StringListInput, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.listWidget = self.ui.listWidget
        self.listWidget.setFont(QApplication.instance().font())


        self.ui.add_btn.clicked.connect(self._on_add_item)
        self.ui.edit_btn.clicked.connect(self._on_edit_item)
        self.listWidget.itemDoubleClicked.connect(self._on_edit_item)
        self.ui.delete_btn.clicked.connect(self._on_del_item)
        self.ui.moveup_btn.clicked.connect(lambda :self._on_move_item("up"))
        self.ui.movedown_btn.clicked.connect(lambda :self._on_move_item("down"))

