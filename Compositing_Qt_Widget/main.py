import sys, os

sys.path.append(os.path.abspath(""))

from PySide2.QtCore import Slot, QCoreApplication
from PySide2.QtGui import Qt, QKeySequence, QFont
from PySide2.QtWidgets import QListWidget, QHBoxLayout, QVBoxLayout, QPushButton, QWidget, QSpacerItem, QSizePolicy, \
    QInputDialog, QListWidgetItem, QApplication, QDialog
from Compositing_Qt_Widget.StringListInput import StringListInput
from Compositing_Qt_Widget.StringListInputDesigned import StringListInputDesigned

str_list = ["www.ironmesh.ru", "https://t.me/ironmesh_studio_rus", "by Ivan Balakirev"]

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setFont(QFont("Comic Sans", 20, QFont.Normal))
    app.setStyle("Fusion")
    window = QWidget()
    layout = QHBoxLayout(window)

    sli = StringListInput()
    sli.set_list(["StringListInput", ""] + (str_list))
    sli.string_added.connect(lambda s: print(f"String has been added: {s}"))
    sli.string_changed.connect(lambda row: print(f"String has been edited in row: {row}"))
    sli.string_deleted.connect(lambda s: print(f"String has been deleted: {s}"))
    layout.addWidget(sli)

    sli2 = StringListInputDesigned()
    sli2.set_list(["StringListInputDesigned", ""] + (str_list))
    layout.addWidget(sli2)
    window.show()
    window.resize(800, 300)
    sys.exit(app.exec_())