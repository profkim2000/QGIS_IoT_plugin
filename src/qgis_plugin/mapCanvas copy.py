from qgis.gui import QgsMapCanvasItem
from qgis.core import QgsPointXY, QgsMessageLog, Qgis
from qgis.PyQt.QtGui import QPixmap
from qgis.PyQt.QtCore import QRectF
import os

from qgis.core import QgsCoordinateReferenceSystem, QgsCoordinateTransform, QgsProject

class MapCanvas(QgsMapCanvasItem):
    def __init__(self, canvas):
        super().__init__(canvas)
        self.setItemScenePos = self.setPos
        self.pixmap = None
        self.canvas2 = canvas

        plugin_dir = os.path.dirname(__file__)
        image_path = os.path.join(plugin_dir, "alert_fire.png")
        self.pixmap_alert_fire = QPixmap(image_path)
        self.pixmap = QPixmap(image_path)
        

    def paint(self, painter, option, widget):
        #if None != self.pixmap:
            _width = self.pixmap.width()
            _height = self.pixmap.height()
            #gsMessageLog.logMessage(f"pixmap.width = {_width}, pixmap.height = {_height}", "IOT_DT_Module", Qgis.Info)
            painter.drawPixmap(-self.pixmap.width() // 2, 
                               -self.pixmap.height() // 2, 
                               self.pixmap)

    def boundingRect(self):        
        # 이미지가 그려질 영역 정의
        #if None != self.pixmap:
            return QRectF(-self.pixmap.width() // 2, 
                          -self.pixmap.height() // 2, 
                          self.pixmap.width(), 
                          self.pixmap.height())
        
    
    
    # 캔버스에 그림을 그린다. 지금은 그리려는 image_type에 상관없이 alert_fire만 그린다.
    def draw(self, lon, lat, image_type) :        
        QgsMessageLog.logMessage(f"draw lot={lon}, lat={lat}", "IOT_DT_Module", Qgis.Info)
        
        # 좌표변환(gps 4326을 osm 3857로)
        #src_crs = QgsCoordinateReferenceSystem("EPSG:4326")
        #dest_crs = self.canvas2.mapSettings().destinationCrs()

        #QgsMessageLog.logMessage(f"draw dest_crs={dest_crs}", "IOT_DT_Module", Qgis.Info)

        #transform = QgsCoordinateTransform(src_crs, dest_crs, QgsProject.instance())

        #point_4326 = QgsPointXY(lon, lat)
        #point_transformed = transform.transform(point_4326)


        #map_point = QgsPointXY(lon, lat)
        #screen_point = self.canvas().getCoordinateTransform().transform(map_point)
        #screen_point = self.toCanvasCoordinates(map_point)
        #self.setPos(screen_point.x(), screen_point.y())
                
        #QgsMessageLog.logMessage(f"draw point_transformed={point_transformed.x()}, point_transformed.y()={point_transformed.y()}", "IOT_DT_Module", Qgis.Info)

        #self.setPos(point_transformed.x(), point_transformed.y())
        #self.setPos(14000000.0, 4300000.0)

        #QgsMessageLog.logMessage("draw 3", "IOT_DT_Module", Qgis.Info)


        #self.pixmap = self.pixmap_alert_fire
        
        #self.update()

        #QgsMessageLog.logMessage("draw 9", "IOT_DT_Module", Qgis.Info)