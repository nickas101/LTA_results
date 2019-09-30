import os
import sys
import glob
import pyodbc 
from pandas import DataFrame
import pandas as pd


import scipy.ndimage as ndimage
import numpy as np

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


def main(search_text = "Siward"):
    global connection
    global df



    
    unit_name = 'test1'
    freq_nom = 26

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

    command = "select * from runData where runData.purpose like '%" + str(search_text) + "%'"


    df = pd.read_sql(command, connection)

    # **********************************************************

    # print(df['purpose'])
    #
    # sys.exit()

    # **********************************************************

    # freq_nom_hz = freq_nom * 1000000
    #
    #
    # df.sort_values(['measDate'], ascending=[True], inplace=True)
    #
    # df_freq = df['frq']
    # df_freq_ppm = 1000000 * (df_freq - freq_nom_hz)/freq_nom_hz
    # df['frq_ppm'] = df_freq_ppm
    #
    # # gaussian filter
    # df_filtered = ndimage.gaussian_filter(df_freq, sigma=25, order=0)
    #
    # df['frq_flt'] = df_filtered
    #
    # df_freq_ppm_filtered = 1000000 * (df_filtered - freq_nom_hz)/freq_nom_hz
    # df['frq_ppm_filtered'] = df_freq_ppm_filtered






    result = df

    # df = df.drop(columns=[
    #     'pk_locID', 
    #     'fk_runID', 
    #     'fk_brdID', 
    #     'fk_ovenID', 
    #     'pk_brdID', 
    #     'status', 
    #     'vchar',
    #     'pk_runID',
    #     'ppmStartDate',
    #     'operator',
    #     'limUpper',
    #     'limLower',
    #     'email',
    #     'emailSent',
    #     'emailNoteTime',
    #     'opemail',
    #     'sendemail',
    #     'sendopemail',
    #     'prodMonitoring',
    #     'standardProduction',
    #     'limUpper1',
    #     'limLower1',
    #     'hotStore',
    #     'processExperiment',
    #     'designExperiment',
    #     'returnUnits',
    #     'freqDivider',
    #     'rma',
    #     'currentRun',
    #     'sealingMethod',
    #     'glue'
    #     ]) 

    # df['startDate'] = df['startDate'].dt.date
    # df['finishDate'] = df['finishDate'].dt.date

    # # df.replace(to_replace='oven320', value='')

    # df = df.set_index('runNumber')

    # df['nomFrq'] = df['nomFrq']/1000000
    # df['nomFrq'] = round(df['nomFrq'],2)


    # df.sort_values(['runNumber', 'brd', 'loc'], ascending=[True, True, True], inplace=True)

    # # df['amount'] = df.groupby(['runNumber'])['brd'].count()

    # # df['locs'] = df.groupby(['runNumber'])['brd'].prod()

    # df['locs'] = df['loc'].astype(str)

    # df1 = df.groupby(['runNumber'])['locs'].apply(','.join).reset_index()

    # # df1['board'] = df['brd']

    # df1 = df1.set_index('runNumber')



    # df = df.drop(columns=['loc', 'locs'])



    # df1['nbr'] = df.groupby(['runNumber'])['brd'].count()

    # # print(df)

    # result = pd.concat([df1, df], axis=1, join='inner')

    # result = result.drop_duplicates() 

    # result.sort_values(['brd', 'runNumber'], ascending=[True, True], inplace=True)

    # # ******************************

    # result = result.set_index('brd')
    # df = df.drop(columns=['runNumber'])

    # ******************************



    # # filename = filename.replace('.csv', '') + '_filtered.csv'
    # path = r"\\rakdata2\Share\Nikolai\serial\sql_results\\"
    # filename = path + 'result.csv'
    # result.to_csv(filename, encoding = 'utf-8')
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
    #
    #
    #
    #
    #
    # figFvIF = plt.figure(figsize = (16,10))
    #
    # fviHostF = host_subplot(111)
    # plt.subplots_adjust(right = 1) # Was 0.5
    #
    # plotTitle = "\nAgeing data " + str(unit_name) + " (smoothed)"
    # fviHostF.set_title(plotTitle)
    # fviHostF.set_xlabel('Time, ', color='r')
    # fviHostF.set_ylabel('Frequency, ppm', color='b')
    #
    # fviHostF.tick_params(axis = 'y', colors = 'b')
    # fviHostF.tick_params(axis = 'x', colors = 'r')
    #
    # fviHostF.plot(df['measDate'], df['frq_ppm_filtered'], color='b', alpha = 1, label = "Residual", linewidth=1)
    # # fviHost.plot(df_raw['Offset Frequency (Hz)'], df_raw['PN_FLT'], color='b', alpha = 0.5, label = "Residual", linewidth=1)
    # # fviHostF.set_xscale('log')
    #
    # # xfmt = mdates.DateFormatter('%d-%m-%y %H:%M')
    # # fviHostF.xaxis.set_major_formatter(xfmt)
    #
    # # Show the major grid lines with dark grey lines
    # fviHostF.grid(b=True, which='major', color='#666666', linestyle='-', alpha=0.5)
    #
    # # Show the minor grid lines with very faint and almost transparent grey lines
    # fviHostF.minorticks_on()
    # fviHostF.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    #
    #
    # # save_plot = path + r'\\results//' + str(unit_name) + '.png'
    # save_plot = path + r'//' + str(unit_name) + '_smoothed.png'
    # figFvIF.savefig(save_plot, bbox_inches = 'tight')
    #
    # plt.close(figFvIF)

    return df

    # sys.exit()


def plot(index):
    global connection
    global df
    global df_plot

    unit_name = 'test1'
    freq_nom = 26

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

    print("index = " + str(index))

    run_id = str(df['pk_runID'].iloc[index])

    print("run_id = " + str(run_id))

    # command = "select * from measData where measData.fk_locID = '5A09D288-6325-431E-9664-ED7CA5A44FAE' and measData.frq <> '9999'"

    command = "select * from measData where measData.fk_locID in (select pk_locID from locData where locData.fk_runID = '" + str(run_id) + "') and measData.frq <> '9999' and compFreq <> '9999'"

    print(str(command))

    # command = "select * from runData where runData.purpose like '%" + str(search_text) + "%'"
    #
    df_plot = pd.read_sql(command, connection)

    # print(df_plot)

    # **********************************************************

    # print(df['purpose'])
    #
    # sys.exit()

    # **********************************************************

    # freq_nom_hz = freq_nom * 1000000
    #
    #
    # df.sort_values(['measDate'], ascending=[True], inplace=True)
    #
    # df_freq = df['frq']
    # df_freq_ppm = 1000000 * (df_freq - freq_nom_hz)/freq_nom_hz
    # df['frq_ppm'] = df_freq_ppm
    #
    # # gaussian filter
    # df_filtered = ndimage.gaussian_filter(df_freq, sigma=25, order=0)
    #
    # df['frq_flt'] = df_filtered
    #
    # df_freq_ppm_filtered = 1000000 * (df_filtered - freq_nom_hz)/freq_nom_hz
    # df['frq_ppm_filtered'] = df_freq_ppm_filtered


    locations = df_plot['fk_locID'].unique().tolist()

    # df[df.population > 10][['country', 'square']]

    print(locations[1])

    # df_plot = df_plot.sort_values(by=['fk_locID', 'measDate'])

    result = df_plot[df_plot['fk_locID'] == locations[1]]

    result = result.sort_values(by=['measDate'])

    print(result)

    # # test data
    # data = np.array([0.7,0.7,0.7,0.8,0.9,0.9,1.5,1.5,1.5,1.5])
    # fig, ax1 = plt.subplots()
    # bins = np.arange(0.6, 1.62, 0.02)
    #
    # # data = df['frq_ppm_filtered'].to_numpy()
    # # bins = df['measDate'].to_numpy()
    #
    # bins = bins.astype(float)
    #
    #
    #
    # print(data)
    # print(bins)
    #
    # # n1, bins1, patches1 = ax1.hist(data, bins, alpha=0.6, density=False, cumulative=False)
    #
    #
    # ax1.plot(bins, data, color='b', alpha = 1, label = "LTA", linewidth=1)
    # fig.tight_layout()
    #
    #
    # # plot
    # self.plotWidget = FigureCanvas(fig)
    # lay = QtWidgets.QVBoxLayout(self.plot1)
    # lay.setContentsMargins(0, 0, 0, 0)
    # lay.addWidget(self.plotWidget)
    #
    # # add toolbar
    # self.addToolBar(QtCore.Qt.BottomToolBarArea, NavigationToolbar(self.plotWidget, self))






    # result = df_plot.sort(['fk_locID'], ascending=[1, 0])
    # df.sort(['A', 'B'], ascending=[1, 0])

    # df = df.drop(columns=[
    #     'pk_locID',
    #     'fk_runID',
    #     'fk_brdID',
    #     'fk_ovenID',
    #     'pk_brdID',
    #     'status',
    #     'vchar',
    #     'pk_runID',
    #     'ppmStartDate',
    #     'operator',
    #     'limUpper',
    #     'limLower',
    #     'email',
    #     'emailSent',
    #     'emailNoteTime',
    #     'opemail',
    #     'sendemail',
    #     'sendopemail',
    #     'prodMonitoring',
    #     'standardProduction',
    #     'limUpper1',
    #     'limLower1',
    #     'hotStore',
    #     'processExperiment',
    #     'designExperiment',
    #     'returnUnits',
    #     'freqDivider',
    #     'rma',
    #     'currentRun',
    #     'sealingMethod',
    #     'glue'
    #     ])

    # df['startDate'] = df['startDate'].dt.date
    # df['finishDate'] = df['finishDate'].dt.date

    # # df.replace(to_replace='oven320', value='')

    # df = df.set_index('runNumber')

    # df['nomFrq'] = df['nomFrq']/1000000
    # df['nomFrq'] = round(df['nomFrq'],2)

    # df.sort_values(['runNumber', 'brd', 'loc'], ascending=[True, True, True], inplace=True)

    # # df['amount'] = df.groupby(['runNumber'])['brd'].count()

    # # df['locs'] = df.groupby(['runNumber'])['brd'].prod()

    # df['locs'] = df['loc'].astype(str)

    # df1 = df.groupby(['runNumber'])['locs'].apply(','.join).reset_index()

    # # df1['board'] = df['brd']

    # df1 = df1.set_index('runNumber')

    # df = df.drop(columns=['loc', 'locs'])

    # df1['nbr'] = df.groupby(['runNumber'])['brd'].count()

    # # print(df)

    # result = pd.concat([df1, df], axis=1, join='inner')

    # result = result.drop_duplicates()

    # result.sort_values(['brd', 'runNumber'], ascending=[True, True], inplace=True)

    # # ******************************

    # result = result.set_index('brd')
    # df = df.drop(columns=['runNumber'])

    # ******************************

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
    #
    #
    #
    #
    #
    # figFvIF = plt.figure(figsize = (16,10))
    #
    # fviHostF = host_subplot(111)
    # plt.subplots_adjust(right = 1) # Was 0.5
    #
    # plotTitle = "\nAgeing data " + str(unit_name) + " (smoothed)"
    # fviHostF.set_title(plotTitle)
    # fviHostF.set_xlabel('Time, ', color='r')
    # fviHostF.set_ylabel('Frequency, ppm', color='b')
    #
    # fviHostF.tick_params(axis = 'y', colors = 'b')
    # fviHostF.tick_params(axis = 'x', colors = 'r')
    #
    # fviHostF.plot(df['measDate'], df['frq_ppm_filtered'], color='b', alpha = 1, label = "Residual", linewidth=1)
    # # fviHost.plot(df_raw['Offset Frequency (Hz)'], df_raw['PN_FLT'], color='b', alpha = 0.5, label = "Residual", linewidth=1)
    # # fviHostF.set_xscale('log')
    #
    # # xfmt = mdates.DateFormatter('%d-%m-%y %H:%M')
    # # fviHostF.xaxis.set_major_formatter(xfmt)
    #
    # # Show the major grid lines with dark grey lines
    # fviHostF.grid(b=True, which='major', color='#666666', linestyle='-', alpha=0.5)
    #
    # # Show the minor grid lines with very faint and almost transparent grey lines
    # fviHostF.minorticks_on()
    # fviHostF.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    #
    #
    # # save_plot = path + r'\\results//' + str(unit_name) + '.png'
    # save_plot = path + r'//' + str(unit_name) + '_smoothed.png'
    # figFvIF.savefig(save_plot, bbox_inches = 'tight')
    #
    # plt.close(figFvIF)

    return result





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
        # QMessageBox.information(self, "ListWidget", "You clicked: " + item.text())
        # print(item)
        index = self.listWidget.currentRow()
        result = plot(index)

        # test data
        # data = np.array([0.7,0.7,0.7,0.8,0.9,0.9,1.5,1.5,1.5,1.5])
        fig, ax1 = plt.subplots()
        # bins = np.arange(0.6, 1.62, 0.02)


        # data = result['compFreq'].to_numpy()
        # bins = result['measDate'].to_numpy()

        data = result['compFreq']
        bins = result['measDate']

        # bins = bins.astype(float)

        # print(data)
        # print(bins)

        # n1, bins1, patches1 = ax1.hist(data, bins, alpha=0.6, density=False, cumulative=False)

        ax1.plot(bins, data, color='b', alpha = 1, label = "LTA", linewidth=1)
        fig.tight_layout()

        # plot
        self.plotWidget = FigureCanvas(fig)
        lay = QtWidgets.QVBoxLayout(self.plot1)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self.plotWidget)

        # add toolbar
        self.addToolBar(QtCore.Qt.BottomToolBarArea, NavigationToolbar(self.plotWidget, self))






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



        # # test data
        # data = np.array([0.7,0.7,0.7,0.8,0.9,0.9,1.5,1.5,1.5,1.5])
        # fig, ax1 = plt.subplots()
        # bins = np.arange(0.6, 1.62, 0.02)
        #
        # # data = df['frq_ppm_filtered'].to_numpy()
        # # bins = df['measDate'].to_numpy()
        #
        # bins = bins.astype(float)
        #
        # print(data)
        # print(bins)
        #
        # # n1, bins1, patches1 = ax1.hist(data, bins, alpha=0.6, density=False, cumulative=False)
        #
        # ax1.plot(bins, data, color='b', alpha = 1, label = "LTA", linewidth=1)
        # fig.tight_layout()
        #
        # # plot
        # self.plotWidget = FigureCanvas(fig)
        # lay = QtWidgets.QVBoxLayout(self.plot1)
        # lay.setContentsMargins(0, 0, 0, 0)
        # lay.addWidget(self.plotWidget)
        #
        # # add toolbar
        # self.addToolBar(QtCore.Qt.BottomToolBarArea, NavigationToolbar(self.plotWidget, self))

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())







 
    # execute application
    # sys.exit( app.exec_() )