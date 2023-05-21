from typing import Optional
from PySide6 import QtWidgets
import os
import PySide6.QtCore
import PySide6.QtWidgets
import cv2

import main_seq_conv_ui


class main_win_conveter(main_seq_conv_ui.Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self):
        super(main_win_conveter,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sequence Converter")
        self.save_reset_buttonBox.accepted.connect(self.getinputs)
        self.seq_dir_TB.clicked.connect(self.get_seqpath)
        self.out_dir_TB.clicked.connect(self.get_outpath)

    def get_seqpath(self):
        seq_path = QtWidgets.QFileDialog.getExistingDirectory(self,'Select Folder')
        if seq_path:
            self.seq_dir_LE.setText(seq_path)
        
        return seq_path

    def get_outpath(self):
        out_path,ext = QtWidgets.QFileDialog.getOpenFileName(self,'Select Folder')
        if out_path:
            self.out_dir_LE.setText(out_path)
        
        return out_path


    def getinputs(self):
        out_path = self.out_dir_LE.text()
        seq_path = self.seq_dir_LE.text()

        fps = self.fps_spinbox.value()
        res_x = self.res_spinBox_width.value() 
        res_y = self.res_spinBox_height.value()
        def_res = self.def_res_CB.isChecked()

        print(seq_path,out_path,fps,res_x,res_y,def_res)

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    applaunch = main_win_conveter()
    applaunch.show()
    app.exec()