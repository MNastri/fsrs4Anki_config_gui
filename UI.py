import sys

from PyQt5 import QtCore, QtGui, QtWidgets

UI_SIZE = (1350, 430)
TABLE_POS = (170, 10)
TABLE_SIZE = (UI_SIZE[0] - TABLE_POS[0] - 10, 200)
TEXTW_POS = (10, 220)
TEXTW_SIZE = (UI_SIZE[0] - TEXTW_POS[0] - 10, 200)
LAYOUT_POS = (10, 10)
LAYOUT_SIZE = (150, 10 + (23 + 10) * 5)
COLUMN_NAMES = ("name", "weights", "retention", "interval", "easy", "hard")
DEFAULT_DUMMY_DECKS = (
    (
        "global config for FSRS4Anki",
        (1.0, 1.0, 5.0, -0.5, -0.5, 0.2, 1.4, -0.12, 0.8, 2.0, -0.2, 0.2, 1.0),
        0.9,
        36500,
        1.3,
        1.2,
    ),
    (
        "ALL::Learning::English::Reading",
        (
            1.1475,
            1.401,
            5.1483,
            -1.4221,
            -1.2282,
            0.035,
            1.4668,
            -0.1286,
            0.7539,
            1.9671,
            -0.2307,
            0.32,
            0.9451,
        ),
        0.9,
        36500,
        1.3,
        1.2,
    ),
    (
        "ALL::Archive",
        (
            1.2879,
            0.5135,
            4.9532,
            -1.502,
            -1.0922,
            0.0081,
            1.3771,
            -0.0294,
            0.6718,
            1.8335,
            -0.4066,
            0.7291,
            0.5517,
        ),
        0.9,
        36500,
        1.3,
        1.2,
    ),
)


def generate_code_from(data):
    ...


class UiDialog:
    def setup_ui(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(*UI_SIZE)
        dialog.setWindowTitle("Code string generator")
        self._setup_buttons(dialog)
        self._setup_table(dialog)
        self._setup_text(dialog)
        self._setup_layout(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)
        self._add_dummy_data()

    def _setup_buttons(self, dialog):
        self.convert_to_text_button = QtWidgets.QPushButton("Convert to text", dialog)
        self.convert_to_text_button.setEnabled(True)
        self.convert_to_text_button.clicked.connect(self._convert_to_text_button)
        self.convert_to_table_button = QtWidgets.QPushButton("Convert to table", dialog)
        self.convert_to_table_button.setEnabled(False)  # todo
        self.add_deck_to_table_button = QtWidgets.QPushButton(
            "Add deck to table", dialog
        )
        self.add_deck_to_table_button.setEnabled(True)
        self.add_deck_to_table_button.clicked.connect(self._add_deck_to_table)
        self.remove_deck_from_table_button = QtWidgets.QPushButton(
            "Remove deck from table", dialog
        )
        self.remove_deck_from_table_button.setEnabled(True)
        self.remove_deck_from_table_button.clicked.connect(self._remove_deck_from_table)
        self.import_from_config_button = QtWidgets.QPushButton(
            "Import from config", dialog
        )
        self.import_from_config_button.setEnabled(False)  # todo
        self.export_to_config_button = QtWidgets.QPushButton("Export to config", dialog)
        self.export_to_config_button.setEnabled(False)  # todo

    def _setup_table(self, dialog):
        self.table_widget = QtWidgets.QTableWidget(dialog)
        self.table_widget.setGeometry(QtCore.QRect(*TABLE_POS, *TABLE_SIZE))
        self.table_widget.setColumnCount(6)
        self.table_widget.setHorizontalHeaderLabels(COLUMN_NAMES)
        self.table_widget.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents
        )

    def _setup_text(self, dialog):
        self.text_widget = QtWidgets.QTextEdit(
            "Click 'To text' to generate the custom scheduler code from the "
            "table above OR paste the code from your custom scheduler here "
            "and click 'To table' to generate a table",
            dialog,
        )
        self.text_widget.setGeometry(QtCore.QRect(*TEXTW_POS, *TEXTW_SIZE))

    def _setup_layout(self, dialog):
        self.vertical_layout_widget = QtWidgets.QWidget(dialog)
        self.vertical_layout_widget.setGeometry(QtCore.QRect(*LAYOUT_POS, *LAYOUT_SIZE))
        self.vertical_layout = QtWidgets.QVBoxLayout(self.vertical_layout_widget)
        self.vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout.addWidget(self.convert_to_text_button)
        self.vertical_layout.addWidget(self.convert_to_table_button)
        self.vertical_layout.addWidget(self.add_deck_to_table_button)
        self.vertical_layout.addWidget(self.remove_deck_from_table_button)
        self.vertical_layout.addWidget(self.export_to_config_button)
        self.vertical_layout.addWidget(self.import_from_config_button)
        self.vertical_layout_widget.setLayout(self.vertical_layout)

    def _add_deck_to_table(self):
        row_count = self.table_widget.rowCount()
        self.table_widget.insertRow(row_count)
        for column, data in enumerate(DEFAULT_DUMMY_DECKS[0]):
            self.table_widget.setItem(
                row_count, column, QtWidgets.QTableWidgetItem(str(data))
            )

    def _remove_deck_from_table(self):
        if not self.table_widget.selectionModel().hasSelection():
            return
        selected_items = self.table_widget.selectedItems()
        if isinstance(selected_items, list):
            selected_rows = set(item.row() for item in selected_items)
        else:
            selected_rows = set(selected_items.row())
        for row in reversed(sorted(selected_rows)):
            self.table_widget.removeRow(row)
        return

    def _get_data_from_table(self):
        row_count = self.table_widget.rowCount()
        column_count = len(COLUMN_NAMES)
        data = []
        for row in range(row_count):
            data += (
                [
                    self.table_widget.item(row, column).text()
                    for column in range(column_count)
                ],
            )
        return data

    def _convert_to_text_button(self):
        data = self._get_data_from_table()
        text = generate_code_from(data)
        self.text_widget.setText(text)

    def _add_dummy_data(self):
        for row, deck in enumerate(DEFAULT_DUMMY_DECKS):
            number_of_rows = self.table_widget.rowCount()
            self.table_widget.insertRow(number_of_rows)
            for column, data in enumerate(deck):
                self.table_widget.setItem(
                    row, column, QtWidgets.QTableWidgetItem(str(data))
                )
        # self.table_widget.selectRow(0)
        self.table_widget.resizeColumnsToContents()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = UiDialog()
    ui.setup_ui(main_window)
    main_window.show()
    sys.exit(app.exec_())
