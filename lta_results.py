import os
import sys
import glob
import pyodbc 
from pandas import DataFrame
import pandas as pd


import scipy.ndimage as ndimage
import numpy as np
import time

from mpl_toolkits.axes_grid1 import host_subplot
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtGui import QIcon

import matplotlib
matplotlib.use('QT5Agg')

import matplotlib.pylab as plt
from matplotlib.backends.backend_qt5agg import FigureCanvas 
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from matplotlib.figure import Figure
from matplotlib import animation

# from PyQt4 import QtGui
#
# from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
# from matplotlib.figure import Figure


connection = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                        "Server=akl-longage3\LONGAGE3;"
                        "Database=LTMAL3;"
                        "UID=RAKON\nikolai;"
                        "Trusted_Connection=yes;")

df = pd.DataFrame()
df_plot = pd.DataFrame()

unit_name = 'test1'
# freq_nom = 26


def main(search_text = "Siward"):
    global connection
    global df
    # global freq_nom



    


    # register_matplotlib_converters()
    
    # if all_units:
    #     command = "select * from locData join brdData on locData.fk_brdID = brdData.pk_brdID join runData on runData.pk_runID = locData.fk_runID where runData.currentRun = 'True' and runData.finishDate < CURRENT_TIMESTAMP"
    # elif crystalType == '':
    #     if moustrap:
    #         command = "select * from locData join brdData on locData.fk_brdID = brdData.pk_brdID join runData on runData.pk_runID = locData.fk_runID where runData.currentRun = 'True' and runData.finishDate < CURRENT_TIMESTAMP and runData.oscillator = 'Mousetrap'"
    #     else:
    #         command = "select * from locData join brdData on locData.fk_brdID = brdData.pk_brdID join runData on runData.pk_runID = locData.fk_runID where runData.currentRun = 'True' and runData.finishDate < CURRENT_TIMESTAMP and runData.oscillator <> 'Mousetrap'"
    # else:
    #     if moustrap:
    #         command = "select * from locData join brdData on locData.fk_brdID = brdData.pk_brdID join runData on runData.pk_runID = locData.fk_runID where runData.currentRun = 'True' and runData.finishDate < CURRENT_TIMESTAMP and runData.oscillator = 'Mousetrap' and runData.crystalType = " + crystalType
    #     else:
    #         command = "select * from locData join brdData on locData.fk_brdID = brdData.pk_brdID join runData on runData.pk_runID = locData.fk_runID where runData.currentRun = 'True' and runData.finishDate < CURRENT_TIMESTAMP and runData.oscillator <> 'Mousetrap' and runData.crystalType = " + crystalType


    # command = "select * from measData where measData.fk_locID = '5A09D288-6325-431E-9664-ED7CA5A44FAE' and measData.frq <> '9999'"

    command = "select * from runData where runData.purpose like '%" + str(search_text) + "%' or runData.comment like '%" + str(search_text) + "%' or runData.packetNumber like '%" + str(search_text) + "%' or runData.crystalNumber like '%" + str(search_text) + "%'"


    df = pd.read_sql(command, connection)
    result = df



    # Examples

    # df['startDate'] = df['startDate'].dt.date
    # df['finishDate'] = df['finishDate'].dt.date
    # # df.replace(to_replace='oven320', value='')
    # df = df.set_index('runNumber')
    # df['nomFrq'] = round(df['nomFrq'],2)
    # df.sort_values(['runNumber', 'brd', 'loc'], ascending=[True, True, True], inplace=True)
    # # df['amount'] = df.groupby(['runNumber'])['brd'].count()
    # # df['locs'] = df.groupby(['runNumber'])['brd'].prod()
    # df['locs'] = df['loc'].astype(str)
    # df1 = df.groupby(['runNumber'])['locs'].apply(','.join).reset_index()
    # df1 = df1.set_index('runNumber')
    # df = df.drop(columns=['loc', 'locs'])
    # result = pd.concat([df1, df], axis=1, join='inner')
    # result = result.drop_duplicates()
    # # gaussian filter
    # df_filtered = ndimage.gaussian_filter(df_freq, sigma=25, order=0)

    return df


def plot(index):
    global connection
    global df
    global df_plot


    print("index = " + str(index))

    run_id = str(df['pk_runID'].iloc[index])

    # freq_nom = float(df['nomFrq'].iloc[index])

    print("run_id = " + str(run_id))
    # print("freq_nom = " + str(freq_nom))


    command = "select * from measData where measData.fk_locID in (select pk_locID from locData where locData.fk_runID = '" + str(run_id) + "') and measData.frq <> '9999' and compFreq <> '9999'"

    print(str(command))

    # command = "select * from runData where runData.purpose like '%" + str(search_text) + "%'"
    #
    df_plot = pd.read_sql(command, connection)

    # print(df_plot)


    locations = df_plot['fk_locID'].unique().tolist()

    # df[df.population > 10][['country', 'square']]

    print(locations[1])

    # df_plot = df_plot.sort_values(by=['fk_locID', 'measDate'])

    result = df_plot

    # result = df_plot[df_plot['fk_locID'] == locations[1]]
    #
    # result = result.sort_values(by=['measDate'])

    # print(result)



    # # filename = filename.replace('.csv', '') + '_filtered.csv'
    path = r"\\rakdata2\Share\Nikolai\serial\sql_results\\"
    filename = path + 'result.csv'
    result.to_csv(filename, encoding = 'utf-8')
    #
    #
    #
    #
    #
    # figFvI = plt.figure(figsize = (16,10))
    #
    # fviHost = host_subplot(111)
    # plt.subplots_adjust(right = 1) # Was 0.5
    #
    # plotTitle = "\nAgeing data " + str(unit_name)
    # fviHost.set_title(plotTitle)
    # fviHost.set_xlabel('Time, ', color='r')
    # fviHost.set_ylabel('Frequency, ppm', color='b')
    #
    # fviHost.tick_params(axis = 'y', colors = 'b')
    # fviHost.tick_params(axis = 'x', colors = 'r')
    #
    # fviHost.plot(df['measDate'], df['frq_ppm'], color='b', alpha = 1, label = "Residual", linewidth=.5)
    # # fviHost.plot(df_raw['Offset Frequency (Hz)'], df_raw['PN_FLT'], color='b', alpha = 0.5, label = "Residual", linewidth=1)
    # # fviHost.set_xscale('log')
    #
    # # Show the major grid lines with dark grey lines
    # fviHost.grid(b=True, which='major', color='#666666', linestyle='-', alpha=0.5)
    #
    # # Show the minor grid lines with very faint and almost transparent grey lines
    # fviHost.minorticks_on()
    # fviHost.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    #
    #
    # # save_plot = path + r'\\results//' + str(unit_name) + '.png'
    # save_plot = path + r'//' + str(unit_name) + '.png'
    # figFvI.savefig(save_plot, bbox_inches = 'tight')
    #
    # plt.close(figFvI)
    #


    return result, locations





# **************************

# print(os.getcwd())
# sys.exit()

# project_path = r"\\Akl-file-01\Departments\Engineering - Product R&D\Stored Files\Nikolai\scripts\LTA_results\\"

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('2.ui', self)

        self.setWindowIcon(QIcon('banana.png'))
        self.setWindowTitle("LTA results")

        self.pushButton_2.clicked.connect(self.buttonClicked)
        self.pushButton_plot.clicked.connect(self.listItemDoubleClicked)

    def listItemClicked(self, item):
        # QMessageBox.information(self, "ListWidget", "You clicked: " + item.text())
        # print(item)
        index = self.listWidget.currentRow()

        # df['purpose'].iloc[index]

        # print(df.iloc[index])

        freq = str(df['nomFrq'].iloc[index] / 1000000) + "MHz"
        purpose = str(df['purpose'].iloc[index])


        self.label12.setText(str(freq))
        self.label101.setText(purpose)

        return self.listWidget.currentRow()

    def itemSelectionChanged (self):
        # QMessageBox.information(self, "ListWidget", "You clicked: " + item.text())
        # print(item)
        index = self.listWidget.currentRow()

        # df['purpose'].iloc[index]

        # print(df.iloc[index])

        freq = str(df['nomFrq'].iloc[index] / 1000000) + "MHz"
        purpose = str(df['purpose'].iloc[index])
        crystal_type = str(df['crystalType'].iloc[index])
        owner = str(df['owner'].iloc[index])
        sap = str(df['crystalNumber'].iloc[index])


        self.label12.setText(str(freq))
        self.label101.setText(purpose)
        self.label_7.setText(crystal_type)
        self.label_15.setText(owner)
        self.label_17.setText(sap)

        return self.listWidget.currentRow()

    def listItemDoubleClicked(self, item):
        # try:
        #     fig.clf()
        #
        # except:
        #     pass

        # QMessageBox.information(self, "ListWidget", "You clicked: " + item.text())
        # print(item)
        index = self.listWidget.currentRow()
        result, locations = plot(index)

        freq_nom = float(df['nomFrq'].iloc[index])
        freq_nom_str = str(float(df['nomFrq'].iloc[index]) / 1000000) + "MHz"
        crystal_type = df['crystalType'].iloc[index]
        crystal_number = df['crystalNumber'].iloc[index]
        packet_number = df['packetNumber'].iloc[index]

        print("freq_nom = " + str(freq_nom))

        # plt.ion()

        fig, ax1 = plt.subplots()
        plotTitle = "Ageing data for " + str(freq_nom_str) + ", " + str(crystal_type) + ", SAP number " + str(crystal_number) + ", packet #" + str(packet_number)
        ax1.set_title(plotTitle)
        ax1.set_xlabel('Time')
        ax1.set_ylabel('Frequency, ppm')
        # ax1.tick_params(axis = 'y', colors = 'b')

        for location in locations:

            result_single = df_plot[df_plot['fk_locID'] == location]
            result_single = result_single.sort_values(by=['measDate'])

            freq_ppm = 1000000 * (result_single['compFreq'] - freq_nom) / freq_nom

            data = freq_ppm
            bins = result_single['measDate']

            ax1.plot(bins, data, alpha=1, label="LTA", linewidth=1)


        # Show the major grid lines with dark grey lines
        ax1.grid(b=True, which='major', color='#666666', linestyle='-', alpha=0.5)

        # Show the minor grid lines with very faint and almost transparent grey lines
        ax1.minorticks_on()
        ax1.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

        # fig.subplots_adjust(left=0.01, right=0.9, top=0.9, bottom=0.1)
        # ax1.margins(3)

        fig.tight_layout()

        # plot
        self.plotWidget = FigureCanvas(fig)
        lay = QtWidgets.QVBoxLayout(self.plot1)
        # lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self.plotWidget)

        # add toolbar
        tb = self.addToolBar(QtCore.Qt.BottomToolBarArea, NavigationToolbar(self.plotWidget, self))

        # def unfill(self):
        #     def deleteItems(layout):
        #         if layout is not None:
        #             while layout.count():
        #                 item = layout.takeAt(0)
        #                 widget = item.widget()
        #                 if widget is not None:
        #                     widget.deleteLater()
        #                 else:
        #                     deleteItems(item.layout())
        #
        #     deleteItems(self.ui.verticalLayout)


        # time.sleep(10)
        # tb.hide()
        # self.destroy(True)

        # time.sleep(20)
        # del tb
        # lay.removeWidget(self.plotWidget)

        # fig.clear()
        # fig.clf()






        # df['purpose'].iloc[index]

        # print(df.iloc[index])
        #
        # freq = str(df['nomFrq'].iloc[index] / 1000000) + "MHz"
        # purpose = str(df['purpose'].iloc[index])
        #
        #
        # self.label12.setText(str(freq))
        # self.label101.setText(purpose)
        #
        # return self.listWidget.currentRow()

    def buttonClicked(self):

        search_text = self.lineEdit.text()

        # df = main(search_text)
        main(search_text)
        self.listWidget.clear()

        self.label12.clear()
        self.label101.clear()
        self.label_7.clear()
        self.label_15.clear()
        self.label_17.clear()

        # print(df['purpose'])

        self.listWidget.addItems(df['purpose'])

        self.listWidget.itemClicked.connect(self.listItemClicked)
        self.listWidget.itemSelectionChanged.connect(self.itemSelectionChanged)
        self.listWidget.itemDoubleClicked.connect(self.listItemDoubleClicked)


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())