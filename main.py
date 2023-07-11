# © 2023 Karan Mirajkar - Some Rights Reserved

# This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 License.
# To view a copy of this license, visit https://creativecommons.org/licenses/.

# You are free to:
#   - Share: Copy and redistribute the material in any medium or format
#   - Adapt: Remix, transform, and build upon the material

# Under the following terms:
#   - Attribution: You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
#   - ShareAlike: If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.




from typing import Optional
from PySide6 import QtWidgets
import os
import PySide6.QtCore
import PySide6.QtWidgets
import cv2

import cv2_converter
import main_seq_conv_ui
import progress_ui


class main_win_conveter(main_seq_conv_ui.Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self):
        super(main_win_conveter,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sequence Converter")
        self.save_reset_buttonBox.accepted.connect(self.convert)
        #self.save_reset_buttonBox.accepted.connect(self.progress)
        self.save_reset_buttonBox.rejected.connect(self.closeprogram)
        self.save_reset_buttonBox.button(QtWidgets.QDialogButtonBox.Reset).clicked.connect(self.resetui)
        self.seq_dir_TB.clicked.connect(self.get_seqpath)
        self.out_dir_TB.clicked.connect(self.get_outpath)

    def get_seqpath(self):
        seq_path = QtWidgets.QFileDialog.getExistingDirectory(self,'Select Folder')
        if seq_path:
            self.seq_dir_LE.setText(seq_path)
        return seq_path

    def get_outpath(self):
        out_path,ext = QtWidgets.QFileDialog.getSaveFileName(self,'Select File')
        if out_path:
            self.out_dir_LE.setText(out_path)
        return out_path


    def convert(self):
        out_path = self.out_dir_LE.text()
        seq_path = self.seq_dir_LE.text()

        fps = self.fps_spinbox.value()
        res_x = self.res_spinBox_width.value() 
        res_y = self.res_spinBox_height.value()

        #set resolution
        def_res = self.def_res_CB.isChecked()
        if def_res is True:
            
            seq_path += '/'
            img_path = os.path.join(seq_path,os.listdir(seq_path)[0])
            img_path = img_path.replace('\\','/')
            # print(img_path)
            res = list(cv2.imread(img_path).shape)
            del res[2]
            res.reverse()
            # print(res)
        else:
            res = [res_x,res_y]

        # #converting to .mp4 here
        # pr = cv2_converter.seq_converter(seq_path,out_path,fps,res)

        cv2_converter.seq_converter(seq_path,out_path,fps,res)

        os.system(out_path)

        # #setting up progress bar
        # prog = progressdialog()
        # # prog.progressBar.setValue(pr)
        # prog.exec()

        # prog.res_out_LB.setText(res)
        # prog.fps_out_LB.setText(str(fps))
        # prog.path_out_LB.setText(out_path)

        print(seq_path,out_path,fps,res,def_res)

    def resetui(self):
        self.out_dir_LE.setText("")
        self.seq_dir_LE.setText("")

        self.fps_spinbox.setValue(0)
        self.res_spinBox_width.setValue(0) 
        self.res_spinBox_height.setValue(0)
        self.def_res_CB.setChecked(True)

    def closeprogram(self):
        print('close')
        QtWidgets.QApplication.exit()

    def progress(self):
        
        prog = progressdialog()
        prog.exec()


#Add Progress UI
class progressdialog(progress_ui.Ui_Dialog,QtWidgets.QDialog):
    def __init__(self):
        super(progressdialog,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Progress")
        #main_win_conveter.convert.
        
        #self.progress_parm()

    def getres(self):
        seq_path = main_win_conveter.seq_dir_LE.text()
        seq_path += '/'
        img_path = os.path.join(seq_path,os.listdir(seq_path)[0])
        img_path = img_path.replace('\\','/')
        print(img_path)
        res = list(cv2.imread(img_path).shape)
        del res[2]
        res.reverse()
        self.res_out_LB.setText(res)
        print(res)


    # def progress_parm(self):
    #     self.progressBar.setValue(5)

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    applaunch = main_win_conveter()
    applaunch.show() 
    app.exec()