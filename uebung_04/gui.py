import sys
from PyQt5.QtWidgets import *

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.createLayout()
        self.createConnects()

    def createLayout(self):
        #* Fenstertitel / Layout
        self.setWindowTitle("Aufgabe GUI")
        layout = QFormLayout()
        self.setMinimumSize(500,250)

        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
 
        save = QAction("Save", self)
        save.triggered.connect(self.menu_save)
        quit = QAction("Quit", self)
        quit.triggered.connect(self.menu_quit)
 
        filemenu.addAction(save)
        filemenu.addAction(quit)

        #* Zentrierung der Widgets
        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)

        #* Widgets erstellen
        #Labels
        labelVorname = QLabel("Vorname:")
        labelName = QLabel("Name:")
        labelGeburstag = QLabel("Geburtstag:")
        labelAdresse = QLabel("Adresse:")
        labelPostLeitzahl = QLabel("Postleitzahl:")
        labelOrt = QLabel("Ort:")
        labelLand = QLabel("Land:")

        #Edits
        editVorname = QLineEdit()
        editName = QLineEdit()
        editGeburstag = QDateEdit()
        editAdresse = QLineEdit()
        editPostLeitzahl = QLineEdit()
        editOrt = QLineEdit()
        editLand = QComboBox()

        #Item in ComboBox
        editLand.addItem("Deutschland")
        editLand.addItem("Schweiz")
        editLand.addItem("Österreich")
        editLand.addItem("Frankreich")
        editLand.addItem("Italien")
        editLand.addItem("andere")

        #Button
        buttonSave = QPushButton("Save")
        buttonSave.clicked.connect(self.menu_save)

        #* Layout füllen
        layout.addRow(labelVorname, editVorname)
        layout.addRow(labelName, editName)
        layout.addRow(labelGeburstag, editGeburstag)
        layout.addRow(labelAdresse, editAdresse)
        layout.addRow(labelPostLeitzahl, editPostLeitzahl)
        layout.addRow(labelOrt, editOrt)
        layout.addRow(labelLand, editLand)
        layout.addRow(buttonSave)

        #* Fenster anzeigen
        self.show()

    
    def menu_save(self):
        widgets = self.centralWidget().layout()
        data = {
            "Vorname": widgets.itemAt(1).widget().text(),
            "Name": widgets.itemAt(3).widget().text(),
            "Geburtstag": widgets.itemAt(5).widget().date().toString("dd MM yyyy"),
            "Adresse": widgets.itemAt(7).widget().text(),
            "Postleitzahl": widgets.itemAt(9).widget().text(),
            "Ort": widgets.itemAt(11).widget().text(),
            "Land": widgets.itemAt(13).widget().currentText()
        }

        with open("./test.txt", "w") as file:
            for key, value in data.items():
                file.write(f"{key}: {value}\n")

        QMessageBox.information(self, "Saved", "Data has been saved to output.txt")
 
    def menu_quit(self):
        self.close()

    def createConnects(self):
        pass




def main():
    app = QApplication(sys.argv)  
    mainwindow = Fenster()       
    mainwindow.raise_()           
    app.exec_()                   

if __name__ == '__main__':
    main()