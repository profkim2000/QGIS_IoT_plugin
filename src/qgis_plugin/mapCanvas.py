from qgis.gui import QgsMapCanvasItem
from qgis.utils import iface
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QRectF
from qgis.core import QgsPointXY, QgsCoordinateReferenceSystem, QgsCoordinateTransform, QgsProject
from qgis.core import QgsMessageLog
import os

class CanvasImageItem(QgsMapCanvasItem):
    def __init__(self, canvas, map_point, src_epsg, target_epsg, erase_others = True):
        super(CanvasImageItem, self).__init__(canvas)
        self.canvas = canvas

        if True == erase_others :
            self.removeAll(canvas)
        
        self.map_point = self.transform(map_point, src_epsg, target_epsg)

        # 플러그인 폴더에서 이미지 가져오기
        plugin_dir = os.path.dirname(__file__)
        image_path = os.path.join(plugin_dir, "alert_fire.png")
        self.pixmap = QPixmap(image_path)
        self.setZValue(100) # 다른 레이어보다 위에 그리도록 설정


    def paint(self, painter, option, widget):
        # 지도 좌표를 화면 좌표로 변환        
        point = self.toCanvasCoordinates(self.map_point)
        
        # 이미지 크기 설정 (예: 64x64)
        w, h = 64, 64
        rect = QRectF(point.x() - w/2, point.y() - h/2, w, h)
        
        painter.drawPixmap(rect, self.pixmap, QRectF(self.pixmap.rect()))


    def boundingRect(self):
        # 화면 전체를 갱신 범위로 지정
        return QRectF(0, 0, self.canvas.width(), self.canvas.height())
    

    # 기존 거는 다 삭제
    def removeAll(self, canvas):
        items  = canvas.items()
        for item in items :
            if isinstance(item, QgsMapCanvasItem) and item != self :
                canvas.scene().removeItem(item)


    # 좌표 변환
    def transform(self, map_point, src_epsg, target_epsg):
        crs_source = QgsCoordinateReferenceSystem(f"EPSG:{src_epsg}")
        crs_target = QgsCoordinateReferenceSystem(f"EPSG:{target_epsg}")
        transformer = QgsCoordinateTransform(crs_source, crs_target, QgsProject.instance())
        point = transformer.transform(map_point)
        return point