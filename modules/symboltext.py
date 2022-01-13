from GUI.ui_interface import *


class SymbolTextWidget(QWidget):

    def __init__(self, symbolText: str, parent=None):
        from matplotlib.figure import Figure
        from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

        super().__init__(parent)

        layout = QHBoxLayout(self)

        layout.setContentsMargins(0, 0, 0, 0)

        r, g, b, a = self.palette().base().color().getRgbF()
        self.tex_figure = Figure(edgecolor=(r, g, b), facecolor=(r, g, b))
        self._canvas = FigureCanvas(self.tex_figure)
        layout.addWidget(self._canvas, alignment=Qt.AlignCenter)
        self.tex_figure.clear()

        text = self.tex_figure.suptitle(
            symbolText,
            x=0.0,
            y=1.0,

            horizontalalignment='left',
            verticalalignment='top',
            size=QFont().pointSize() * 1.8,

        )

        self._canvas.draw()
        (x0, y0), (x1, y1) = text.get_window_extent().get_points()
        w = x1 - x0
        h = y1 - y0

        self.tex_figure.set_size_inches(w, h)
        self.setFixedSize(w, h)
