# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Heylon\Documents\RIFEstuff\RIFE-Colab\main_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(948, 655)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.inputLabel = QtWidgets.QLabel(self.centralwidget)
        self.inputLabel.setObjectName("inputLabel")
        self.gridLayout.addWidget(self.inputLabel, 0, 1, 1, 1)
        self.inputFilePathText = QtWidgets.QLineEdit(self.centralwidget)
        self.inputFilePathText.setObjectName("inputFilePathText")
        self.gridLayout.addWidget(self.inputFilePathText, 0, 2, 1, 1)
        self.browseInputButton = QtWidgets.QPushButton(self.centralwidget)
        self.browseInputButton.setObjectName("browseInputButton")
        self.gridLayout.addWidget(self.browseInputButton, 0, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_4.setHorizontalSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 0, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 1, 0, 1, 1)
        self.clearpngsCheck = QtWidgets.QCheckBox(self.groupBox_3)
        self.clearpngsCheck.setChecked(True)
        self.clearpngsCheck.setObjectName("clearpngsCheck")
        self.gridLayout_4.addWidget(self.clearpngsCheck, 2, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setObjectName("label_14")
        self.gridLayout_4.addWidget(self.label_14, 2, 0, 1, 1)
        self.nonlocalpngsCheck = QtWidgets.QCheckBox(self.groupBox_3)
        self.nonlocalpngsCheck.setChecked(True)
        self.nonlocalpngsCheck.setObjectName("nonlocalpngsCheck")
        self.gridLayout_4.addWidget(self.nonlocalpngsCheck, 1, 1, 1, 1)
        self.mpdecimateText = QtWidgets.QLineEdit(self.groupBox_3)
        self.mpdecimateText.setObjectName("mpdecimateText")
        self.gridLayout_4.addWidget(self.mpdecimateText, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setMinimumSize(QtCore.QSize(0, 0))
        self.tab_2.setBaseSize(QtCore.QSize(0, 0))
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_17 = QtWidgets.QLabel(self.groupBox_4)
        self.label_17.setObjectName("label_17")
        self.gridLayout_5.addWidget(self.label_17, 0, 1, 1, 1)
        self.VideostatsInputFPStext = QtWidgets.QLineEdit(self.groupBox_4)
        self.VideostatsInputFPStext.setEnabled(False)
        self.VideostatsInputFPStext.setObjectName("VideostatsInputFPStext")
        self.gridLayout_5.addWidget(self.VideostatsInputFPStext, 0, 2, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox_4)
        self.label_16.setObjectName("label_16")
        self.gridLayout_5.addWidget(self.label_16, 0, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.groupBox_4)
        self.label_18.setObjectName("label_18")
        self.gridLayout_5.addWidget(self.label_18, 0, 3, 1, 1)
        self.VideostatsOutputFPStext = QtWidgets.QLineEdit(self.groupBox_4)
        self.VideostatsOutputFPStext.setEnabled(False)
        self.VideostatsOutputFPStext.setObjectName("VideostatsOutputFPStext")
        self.gridLayout_5.addWidget(self.VideostatsOutputFPStext, 0, 4, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_4)
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.scenechangeSensitivityNumber = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.scenechangeSensitivityNumber.setMaximum(1.0)
        self.scenechangeSensitivityNumber.setSingleStep(0.01)
        self.scenechangeSensitivityNumber.setProperty("value", 0.2)
        self.scenechangeSensitivityNumber.setObjectName("scenechangeSensitivityNumber")
        self.gridLayout_2.addWidget(self.scenechangeSensitivityNumber, 4, 1, 1, 1)
        self.batchthreadsNumber = QtWidgets.QSpinBox(self.groupBox)
        self.batchthreadsNumber.setMinimum(1)
        self.batchthreadsNumber.setMaximum(999999999)
        self.batchthreadsNumber.setProperty("value", 2)
        self.batchthreadsNumber.setObjectName("batchthreadsNumber")
        self.gridLayout_2.addWidget(self.batchthreadsNumber, 6, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 5, 0, 1, 1)
        self.modeSelect = QtWidgets.QComboBox(self.groupBox)
        self.modeSelect.setObjectName("modeSelect")
        self.modeSelect.addItem("")
        self.modeSelect.addItem("")
        self.modeSelect.addItem("")
        self.gridLayout_2.addWidget(self.modeSelect, 3, 1, 1, 1)
        self.useAccurateFPSCheckbox = QtWidgets.QCheckBox(self.groupBox)
        self.useAccurateFPSCheckbox.setChecked(True)
        self.useAccurateFPSCheckbox.setObjectName("useAccurateFPSCheckbox")
        self.gridLayout_2.addWidget(self.useAccurateFPSCheckbox, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 6, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.interpolationFactorSelect = QtWidgets.QComboBox(self.groupBox)
        self.interpolationFactorSelect.setEditable(True)
        self.interpolationFactorSelect.setObjectName("interpolationFactorSelect")
        self.interpolationFactorSelect.addItem("")
        self.interpolationFactorSelect.addItem("")
        self.interpolationFactorSelect.addItem("")
        self.interpolationFactorSelect.addItem("")
        self.interpolationFactorSelect.addItem("")
        self.interpolationFactorSelect.addItem("")
        self.interpolationFactorSelect.addItem("")
        self.interpolationFactorSelect.addItem("")
        self.interpolationFactorSelect.addItem("")
        self.interpolationFactorSelect.addItem("")
        self.gridLayout_2.addWidget(self.interpolationFactorSelect, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.gpuidsSelect = QtWidgets.QComboBox(self.groupBox)
        self.gpuidsSelect.setEditable(True)
        self.gpuidsSelect.setObjectName("gpuidsSelect")
        self.gpuidsSelect.addItem("")
        self.gpuidsSelect.addItem("")
        self.gpuidsSelect.addItem("")
        self.gridLayout_2.addWidget(self.gpuidsSelect, 5, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 1, 0, 1, 1)
        self.accountForDuplicateFramesCheckbox = QtWidgets.QCheckBox(self.groupBox)
        self.accountForDuplicateFramesCheckbox.setChecked(True)
        self.accountForDuplicateFramesCheckbox.setObjectName("accountForDuplicateFramesCheckbox")
        self.gridLayout_2.addWidget(self.accountForDuplicateFramesCheckbox, 1, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 3, 0, 1, 1)
        self.autoencodeBlocksizeNumber = QtWidgets.QSpinBox(self.groupBox_2)
        self.autoencodeBlocksizeNumber.setMinimum(1)
        self.autoencodeBlocksizeNumber.setMaximum(999999999)
        self.autoencodeBlocksizeNumber.setProperty("value", 3000)
        self.autoencodeBlocksizeNumber.setObjectName("autoencodeBlocksizeNumber")
        self.gridLayout_3.addWidget(self.autoencodeBlocksizeNumber, 4, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 2, 0, 1, 1)
        self.nvencCheck = QtWidgets.QCheckBox(self.groupBox_2)
        self.nvencCheck.setChecked(True)
        self.nvencCheck.setObjectName("nvencCheck")
        self.gridLayout_3.addWidget(self.nvencCheck, 1, 1, 1, 1)
        self.crfoutNumber = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.crfoutNumber.setMinimum(-10.0)
        self.crfoutNumber.setMaximum(100.0)
        self.crfoutNumber.setSingleStep(0.25)
        self.crfoutNumber.setProperty("value", 20.0)
        self.crfoutNumber.setObjectName("crfoutNumber")
        self.gridLayout_3.addWidget(self.crfoutNumber, 2, 1, 1, 1)
        self.autoencodeCheck = QtWidgets.QCheckBox(self.groupBox_2)
        self.autoencodeCheck.setObjectName("autoencodeCheck")
        self.gridLayout_3.addWidget(self.autoencodeCheck, 3, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 4, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 1, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 0, 0, 1, 1)
        self.loopoutputCheck = QtWidgets.QCheckBox(self.groupBox_2)
        self.loopoutputCheck.setObjectName("loopoutputCheck")
        self.gridLayout_3.addWidget(self.loopoutputCheck, 0, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_19 = QtWidgets.QLabel(self.groupBox_5)
        self.label_19.setObjectName("label_19")
        self.gridLayout_6.addWidget(self.label_19, 1, 0, 1, 1)
        self.targetFPSnumber = QtWidgets.QDoubleSpinBox(self.groupBox_5)
        self.targetFPSnumber.setDecimals(3)
        self.targetFPSnumber.setMaximum(9999999999999.0)
        self.targetFPSnumber.setSingleStep(0.001)
        self.targetFPSnumber.setProperty("value", 59.0)
        self.targetFPSnumber.setObjectName("targetFPSnumber")
        self.gridLayout_6.addWidget(self.targetFPSnumber, 1, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox_5)
        self.label_20.setObjectName("label_20")
        self.gridLayout_6.addWidget(self.label_20, 0, 0, 1, 2)
        self.verticalLayout_5.addWidget(self.groupBox_5)
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.interpolationProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.interpolationProgressBar.setProperty("value", 0)
        self.interpolationProgressBar.setObjectName("interpolationProgressBar")
        self.verticalLayout.addWidget(self.interpolationProgressBar)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.extractFramesButton = QtWidgets.QPushButton(self.centralwidget)
        self.extractFramesButton.setObjectName("extractFramesButton")
        self.horizontalLayout_3.addWidget(self.extractFramesButton)
        self.interpolateFramesButton = QtWidgets.QPushButton(self.centralwidget)
        self.interpolateFramesButton.setObjectName("interpolateFramesButton")
        self.horizontalLayout_3.addWidget(self.interpolateFramesButton)
        self.encodeOutputButton = QtWidgets.QPushButton(self.centralwidget)
        self.encodeOutputButton.setObjectName("encodeOutputButton")
        self.horizontalLayout_3.addWidget(self.encodeOutputButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.runAllStepsButton = QtWidgets.QPushButton(self.centralwidget)
        self.runAllStepsButton.setObjectName("runAllStepsButton")
        self.horizontalLayout_2.addWidget(self.runAllStepsButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 948, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RIFE Colab GUI"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>RIFE Colab GUI 0.15</p></body></html>"))
        self.inputLabel.setText(_translate("MainWindow", "Input file"))
        self.browseInputButton.setText(_translate("MainWindow", "Browse"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Frame extraction options"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><span style=\" font-weight:600;\">Mpdecimate (Mode 3/4) -</span>\n"
"<br>Duplicate frame removal strength (high,low,frac)</body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Non local PNGs - </span>(Store PNGs in a temp folder)</p></body></html>"))
        self.clearpngsCheck.setText(_translate("MainWindow", "Enable"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Clear PNGs after interpolation finished -</span></p></body></html>"))
        self.nonlocalpngsCheck.setText(_translate("MainWindow", "Enable"))
        self.mpdecimateText.setText(_translate("MainWindow", "64*12,64*8,0.33"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Extraction"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Input video stats"))
        self.label_17.setText(_translate("MainWindow", "Input FPS"))
        self.label_16.setText(_translate("MainWindow", "Video FPS"))
        self.label_18.setText(_translate("MainWindow", "Output FPS"))
        self.groupBox.setTitle(_translate("MainWindow", "Interpolation options"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Frame handling mode -</span></p>\n"
"<p>Mode 1 - no duplicate frame handling (Fastest)<br>\n"
"Mode 3 - duplicate frame handling with adaptive interpolation factor (Slowest, works best)<br>\n"
"Mode 4 - duplicate frame handling with fixed interpolation factor (Slow, works well)\n"
"</body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Scene change sensitivity -</span></p><p>Lower is more sensitivity<br/>Higher is less sensitivity</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">GPU ID\'s -</span></p><p>Separate ID numbers using commas for multi-gpu processing</p></body></html>"))
        self.modeSelect.setCurrentText(_translate("MainWindow", "1"))
        self.modeSelect.setItemText(0, _translate("MainWindow", "1"))
        self.modeSelect.setItemText(1, _translate("MainWindow", "3"))
        self.modeSelect.setItemText(2, _translate("MainWindow", "4"))
        self.useAccurateFPSCheckbox.setText(_translate("MainWindow", "Enable"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Batch processing threads -</span></p><p>If not seeing 100% CUDA use on GPU<br/>Increase batch threads<br/>If using too much VRAM<br/>Decrease batch threads</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<b>Get FPS from FFmpeg TBC -</b>"))
        self.interpolationFactorSelect.setItemText(0, _translate("MainWindow", "2"))
        self.interpolationFactorSelect.setItemText(1, _translate("MainWindow", "4"))
        self.interpolationFactorSelect.setItemText(2, _translate("MainWindow", "8"))
        self.interpolationFactorSelect.setItemText(3, _translate("MainWindow", "16"))
        self.interpolationFactorSelect.setItemText(4, _translate("MainWindow", "32"))
        self.interpolationFactorSelect.setItemText(5, _translate("MainWindow", "64"))
        self.interpolationFactorSelect.setItemText(6, _translate("MainWindow", "128"))
        self.interpolationFactorSelect.setItemText(7, _translate("MainWindow", "256"))
        self.interpolationFactorSelect.setItemText(8, _translate("MainWindow", "512"))
        self.interpolationFactorSelect.setItemText(9, _translate("MainWindow", "1024"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Interpolation factor -</span></p></body></html>"))
        self.gpuidsSelect.setItemText(0, _translate("MainWindow", "0"))
        self.gpuidsSelect.setItemText(1, _translate("MainWindow", "1"))
        self.gpuidsSelect.setItemText(2, _translate("MainWindow", "1,0"))
        self.label_21.setText(_translate("MainWindow", "<b>Account for duplicate frames in FPS calculation -</b><br>\n"
"Slow to calculate FPS when enabled"))
        self.accountForDuplicateFramesCheckbox.setText(_translate("MainWindow", "Enable"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Interpolation"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Encoding options"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Auto encoding -</span></p>\n"
"<p>Begin encoding the output while interpolation is still running<br>\n"
"Saves space for interpolated png frames (Good for low space disks)<br>\n"
"May slightly lower encoding quality</body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Output quality level (CRF) -</span></p>\n"
"<p>Less is higher quality<br>\n"
"More is lower quality</p></body></html>"))
        self.nvencCheck.setText(_translate("MainWindow", "Enable NVENC"))
        self.autoencodeCheck.setText(_translate("MainWindow", "Enable auto encoding"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Auto encoding block size -</span></p>\n"
"<p>Higher block size saves less disk space<br>Lower block size potentially reduces encoding quality/compression</p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Use NVENC -</span></p>\n"
"<p>Enabled - Use Nvidia\'s hardware video encoder (Fast, less quality)<br>\n"
"Disabled - Use x264 (Slow, more quality)</p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Loop output -</span></p></body></html>"))
        self.loopoutputCheck.setText(_translate("MainWindow", "Enable"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Encoding"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Batch processing"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Target FPS -</span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body>From this page, select an input folder, and set a target FPS and then click Run batch<br>The target FPS sets the minimum output FPS. The interpolator will use a high enough interpolation factor to meet or exceed it.\n"
"<br>\n"
"For looped output, add [l] to the folder or filename of a batch input</body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Batch processing"))
        self.extractFramesButton.setText(_translate("MainWindow", "Step 1: Extract frames"))
        self.interpolateFramesButton.setText(_translate("MainWindow", "Step 2: Interpolate"))
        self.encodeOutputButton.setText(_translate("MainWindow", "Step 3: Encode output"))
        self.runAllStepsButton.setText(_translate("MainWindow", "Run all steps"))
