import sys

from PyQt5 import QtCore, QtGui, QtWidgets


class UiDialog:
    def setup_ui(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(900, 430)
        dialog.setWindowTitle("code string generator")

        self.convert_to_text_button = QtWidgets.QPushButton("Convert to text", dialog)
        self.convert_to_text_button.setEnabled(False)  # todo
        self.convert_to_table_button = QtWidgets.QPushButton("Convert to table", dialog)
        self.convert_to_table_button.setEnabled(False)  # todo
        self.add_deck_to_table_button = QtWidgets.QPushButton(
            "Add deck to table", dialog
        )
        self.add_deck_to_table_button.setEnabled(False)  # todo
        self.remove_deck_from_table_button = QtWidgets.QPushButton(
            "Remove deck from table", dialog
        )
        self.remove_deck_from_table_button.setEnabled(False)  # todo
        self.import_from_config_button = QtWidgets.QPushButton(
            "Import from config", dialog
        )
        self.import_from_config_button.setEnabled(False)  # todo
        self.export_to_config_button = QtWidgets.QPushButton("Export to config", dialog)
        self.export_to_config_button.setEnabled(False)  # todo

        self.table_widget = QtWidgets.QTableWidget(dialog)
        self.table_widget.setGeometry(QtCore.QRect(120, 10, 770, 200))
        self.table_widget.setColumnCount(6)
        self.table_widget.setHorizontalHeaderLabels(
            ["name", "weights", "retention", "interval", "easy", "hard"]
        )

        self.text_widget = QtWidgets.QTextEdit(
            "Click 'To text' to generate the custom scheduler code from the "
            "table above OR paste the code from your custom scheduler here "
            "and click 'To table' to generate a table",
            dialog,
        )
        self.text_widget.setGeometry(QtCore.QRect(10, 220, 880, 200))
        # Set up the layout
        self.vertical_layout_widget = QtWidgets.QWidget(dialog)
        self.vertical_layout_widget.setGeometry(QtCore.QRect(10, 10, 100, 10 + 33 * 5))
        self.vertical_layout = QtWidgets.QVBoxLayout(self.vertical_layout_widget)
        self.vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout.addWidget(self.convert_to_text_button)
        self.vertical_layout.addWidget(self.convert_to_table_button)
        self.vertical_layout.addWidget(self.add_deck_to_table_button)
        self.vertical_layout.addWidget(self.remove_deck_from_table_button)
        self.vertical_layout.addWidget(self.export_to_config_button)
        self.vertical_layout.addWidget(self.import_from_config_button)
        self.vertical_layout_widget.setLayout(self.vertical_layout)

        QtCore.QMetaObject.connectSlotsByName(dialog)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = UiDialog()

    ui.setup_ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
