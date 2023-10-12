import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QWidget, QVBoxLayout
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from random import randrange

class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        
    
    def create_sample_graph(self):
        ax = self.figure.add_subplot(111)
        x = [1, 2, 4, 7, 5]
        y = [3, 12, 9, 8, 6]
        ax.plot(x, y)
        ax.set_title("grafik ulan")
        self.canvas.draw()  

    
    def plot_sample_graph(self):
        ax = self.figure.add_subplot(111)
        x = [1, 2, 3, 4, 5]
        y = [3, 5, 2, 8, 6]
        
        # Grafiği çiz
        ax.plot(x, y, marker='o', color='b', linestyle='-', linewidth=2, markersize=8, label='Veri Noktaları')
        
        # Eksen etiketleri ve başlığı ekle
        ax.set_xlabel('X Ekseni')
        ax.set_ylabel('Y Ekseni')
        ax.set_title('Özelleştirilmiş Grafik Başlığı')
        
        # Kılavuz ekle
        ax.legend()
        
        # Eksen aralıklarını belirle
        ax.set_xlim(0, 6)
        ax.set_ylim(0, 10)
        
        # Rete ekle
        ax.grid(True, linestyle='--', alpha=0.5)
        
        # İşaretleme okları ekle
        ax.annotate('Büyük Yükseliş', xy=(3, 8), xytext=(4, 9),
                    arrowprops=dict(facecolor='red', arrowstyle='->'),
                    fontsize=10, color='red')
        
        # İşaretleme metni ekle
        ax.text(2.5, 3.5, 'Düşüş', fontsize=12, color='green')
        
        # Grafik güncelle
        self.canvas.draw()
