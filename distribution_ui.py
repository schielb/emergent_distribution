# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'distribution_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1093, 1180)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../.designer/backup/favicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.setup_frame = QtWidgets.QFrame(Dialog)
        self.setup_frame.setGeometry(QtCore.QRect(40, 30, 471, 80))
        self.setup_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setup_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setup_frame.setObjectName("setup_frame")
        self.varNum_comboBox = QtWidgets.QComboBox(self.setup_frame)
        self.varNum_comboBox.setGeometry(QtCore.QRect(160, 40, 86, 25))
        self.varNum_comboBox.setObjectName("varNum_comboBox")
        self.varNum_comboBox.addItem("")
        self.varNum_comboBox.addItem("")
        self.varNum_comboBox.addItem("")
        self.varNum_comboBox.addItem("")
        self.varNum_comboBox.addItem("")
        self.varNum_comboBox.addItem("")
        self.varNum_comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.setup_frame)
        self.label.setGeometry(QtCore.QRect(160, 20, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.setup_frame)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 51, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.setup_frame)
        self.label_3.setGeometry(QtCore.QRect(80, 20, 51, 17))
        self.label_3.setObjectName("label_3")
        self.grid_slider = QtWidgets.QSlider(self.setup_frame)
        self.grid_slider.setGeometry(QtCore.QRect(350, 40, 31, 16))
        self.grid_slider.setMaximum(1)
        self.grid_slider.setProperty("value", 1)
        self.grid_slider.setOrientation(QtCore.Qt.Horizontal)
        self.grid_slider.setObjectName("grid_slider")
        self.label_4 = QtWidgets.QLabel(self.setup_frame)
        self.label_4.setGeometry(QtCore.QRect(390, 40, 61, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.setup_frame)
        self.label_5.setGeometry(QtCore.QRect(310, 40, 41, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.setup_frame)
        self.label_6.setGeometry(QtCore.QRect(330, 20, 81, 17))
        self.label_6.setObjectName("label_6")
        self.rows_spinBox = QtWidgets.QSpinBox(self.setup_frame)
        self.rows_spinBox.setEnabled(False)
        self.rows_spinBox.setGeometry(QtCore.QRect(10, 40, 61, 30))
        self.rows_spinBox.setMinimum(1)
        self.rows_spinBox.setMaximum(60)
        self.rows_spinBox.setProperty("value", 12)
        self.rows_spinBox.setObjectName("rows_spinBox")
        self.cols_spinBox = QtWidgets.QSpinBox(self.setup_frame)
        self.cols_spinBox.setEnabled(False)
        self.cols_spinBox.setGeometry(QtCore.QRect(80, 40, 61, 30))
        self.cols_spinBox.setMinimum(1)
        self.cols_spinBox.setMaximum(100)
        self.cols_spinBox.setProperty("value", 20)
        self.cols_spinBox.setObjectName("cols_spinBox")
        self.run_frame = QtWidgets.QFrame(Dialog)
        self.run_frame.setGeometry(QtCore.QRect(510, 30, 261, 80))
        self.run_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.run_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.run_frame.setObjectName("run_frame")
        self.prev_pushButton = QtWidgets.QPushButton(self.run_frame)
        self.prev_pushButton.setEnabled(False)
        self.prev_pushButton.setGeometry(QtCore.QRect(10, 50, 89, 25))
        self.prev_pushButton.setObjectName("prev_pushButton")
        self.next_pushButton = QtWidgets.QPushButton(self.run_frame)
        self.next_pushButton.setEnabled(False)
        self.next_pushButton.setGeometry(QtCore.QRect(110, 50, 89, 25))
        self.next_pushButton.setObjectName("next_pushButton")
        self.checkBox = QtWidgets.QCheckBox(self.run_frame)
        self.checkBox.setGeometry(QtCore.QRect(10, 10, 131, 23))
        self.checkBox.setObjectName("checkBox")
        self.step_pushButton = QtWidgets.QPushButton(self.run_frame)
        self.step_pushButton.setGeometry(QtCore.QRect(130, 10, 121, 30))
        self.step_pushButton.setObjectName("step_pushButton")
        self.return_pushButton = QtWidgets.QPushButton(self.run_frame)
        self.return_pushButton.setEnabled(False)
        self.return_pushButton.setGeometry(QtCore.QRect(210, 50, 41, 25))
        self.return_pushButton.setObjectName("return_pushButton")
        self.randomVars_pushButton = QtWidgets.QPushButton(Dialog)
        self.randomVars_pushButton.setGeometry(QtCore.QRect(40, 130, 191, 25))
        self.randomVars_pushButton.setObjectName("randomVars_pushButton")
        self.map_frame = QtWidgets.QFrame(Dialog)
        self.map_frame.setGeometry(QtCore.QRect(40, 160, 1021, 621))
        self.map_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.map_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.map_frame.setObjectName("map_frame")
        self.randomOnOff_pushButton = QtWidgets.QPushButton(Dialog)
        self.randomOnOff_pushButton.setGeometry(QtCore.QRect(470, 130, 191, 25))
        self.randomOnOff_pushButton.setObjectName("randomOnOff_pushButton")
        self.clusterOnOff_pushButton = QtWidgets.QPushButton(Dialog)
        self.clusterOnOff_pushButton.setGeometry(QtCore.QRect(700, 130, 181, 25))
        self.clusterOnOff_pushButton.setObjectName("clusterOnOff_pushButton")
        self.environment_frame = QtWidgets.QFrame(Dialog)
        self.environment_frame.setGeometry(QtCore.QRect(770, 30, 291, 80))
        self.environment_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.environment_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.environment_frame.setObjectName("environment_frame")
        self.solution_comboBox = QtWidgets.QComboBox(self.environment_frame)
        self.solution_comboBox.setGeometry(QtCore.QRect(10, 40, 141, 29))
        self.solution_comboBox.setObjectName("solution_comboBox")
        self.solution_comboBox.addItem("")
        self.solution_comboBox.addItem("")
        self.solution_comboBox.addItem("")
        self.solution_comboBox.addItem("")
        self.label_7 = QtWidgets.QLabel(self.environment_frame)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 121, 21))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.envorinment_verticalSlider = QtWidgets.QSlider(self.environment_frame)
        self.envorinment_verticalSlider.setEnabled(False)
        self.envorinment_verticalSlider.setGeometry(QtCore.QRect(160, 20, 20, 41))
        self.envorinment_verticalSlider.setMaximum(1)
        self.envorinment_verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.envorinment_verticalSlider.setObjectName("envorinment_verticalSlider")
        self.label_8 = QtWidgets.QLabel(self.environment_frame)
        self.label_8.setGeometry(QtCore.QRect(160, 0, 80, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.environment_frame)
        self.label_9.setGeometry(QtCore.QRect(160, 60, 80, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.environment_frame)
        self.label_10.setGeometry(QtCore.QRect(179, 20, 111, 41))
        self.label_10.setObjectName("label_10")
        self.percentOff_spinBox = QtWidgets.QSpinBox(Dialog)
        self.percentOff_spinBox.setEnabled(False)
        self.percentOff_spinBox.setGeometry(QtCore.QRect(410, 130, 52, 25))
        self.percentOff_spinBox.setMinimum(10)
        self.percentOff_spinBox.setMaximum(90)
        self.percentOff_spinBox.setSingleStep(10)
        self.percentOff_spinBox.setObjectName("percentOff_spinBox")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(280, 130, 141, 25))
        self.label_11.setObjectName("label_11")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(40, 810, 1021, 361))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 30, 511, 141))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.var1_progressBar = QtWidgets.QProgressBar(self.frame_2)
        self.var1_progressBar.setGeometry(QtCore.QRect(30, 10, 16, 101))
        self.var1_progressBar.setProperty("value", 24)
        self.var1_progressBar.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.var1_progressBar.setTextVisible(False)
        self.var1_progressBar.setOrientation(QtCore.Qt.Vertical)
        self.var1_progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.var1_progressBar.setObjectName("var1_progressBar")
        self.var2_progressBar = QtWidgets.QProgressBar(self.frame_2)
        self.var2_progressBar.setGeometry(QtCore.QRect(80, 10, 16, 101))
        self.var2_progressBar.setProperty("value", 24)
        self.var2_progressBar.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.var2_progressBar.setTextVisible(False)
        self.var2_progressBar.setOrientation(QtCore.Qt.Vertical)
        self.var2_progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.var2_progressBar.setObjectName("var2_progressBar")
        self.var3_progressBar = QtWidgets.QProgressBar(self.frame_2)
        self.var3_progressBar.setGeometry(QtCore.QRect(130, 10, 16, 101))
        self.var3_progressBar.setProperty("value", 24)
        self.var3_progressBar.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.var3_progressBar.setTextVisible(False)
        self.var3_progressBar.setOrientation(QtCore.Qt.Vertical)
        self.var3_progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.var3_progressBar.setObjectName("var3_progressBar")
        self.var5_progressBar = QtWidgets.QProgressBar(self.frame_2)
        self.var5_progressBar.setGeometry(QtCore.QRect(230, 10, 16, 101))
        self.var5_progressBar.setProperty("value", 24)
        self.var5_progressBar.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.var5_progressBar.setTextVisible(False)
        self.var5_progressBar.setOrientation(QtCore.Qt.Vertical)
        self.var5_progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.var5_progressBar.setObjectName("var5_progressBar")
        self.var4_progressBar = QtWidgets.QProgressBar(self.frame_2)
        self.var4_progressBar.setGeometry(QtCore.QRect(180, 10, 16, 101))
        self.var4_progressBar.setProperty("value", 24)
        self.var4_progressBar.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.var4_progressBar.setTextVisible(False)
        self.var4_progressBar.setOrientation(QtCore.Qt.Vertical)
        self.var4_progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.var4_progressBar.setObjectName("var4_progressBar")
        self.var7_progressBar = QtWidgets.QProgressBar(self.frame_2)
        self.var7_progressBar.setGeometry(QtCore.QRect(330, 10, 16, 101))
        self.var7_progressBar.setProperty("value", 24)
        self.var7_progressBar.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.var7_progressBar.setTextVisible(False)
        self.var7_progressBar.setOrientation(QtCore.Qt.Vertical)
        self.var7_progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.var7_progressBar.setObjectName("var7_progressBar")
        self.var8_progressBar = QtWidgets.QProgressBar(self.frame_2)
        self.var8_progressBar.setGeometry(QtCore.QRect(380, 10, 16, 101))
        self.var8_progressBar.setProperty("value", 24)
        self.var8_progressBar.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.var8_progressBar.setTextVisible(False)
        self.var8_progressBar.setOrientation(QtCore.Qt.Vertical)
        self.var8_progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.var8_progressBar.setObjectName("var8_progressBar")
        self.var6_progressBar = QtWidgets.QProgressBar(self.frame_2)
        self.var6_progressBar.setGeometry(QtCore.QRect(280, 10, 16, 101))
        self.var6_progressBar.setProperty("value", 24)
        self.var6_progressBar.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.var6_progressBar.setTextVisible(False)
        self.var6_progressBar.setOrientation(QtCore.Qt.Vertical)
        self.var6_progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.var6_progressBar.setObjectName("var6_progressBar")
        self.varBar1_label = QtWidgets.QLabel(self.frame_2)
        self.varBar1_label.setGeometry(QtCore.QRect(10, 110, 51, 21))
        self.varBar1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.varBar1_label.setObjectName("varBar1_label")
        self.varBar2_label = QtWidgets.QLabel(self.frame_2)
        self.varBar2_label.setGeometry(QtCore.QRect(60, 110, 51, 21))
        self.varBar2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.varBar2_label.setObjectName("varBar2_label")
        self.varBar3_label = QtWidgets.QLabel(self.frame_2)
        self.varBar3_label.setGeometry(QtCore.QRect(110, 110, 51, 21))
        self.varBar3_label.setAlignment(QtCore.Qt.AlignCenter)
        self.varBar3_label.setObjectName("varBar3_label")
        self.varBar4_label = QtWidgets.QLabel(self.frame_2)
        self.varBar4_label.setGeometry(QtCore.QRect(160, 110, 51, 21))
        self.varBar4_label.setAlignment(QtCore.Qt.AlignCenter)
        self.varBar4_label.setObjectName("varBar4_label")
        self.varBar5_label = QtWidgets.QLabel(self.frame_2)
        self.varBar5_label.setGeometry(QtCore.QRect(210, 110, 51, 21))
        self.varBar5_label.setAlignment(QtCore.Qt.AlignCenter)
        self.varBar5_label.setObjectName("varBar5_label")
        self.varBar6_label = QtWidgets.QLabel(self.frame_2)
        self.varBar6_label.setGeometry(QtCore.QRect(260, 110, 51, 21))
        self.varBar6_label.setAlignment(QtCore.Qt.AlignCenter)
        self.varBar6_label.setObjectName("varBar6_label")
        self.varBar7_label = QtWidgets.QLabel(self.frame_2)
        self.varBar7_label.setGeometry(QtCore.QRect(310, 110, 51, 21))
        self.varBar7_label.setAlignment(QtCore.Qt.AlignCenter)
        self.varBar7_label.setObjectName("varBar7_label")
        self.varBar8_label = QtWidgets.QLabel(self.frame_2)
        self.varBar8_label.setGeometry(QtCore.QRect(360, 110, 51, 21))
        self.varBar8_label.setAlignment(QtCore.Qt.AlignCenter)
        self.varBar8_label.setObjectName("varBar8_label")
        self.totalGoal_line = QtWidgets.QFrame(self.frame_2)
        self.totalGoal_line.setGeometry(QtCore.QRect(20, 3, 431, 16))
        self.totalGoal_line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.totalGoal_line.setLineWidth(2)
        self.totalGoal_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.totalGoal_line.setObjectName("totalGoal_line")
        self.totalGoal_label = QtWidgets.QLabel(self.frame_2)
        self.totalGoal_label.setGeometry(QtCore.QRect(410, 10, 91, 21))
        self.totalGoal_label.setObjectName("totalGoal_label")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(10, 10, 191, 21))
        self.label_13.setObjectName("label_13")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(10, 200, 541, 151))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.collisions1_progressBar = QtWidgets.QProgressBar(self.frame_3)
        self.collisions1_progressBar.setGeometry(QtCore.QRect(30, 10, 16, 101))
        self.collisions1_progressBar.setProperty("value", 24)
        self.collisions1_progressBar.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.collisions1_progressBar.setTextVisible(False)
        self.collisions1_progressBar.setOrientation(QtCore.Qt.Vertical)
        self.collisions1_progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.collisions1_progressBar.setObjectName("collisions1_progressBar")
        self.collisions2_progressBar = QtWidgets.QProgressBar(self.frame_3)
        self.collisions2_progressBar.setGeometry(QtCore.QRect(80, 10, 16, 101))
        self.collisions2_progressBar.setProperty("value", 24)
        self.collisions2_progressBar.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.collisions2_progressBar.setTextVisible(False)
        self.collisions2_progressBar.setOrientation(QtCore.Qt.Vertical)
        self.collisions2_progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.collisions2_progressBar.setObjectName("collisions2_progressBar")
        self.collisions3_progressBar = QtWidgets.QProgressBar(self.frame_3)
        self.collisions3_progressBar.setGeometry(QtCore.QRect(130, 10, 16, 101))
        self.collisions3_progressBar.setProperty("value", 24)
        self.collisions3_progressBar.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.collisions3_progressBar.setTextVisible(False)
        self.collisions3_progressBar.setOrientation(QtCore.Qt.Vertical)
        self.collisions3_progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.collisions3_progressBar.setObjectName("collisions3_progressBar")
        self.collisions5_progressBar = QtWidgets.QProgressBar(self.frame_3)
        self.collisions5_progressBar.setGeometry(QtCore.QRect(230, 10, 16, 101))
        self.collisions5_progressBar.setProperty("value", 24)
        self.collisions5_progressBar.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.collisions5_progressBar.setTextVisible(False)
        self.collisions5_progressBar.setOrientation(QtCore.Qt.Vertical)
        self.collisions5_progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.collisions5_progressBar.setObjectName("collisions5_progressBar")
        self.collisions4_progressBar = QtWidgets.QProgressBar(self.frame_3)
        self.collisions4_progressBar.setGeometry(QtCore.QRect(180, 10, 16, 101))
        self.collisions4_progressBar.setProperty("value", 24)
        self.collisions4_progressBar.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.collisions4_progressBar.setTextVisible(False)
        self.collisions4_progressBar.setOrientation(QtCore.Qt.Vertical)
        self.collisions4_progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.collisions4_progressBar.setObjectName("collisions4_progressBar")
        self.collisions7_progressBar = QtWidgets.QProgressBar(self.frame_3)
        self.collisions7_progressBar.setGeometry(QtCore.QRect(330, 10, 16, 101))
        self.collisions7_progressBar.setProperty("value", 24)
        self.collisions7_progressBar.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.collisions7_progressBar.setTextVisible(False)
        self.collisions7_progressBar.setOrientation(QtCore.Qt.Vertical)
        self.collisions7_progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.collisions7_progressBar.setObjectName("collisions7_progressBar")
        self.collisions8_progressBar = QtWidgets.QProgressBar(self.frame_3)
        self.collisions8_progressBar.setGeometry(QtCore.QRect(380, 10, 16, 101))
        self.collisions8_progressBar.setProperty("value", 24)
        self.collisions8_progressBar.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.collisions8_progressBar.setTextVisible(False)
        self.collisions8_progressBar.setOrientation(QtCore.Qt.Vertical)
        self.collisions8_progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.collisions8_progressBar.setObjectName("collisions8_progressBar")
        self.collisions6_progressBar = QtWidgets.QProgressBar(self.frame_3)
        self.collisions6_progressBar.setGeometry(QtCore.QRect(280, 10, 16, 101))
        self.collisions6_progressBar.setProperty("value", 24)
        self.collisions6_progressBar.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.collisions6_progressBar.setTextVisible(False)
        self.collisions6_progressBar.setOrientation(QtCore.Qt.Vertical)
        self.collisions6_progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.collisions6_progressBar.setObjectName("collisions6_progressBar")
        self.collisionsBar1_label = QtWidgets.QLabel(self.frame_3)
        self.collisionsBar1_label.setGeometry(QtCore.QRect(10, 110, 51, 21))
        self.collisionsBar1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.collisionsBar1_label.setObjectName("collisionsBar1_label")
        self.collisionsBar2_label = QtWidgets.QLabel(self.frame_3)
        self.collisionsBar2_label.setGeometry(QtCore.QRect(60, 110, 51, 21))
        self.collisionsBar2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.collisionsBar2_label.setObjectName("collisionsBar2_label")
        self.collisionsBar3_label = QtWidgets.QLabel(self.frame_3)
        self.collisionsBar3_label.setGeometry(QtCore.QRect(110, 110, 51, 21))
        self.collisionsBar3_label.setAlignment(QtCore.Qt.AlignCenter)
        self.collisionsBar3_label.setObjectName("collisionsBar3_label")
        self.collisionsBar4_label = QtWidgets.QLabel(self.frame_3)
        self.collisionsBar4_label.setGeometry(QtCore.QRect(160, 110, 51, 21))
        self.collisionsBar4_label.setAlignment(QtCore.Qt.AlignCenter)
        self.collisionsBar4_label.setObjectName("collisionsBar4_label")
        self.collisionsBar5_label = QtWidgets.QLabel(self.frame_3)
        self.collisionsBar5_label.setGeometry(QtCore.QRect(210, 110, 51, 21))
        self.collisionsBar5_label.setAlignment(QtCore.Qt.AlignCenter)
        self.collisionsBar5_label.setObjectName("collisionsBar5_label")
        self.collisionsBar6_label = QtWidgets.QLabel(self.frame_3)
        self.collisionsBar6_label.setGeometry(QtCore.QRect(260, 110, 51, 21))
        self.collisionsBar6_label.setAlignment(QtCore.Qt.AlignCenter)
        self.collisionsBar6_label.setObjectName("collisionsBar6_label")
        self.collisionsBar7_label = QtWidgets.QLabel(self.frame_3)
        self.collisionsBar7_label.setGeometry(QtCore.QRect(310, 110, 51, 21))
        self.collisionsBar7_label.setAlignment(QtCore.Qt.AlignCenter)
        self.collisionsBar7_label.setObjectName("collisionsBar7_label")
        self.collisionsBar8_label = QtWidgets.QLabel(self.frame_3)
        self.collisionsBar8_label.setGeometry(QtCore.QRect(360, 110, 51, 21))
        self.collisionsBar8_label.setAlignment(QtCore.Qt.AlignCenter)
        self.collisionsBar8_label.setObjectName("collisionsBar8_label")
        self.totalGoal_label_2 = QtWidgets.QLabel(self.frame_3)
        self.totalGoal_label_2.setGeometry(QtCore.QRect(410, 10, 91, 21))
        self.totalGoal_label_2.setObjectName("totalGoal_label_2")
        self.textEdit = QtWidgets.QTextEdit(self.frame_3)
        self.textEdit.setGeometry(QtCore.QRect(410, 34, 121, 111))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(10, 180, 331, 21))
        self.label_14.setObjectName("label_14")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(40, 790, 80, 21))
        self.label_12.setObjectName("label_12")
        self.clusterType_comboBox = QtWidgets.QComboBox(Dialog)
        self.clusterType_comboBox.setEnabled(False)
        self.clusterType_comboBox.setGeometry(QtCore.QRect(890, 130, 81, 25))
        self.clusterType_comboBox.setObjectName("clusterType_comboBox")
        self.clusterType_comboBox.addItem("")
        self.clusterType_comboBox.addItem("")
        self.clusterPercent_comboBox = QtWidgets.QComboBox(Dialog)
        self.clusterPercent_comboBox.setEnabled(False)
        self.clusterPercent_comboBox.setGeometry(QtCore.QRect(980, 130, 71, 25))
        self.clusterPercent_comboBox.setObjectName("clusterPercent_comboBox")
        self.clusterPercent_comboBox.addItem("")
        self.clusterPercent_comboBox.addItem("")
        self.clusterPercent_comboBox.addItem("")
        self.clusterPercent_comboBox.addItem("")
        self.clusterPercent_comboBox.addItem("")

        self.retranslateUi(Dialog)
        self.varNum_comboBox.setCurrentIndex(0)
        self.solution_comboBox.setCurrentIndex(3)
        self.clusterPercent_comboBox.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Emergence Test"))
        self.varNum_comboBox.setCurrentText(_translate("Dialog", "2"))
        self.varNum_comboBox.setItemText(0, _translate("Dialog", "2"))
        self.varNum_comboBox.setItemText(1, _translate("Dialog", "3"))
        self.varNum_comboBox.setItemText(2, _translate("Dialog", "4"))
        self.varNum_comboBox.setItemText(3, _translate("Dialog", "5"))
        self.varNum_comboBox.setItemText(4, _translate("Dialog", "6"))
        self.varNum_comboBox.setItemText(5, _translate("Dialog", "7"))
        self.varNum_comboBox.setItemText(6, _translate("Dialog", "8"))
        self.label.setText(_translate("Dialog", "Sensors"))
        self.label_2.setText(_translate("Dialog", "Rows"))
        self.label_3.setText(_translate("Dialog", "Cols"))
        self.label_4.setText(_translate("Dialog", "Square"))
        self.label_5.setText(_translate("Dialog", "Hex"))
        self.label_6.setText(_translate("Dialog", "Grid Type"))
        self.prev_pushButton.setText(_translate("Dialog", "Previous"))
        self.next_pushButton.setText(_translate("Dialog", "Next"))
        self.checkBox.setText(_translate("Dialog", "Automatic"))
        self.step_pushButton.setText(_translate("Dialog", "Step"))
        self.return_pushButton.setText(_translate("Dialog", ">>"))
        self.randomVars_pushButton.setText(_translate("Dialog", "Randomize Vars"))
        self.randomOnOff_pushButton.setText(_translate("Dialog", "Randomize On/Off"))
        self.clusterOnOff_pushButton.setText(_translate("Dialog", "Enable Clustering"))
        self.solution_comboBox.setItemText(0, _translate("Dialog", "Random"))
        self.solution_comboBox.setItemText(1, _translate("Dialog", "Rand Loop"))
        self.solution_comboBox.setItemText(2, _translate("Dialog", "Assign Loop"))
        self.solution_comboBox.setItemText(3, _translate("Dialog", "Emergence"))
        self.label_7.setText(_translate("Dialog", "Solution"))
        self.label_8.setText(_translate("Dialog", "Dynamic"))
        self.label_9.setText(_translate("Dialog", "Static"))
        self.label_10.setText(_translate("Dialog", "Environment"))
        self.label_11.setText(_translate("Dialog", "Percentage Off:"))
        self.varBar1_label.setText(_translate("Dialog", "100%"))
        self.varBar2_label.setText(_translate("Dialog", "100%"))
        self.varBar3_label.setText(_translate("Dialog", "100%"))
        self.varBar4_label.setText(_translate("Dialog", "100%"))
        self.varBar5_label.setText(_translate("Dialog", "100%"))
        self.varBar6_label.setText(_translate("Dialog", "100%"))
        self.varBar7_label.setText(_translate("Dialog", "100%"))
        self.varBar8_label.setText(_translate("Dialog", "100%"))
        self.totalGoal_label.setText(_translate("Dialog", "Goal: 100%"))
        self.label_13.setText(_translate("Dialog", "Total of Each Variable"))
        self.collisionsBar1_label.setText(_translate("Dialog", "100%"))
        self.collisionsBar2_label.setText(_translate("Dialog", "100%"))
        self.collisionsBar3_label.setText(_translate("Dialog", "100%"))
        self.collisionsBar4_label.setText(_translate("Dialog", "100%"))
        self.collisionsBar5_label.setText(_translate("Dialog", "100%"))
        self.collisionsBar6_label.setText(_translate("Dialog", "100%"))
        self.collisionsBar7_label.setText(_translate("Dialog", "100%"))
        self.collisionsBar8_label.setText(_translate("Dialog", "100%"))
        self.totalGoal_label_2.setText(_translate("Dialog", "Goal: ~0%"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">I.e. all the reds collectively have \'x\' neighbors; what percentage of \'x\' are other reds?</p></body></html>"))
        self.label_14.setText(_translate("Dialog", "Collisions / Redundancy of Nearby Data"))
        self.label_12.setText(_translate("Dialog", "Analysis"))
        self.clusterType_comboBox.setItemText(0, _translate("Dialog", "Blank"))
        self.clusterType_comboBox.setItemText(1, _translate("Dialog", "Filled"))
        self.clusterPercent_comboBox.setItemText(0, _translate("Dialog", "10%"))
        self.clusterPercent_comboBox.setItemText(1, _translate("Dialog", "20%"))
        self.clusterPercent_comboBox.setItemText(2, _translate("Dialog", "30%"))
        self.clusterPercent_comboBox.setItemText(3, _translate("Dialog", "40%"))
        self.clusterPercent_comboBox.setItemText(4, _translate("Dialog", "50%"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
