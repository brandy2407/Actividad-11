from PySide2.QtWidgets import QMainWindow,QFileDialog,QMessageBox
from PySide2.QtCore import Slot
from ui_tarea import Ui_MainWindow
from Actividad_09.particula import Particula
from Actividad_09.administrar import Administrar

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.administrar = Administrar()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.agregarfinal_pushButton.clicked.connect(self.click_agregar)
        self.ui.agregarinicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)
        self.ui.actionAbir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)

    @Slot()
    def action_abrir_archivo(self):
        ubicacion =  QFileDialog.getOpenSaveFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        print(ubicacion)
        if self.administrar.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se abrio el archivo" + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error" ,
                "Error al abrir el archivo" + ubicacion
            )

    @Slot()
    def action_guardar_archivo(self):
        ubicacion = QFileDialog.getSaveFileName( 
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        print(ubicacion)
        if self.administrar.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se pudo crear el archivo" + ubicacion 
            )
        else: 
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo crear el archivo " + ubicacion
            )
    

    @Slot()
    def click_agregar_inicio(self):
        id = self.ui.id_lineEdit.text()
        origen_x = self.ui.origenx_spinBox.value()
        origen_y = self.ui.origeny_spinBox.value()
        destino_x = self.ui.destinox_spinBox.value()
        destino_y = self.ui.destinoy_spinBox.value()
        velocidad = self.ui.spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()
        distancia = self.ui.distancia_doubleSpinBox
        particula = Particula(id , origen_x , origen_y , destino_x , destino_y , velocidad , red , green , blue , distancia)
        self.administrar.agregar_inicio(particula)

    @Slot()
    def click_agregar(self):
        id = self.ui.id_lineEdit.text()
        origen_x = self.ui.origenx_spinBox.value()
        origen_y = self.ui.origeny_spinBox.value()
        destino_x = self.ui.destinox_spinBox.value()
        destino_y = self.ui.destinoy_spinBox.value()
        velocidad = self.ui.spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()
        distancia = self.ui.distancia_doubleSpinBox
        particula = Particula(id , origen_x , origen_y , destino_x , destino_y , velocidad , red , green , blue , distancia )
        self.administrar.agregar_final(particula)
    
    @Slot()
    def click_mostrar(self):
        #self.particula.mostrar()
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.administrar))

    
    


        #print(id, origen_x, origen_y, destino_x, destino_y, red, green, blue)
        #self.ui.salida.insertPlainText(str(id) + str(origen_x )+ str(origen_y)+ str(destino_x) + str(destino_y) + str(red) + str(green) + str(blue)) 