"""
gatefilter.py

Driver function that creates ARTView display.
"""
import os
from PyQt4 import QtGui, QtCore
import sys

from ..core import Variable
from ..components import RadarDisplay, Menu
from ._common import _add_all_advanced_tools, _parse_dir, _parse_field
from ..plugins import GateFilter

def run(DirIn=None, filename=None, field=None):
    """
    artview execution for filtering gates radar display
    """
    DirIn = _parse_dir(DirIn)

    app = QtGui.QApplication(sys.argv)

    # start Menu and initiate Vradar
    menu = Menu(DirIn, filename, mode="Radar", name="Menu")
    Vradar = menu.Vradar

    field = _parse_field(Vradar.value, field)

    # start Displays
    Vtilt = Variable(0)
    plot1 = RadarDisplay(Vradar, Variable(field), Vtilt, name="Display",
                         parent=menu)
    filt = GateFilter(Vradar=Vradar, Vgatefilter=plot1.Vgatefilter,
                 name="GateFilter", parent=None)
    plot1._gatefilter_toggle_on()
    
    menu.addLayoutWidget(filt)

    # add grafical starts
    _add_all_advanced_tools(menu)

    menu.setGeometry(0, 0, 500, 300)

    # start program
    app.exec_()