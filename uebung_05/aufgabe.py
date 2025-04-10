from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate
import sys
import webbrowser


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

        load = QAction("Load", self)
        load.triggered.connect(self.load)
        save = QAction("Save", self)
        save.triggered.connect(self.save)
        quit = QAction("Quit", self)
        quit.triggered.connect(self.menu_quit)
 
        filemenu.addAction(save)
        filemenu.addAction(quit)

        #* Zentrierung der widgets
        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)

        #* widgets erstellen
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
        buttonKarte = QPushButton("Auf Karte")
        buttonKarte.clicked.connect(self.auf_karte)
        buttonLoad = QPushButton("Load")
        buttonLoad.clicked.connect(self.load)
        buttonSave = QPushButton("Save")
        buttonSave.clicked.connect(self.save)

        #* Layout füllen
        layout.addRow(labelVorname, editVorname)
        layout.addRow(labelName, editName)
        layout.addRow(labelGeburstag, editGeburstag)
        layout.addRow(labelAdresse, editAdresse)
        layout.addRow(labelPostLeitzahl, editPostLeitzahl)
        layout.addRow(labelOrt, editOrt)
        layout.addRow(labelLand, editLand)
        layout.addRow(buttonKarte)
        layout.addRow(buttonLoad)
        layout.addRow(buttonSave)

        #* Fenster anzeigen
        self.show()


    def auf_karte(self):
        widgets = self.centralWidget().layout()
        data = [
            widgets.itemAt(7).widget().text(), #Adresse [0]
            widgets.itemAt(9).widget().text(), #Postleitzahl [1]
            widgets.itemAt(11).widget().text(), #Ort [2]
            widgets.itemAt(13).widget().currentText() #Land [3]
            ]

        link = f"https://www.google.com/maps/place/{data[0]}+{data[1]}+{data[2]}"

        webbrowser.open(link) #Link Opener

    def load(self):
        openFile = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "", "", "Text file (*.txt)", options=openFile)
        data = {}
    
        if not fileName:
            return

        with open(fileName, "r") as file:
            for line in file:
                key, value = line.strip().split(": ")
                data[key] = value

        widgets = self.centralWidget().layout()
        widgets.itemAt(1).widget().setText(data["Vorname"])
        widgets.itemAt(3).widget().setText(data["Name"])
        widgets.itemAt(5).widget().setDate(QDate.fromString(data["Geburtstag"], "dd MM yyyy"))
        widgets.itemAt(7).widget().setText(data["Adresse"])
        widgets.itemAt(9).widget().setText(data["Postleitzahl"])
        widgets.itemAt(11).widget().setText(data["Ort"])
        index = widgets.itemAt(13).widget().findText(data["Land"])
        widgets.itemAt(13).widget().setCurrentIndex(index)

        QMessageBox.information(self, "Loaded", f"Data has been loaded from {fileName}")


    def save(self):
        saveFile = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()", "","Text (*.txt)", options=saveFile)

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

        with open(fileName, "w") as file:
            for key, value in data.items():
                file.write(f"{key}: {value}\n")

        QMessageBox.information(self, "Saved", f"Data has been saved to {fileName}")
     
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