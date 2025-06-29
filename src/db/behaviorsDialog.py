# behaviorsDialog.py

from annot.behavior import Behavior
from db.behaviorsDialog_ui import Ui_BehaviorsDialog
from qtpy.QtCore import (QAbstractItemModel, QModelIndex, QPersistentModelIndex,
    QSortFilterProxyModel, Signal, Slot)
from qtpy.Core import Qt
from qtpy.QtGui import QColor, QIntValidator
from qtpy.QtWidgets import (QColorDialog, QDialog, QHeaderView, QLineEdit,
    QMessageBox, QStyledItemDelegate, QStyleOptionViewItem, QWidget)
from os.path import expanduser, sep
from typing import List, Union

class CheckboxFilterProxyModel(QSortFilterProxyModel):
    def __init__(self):
        super().__init__()
        self.filterActive = False
        self.filterColumn = None
        self.currentSortCol = -1
        self.currentSortOrder = Qt.AscendingOrder
        self.setFilterRole(Qt.ItemIsUserCheckable)
        self.setDynamicSortFilter(False)
        self.base_model = None

    def __iter__(self):
        return CheckboxFilterProxyModelIterator(self)

    # def setSourceModel(self, model):
    #     self.base_model = model
    #     super().setSourceModel(model)
    #     if model:
    #         self.sourceModel().dataChanged.connect(self.noteDataChanged)
    #         self.sourceModel().layoutChanged.connect(self.noteLayoutChanged)

    def setFilterColumn(self, col):
        if col != self.filterColumn:
            self.filterColumn = col
            self.invalidateFilter()
            self.sort(self.currentSortCol, self.currentSortOrder)
            self.layoutChanged.emit()

    def setFilterActive(self, active):
        active = bool(active)
        if active != self.filterActive:
            self.filterActive = active
            self.invalidateFilter()
            self.sort(self.currentSortCol, self.currentSortOrder)
            self.layoutChanged.emit()

    def filterAcceptsRow(self, source_row: int, source_parent: QModelIndex) -> bool:
        if not self.filterActive or self.filterColumn == None:
            return True
        srcIdx = self.sourceModel().index(source_row, self.filterColumn)
        datum = srcIdx.data(role=Qt.CheckStateRole)
        if isinstance(datum, int):
            return bool(datum)
        elif srcIdx.data() is None:
            return False
        else:
            print(f"Unexpected data type: {type(srcIdx.data())}")
        return True

    def sort(self, col, order):
        self.currentSortCol = col
        self.currentSortOrder = order
        super().sort(col, order)

    @Slot(QModelIndex, QModelIndex)
    def noteDataChanged(self, indexStart, indexEnd):
        self.invalidateFilter()
        self.sort(self.currentSortCol, self.currentSortOrder)
        self.dataChanged.emit(self.mapFromSource(indexStart), self.mapFromSource(indexEnd))

    @Slot()
    def noteLayoutChanged(self):
        self.invalidate()
        self.sort(self.currentSortCol, self.currentSortOrder)
        self.layoutChanged.emit()

class CheckboxFilterProxyModelIterator():
    def __init__(self, model):
        self.model = model

    def __iter__(self):
        self.sourceIter = iter(self.model.sourceModel())
        self.ix = 0
        return self

    def __next__(self):
        item = next(self.sourceIter)
        while not self.model.filterAcceptsRow(self.ix, None):
            self.ix += 1
            item = next(self.sourceIter)
        self.ix += 1
        return item

class BehaviorItemDelegate(QStyledItemDelegate):
    """
    Delegate class that renders QColor objects as colors
    and instantiates a QColorDialog when the user wants to edit them.
    Most everything else is handled by the QStyledItemDelegate superclass.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

    def paint(self, painter, option, index):
        """
        Override behavior for QColor objects
        """
        if isinstance(index.data(), QColor):
            painter.fillRect(option.rect, index.data())
            return
        super().paint(painter, option, index)

    def createEditor(self, parent: QWidget, option: QStyleOptionViewItem, index: Union[QModelIndex, QPersistentModelIndex]) -> QWidget:
        if isinstance(index.data(), QColor):
            editor = QColorDialog(index.data(), parent=parent)
            return editor
        editor = super().createEditor(parent, option, index)
        if (isinstance(editor, QLineEdit) and
            index.model().headerData(index.column(), Qt.Horizontal, Qt.DisplayRole) == 'hot_key'):
            editor.setInputMask('a')    # restrict user input to no more than a single upper or lower case character
        return editor

    def setModelData(self, editor, model, index):
        if isinstance(index.data(), QColor):
            if editor.result() == QDialog.Accepted:
                model.setData(index, editor.currentColor(), role=Qt.EditRole)
            return
        super().setModelData(editor, model, index)

class BehaviorsDialog(QDialog):

    quitting = Signal()
    trialsChanged = Signal()

    def __init__(self, bento):
        super().__init__()
        self.bento = bento
        self.ui = Ui_BehaviorsDialog()
        self.ui.setupUi(self)
        bento.quitting.connect(self.quit)
        self.quitting.connect(self.bento.quit)

        self.base_model = self.createBehaviorsTableModel()
        self.proxy_model = CheckboxFilterProxyModel()
        self.proxy_model.setSourceModel(self.base_model)
        try:
            activeColumn = self.base_model.header().index("active")
        except ValueError:
            activeColumn = None
        self.proxy_model.setFilterColumn(activeColumn)

        self.ui.hideInactiveBehaviorsCheckBox.stateChanged.connect(self.updateRowVisibility)
        self.ui.addBehaviorPushButton.clicked.connect(self.addNewRow)
        self.updateRowVisibility(self.ui.hideInactiveBehaviorsCheckBox.isChecked())
        self.setBehaviorsModel(self.proxy_model)
        self.proxy_model.sort(self.base_model.header().index("name"), Qt.AscendingOrder)

    # Behaviors Data

    def setBehaviorsModel(self, model):
        oldModel = self.ui.behaviorsTableView.selectionModel()
        self.ui.behaviorsTableView.setItemDelegate(BehaviorItemDelegate())
        self.ui.behaviorsTableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.behaviorsTableView.resizeColumnsToContents()
        self.ui.behaviorsTableView.setSortingEnabled(True)
        self.ui.behaviorsTableView.setAutoScroll(False)
        self.ui.behaviorsTableView.setModel(model)
        if oldModel:
            oldModel.deleteLater()

    def createBehaviorsTableModel(self):
        model = self.bento.behaviors
        # header = model.header()
        # model.setImmutable(header.index('name'))
        return model

    @Slot(int)
    def updateRowVisibility(self, filterRows):
        self.proxy_model.setFilterActive(bool(filterRows))

    def keyPressEvent(self, event):
        """
        Handle key press events in the dialog (but not individual items)
        """
        if event.key() in (Qt.Key_Delete, Qt.Key_Backspace):
            self.deleteRows()
            event.accept()

    def addNewRow(self):
        """
        Add a row to the model initialized as "New Behavior"
        """
        # print(f"addNewRow: behaviors.len = {self.bento.behaviors.len()+1}")
        nameColumn = self.base_model.header().index("name")
        if not self.bento.behaviors.get("New Behavior"):
            if self.proxy_model.insertRows(0, 1, QModelIndex()):
                for itemRow in range(self.proxy_model.rowCount()):
                    index = self.proxy_model.index(itemRow, nameColumn, QModelIndex())
                    if self.proxy_model.data(index) == '':
                        self.proxy_model.setData(index, "New_Behavior", role=Qt.EditRole)
                        self.ui.behaviorsTableView.selectRow(itemRow)
                        self.ui.behaviorsTableView.scrollTo(index)
                        break

    def deleteRows(self):
        """
        Delete all the selected rows from the model
        """
        msgBox = QMessageBox(
            QMessageBox.Question,
            "Delete Rows",
            "This will delete the selected behaviors and any bouts using them in the current trial.  Okay to continue?",
            buttons=QMessageBox.Yes | QMessageBox.Cancel)
        result = msgBox.exec()
        if result == QMessageBox.Yes:
            selectedIndexes = self.ui.behaviorsTableView.selectedIndexes()
            self.ui.behaviorsTableView.clearSelection()
            model = self.ui.behaviorsTableView.model()
            # Remove bouts with the selected behavior(s) from the trial data
            nameColumn = self.base_model.header().index("name")
            for ix in selectedIndexes:
                name = model.data(ix.siblingAtColumn(nameColumn))
                self.bento.deleteAnnotationsByName(name)
            # Delete the behaviors
            for ix in selectedIndexes:
                model.removeRow(ix.row())

    @Slot()
    def accept(self):
        self.bento.saveBehaviors()
        # super().accept()  # don't close the window on accept

    @Slot()
    def reject(self):
        #TODO: Figure out a way to cancel updates.  Maybe an undo facility?
        pass
        # super().reject()  # don't close the window on reject (== discard, cancel)

    @Slot()
    def quit(self):
        self.done(0)

    @Slot()
    def toggleVisibility(self):
        if self.isVisible():
            self.geometry = self.saveGeometry()
        else:
            self.restoreGeometry(self.geometry)
        self.setVisible(not self.isVisible())
