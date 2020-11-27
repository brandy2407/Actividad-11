from PySide2.QtWidgets import QMainWindow,QFileDialog,QMessageBox,QTableWidgetItem,QGraphicsScene
from PySide2.QtCore import Slot
from PySide2.QtGui import QPen, QColor, QTransform
from ui_tarea import Ui_MainWindow
from Actividad_09.particula import Particula
from Actividad_09.administrar import Administrar
from random import randint

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

        self.ui.mostrar_tabla_pushButton_2.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_id)

        self.ui.dibujar.clicked.connect(self.dibujar)
        self.ui.limpiar.clicked.connect(self.limpiar)
        
        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

        self.ui.id.clicked.connect(self.ordenar_id)
        self.ui.velocidad.clicked.connect(self.ordenar_velocidad)
        self.ui.distancia.clicked.connect(self.ordenar_distancia)
    

    @Slot()
    def ordenar_id(self):  
        self.administrar.orden(False, "id")
    @Slot()
    def ordenar_velocidad(self):
        self.administrar.orden(False,"velocidad")
    @Slot()
    def ordenar_distancia(self):
        self.administrar.orden(True,"distancia")


    def wheelEvent(self, event):
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)
    @Slot()
    def dibujar(self):
        pen = QPen()
        pen.setWidth(2)
        
        for i in range(80):
           r = randint(0, 255)
           g =  randint(0, 255)
           b = randint(0, 255)
           color = QColor(r, g, b)
           pen.setColor(color)
           
           origen_x = randint(0, 500)
           origen_y = randint(0, 500)
           destino_x = randint(0, 500)
           destino_y = randint(0, 500)
           
           self.scene.addEllipse(origen_x, origen_y, 5, 5, pen)
           self.scene.addEllipse(destino_x, destino_y, 5, 5, pen)
           self.scene.addLine( origen_x+5, origen_y+5, destino_x, destino_y, pen)

    @Slot()
    def limpiar(self):
        self.scene.clear()

    @Slot()
    def buscar_id(self):
        id = int(self.ui.buscar_lineEdit.text())
        encontrado = False
        for particula in self.administrar:
            if id == int(particula.id):
                self.ui.tabla.clear()
                self.ui.tabla.setColumnCount(10)
                headers = ['Id', 'Origen_x' , 'Origen_y' ,'Destino_x','Destino_y','Velocidad', 'Red','Green','Blue','Distancia']
                self.ui.tabla.setHorizontalHeaderLabels(headers)
                self.ui.tabla.setRowCount(1)
                
                id_wiedget = QTableWidgetItem(str(particula.id))
                origen_x_wiedget = QTableWidgetItem(str(particula.origen_x))
                origen_y_wiedget = QTableWidgetItem(str(particula.origen_y))
                destino_x_wiedget = QTableWidgetItem(str(particula.destino_x))
                destino_y_wiedget = QTableWidgetItem(str(particula.destino_y))
                velocidad_wiedget = QTableWidgetItem(str(particula.velocidad))
                red_wiedget = QTableWidgetItem(str(particula.red))
                green_wiedget = QTableWidgetItem(str(particula.green))
                blue_wiedget = QTableWidgetItem(str(particula.blue))
                distancia_wiedget = QTableWidgetItem(str(particula.distancia))

                self.ui.tabla.setItem(0, 0, id_wiedget )
                self.ui.tabla.setItem(0, 1, origen_x_wiedget )
                self.ui.tabla.setItem(0, 2, origen_y_wiedget )
                self.ui.tabla.setItem(0, 3, destino_x_wiedget )
                self.ui.tabla.setItem(0, 4, destino_y_wiedget )
                self.ui.tabla.setItem(0, 5, velocidad_wiedget )
                self.ui.tabla.setItem(0, 6, red_wiedget )
                self.ui.tabla.setItem(0, 7, green_wiedget )
                self.ui.tabla.setItem(0, 8, blue_wiedget)
                self.ui.tabla.setItem(0, 9, distancia_wiedget)
                
                encontrado = True
                return

        if encontrado == False:
            QMessageBox.warning(
                self,
                "Atención",
                f'El Id: "{id}" no fue encontrado'
            )   

    @Slot()
    def mostrar_tabla(self):
        self.ui.tabla.setColumnCount(10)
        headers = ['Id', 'Origen_x' , 'Origen_y' ,'Destino_x','Destino_y','Velocidad', 'Red','Green','Blue','Distancia']
        self.ui.tabla.setHorizontalHeaderLabels(headers)
        self.ui.tabla.setRowCount(len(self.administrar))
        
        row = 0
        for particula in self.administrar:
            id_wiedget = QTableWidgetItem(str(particula.id))
            origen_x_wiedget = QTableWidgetItem(str(particula.origen_x))
            origen_y_wiedget = QTableWidgetItem(str(particula.origen_y))
            destino_x_wiedget = QTableWidgetItem(str(particula.destino_x))
            destino_y_wiedget = QTableWidgetItem(str(particula.destino_y))
            velocidad_wiedget = QTableWidgetItem(str(particula.velocidad))
            red_wiedget = QTableWidgetItem(str(particula.red))
            green_wiedget = QTableWidgetItem(str(particula.green))
            blue_wiedget = QTableWidgetItem(str(particula.blue))
            distancia_wiedget = QTableWidgetItem(str(particula.distancia))
            
            self.ui.tabla.setItem(row, 0, id_wiedget )
            self.ui.tabla.setItem(row, 1, origen_x_wiedget )
            self.ui.tabla.setItem(row, 2, origen_y_wiedget )
            self.ui.tabla.setItem(row, 3, destino_x_wiedget )
            self.ui.tabla.setItem(row, 4, destino_y_wiedget )
            self.ui.tabla.setItem(row, 5, velocidad_wiedget )
            self.ui.tabla.setItem(row, 6, red_wiedget )
            self.ui.tabla.setItem(row, 7, green_wiedget )
            self.ui.tabla.setItem(row, 8, blue_wiedget)
            self.ui.tabla.setItem(row, 9, distancia_wiedget)
            row += 1
        
    @Slot()
    def action_abrir_archivo(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
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
        id = int(self.ui.id_lineEdit.text())
        origen_x = int(self.ui.origenx_spinBox.value())
        origen_y = self.ui.origeny_spinBox.value()
        destino_x = self.ui.destinox_spinBox.value()
        destino_y = self.ui.destinoy_spinBox.value()
        velocidad = self.ui.spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()
        particula = Particula(id , origen_x , origen_y , destino_x , destino_y , velocidad , red , green , blue)
        self.administrar.agregar_inicio(particula)

    @Slot()
    def click_agregar(self):
        id = int(self.ui.id_lineEdit.text())
        origen_x = self.ui.origenx_spinBox.value()
        origen_y = self.ui.origeny_spinBox.value()
        destino_x = self.ui.destinox_spinBox.value()
        destino_y = self.ui.destinoy_spinBox.value()
        velocidad = self.ui.spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()
        particula = Particula(id , origen_x , origen_y , destino_x , destino_y , velocidad , red , green , blue)
        self.administrar.agregar_final(particula)
    
    @Slot()
    def click_mostrar(self):
        #self.particula.mostrar()
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.administrar))

    
    


        #print(id, origen_x, origen_y, destino_x, destino_y, red, green, blue)
        #self.ui.salida.insertPlainText(str(id) + str(origen_x )+ str(origen_y)+ str(destino_x) + str(destino_y) + str(red) + str(green) + str(blue)) 