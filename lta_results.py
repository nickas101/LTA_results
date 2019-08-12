import os
import sys
import glob
import pyodbc 
from pandas import DataFrame
import pandas as pd

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter.ttk import Combobox 

import numpy
from numpy import copy
import scipy.ndimage as ndimage

import matplotlib
import matplotlib.pyplot as plt
from os.path import splitext
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA

import matplotlib.dates as mdates

from pandas.plotting import register_matplotlib_converters




def main():
    
    connection = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                        "Server=akl-longage3\LONGAGE3;"
                        "Database=LTMAL3;"
                        "UID=RAKON\nikolai;"
                        "Trusted_Connection=yes;")


    
    unit_name = 'test1'
    freq_nom = 26

    register_matplotlib_converters()
    
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


    command = "select * from measData where measData.fk_locID = '0A51A4A0-6FB2-4D69-93B0-5E04659C5C71' and measData.frq <> '9999'"


    df = pd.read_sql(command, connection)

    freq_nom_hz = freq_nom * 1000000
    

    df.sort_values(['measDate'], ascending=[True], inplace=True)

    df_freq = df['frq']
    df_freq_ppm = 1000000 * (df_freq - freq_nom_hz)/freq_nom_hz
    df['frq_ppm'] = df_freq_ppm

    # gaussian filter
    df_filtered = ndimage.gaussian_filter(df_freq, sigma=25, order=0)

    df['frq_flt'] = df_filtered

    df_freq_ppm_filtered = 1000000 * (df_filtered - freq_nom_hz)/freq_nom_hz
    df['frq_ppm_filtered'] = df_freq_ppm_filtered



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



    # filename = filename.replace('.csv', '') + '_filtered.csv'  
    path = r"\\rakdata2\Share\Nikolai\serial\sql_results\\" 
    filename = path + 'result.csv'
    result.to_csv(filename, encoding = 'utf-8')





    figFvI = plt.figure(figsize = (16,10))

    fviHost = host_subplot(111)
    plt.subplots_adjust(right = 1) # Was 0.5

    plotTitle = "\nAgeing data " + str(unit_name)
    fviHost.set_title(plotTitle)
    fviHost.set_xlabel('Time, ', color='r')
    fviHost.set_ylabel('Frequency, ppm', color='b')

    fviHost.tick_params(axis = 'y', colors = 'b')
    fviHost.tick_params(axis = 'x', colors = 'r')

    fviHost.plot(df['measDate'], df['frq_ppm'], color='b', alpha = 1, label = "Residual", linewidth=.5)
    # fviHost.plot(df_raw['Offset Frequency (Hz)'], df_raw['PN_FLT'], color='b', alpha = 0.5, label = "Residual", linewidth=1)
    # fviHost.set_xscale('log')

    # Show the major grid lines with dark grey lines
    fviHost.grid(b=True, which='major', color='#666666', linestyle='-', alpha=0.5)

    # Show the minor grid lines with very faint and almost transparent grey lines
    fviHost.minorticks_on()
    fviHost.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

    
    # save_plot = path + r'\\results//' + str(unit_name) + '.png'
    save_plot = path + r'//' + str(unit_name) + '.png'
    figFvI.savefig(save_plot, bbox_inches = 'tight')

    plt.close(figFvI)






    figFvIF = plt.figure(figsize = (16,10))

    fviHostF = host_subplot(111)
    plt.subplots_adjust(right = 1) # Was 0.5

    plotTitle = "\nAgeing data " + str(unit_name) + " (smoothed)"
    fviHostF.set_title(plotTitle)
    fviHostF.set_xlabel('Time, ', color='r')
    fviHostF.set_ylabel('Frequency, ppm', color='b')

    fviHostF.tick_params(axis = 'y', colors = 'b')
    fviHostF.tick_params(axis = 'x', colors = 'r')

    fviHostF.plot(df['measDate'], df['frq_ppm_filtered'], color='b', alpha = 1, label = "Residual", linewidth=1)
    # fviHost.plot(df_raw['Offset Frequency (Hz)'], df_raw['PN_FLT'], color='b', alpha = 0.5, label = "Residual", linewidth=1)
    # fviHostF.set_xscale('log')

    # xfmt = mdates.DateFormatter('%d-%m-%y %H:%M')
    # fviHostF.xaxis.set_major_formatter(xfmt)

    # Show the major grid lines with dark grey lines
    fviHostF.grid(b=True, which='major', color='#666666', linestyle='-', alpha=0.5)

    # Show the minor grid lines with very faint and almost transparent grey lines
    fviHostF.minorticks_on()
    fviHostF.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

    
    # save_plot = path + r'\\results//' + str(unit_name) + '.png'
    save_plot = path + r'//' + str(unit_name) + '_smoothed.png'
    figFvIF.savefig(save_plot, bbox_inches = 'tight')

    plt.close(figFvIF)





    msg_finish = Tk()
    msg_finish.withdraw()
    msg_finish=messagebox.showinfo("Done","Results are in: " + filename)
    sys.exit()



def clicked_start():
    
    global crystalType
    global moustrap
    global all_units
    
    crystalType = combo.get()
    moustrap = chk_state.get()
    all_units = chk2_state.get()
    

    if crystalType == 'All types':
        crystalType = ''
    else:
        crystalType = "'" + crystalType + "'"

    print(crystalType)

    root.destroy()
    main()


def clicked():

    if chk2_state.get():
        chk.configure(state='disabled')  
        combo.configure(state='disabled')

    else:
        chk.configure(state = 'normal')  
        combo.configure(state = 'normal')





# User settings
# **************************

moustrap = False
all_units = True
crystalType = "'RSX-5'"


# **************************

root = Tk()
root.title('Overdue crystals')
root.geometry('310x180+350+250')

chk_state = BooleanVar()  
chk_state.set(moustrap) 
chk = Checkbutton(root, text='Moustrap', var=chk_state)  
chk.grid(column = 0, row = 1)


lbl = Label(root, text="Crtystal Type")
lbl.grid(column=0, row=2, sticky=E)

combo = Combobox(root)  
combo['values'] = ('All types', 'RSX-5', 'RSX-5B', 'RSX-10', 'RSX-11')  
combo.current(0) 
combo.grid(column = 1, row = 2)  

chk2_state = BooleanVar()  
chk2_state.set(False) 
chk2 = Checkbutton(root, text='All units', var=chk2_state, command = clicked)
chk2.grid(column = 0, row = 3)

lbl_103 = Label(root, text="")
lbl_103.grid(column=1, row=18)
lbl_104 = Label(root, text="")
lbl_104.grid(column=1, row=19)


btn_start = Button(root, text = "Start", bg='green',fg='white', font='arial 18', command = clicked_start)
btn_start.grid(column = 2, row = 30, sticky=W)

root.mainloop()