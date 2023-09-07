

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from tkinter import filedialog as fd
from tkinter import messagebox as msbox
import pandas as pd
from tabulate import tabulate
from tksheet import Sheet
import seaborn as sns
import matplotlib.pyplot as plt
import scipy as spy
from scipy.stats import shapiro

import numpy as np
from outliers import smirnov_grubbs as grubbs
from tableview import file_in_html
from charts import boxplot_single, trend, trend1f, besch_stat, violin_single, stripplot_single, countplot, pieplot,pareto_one_column 
from charts import boxplot1f, violin1f, strip1f, scatterplot,scatter1f, regression_single, barplot1f, barplot2f, pareto
from charts import regression1f, boxplot2f, swarmplot_single, swarmplot1f, swarmplot2f, strip2f, violin2f, scatter3d, error_bar_dia_single
from charts import error_bar_dia_1f, error_bar_dia_2f
from stat_charts import qq_plot, histogram, normality_test, CPA, urwertkarte, xquer_s, LREG, outliert
from stat_charts import contingency_table

import CSVpySTAT_support

    



class Toplevel1:
    
    global df
    
    def __init__(self, top=None):
        
        class SampleObj(object):
            def __init__(self, df):
                self.df = ''
        
        
        ###check float
        def isfloat(x):
            try:
                float(x)
            except ValueError:
                return False
            else:
                return True
        
        
        def file_open():
            filetypes = (
                ('CSV files', '*.csv'),
                ('All files', '*.*')
            )
            
            filename = fd.askopenfilename(
                title='Open a file',
                filetypes=filetypes)
        
            self.Entry1.delete(0, END)
            self.Entry1.insert(1,filename)
            self.Label303.configure(text=filename)
            
            f = open(filename, "r", errors='ignore')
    
    
    
            log = 'open file name: ' + filename + '\n'
            fline = f.readline()
            fline2 = f.readline()
            
            print('#'*30 + '\n')
            print('File - Information \n')
            print('Preview to the first 2 lines: \n')
            print('first line:', fline)
            print('second line:', fline2)
            
            
            eintrag = log + '\n' + 'File Info \n' +  'Preview to the first 2 lines: \n' + 'first line:\n' + fline + '\n' + 'second line:' + '\n' + fline2
            
            
            self.Scrolledtext1.insert('1.0', eintrag)
            f.close
    
                   
            
            
            return filename
        
        def read_table():
            global df
        ##Tabellen neu einlesen                                                                
            self.TCombobox9.configure(values=list(df.columns))
            self.TCombobox11.configure(values=list(df.columns))
            self.TCombobox14.configure(values=list(df.columns))
            self.TCombobox62.configure(values=list(df.columns))
            self.TCombobox208.configure(values=list(df.columns))
            self.TCombobox222.configure(values=list(df.columns))
            self.TCombobox6.configure(values=list(df.columns))
            self.TCombobox85.configure(values=list(df.columns))
            self.TCombobox86.configure(values=list(df.columns))
            
            values=df.select_dtypes(include=['float', 'int'])
            self.TCombobox4.configure(values=list(values.columns))
            self.TCombobox5.configure(values=list(df.columns))
            cat1=df.select_dtypes(include=['object', 'datetime'])
            #self.TCombobox6.configure(values=list(cat1.columns))
            
            values=df.select_dtypes(include=['float', 'int'])
            self.TCombobox72.configure(values=list(values.columns))
            values=df.select_dtypes(include=['float', 'int'])
            self.TCombobox73.configure(values=list(values.columns))
            
                        
            tabi=df.select_dtypes(include=['object', 'datetime'])
            #self.TCombobox85.configure(values=list(tabi.columns))
            #self.TCombobox86.configure(values=list(tabi.columns))            
            self.TCombobox91.configure(values=list(tabi.columns))
            self.TCombobox412.configure(values=list(tabi.columns))
            self.TCombobox512.configure(values=list(tabi.columns))
            
            ta=df.select_dtypes(exclude=['float'])
            self.TCombobox102.configure(values=list(ta.columns))
            self.TCombobox103.configure(values=list(ta.columns)) 
        
        
        
        def file2_open():
            filetypes = (
                ('CSV files', '*.csv'),
                ('All files', '*.*')
            )
            
            filename = fd.askopenfilename(
                title='Open a file',
                filetypes=filetypes)
        
            self.Entry2.delete(0, END)
            self.Entry2.insert(1,filename)
            
            f = open(filename, "r", errors='ignore')
    
    
    
            log = 'open second file name: ' + filename + '\n'
            
            print('#'*30)
            print('File Information \n')
            print('Preview to the first 2 lines: \n')
            print('first line:', f.readline())
            print('second line:', f.readline())
            
            
            eintrag = log + '\n' +  'File Info \nPreview to the first 2 lines: \n' + 'first line:\n' + f.readline() + '\n' + 'second line:' + '\n' + f.readline()
            
            
            self.Scrolledtext1.insert('1.0', eintrag)
            f.close
    
                   
            
            
            return filename
        
        
        
        
        
        
        
        def read_csv():
            global df
            print ('File einlesen')
            
            fn = self.Entry1.get()
            
            if fn == '':
                msbox.showinfo(title='File is missing', message='No File chooesed')
            
            
            seperator = self.TCombobox1.get()
            comma = self.TCombobox2.get()
            head = self.TCombobox3.get()
            datatableno = var1.get()
            
            if seperator =='':
                seperator =','
                comma = '.'
                head ='no'
            elif seperator =='tab':
                seperator = '\t'
            elif seperator =='space':
                seperator = '\s+'
            
            if head =='yes':
                hd = 0
            elif head =='no':
                hd = 1
            
            
            df=pd.read_csv(fn,sep=seperator ,decimal=comma, header=hd,encoding='iso-8859-1', engine='python')
            
            ##Tabelle + Formate einblenden
            self.Scrolledtext2.insert(END, df)
            
            self.Scrolledtext2.insert(END, '\n')
            self.Scrolledtext2.insert(END, df.dtypes)
            
            
            if datatableno ==1:
                print('no tableview')
            else:
                
                
                ##Tabelle darstellen            
                self.frame1.grid_columnconfigure(0, weight = 1)
                self.frame1.grid_rowconfigure(0, weight = 1)
                self.sheet = Sheet(self.frame1,
                                   data=df.values.tolist())

                #if head =='yes':
                self.sheet.headers(df.columns)
                
                    
                self.sheet.enable_bindings()
                self.frame1.grid(row = 0, column = 0, sticky = "nswe")
                self.sheet.grid(row = 0, column = 0, sticky = "nswe")
            
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            self.Scrolledtext1.insert(END, '\nCSV Data loaded')
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            
                                     
            ##Tabellen neu einlesen                                                                
            self.TCombobox9.configure(values=list(df.columns))
            self.TCombobox11.configure(values=list(df.columns))
            self.TCombobox14.configure(values=list(df.columns))
            self.TCombobox62.configure(values=list(df.columns))
            self.TCombobox208.configure(values=list(df.columns))
            self.TCombobox222.configure(values=list(df.columns))
            self.TCombobox6.configure(values=list(df.columns))
            self.TCombobox85.configure(values=list(df.columns))
            self.TCombobox86.configure(values=list(df.columns))
            
            
            values=df.select_dtypes(include=['float', 'int'])
            self.TCombobox4.configure(values=list(values.columns))
            self.TCombobox8.configure(values=list(values.columns))
            self.TCombobox5.configure(values=list(df.columns))
            cat1=df.select_dtypes(include=['object', 'datetime'])
            #self.TCombobox6.configure(values=list(cat1.columns))
            
            values=df.select_dtypes(include=['float', 'int'])
            self.TCombobox72.configure(values=list(values.columns))
            values=df.select_dtypes(include=['float', 'int'])
            self.TCombobox73.configure(values=list(values.columns))
            self.TCombobox802.configure(values = list(values.columns))
            self.TCombobox803.configure(values = list(values.columns))
            self.TCombobox806.configure(values = list(values.columns))
                        
            tabi=df.select_dtypes(include=['object', 'datetime'])
            #self.TCombobox85.configure(values=list(tabi.columns))
            #self.TCombobox86.configure(values=list(tabi.columns))            
            self.TCombobox91.configure(values=list(tabi.columns))
            self.TCombobox412.configure(values=list(tabi.columns))
            self.TCombobox512.configure(values=list(tabi.columns))
            
            ta=df.select_dtypes(exclude=['float'])
            self.TCombobox102.configure(values=list(ta.columns))
            self.TCombobox103.configure(values=list(ta.columns)) 
            
            
            
            return (df)
        
        def read2_csv():
            global df2
            print ('File einlesen')
            
            fn = self.Entry2.get()
            
            if fn == '':
                tk.messagebox.showinfo(title='File is missing', message='No File chooesed')
            
            
            seperator = self.TCombobox16.get()
            comma = self.TCombobox17.get()
            head = self.TCombobox18.get()
            
            if seperator =='':
                seperator =','
                comma = '.'
                head ='no'
            elif seperator =='tab':
                seperator = '\t'
            elif seperator =='space':
                seperator = '\s+'
            
            if head =='yes':
                hd = 0
            elif head =='no':
                hd = 1
            
            
            df2=pd.read_csv(fn,sep=seperator ,decimal=comma, header=hd, encoding='iso-8859-1', engine='python')
            
            self.Scrolledtext1.insert(END, 30*'#')
            self.Scrolledtext1.insert(END, '\nsecond CSV Data loaded')
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            
            ##Tabelle + Formate einblenden
            self.Scrolledtext1.insert(END, df2)
            
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, df2.dtypes)
            
            self.TCombobox20.configure(values=list(df2.columns))
            
            return (df2)
        
        
        
        
        
        
        
        def change_format():
            global df
            print('Change Format')
            print(df)
            
            curr_format = self.TCombobox9.get()
            
            format_col = df[curr_format].dtypes
            
            new_format = self.TCombobox10.get()
            
            if new_format =='datetime':
                df[curr_format] = df[curr_format].astype('datetime64[ns]')
            if new_format =='float':
                df[curr_format] = df[curr_format].astype(float)
            if new_format =='int':
                df[curr_format] = df[curr_format].astype(int)
            if new_format =='category':
                df[curr_format] = df[curr_format].astype('category')
            if new_format =='object':
                df[curr_format] = df[curr_format].astype(str)
            
            print(df[curr_format].dtypes)
            print(df.dtypes)
            read_table()
            
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            self.Scrolledtext1.insert(END, '\nChange Format')
            self.Scrolledtext1.insert(END, '\nColumn: ' + curr_format)
            self.Scrolledtext1.insert(END, '\nCurrent Format: ' + str(format_col))
            self.Scrolledtext1.insert(END, '\nNew Format: ' + str(new_format))
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            
            return df
            
            
            
        def current_format():
            global df
            print('Current Format')
            
             
            
            curr_format = self.TCombobox9.get()
            
            format_col = df[curr_format].dtypes
            
            print (curr_format)
            print(format_col)
        
            self.Label12.configure(text=format_col)    
            
            if format_col =='object':
                self.value_list4 = ['int', 'datetime']
                self.TCombobox10.configure(values=self.value_list4)
            if format_col =='int':
                self.value_list4 = ['float']
                self.TCombobox10.configure(values=self.value_list4)
            if format_col =='int64':
                self.value_list4 = ['float']
                self.TCombobox10.configure(values=self.value_list4)
        
        def filter_col():
            print('filter col')
            filtercolumn = self.TCombobox11.get()
            #df[filtercolumn] =(df[filtercolumn].astype(str))
            list_o_filtercrit = df[filtercolumn].tolist()
            
            fileformat = df[filtercolumn].dtypes
            
            if fileformat !='object':
                
                filtercontent = sorted(set(list_o_filtercrit))
                self.TCombobox13.configure(values=filtercontent)
            if fileformat =='object':
                filtercontent = np.unique(list_o_filtercrit).tolist()
                self.TCombobox13.configure(values=filtercontent)
            
            
            if fileformat =='int':
                self.value_list5 = ['==', '>=', '<=', '!=']
                self.TCombobox12.configure(values=self.value_list5)
            
            if fileformat =='float':
                self.value_list5 = ['==', '>=', '<=', '!=']
                self.TCombobox12.configure(values=self.value_list5)
            
            if fileformat =='int64':
                self.value_list5 = ['==', '>=', '<=', '!=']
                self.TCombobox12.configure(values=self.value_list5)
            
            if fileformat =='float64':
                self.value_list5 = ['==', '>=', '<=', '!=']
                self.TCombobox12.configure(values=self.value_list5)
            
            if fileformat =='datetime64[ns]':
                self.value_list5 = ['==', '>=', '<=', '!=']
                self.TCombobox12.configure(values=self.value_list5)
            
            if fileformat =='object':
                self.value_list5 = ['==','!=']
                self.TCombobox12.configure(values=self.value_list5)
            
            
            
            
            
            read_table()
            
            
        def set_filter():
            print('set filter')
            global df
            filtercolumn = self.TCombobox11.get()
            filtercrit = self.TCombobox12.get()
            filtercontent = self.TCombobox13.get()
            
            fileformat = df[filtercolumn].dtypes
            
            if fileformat == 'object':
                           
                if filtercrit =="==":
                    df = df[df[filtercolumn]==str(filtercontent)]
                if filtercrit =="!=":
                    df = df[df[filtercolumn]!=str(filtercontent)]
            
            if fileformat =='float':
                if filtercrit =="==":
                    df = df[df[filtercolumn]==float(filtercontent)]
                if filtercrit =="!=":
                    df = df[df[filtercolumn]!=float(filtercontent)]
                if filtercrit =="<=":
                    df = df[df[filtercolumn]<=float(filtercontent)]
                if filtercrit ==">=":
                    df = df[df[filtercolumn]>=float(filtercontent)]
            
            if fileformat =='int':
                if filtercrit =="==":
                    df = df[df[filtercolumn]==int(filtercontent)]
                if filtercrit =="!=":
                    df = df[df[filtercolumn]!=int(filtercontent)]
                if filtercrit =="<=":
                    df = df[df[filtercolumn]<=int(filtercontent)]
                if filtercrit ==">=":
                    df = df[df[filtercolumn]>=int(filtercontent)]
            
            
            if fileformat =='float64':
                if filtercrit =="==":
                    df = df[df[filtercolumn]==float(filtercontent)]
                if filtercrit =="!=":
                    df = df[df[filtercolumn]!=float(filtercontent)]
                if filtercrit =="<=":
                    df = df[df[filtercolumn]<=float(filtercontent)]
                if filtercrit ==">=":
                    df = df[df[filtercolumn]>=float(filtercontent)]
            
            if fileformat =='int64':
                if filtercrit =="==":
                    df = df[df[filtercolumn]==int(filtercontent)]
                if filtercrit =="!=":
                    df = df[df[filtercolumn]!=int(filtercontent)]
                if filtercrit =="<=":
                    df = df[df[filtercolumn]<=int(filtercontent)]
                if filtercrit ==">=":
                    df = df[df[filtercolumn]>=int(filtercontent)]
            
            if fileformat =='datetime64[ns]':
                if filtercrit =="==":
                    df = df[df[filtercolumn]==(filtercontent)]
                if filtercrit =="!=":
                    df = df[df[filtercolumn]!=(filtercontent)]
                if filtercrit =="<=":
                    df = df[df[filtercolumn]<=(filtercontent)]
                if filtercrit ==">=":
                    df = df[df[filtercolumn]>=(filtercontent)]
            
            
            print(df)
            
            
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            self.Scrolledtext1.insert(END, '\nFilter by column')
            self.Scrolledtext1.insert(END, '\nColumn: ' + filtercolumn)
            self.Scrolledtext1.insert(END, '\nFilter Criteria: ' + str(filtercrit))
            self.Scrolledtext1.insert(END, '\nFilter Content: ' + str(filtercontent))
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            
            
            ##Tabelle + Formate einblenden
            self.Scrolledtext1.insert(END, df)
            
            ##Tabelle darstellen            
            self.frame1.grid_columnconfigure(0, weight = 1)
            self.frame1.grid_rowconfigure(0, weight = 1)
            self.sheet = Sheet(self.frame1,
                               data=df.values.tolist())
            
            self.sheet.headers(df.columns)
                
            self.sheet.enable_bindings()
            self.frame1.grid(row = 0, column = 0, sticky = "nswe")
            self.sheet.grid(row = 0, column = 0, sticky = "nswe")
             
        def sort_column():
            print('sort column')
            global df
            
            column_to_sort = self.TCombobox14.get()
            sort_direction = self.TCombobox15.get()
            
            if sort_direction == 'AZ':
                a_t_f = 1
            if sort_direction == 'ZA':
                a_t_f = 0
            
            
            df = df.sort_values(by=column_to_sort, ascending=a_t_f)
            
            print(df)
            
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            self.Scrolledtext1.insert(END, '\nSort by column')
            self.Scrolledtext1.insert(END, '\nColumn: ' + column_to_sort)
            self.Scrolledtext1.insert(END, '\nSort direction: ' + str(sort_direction))
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            
            ##Tabelle + Formate einblenden
            self.Scrolledtext2.insert(END, df)
            self.Scrolledtext2.insert(END, df.dtypes)
            
            ##Tabelle darstellen            
            self.frame1.grid_columnconfigure(0, weight = 1)
            self.frame1.grid_rowconfigure(0, weight = 1)
            self.sheet = Sheet(self.frame1,
                               data=df.values.tolist())
            
            self.sheet.headers(df.columns)
                
            self.sheet.enable_bindings()
            self.frame1.grid(row = 0, column = 0, sticky = "nswe")
            self.sheet.grid(row = 0, column = 0, sticky = "nswe")
        
        def join_table():
            global df, df2, result_df
            
            
            column_T2 = self.TCombobox20.get()
            art_to_join = self.TCombobox21.get()
            
            if art_to_join == 'outer':
                df = pd.merge(df, df2, how='outer', on=column_T2)
            elif art_to_join =='inner':
                df = pd.merge(df, df2, how='inner', on=column_T2)
            elif art_to_join =='left outer':
                df = pd.merge(df, df2, how='left', on=column_T2)
            elif art_to_join =='right outer':
                df = pd.merge(df, df2, how='right', on=column_T2)
            
            print(df)
            
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            self.Scrolledtext1.insert(END, '\nJoin Dataframes')
            self.Scrolledtext1.insert(END, '\nKey Column: ' + column_T2)
            self.Scrolledtext1.insert(END, '\nJoin Criteria: ' + str(art_to_join))
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            
            
            
            ##Tabelle darstellen            
            self.frame1.grid_columnconfigure(0, weight = 1)
            self.frame1.grid_rowconfigure(0, weight = 1)
            self.sheet = Sheet(self.frame1,
                               data=df.values.tolist())
            
            self.sheet.headers(df.columns)
                
            self.sheet.enable_bindings()
            self.frame1.grid(row = 0, column = 0, sticky = "nswe")
            self.sheet.grid(row = 0, column = 0, sticky = "nswe")
            
            read_table()
        
        def save_CSV():
            print('Save as File')
            global df
            
            
            
            liste = self.sheet.get_sheet_data(return_copy = False, get_header = False, get_index = False)
            headercol = self.sheet.headers(newheaders = None, index = None, reset_col_positions = False, show_headers_if_not_sheet = True)
            
            indexneed = var10.get()
            
            df2 = pd.DataFrame (liste)
            df2.columns = headercol
            #print(df2)
            
            
            filetypes = (
                ('CSV files', '*.csv'),
                ('All files', '*.*')
            )
            
            filename = fd.asksaveasfile(
                title='Save a file',
                filetypes=filetypes)
            
            
            if indexneed == 1:
                df2.to_csv(filename.name, sep=';', decimal=',', header =True, index=True)
                self.Label303.configure(text=filename.name)
            else:
                df2.to_csv(filename.name, sep=';', decimal=',', header =True, index=False)
                self.Label303.configure(text=filename.name)
            
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            self.Scrolledtext1.insert(END, '\nSave Dataframe')
            self.Scrolledtext1.insert(END, '\nFilename: ' + str(filename.name))
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
        
        
        def save_current_CSV_name():
            print('Save File')
            
            filename = self.Entry1.get()
            indexneed = var10.get()
            
            
            
            
            if filename =='':
                filename = 'new.csv'
            
            global df
            
            liste = self.sheet.get_sheet_data(return_copy = False, get_header = False, get_index = False)
            
            headercol = self.sheet.headers(newheaders = None, index = None, reset_col_positions = False, show_headers_if_not_sheet = True)
            

            
            
            df2 = pd.DataFrame (liste)
            df2.columns = headercol
            
            
            
            if indexneed == 1:
                df2.to_csv(filename, sep=';', decimal=',', header =True, index=True)
                self.Label303.configure(text=filename)
            
            else:
                df2.to_csv(filename, sep=';', decimal=',', header =True, index=False)
                self.Label303.configure(text=filename)
            
            
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            self.Scrolledtext1.insert(END, '\nSave Dataframe')
            self.Scrolledtext1.insert(END, '\nFilename: ' + str(filename))
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            
            self.Entry1.delete(0, END)
            self.Entry1.insert(1,filename)
            self.TCombobox1.set('')
            self.TCombobox1.insert(1,';')
            self.TCombobox2.set('')
            self.TCombobox2.insert(1,',')
            self.TCombobox3.set('')
            self.TCombobox3.insert(1,'yes')
            
            read_csv()
        
        
        
        
        def append_CSV():
            print('Append Dataframe')
            global df, df2
            
            if len(df.columns) != len(df2.columns):
                print("Columns do not match!! Dataframe has " + str(len(df.columns)) + " columns. CSV file has " + str(len(df2.columns)) + " columns.")            
                print('please try again!')
        
                #raise Exception("Columns do not match!! Dataframe has " + str(len(df.columns)) + " columns. CSV file has " + str(len(pd.read_csv(add_table, nrows=1, sep=trennzeichen).columns)) + " columns.")
            elif not (df.columns == df2.columns).all():
                print("Columns and column order of dataframe and csv file do not match!!")
                print('please try again!')
                #raise Exception("Columns and column order of dataframe and csv file do not match!!")
            else:
                df = df.append(df2)
        
            read_table()
        
            print(df)
            
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            self.Scrolledtext1.insert(END, '\nAppend Second Dataframe')
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            
            
            ##Tabelle darstellen            
            self.frame1.grid_columnconfigure(0, weight = 1)
            self.frame1.grid_rowconfigure(0, weight = 1)
            self.sheet = Sheet(self.frame1,
                               data=df.values.tolist())
            
            self.sheet.headers(df.columns)
                
            self.sheet.enable_bindings()
            self.frame1.grid(row = 0, column = 0, sticky = "nswe")
            self.sheet.grid(row = 0, column = 0, sticky = "nswe")
            
        def plot_df():
            print('plotvalues')
            global df
            plotfunction = self.TCombobox7.get()
            messwert = self.TCombobox4.get()
            ut = self.Entry54.get()
            lt = self.Entry55.get()
            spdt = self.TCombobox5.get()
            factorx = self.TCombobox6.get()
            factorz = self.TCombobox8.get()
            print(plotfunction)
            
                    
            if spdt !='':
                w1 = 'a'
            else:
                w1=''
            if factorx !='':
                w2 = 'b'
            else:
                w2=''
            if factorz !='':
                w3 = 'c'
            else:
                w3=''
                
                
                
            wert = w1+w2+w3
            print(wert)
            
            if wert == '':
                if plotfunction =='Boxplot':
                    boxplot_single(df, messwert, lt, ut)
                elif plotfunction =='Violinplot':
                    violin_single(df, messwert, lt, ut)
                elif plotfunction =='Stripplot':
                    stripplot_single(df, messwert, lt, ut)
                elif plotfunction =='Swarmplot':
                    swarmplot_single(df, messwert, lt, ut)
                elif plotfunction =='Error Bar Plot':
                    error_bar_dia_single(df, messwert, lt, ut)
                
                
            elif wert == 'a':
                if plotfunction =='Time Series Plot':
                    trend(df, messwert, lt, ut, spdt)
                elif plotfunction =='Boxplot':
                    boxplot1f(df, messwert, lt, ut,spdt)
                elif plotfunction =='Violinplot':
                    violin1f(df, messwert, lt, ut,spdt)
                elif plotfunction =='Stripplot':
                    strip1f(df, messwert, lt, ut,spdt)
                elif plotfunction =='Scatterplot':
                    scatterplot(df,messwert, lt,ut, spdt)
                elif plotfunction =='Regressionplot':
                    regression_single(df, messwert, lt, ut, spdt)
                elif plotfunction =='Swarmplot':
                    swarmplot1f(df, messwert, lt, ut, spdt) 
                elif plotfunction =='Barplot':
                    barplot1f(df, messwert, lt, ut, spdt)
                elif plotfunction =='Countplot':
                    countplot(df, spdt, lt, ut)
                elif plotfunction =='Pieplot': 
                    pieplot(df, spdt)
                elif plotfunction =='Pareto':
                    if messwert !='':
                        pareto(df, messwert, spdt)
                    else:
                        pareto_one_column(df, spdt)
                elif plotfunction == 'Error Bar Plot':
                    error_bar_dia_1f(df, messwert, lt, ut, spdt)
            
            elif wert =='ab':
                if plotfunction=='Regressionplot':
                    regression1f(df, messwert, lt, ut, spdt, factorx)
                if plotfunction=='Boxplot':
                    boxplot2f(df, messwert, lt, ut, spdt, factorx)
                if plotfunction =='Violinplot':
                    violin2f(df, messwert, lt, ut,spdt, factorx)
                if plotfunction =='Swarmplot':
                    swarmplot2f(df, messwert, lt, ut,spdt, factorx)
                if plotfunction =='Stripplot':
                    strip2f(df, messwert, lt, ut,spdt, factorx)
                if plotfunction =='Barplot':
                    barplot2f(df, messwert, lt, ut,spdt, factorx)    
                if plotfunction =='Scatterplot':
                    scatter1f(df, messwert, lt, ut, spdt, factorx)
                if plotfunction =='Time Series Plot':
                    trend1f(df, messwert, lt, ut, spdt, factorx)
                if plotfunction =='Error Bar Plot':
                    error_bar_dia_2f(df, messwert, lt, ut, spdt, factorx)
                    
            
            elif wert =='ac':
                if plotfunction =='Scatterplot':
                    scatter3d(df,messwert, spdt, factorx, factorz)

                        
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            self.Scrolledtext1.insert(END, '\nPlot: ' + plotfunction)
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            
            
            
        def plot_stat():
            global df
            
            print('plotstatistic')
            global df
            plotfunction = self.TCombobox63.get()
            messwert = self.TCombobox62.get()
            ut = self.Entry66.get()
            lt = self.Entry65.get()
            samplesize = self.TCombobox67.get()
            
            #self.value_list63 = ['Descriptive Statistics', 'X-Bar Chart', 'Xbar/R-Chart', 'Xbar/s-Chart', 'Capability Analysis', 'Histogram', 'QQ-Plot', 'Test of normal Distribution']
            
            print(plotfunction)
            
            if plotfunction=='Descriptive Statistics':
                besch_stat(df, messwert)
            if plotfunction =='QQ-Plot':
                qq_plot(df, messwert)
            if plotfunction =='Histogram':
                histogram(df, messwert)
            if plotfunction =='Test of normal Distribution':
                normality_test(df,messwert)
            if plotfunction =='Capability Analysis':
                CPA(df, messwert, lt, ut)
            if plotfunction =='Single Value Chart':
                urwertkarte(df, messwert, lt, ut)
            if plotfunction =='Xbar/s-Chart':
                xquer_s(df, messwert, lt, ut, samplesize)
            if plotfunction =='Outlier-Test':
                outliert(df, messwert)
                
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            self.Scrolledtext1.insert(END, '\nPlot: ' + plotfunction)
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
        
        def plot_L_Reg():
            global df
            yv = self.TCombobox72.get()
            xv = self.TCombobox73.get()
            LREG(df, yv, xv)
            
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            self.Scrolledtext1.insert(END, '\nPlot: Linear Regression Plot')
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            
  
            
##################################################
##statistics
###########################################################################

        def table_statistics():
            global df
            filename = 'stat_df.csv'
            print('Table Statistics')
            
            
            stat = df.describe()
            
            
            self.Scrolledtext1.insert(END, 30*'#')
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, stat)
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')            
            
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            self.Scrolledtext1.insert(END, '\nDescriptive Statistics whoole Dataframe:')
            self.Scrolledtext1.insert(END, '\nSave with file name: ' + filename + '\nInto root folder')
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')            
            
            
            
            df_stats = df.describe(include='all')
            df_stats.to_csv(filename, sep=';', decimal=',', header =True)
            print(tabulate(df_stats, headers='keys', tablefmt='psql'))
            
            df2=pd.read_csv(filename,sep=';' ,decimal=',', header=0, engine='python')
            file_in_html(df2)
            
            
            
            
        ####truncate values
        def truncate(n, decimals=0):
                multiplier = 10 ** decimals
                return int(n * multiplier) / multiplier

###########################################################################        

        def seq_nr():
            global df
            print('build sequence nr')
            seq_count = len(df)
            print(seq_count)
            seq_count=int(seq_count)
            
            
            name_col = self.Entry83.get()
            
            seq_nr_from = self.Entry82.get()
                       
            if name_col !='':
                name_col=name_col
            else:
                name_col='seq #'
            
            if seq_nr_from !='':
                seq_nr_from = int(seq_nr_from)
            else:
                seq_nr_from = 1
                
            
            
            df[name_col] = range(seq_nr_from, seq_count+seq_nr_from)
            
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            self.Scrolledtext1.insert(END, '\nCreate Column with sequence number')
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            
            print(df)
            
            ##Tabelle darstellen            
            self.frame1.grid_columnconfigure(0, weight = 1)
            self.frame1.grid_rowconfigure(0, weight = 1)
            self.sheet = Sheet(self.frame1,
                               data=df.values.tolist())
            
            self.sheet.headers(df.columns)
                
            self.sheet.enable_bindings()
            self.frame1.grid(row = 0, column = 0, sticky = "nswe")
            self.sheet.grid(row = 0, column = 0, sticky = "nswe")
        
            read_table()    
        
        
        def combine_column():
            print('Combine factor columns:')
            print('#'*50)    
            
            global df
            col1 = self.TCombobox85.get()
            col2 = self.TCombobox86.get()
            name_col = self.Entry87.get()
            
            df[col1 + '(2)'] = df[col1].astype(str)
            df[col2 + '(2)'] = df[col2].astype(str)
            
            if name_col !='':
                name_col =name_col
            else:
                name_col =col1 + "_" + col2
            
            
            
            df[name_col] = df[col1 +'(2)'] + '_' + df[col2 +'(2)']
            
            
            print(df)
            
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            self.Scrolledtext1.insert(END, '\nCombine Columns')
            self.Scrolledtext1.insert(END, '\nColumn1:' + col1)
            self.Scrolledtext1.insert(END, '\nColumn2:' + col2)
            self.Scrolledtext1.insert(END, '\nNew Column Name:' + name_col)
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            
            
            ##Tabelle darstellen            
            self.frame1.grid_columnconfigure(0, weight = 1)
            self.frame1.grid_rowconfigure(0, weight = 1)
            self.sheet = Sheet(self.frame1,
                               data=df.values.tolist())
            
            self.sheet.headers(df.columns)
                
            self.sheet.enable_bindings()
            self.frame1.grid(row = 0, column = 0, sticky = "nswe")
            self.sheet.grid(row = 0, column = 0, sticky = "nswe")
            
            read_table()

        def split_column():
            global df
            print('split column')
            
            
            column_name = self.TCombobox91.get()
            delimeter_name = self.Entry92.get()
            
            df[[column_name,column_name + str(2)]] = df[column_name].str.split(delimeter_name,expand=True)
            
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            self.Scrolledtext1.insert(END, '\nSplit Column: ' + column_name )
            self.Scrolledtext1.insert(END, '\nNew Column1:' + column_name)
            self.Scrolledtext1.insert(END, '\nNew Column2:' + column_name + str(2))
            self.Scrolledtext1.insert(END, '\nDelimeter:' + delimeter_name)
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            
            ##Tabelle darstellen            
            self.frame1.grid_columnconfigure(0, weight = 1)
            self.frame1.grid_rowconfigure(0, weight = 1)
            self.sheet = Sheet(self.frame1,
                               data=df.values.tolist())
            
            self.sheet.headers(df.columns)
                
            self.sheet.enable_bindings()
            self.frame1.grid(row = 0, column = 0, sticky = "nswe")
            self.sheet.grid(row = 0, column = 0, sticky = "nswe")

            read_table()
            
        def crosstable():
            global df
            print('crosstable')
            
            table1 = self.TCombobox102.get()
            table2 = self.TCombobox103.get()
            tableoption = self.TCombobox104.get()
            
            
            
            if tableoption =='cross sum table':
                ctcalc = pd.crosstab(index=df[table1], columns=df[table2])
                print(tabulate(ctcalc, headers='keys', tablefmt='psql'))
                
                
                ctcalc.to_csv('crosstable.csv', sep=';', decimal=',', header =True)
                
                df2=pd.read_csv('crosstable.csv',sep=';' ,decimal=',', header=0, engine='python')
                file_in_html(df2)
            elif tableoption =='cross sum table with total':
                ctv=pd.crosstab(index=df[table1], columns=df[table2], margins=True)
                print(tabulate(ctv, headers='keys', tablefmt='psql'))
                ctv.to_csv('crosstable.csv', sep=';', decimal=',', header =True)
                
                df2=pd.read_csv('crosstable.csv',sep=';' ,decimal=',', header=0, engine='python')
                file_in_html(df2)
            elif tableoption =='cross percent table':
                ct = pd.crosstab(index=df[table1], columns=df[table2], margins=False).applymap(lambda r: r/len(df))
                print(tabulate(ct, headers='keys', tablefmt='psql'))
                ct.to_csv('crosstable.csv', sep=';', decimal=',', header =True)
                
                df2=pd.read_csv('crosstable.csv',sep=';' ,decimal=',', header=0, engine='python')
                file_in_html(df2)
            elif tableoption =='cross percent table with total':
                ct = pd.crosstab(index=df[table1], columns=df[table2], margins=True).applymap(lambda r: r/len(df))
                print(tabulate(ct, headers='keys', tablefmt='psql'))
                ct.to_csv('crosstable.csv', sep=';', decimal=',', header =True)
                
                df2=pd.read_csv('crosstable.csv',sep=';' ,decimal=',', header=0, engine='python')
                file_in_html(df2)
            elif tableoption =='contingency table':
                contingency_table(df, table1, table2)
                
        def delete_rows():
            global df
            print('Delete Rows')
        
            delete_where = self.TCombobox212.get()
            
            delete_option = self.TCombobox202.get()
            
            col_del = self.TCombobox222.get()
            
            cont = self.Entry203.get()
            
            
            #self.value_list202 = ['nan rows', 'empty rows','NA rows', 'zero rows', 'rows with special characters']
            
            
            if delete_where =='whole dataframe':
                if delete_option == 'nan rows':
                    df = df.dropna()
                    
                elif delete_option == 'empty rows':
                    df.replace(' ', np.nan, inplace=True)
                    df= df.dropna()
                elif delete_option == 'NA rows':
                    df.replace('NA', np.nan, inplace=True)
                    df= df.dropna()
                elif delete_option == 'zero rows':
                    df.replace(0, np.nan, inplace=True)
                    df= df.dropna()
                    
                elif delete_option =='rows with special characters':
                    df.replace(cont, np.nan, inplace=True)
                    df= df.dropna()
            
            elif delete_where =='into column':
                if delete_option == 'nan rows':
                    df= df.dropna(subset=[col_del])
                elif delete_option == 'empty rows':
                    df[col_del].replace(' ', np.nan, inplace=True)
                    df= df.dropna(subset=[col_del])
                elif delete_option == 'NA rows':
                    df[col_del].replace('NA', np.nan, inplace=True)
                    df= df.dropna(subset=[col_del])
                elif delete_option == 'zero rows':
                    df[col_del].replace(0, np.nan, inplace=True)
                    df= df.dropna(subset=[col_del])
                elif delete_option =='rows with special characters':
                    df[col_del].replace(cont, np.nan, inplace=True)
                    df= df.dropna(subset=[col_del])
            
            
            
            
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            self.Scrolledtext1.insert(END, '\nDelete:')
            self.Scrolledtext1.insert(END, '\nDelete where:' + delete_where)
            self.Scrolledtext1.insert(END, '\nDelete Option:' + delete_option)
            self.Scrolledtext1.insert(END, '\nDelete into Column:' + col_del)
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            
            
            
            
            ##Tabelle darstellen            
            self.frame1.grid_columnconfigure(0, weight = 1)
            self.frame1.grid_rowconfigure(0, weight = 1)
            self.sheet = Sheet(self.frame1,
                               data=df.values.tolist())
            
            self.sheet.headers(df.columns)
                
            self.sheet.enable_bindings()
            self.frame1.grid(row = 0, column = 0, sticky = "nswe")
            self.sheet.grid(row = 0, column = 0, sticky = "nswe")
            
            read_table()
                
        def replace_into_column():
            global df
            print('replace into columns')
            
            replace_where = self.TCombobox208.get()
            print(replace_where)
            
            replace_option = self.TCombobox206.get()
            print(replace_option)
            
            repl_what = self.Entry207.get()
            print(repl_what)
            repl_with = self.Entry217.get()            
            print(repl_with)
            #self.value_list206 = ['value','character','float to point comma', 'point to float comma']
            
            if replace_option =='character':
                
                df[replace_where] = df[replace_where].str.replace(repl_what, repl_with)
                
                
            elif replace_option =='value':
                df[replace_where].replace(float(repl_what), float(repl_with), inplace=True)     
            elif replace_option =='float to point comma':
                df[replace_where]=df[replace_where].str.replace(',','.').astype(float)
            elif replace_option =='point to float comma':
                df[replace_where]=df[replace_where].astype(str)
                df[replace_where]=df[replace_where].str.replace('.',',', regex=True).astype(str)
            elif replace_option =='Column Name':
                df= df.rename(columns={replace_where:repl_with})
            
            
            
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            self.Scrolledtext1.insert(END, '\nReplace:')
            self.Scrolledtext1.insert(END, '\nReplace where:' + replace_where)
            self.Scrolledtext1.insert(END, '\nReplace Option:' + replace_option)
            self.Scrolledtext1.insert(END, '\nReplace what:' + repl_what)
            self.Scrolledtext1.insert(END, '\nReplace with:' + repl_with)
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            
            
            
            ##Tabelle darstellen            
            self.frame1.grid_columnconfigure(0, weight = 1)
            self.frame1.grid_rowconfigure(0, weight = 1)
            self.sheet = Sheet(self.frame1,
                               data=df.values.tolist())
            
            self.sheet.headers(df.columns)
                
            self.sheet.enable_bindings()
            self.frame1.grid(row = 0, column = 0, sticky = "nswe")
            self.sheet.grid(row = 0, column = 0, sticky = "nswe")
            
            read_table()
            
        def show_fr():
            global df
            print('column first row')
            
            col = self.TCombobox412.get()
            
            fr_val = df[col][1]

            self.Label414.configure(text=fr_val)  
        
        
        def convert_date():
            global df
            print('create convert date column')
            
            col_name = self.TCombobox412.get()
            
            current_format = self.TCombobox402.get()
            
            
            new_col_name = self.Entry403.get()
            
            if new_col_name !='':
                new_col_name = new_col_name
            else:
                new_col_name ='Datetime'
            
            #self.value_list402 = ['yyyy-mm-dd hh:mm:ss', 'yyyy/mm/dd hh:mm:ss','dd-mm-yyyy hh:mm:ss', 'yyyy-mm-ddThh:mm:ss', 'dd.mm.yyyy hh:mm:ss', 'dd.mm.yyyy hh:mm', 'dd.mm.yyyy hh', 'dd.mm.yyyy']
            
            if current_format =='yyyy/mm/dd hh:mm:ss':
                df[new_col_name] = pd.to_datetime(df[col_name], format='%Y/%m/%d %H:%M:%S')
                df[new_col_name] = df[new_col_name].astype('datetime64[ns]')
            
            elif current_format =='yyyy-mm-dd hh:mm:ss':
                df[new_col_name] = pd.to_datetime(df[col_name], format='%Y-%m-%d %H:%M:%S')
                df[new_col_name] = df[new_col_name].astype('datetime64[ns]')
            
            elif current_format =='dd-mm-yyyy hh:mm:ss':
                df[new_col_name] = pd.to_datetime(df[col_name], format='%d-%m-%Y %H:%M:%S')
                df[new_col_name] = df[new_col_name].astype('datetime64[ns]')
            
            elif current_format =='yyyy-mm-ddThh:mm:ss':
                df[new_col_name] = pd.to_datetime(df[col_name], format='%Y-%m-%dT%H:%M:%S')
                df[new_col_name] = df[new_col_name].astype('datetime64[ns]')
            
            elif current_format =='dd.mm.yyyy hh:mm:ss':
                df[new_col_name] = pd.to_datetime(df[col_name], format='%d.%m.%Y %H:%M:%S')
                df[new_col_name] = df[new_col_name].astype('datetime64[ns]')
            elif current_format =='dd.mm.yyyy hh:mm':
                df[new_col_name] = pd.to_datetime(df[col_name], format='%d.%m.%Y %H:%M')
                df[new_col_name] = df[new_col_name].astype('datetime64[ns]')
            elif current_format =='dd.mm.yyyy hh':
                df[new_col_name] = pd.to_datetime(df[col_name], format='%d.%m.%Y %H')
                df[new_col_name] = df[new_col_name].astype('datetime64[ns]')
            elif current_format =='dd.mm.yyyy':
                df[new_col_name] = pd.to_datetime(df[col_name], format='%d.%m.%Y')
                df[new_col_name] = df[new_col_name].astype('datetime64[ns]')
            elif current_format =='dd-mm-yyyy':
                df[new_col_name] = pd.to_datetime(df[col_name], format='%d-%m-%Y')
                df[new_col_name] = df[new_col_name].astype('datetime64[ns]')
            elif current_format =='yyyy-mm-dd':
                df[new_col_name] = pd.to_datetime(df[col_name], format='%Y-%m-%d')
                df[new_col_name] = df[new_col_name].astype('datetime64[ns]')
            
            
            
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            self.Scrolledtext1.insert(END, '\nConvert Datetime Column:')
            self.Scrolledtext1.insert(END, '\nCurrent String Column Name:' + col_name)
            self.Scrolledtext1.insert(END, '\nCurrent Format:' + current_format)
            self.Scrolledtext1.insert(END, '\nNew Column Name:' + new_col_name)
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            
            
            
            ##Tabelle darstellen            
            self.frame1.grid_columnconfigure(0, weight = 1)
            self.frame1.grid_rowconfigure(0, weight = 1)
            self.sheet = Sheet(self.frame1,
                               data=df.values.tolist())
            
            self.sheet.headers(df.columns)
                
            self.sheet.enable_bindings()
            self.frame1.grid(row = 0, column = 0, sticky = "nswe")
            self.sheet.grid(row = 0, column = 0, sticky = "nswe")
            
            read_table()
        
        
        def create_cal_info():
            global df
            print('create calendar info')
            
            col_name = self.TCombobox512.get()
            
            cal_info = self.TCombobox502.get()
            
            
            new_col_name = self.Entry503.get()
            
            if new_col_name !='':
                new_col_name = new_col_name
            else:
                new_col_name =cal_info
            
            #self.value_list502 = ['month', 'day','week', 'year', 'minutes', 'second', 'day name', 'month name', 'day of the year', 'day of the week']
            
            if cal_info =='month':
                df[new_col_name] = df[col_name].dt.month
                df[new_col_name] = df[new_col_name].astype('int')
            elif cal_info=='day':
                df[new_col_name] = df[col_name].dt.day
                df[new_col_name] = df[new_col_name].astype('int')
            elif cal_info=='week':
                df[new_col_name] = df[col_name].dt.isocalendar().week
                df[new_col_name] = df[new_col_name].astype('int')
            elif cal_info=='year':
                df[new_col_name] = df[col_name].dt.year
                df[new_col_name] = df[new_col_name].astype('int')
            elif cal_info=='hour':
                df[new_col_name] = df[col_name].dt.hour
                df[new_col_name] = df[new_col_name].astype('int')
            elif cal_info=='minutes':
                df[new_col_name] = df[col_name].dt.minute
                df[new_col_name] = df[new_col_name].astype('int')
            elif cal_info=='second':
                df[new_col_name] = df[col_name].dt.second
                df[new_col_name] = df[new_col_name].astype('int')
        
            elif cal_info=='day name':
                df[new_col_name] = df[col_name].dt.day_name()
                df[new_col_name] = df[new_col_name].astype('str')
            elif cal_info=='month name':
                df[new_col_name] = df[col_name].dt.month_name()
                df[new_col_name] = df[new_col_name].astype('str')
            elif cal_info=='day of the year':
                df[new_col_name] = df[col_name].dt.dayofyear
                df[new_col_name] = df[new_col_name].astype('int')
            elif cal_info=='day of the week':
                df[new_col_name] = df[col_name].dt.dayofweek
                df[new_col_name] = df[new_col_name].astype('int')
            
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            self.Scrolledtext1.insert(END, '\nGet Datetime Information Column:')
            self.Scrolledtext1.insert(END, '\nCurrent String Column Name:' + col_name)
            self.Scrolledtext1.insert(END, '\nDatetime Information:' + cal_info)
            self.Scrolledtext1.insert(END, '\nNew Column Name:' + new_col_name)
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            
            
            ##Tabelle darstellen            
            self.frame1.grid_columnconfigure(0, weight = 1)
            self.frame1.grid_rowconfigure(0, weight = 1)
            self.sheet = Sheet(self.frame1,
                               data=df.values.tolist())
            
            self.sheet.headers(df.columns)
                
            self.sheet.enable_bindings()
            self.frame1.grid(row = 0, column = 0, sticky = "nswe")
            self.sheet.grid(row = 0, column = 0, sticky = "nswe")
            
            read_table()
        
        def table_correlation():
            print('Table Correlation hole Columns')
            filename='correl_df.csv'
            correlation_df = df.corr()
    
    
            count_column = len(correlation_df.columns)
            print('columns', count_column)
            if count_column > 13:
                print(correlation_df)
            else:
                print(tabulate(correlation_df, headers='keys', tablefmt='psql'))
            
            
            correlation_df.to_csv(filename, sep=';', decimal=',', header =True)
            
            df2=pd.read_csv(filename,sep=';' ,decimal=',', header=0, engine='python')
            file_in_html(df2)

            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            self.Scrolledtext1.insert(END, '\nCorrelation whoole Dataframe:')
            self.Scrolledtext1.insert(END, '\nSave with file name: ' + filename + '\nInto root folder')
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')            


        def create_df():
            global df
            print('Create new DF')
            
            col_anz = self.Entry1302.get()
            
            if col_anz =='':
                col_anz = 1
            
            row_anz = self.Entry1303.get()
            
            if row_anz =='':
                row_anz = 1
            
            
            df= pd.DataFrame(index=np.arange(int(row_anz)), columns=np.arange(int(col_anz)))
            
            
            print (df)
            
            self.TCombobox1306.configure(values=list(df.columns))
            
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            self.Scrolledtext1.insert(END, '\nCreate a new Dataframe:')
            self.Scrolledtext1.insert(END, '\nNumbers of Columns: ' + str(col_anz))
            self.Scrolledtext1.insert(END, '\nNumbers of Rows: ' + str(row_anz))
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            
            
            ##Tabelle darstellen            
            self.frame1.grid_columnconfigure(0, weight = 1)
            self.frame1.grid_rowconfigure(0, weight = 1)
            self.sheet = Sheet(self.frame1,
                               data=df.values.tolist())
            
            self.sheet.headers(df.columns)
                
            self.sheet.enable_bindings()
            self.frame1.grid(row = 0, column = 0, sticky = "nswe")
            self.sheet.grid(row = 0, column = 0, sticky = "nswe")
            
            
            
            read_table()
        
        def create_CN():
            global df
            
            print('Define Column Name')
            
            print (df)
            current_C_name = int(self.TCombobox1306.get())
            print('oldname', current_C_name)
                       
            new_col_name = self.Entry1307.get()
            print('new name', new_col_name)
            
            df= df.rename(columns={current_C_name:new_col_name})
            
            
            
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            self.Scrolledtext1.insert(END, '\nDefine Column Name:')
            self.Scrolledtext1.insert(END, '\nColumn Nr: ' + str(current_C_name))
            self.Scrolledtext1.insert(END, '\nColumn Name: ' + str(new_col_name))
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            print(df)
            
            ##Tabelle darstellen            
            self.frame1.grid_columnconfigure(0, weight = 1)
            self.frame1.grid_rowconfigure(0, weight = 1)
            self.sheet = Sheet(self.frame1,
                               data=df.values.tolist())
            
            self.sheet.headers(df.columns)
                
            self.sheet.enable_bindings()
            self.frame1.grid(row = 0, column = 0, sticky = "nswe")
            self.sheet.grid(row = 0, column = 0, sticky = "nswe")
        
        
        def calc2cols():
            print('Calculation with 2 columns')
            
            col1 = self.TCombobox802.get()
            col2 = self.TCombobox803.get()
            calcfunction = self.TCombobox804.get()
            newcolname = self.Entry804.get()
            
            
            
            if calcfunction =='+':
                if newcolname !='':
                    newcolname = newcolname
                else:
                    newcolname = 'SUM ' + col1 + ';' + col2
                    
                df[newcolname] = df[col1] + df[col2]
            
            
            elif calcfunction =='-':
                if newcolname !='':
                    newcolname = newcolname
                else:
                    newcolname = 'DIV ' + col1 + ';' + col2
                    
                df[newcolname] = df[col1] - df[col2]
            
            
            elif calcfunction =='*':
                if newcolname !='':
                    newcolname = newcolname
                else:
                    newcolname = 'PRODUCT ' + col1 + ';' + col2
                    
                df[newcolname] = df[col1] * df[col2]
            
            
            elif calcfunction =='/':
                if newcolname !='':
                    newcolname = newcolname
                else:
                    newcolname = 'Quotient ' + col1 + ';' + col2
                    
                df[newcolname] = df[col1] / df[col2]
            
            
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            self.Scrolledtext1.insert(END, '\nCalculation 2 Columns:')
            self.Scrolledtext1.insert(END, '\nColumn 1: ' + str(col1))
            self.Scrolledtext1.insert(END, '\nColumn 2: ' + str(col2))
            self.Scrolledtext1.insert(END, '\nMath function: ' + str(calcfunction))
            self.Scrolledtext1.insert(END, '\nNew columnname: ' + str(newcolname))
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            print(df)
            
            ##Tabelle darstellen            
            self.frame1.grid_columnconfigure(0, weight = 1)
            self.frame1.grid_rowconfigure(0, weight = 1)
            self.sheet = Sheet(self.frame1,
                               data=df.values.tolist())
            
            self.sheet.headers(df.columns)
                
            self.sheet.enable_bindings()
            self.frame1.grid(row = 0, column = 0, sticky = "nswe")
            self.sheet.grid(row = 0, column = 0, sticky = "nswe")
        
        def calccolvalue():
            
            print('Calculation column with value')
            
            col = self.TCombobox806.get()
            val = self.Entry807.get()
            calcfunction = self.TCombobox808.get()
            newcolname = self.Entry809.get()
            
                
            
            
            if calcfunction =='+':
                if newcolname !='':
                    newcolname = newcolname
                else:
                    newcolname = 'SUM ' + col + ';' + str(val)
                
                if val =='':
                    msbox.showinfo(title='Value is missing', message='No value')    
                
                df[newcolname] = df[col] + float(val)
                
            
            elif calcfunction =='-':
                if newcolname !='':
                    newcolname = newcolname
                else:
                    newcolname = 'DIV ' + col + ';' + str(val)
                
                if val =='':
                    msbox.showinfo(title='Value is missing', message='No value')        
                
                
                df[newcolname] = df[col] - float(val)
            
            
            elif calcfunction =='*':
                if newcolname !='':
                    newcolname = newcolname
                else:
                    newcolname = 'PRODUCT ' + col + ';' + str(val)
                
                if val =='':
                    msbox.showinfo(title='Value is missing', message='No value')        
                
                df[newcolname] = df[col] * float(val)
            
            
            elif calcfunction =='/':
                if newcolname !='':
                    newcolname = newcolname
                else:
                    newcolname = 'Quotient ' + col + ';' + str(val)
                
                if val =='':
                    msbox.showinfo(title='Value is missing', message='No value')    
                
                df[newcolname] = df[col] / float(val)
            
            elif calcfunction =='^':
                if newcolname !='':
                    newcolname = newcolname
                else:
                    newcolname = 'Power ' + col + ';' + str(val)
                
                if val =='':
                    msbox.showinfo(title='Value is missing', message='No value')    
                    
                df[newcolname] = df[col] **float(val)
            
            
            
            elif calcfunction =='sqrt':
                if newcolname !='':
                    newcolname = newcolname
                else:
                    newcolname = 'Root ' + col + ';' + str(val)
                    
                df[newcolname] = df[col].apply(np.sqrt, axis=1)
            
            
            
            
            
                
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            self.Scrolledtext1.insert(END, '\nCalculation Columns with value:')
            self.Scrolledtext1.insert(END, '\nColumn : ' + str(col))
            self.Scrolledtext1.insert(END, '\nValue: ' + str(val))
            self.Scrolledtext1.insert(END, '\nMath function: ' + str(calcfunction))
            self.Scrolledtext1.insert(END, '\nNew columnname: ' + str(newcolname))
            self.Scrolledtext1.insert(END, '\n')
            self.Scrolledtext1.insert(END, 30*'#')
            print(df)
            
            ##Tabelle darstellen            
            self.frame1.grid_columnconfigure(0, weight = 1)
            self.frame1.grid_rowconfigure(0, weight = 1)
            self.sheet = Sheet(self.frame1,
                               data=df.values.tolist())
            
            self.sheet.headers(df.columns)
                
            self.sheet.enable_bindings()
            self.frame1.grid(row = 0, column = 0, sticky = "nswe")
            self.sheet.grid(row = 0, column = 0, sticky = "nswe")
            

        
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1078x688+239+0")
        top.minsize(1, 1)
        top.maxsize(1351, 738)
        top.resizable(1,  1)
        top.title("CSVpySTAT v0.3")
        top.configure(highlightcolor="black")

        self.top = top
        self.combobox = tk.StringVar()

        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=
            [('selected', _compcolor), ('active',_ana2color)])
        
        
        
        self.TNotebook1 = ttk.Notebook(self.top)
        self.TNotebook1.place(relx=0.019, rely=0.015, relheight=0.459
                , relwidth=0.948)
        self.TNotebook1.configure(takefocus="")
        
        ###Definition of Tabs
        
        
        self.TNotebook1_t13 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t13, padding=4)
        self.TNotebook1.tab(0, text='''New DF''', compound="left"
                ,underline='''-1''', )
        
        
        self.TNotebook1_t1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=4)
        self.TNotebook1.tab(1, text='''CSV Load''', compound="left"
                ,underline='''-1''', )
                
        
        self.TNotebook1_t5 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t5, padding=4)
        self.TNotebook1.tab(2, text='''Datatable''', compound="left"
                ,underline='''-1''', )
        self.TNotebook1_t5.grid_columnconfigure(0, weight = 1)
        self.TNotebook1_t5.grid_rowconfigure(0, weight = 1)
    
        
        self.TNotebook1_t2 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t2, padding=4)
        self.TNotebook1.tab(3, text='''Format table''', compound="left"
                ,underline='''-1''', )
        
        self.TNotebook1_t4 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t4, padding=4)
        self.TNotebook1.tab(4, text='''join/append''', compound="left"
                ,underline='''-1''', )

        
        self.TNotebook1_t3 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t3, padding=4)
        self.TNotebook1.tab(5, text='''Graph''', compound="left"
                ,underline='''-1''', )
               
        
        self.TNotebook1_t6 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t6, padding=4)
        self.TNotebook1.tab(6, text='''Statistics''', compound="left"
                ,underline='''-1''', )
        
        
        self.TNotebook1_t8 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t8, padding=4)
        self.TNotebook1.tab(7, text='''Simple Math''', compound="left"
                ,underline='''-1''', )
        
        
        self.TNotebook1_t7 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t7, padding=4)
        self.TNotebook1.tab(8, text='''Table Functions''', compound="left"
                ,underline='''-1''', )
        
        
        
        self.TNotebook1_t9 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t9, padding=4)
        self.TNotebook1.tab(9, text='''Modify DF''', compound="left"
                ,underline='''-1''', )
        
        self.TNotebook1_t12 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t12, padding=4)
        self.TNotebook1.tab(10, text='''Modify date''', compound="left"
                ,underline='''-1''', )
        
        
        self.TNotebook1_t10 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t10, padding=4)
        self.TNotebook1.tab(11, text='''Save CSV''', compound="left"
                ,underline='''-1''', )
        
        
        self.TNotebook1_t11 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t11, padding=4)
        self.TNotebook1.tab(12, text='''Info''', compound="left"
                ,underline='''-1''', )
        
        
        ###############################################################
        ##tab2 - Datatable (show the loaded dataframe into a grid)
        
        self.frame1 = tk.Frame(self.TNotebook1_t5)
        self.frame1.place(relx=0.0, rely=0.06, height=23, width=79)
        self.frame1.grid_columnconfigure(0, weight = 1)
        self.frame1.grid_rowconfigure(0, weight = 1)
        
        ##################################################################
        ###tab1 -CSV Load
        
        self.Entry1 = tk.Entry(self.TNotebook1_t1)
        self.Entry1.place(relx=0.133, rely=0.069, height=23, relwidth=0.182)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")

        self.Label1 = tk.Label(self.TNotebook1_t1)
        self.Label1.place(relx=0.02, rely=0.069, height=21, width=79)
        self.Label1.configure(anchor='w')
        self.Label1.configure(compound='left')
        self.Label1.configure(text='''Filename:''')

        self.Button1 = tk.Button(self.TNotebook1_t1)
        self.Button1.place(relx=0.333, rely=0.069, height=23, width=43)
        self.Button1.configure(borderwidth="2")
        self.Button1.configure(compound='left')
        self.Button1.configure(command=file_open)
        self.Button1.configure(text='''...''')

        self.Button5 = tk.Button(self.TNotebook1_t1)
        self.Button5.place(relx=0.270, rely=0.85, height=23, width=100)
        self.Button5.configure(borderwidth="2")
        self.Button5.configure(compound='left')
        self.Button5.configure(command=read_csv)
        self.Button5.configure(text='''import csv''')
        

        self.Label2 = tk.Label(self.TNotebook1_t1)
        self.Label2.place(relx=0.02, rely=0.241, height=21, width=89)
        self.Label2.configure(anchor='w')
        self.Label2.configure(compound='left')
        self.Label2.configure(text='''Delimeter:''')

        self.TCombobox1 = ttk.Combobox(self.TNotebook1_t1)
        self.TCombobox1.place(relx=0.137, rely=0.241, relheight=0.072
                , relwidth=0.08)
        self.value_list1 = [',',';','space','tab']
        self.TCombobox1.configure(values=self.value_list1)
        self.TCombobox1.configure(takefocus="")

        self.Label3 = tk.Label(self.TNotebook1_t1)
        self.Label3.place(relx=0.02, rely=0.414, height=21, width=63)
        self.Label3.configure(anchor='w')
        self.Label3.configure(compound='left')
        self.Label3.configure(text='''Coma:''')

        self.TCombobox2 = ttk.Combobox(self.TNotebook1_t1)
        self.TCombobox2.place(relx=0.137, rely=0.414, relheight=0.072
                , relwidth=0.06)
        self.value_list2 = ['.',',']
        self.TCombobox2.configure(values=self.value_list2)
        self.TCombobox2.configure(takefocus="")

        self.Scrolledtext2 = ScrolledText(self.TNotebook1_t1)
        self.Scrolledtext2.place(relx=0.402, rely=0.034, relheight=0.934
                , relwidth=0.59)
        self.Scrolledtext2.configure(background="white")
        self.Scrolledtext2.configure(font="TkTextFont")
        self.Scrolledtext2.configure(insertborderwidth="3")
        self.Scrolledtext2.configure(selectbackground="blue")
        self.Scrolledtext2.configure(selectforeground="white")
        self.Scrolledtext2.configure(wrap="none")

        self.Label4 = tk.Label(self.TNotebook1_t1)
        self.Label4.place(relx=0.02, rely=0.586, height=21, width=70)
        self.Label4.configure(anchor='w')
        self.Label4.configure(compound='left')
        self.Label4.configure(text='''Header:''')

        self.TCombobox3 = ttk.Combobox(self.TNotebook1_t1)
        self.TCombobox3.place(relx=0.137, rely=0.572, relheight=0.072
                , relwidth=0.06)
        self.value_list3 = ['yes','no']
        self.TCombobox3.configure(values=self.value_list3)
        self.TCombobox3.configure(takefocus="")
        
        
        var1 = tk.IntVar()
        self.Checkbutton1 = tk.Checkbutton(self.TNotebook1_t1)
        self.Checkbutton1.place(relx=0.08, rely=0.700, relheight=0.047
                , relwidth=0.3)
        self.Checkbutton1.configure(activebackground="#f9f9f9")
        self.Checkbutton1.configure(justify='left')
        self.Checkbutton1.configure(text='''load Data without tableview''')
        self.Checkbutton1.configure(variable=var1, onvalue=1)
        
        
        ##################################################################      
        ###tab0 -New DF
        
        self.Label1301 = tk.Label(self.TNotebook1_t13)
        self.Label1301.place(relx=0.02, rely=0.03, height=21, width=150)
        self.Label1301.configure(anchor='w')
        self.Label1301.configure(compound='left')
        self.Label1301.configure(text='''New Dataframe:''')
        
        self.Label1302 = tk.Label(self.TNotebook1_t13)
        self.Label1302.place(relx=0.02, rely=0.15, height=21, width=79)
        self.Label1302.configure(anchor='w')
        self.Label1302.configure(compound='left')
        self.Label1302.configure(text='''Columns:''')
        
        self.Entry1302 = tk.Entry(self.TNotebook1_t13)
        self.Entry1302.place(relx=0.133, rely=0.15, height=23, relwidth=0.08)
        self.Entry1302.configure(background="white")
        self.Entry1302.configure(font="TkFixedFont")

        self.Label1303 = tk.Label(self.TNotebook1_t13)
        self.Label1303.place(relx=0.02, rely=0.3, height=21, width=79)
        self.Label1303.configure(anchor='w')
        self.Label1303.configure(compound='left')
        self.Label1303.configure(text='''Rows:''')
        
        self.Entry1303 = tk.Entry(self.TNotebook1_t13)
        self.Entry1303.place(relx=0.133, rely=0.3, height=23, relwidth=0.08)
        self.Entry1303.configure(background="white")
        self.Entry1303.configure(font="TkFixedFont")

        self.Button131 = tk.Button(self.TNotebook1_t13)
        self.Button131.place(relx=0.13, rely=0.45, height=23, width=85)
        self.Button131.configure(borderwidth="2")
        self.Button131.configure(compound='left')
        self.Button131.configure(command=create_df)
        self.Button131.configure(text='''create DF''')
        
        #change Column Name
        self.Label1305 = tk.Label(self.TNotebook1_t13)
        self.Label1305.place(relx=0.35, rely=0.03, height=21, width=150)
        self.Label1305.configure(anchor='w')
        self.Label1305.configure(compound='left')
        self.Label1305.configure(text='''Define Column Name:''')
        
        self.Label1306 = tk.Label(self.TNotebook1_t13)
        self.Label1306.place(relx=0.35, rely=0.15, height=21, width=79)
        self.Label1306.configure(anchor='w')
        self.Label1306.configure(compound='left')
        self.Label1306.configure(text='''Columns Nr:''')
        
        self.TCombobox1306 = ttk.Combobox(self.TNotebook1_t13)
        self.TCombobox1306.place(relx=0.5, rely=0.15, relheight=0.08
                , relwidth=0.1)
        self.TCombobox1306.configure(takefocus="")

        self.Label1307 = tk.Label(self.TNotebook1_t13)
        self.Label1307.place(relx=0.35, rely=0.30, height=21, width=100)
        self.Label1307.configure(anchor='w')
        self.Label1307.configure(compound='left')
        self.Label1307.configure(text='''Column Name:''')
        
        self.Entry1307 = tk.Entry(self.TNotebook1_t13)
        self.Entry1307.place(relx=0.5, rely=0.3, height=23, relwidth=0.15)
        self.Entry1307.configure(background="white")
        self.Entry1307.configure(font="TkFixedFont")

        self.Button1307 = tk.Button(self.TNotebook1_t13)
        self.Button1307.place(relx=0.5, rely=0.45, height=23, width=100)
        self.Button1307.configure(borderwidth="2")
        self.Button1307.configure(compound='left')
        self.Button1307.configure(command=create_CN)
        self.Button1307.configure(text='''Define CN''')

        
        
        ##tab3- Format table
        ##change format
        self.Label110 = tk.Label(self.TNotebook1_t2)
        self.Label110.place(relx=0.02, rely=0.034, height=21, width=150)
        self.Label110.configure(anchor='w')
        self.Label110.configure(compound='left')
        self.Label110.configure(text='''Change Format:''')
        
        

        self.Label10 = tk.Label(self.TNotebook1_t2)
        self.Label10.place(relx=0.02, rely=0.15, height=21, width=74)
        self.Label10.configure(anchor='w')
        self.Label10.configure(compound='left')
        self.Label10.configure(text='''Column:''')

        self.TCombobox9 = ttk.Combobox(self.TNotebook1_t2)
        self.TCombobox9.place(relx=0.175, rely=0.15, relheight=0.072
                , relwidth=0.175)
        self.TCombobox9.configure(takefocus="")

        self.Button5 = tk.Button(self.TNotebook1_t2)
        self.Button5.place(relx=0.25, rely=0.3, height=25, width=25)
        self.Button5.configure(borderwidth="2")
        self.Button5.configure(compound='left')
        self.Button5.configure(command=current_format)
        self.Button5.configure(text='''...''')
        
        
        self.Label11 = tk.Label(self.TNotebook1_t2)
        self.Label11.place(relx=0.02, rely=0.3, height=21, width=115)
        self.Label11.configure(anchor='w')
        self.Label11.configure(compound='left')
        self.Label11.configure(text='''Current Format:''')

        self.Label12 = tk.Label(self.TNotebook1_t2)
        self.Label12.place(relx=0.175, rely=0.3, height=21, width=80)
        self.Label12.configure(anchor='w')
        self.Label12.configure(compound='left')
        self.Label12.configure(text='''Format''')

        self.Label13 = tk.Label(self.TNotebook1_t2)
        self.Label13.place(relx=0.02, rely=0.45, height=21, width=139)
        self.Label13.configure(anchor='w')
        self.Label13.configure(compound='left')
        self.Label13.configure(text='''choose new Format:''')

        self.TCombobox10 = ttk.Combobox(self.TNotebook1_t2)
        self.TCombobox10.place(relx=0.175, rely=0.45, relheight=0.072
                , relwidth=0.174)
        self.value_list4 = ['int','float','object','string', 'datetime']
        self.TCombobox10.configure(values=self.value_list4)
        self.TCombobox10.configure(takefocus="")

        self.Button4 = tk.Button(self.TNotebook1_t2)
        self.Button4.place(relx=0.175, rely=0.6, height=33, width=123)
        self.Button4.configure(borderwidth="2")
        self.Button4.configure(compound='left')
        self.Button4.configure(text='''set new format''')
        self.Button4.configure(command = change_format)
        
        ##set filter into column
        
        self.Label140 = tk.Label(self.TNotebook1_t2)
        self.Label140.place(relx=0.4, rely=0.034, height=21, width=139)
        self.Label140.configure(anchor='w')
        self.Label140.configure(compound='left')
        self.Label140.configure(text='''Set filters:''')
        
        self.Label14 = tk.Label(self.TNotebook1_t2)
        self.Label14.place(relx=0.4, rely=0.150, height=21, width=139)
        self.Label14.configure(anchor='w')
        self.Label14.configure(compound='left')
        self.Label14.configure(text='''Filter Column:''')
        
        self.TCombobox11 = ttk.Combobox(self.TNotebook1_t2)
        self.TCombobox11.place(relx=0.50, rely=0.150, relheight=0.072
                , relwidth=0.175)
        self.TCombobox11.configure(takefocus="")
        
        
        self.Label15 = tk.Label(self.TNotebook1_t2)
        self.Label15.place(relx=0.4, rely=0.3, height=21, width=139)
        self.Label15.configure(anchor='w')
        self.Label15.configure(compound='left')
        self.Label15.configure(text='''Criterium:''')
        
        self.TCombobox12 = ttk.Combobox(self.TNotebook1_t2)
        self.TCombobox12.place(relx=0.50, rely=0.3, relheight=0.072
                , relwidth=0.08 )
        self.value_list5 = ['==', '>=', '<=', '!=']
        self.TCombobox12.configure(values=self.value_list5)
        self.TCombobox12.configure(takefocus="")
        
        
        self.Label16 = tk.Label(self.TNotebook1_t2)
        self.Label16.place(relx=0.4, rely=0.45, height=21, width=60)
        self.Label16.configure(anchor='w')
        self.Label16.configure(compound='left')
        self.Label16.configure(text='''Content:''')
        
        self.Button8 = tk.Button(self.TNotebook1_t2)
        self.Button8.place(relx=0.65, rely=0.3, height=33, width=30)
        self.Button8.configure(borderwidth="2")
        self.Button8.configure(compound='left')
        self.Button8.configure(text='''...''')
        self.Button8.configure(command = filter_col)
        
        
        self.TCombobox13 = ttk.Combobox(self.TNotebook1_t2)
        self.TCombobox13.place(relx=0.50, rely=0.45, relheight=0.072
                , relwidth=0.175)
        self.TCombobox13.configure(takefocus="")
        
        self.Button6 = tk.Button(self.TNotebook1_t2)
        self.Button6.place(relx=0.5, rely=0.6, height=33, width=123)
        self.Button6.configure(borderwidth="2")
        self.Button6.configure(compound='left')
        self.Button6.configure(text='''set new filter''')
        self.Button6.configure(command = set_filter)
        
        ## Sort table by column
        
        self.Label170 = tk.Label(self.TNotebook1_t2)
        self.Label170.place(relx=0.7, rely=0.034, height=21, width=139)
        self.Label170.configure(anchor='w')
        self.Label170.configure(compound='left')
        self.Label170.configure(text='''Sort table by Column:''')
        
        
        self.Label17 = tk.Label(self.TNotebook1_t2)
        self.Label17.place(relx=0.7, rely=0.15, height=21, width=139)
        self.Label17.configure(anchor='w')
        self.Label17.configure(compound='left')
        self.Label17.configure(text='''Sort Column:''')
        
        self.TCombobox14 = ttk.Combobox(self.TNotebook1_t2)
        self.TCombobox14.place(relx=0.80, rely=0.15, relheight=0.072
                , relwidth=0.175)
        
        self.TCombobox14.configure(takefocus="")
        
        
        self.Label18 = tk.Label(self.TNotebook1_t2)
        self.Label18.place(relx=0.7, rely=0.3, height=21, width=139)
        self.Label18.configure(anchor='w')
        self.Label18.configure(compound='left')
        self.Label18.configure(text='''direction''')
        
        self.TCombobox15 = ttk.Combobox(self.TNotebook1_t2)
        self.TCombobox15.place(relx=0.80, rely=0.3, relheight=0.072
                , relwidth=0.09)
        self.value_list6 = ['AZ', 'ZA']
        self.TCombobox15.configure(values=self.value_list6)
        self.TCombobox15.configure(takefocus="")
        
        self.Button7 = tk.Button(self.TNotebook1_t2)
        self.Button7.place(relx=0.8, rely=0.45, height=33, width=123)
        self.Button7.configure(borderwidth="2")
        self.Button7.configure(compound='left')
        self.Button7.configure(text='''sort''')
        self.Button7.configure(command = sort_column)
        
        ###################################################
        
        ##Tab5 - Graph
        
        self.Label51 = tk.Label(self.TNotebook1_t3)
        self.Label51.place(relx=0.02, rely=0.034, height=21, width=150)
        self.Label51.configure(anchor='w')
        self.Label51.configure(compound='left')
        self.Label51.configure(text='''Plot Functions:''')
        
        self.Label5 = tk.Label(self.TNotebook1_t3)
        self.Label5.place(relx=0.02, rely=0.172, height=21, width=112)
        self.Label5.configure(anchor='w')
        self.Label5.configure(compound='left')
        self.Label5.configure(text='''Y Value Column:''')

        self.TCombobox4 = ttk.Combobox(self.TNotebook1_t3)
        self.TCombobox4.place(relx=0.131, rely=0.172, relheight=0.072
                , relwidth=0.175)
        self.TCombobox4.configure(takefocus="")

        self.Label6 = tk.Label(self.TNotebook1_t3)
        self.Label6.place(relx=0.02, rely=0.3, height=21, width=100)
        self.Label6.configure(anchor='w')
        self.Label6.configure(compound='left')
        self.Label6.configure(text='''X Axis Column:''')

        self.TCombobox5 = ttk.Combobox(self.TNotebook1_t3)
        self.TCombobox5.place(relx=0.131, rely=0.3, relheight=0.072
                , relwidth=0.175)
        self.TCombobox5.configure(takefocus="")

        self.Label7 = tk.Label(self.TNotebook1_t3)
        self.Label7.place(relx=0.02, rely=0.45, height=21, width=110)
        self.Label7.configure(anchor='w')
        self.Label7.configure(compound='left')
        self.Label7.configure(text='''Group Column:''')

        self.TCombobox6 = ttk.Combobox(self.TNotebook1_t3)
        self.TCombobox6.place(relx=0.131, rely=0.45, relheight=0.072
                , relwidth=0.174)
        self.TCombobox6.configure(takefocus="")

        self.Label8 = tk.Label(self.TNotebook1_t3)
        self.Label8.place(relx=0.02, rely=0.6, height=21, width=79)
        self.Label8.configure(anchor='w')
        self.Label8.configure(compound='left')
        self.Label8.configure(text='''Diagram:''')

        self.TCombobox7 = ttk.Combobox(self.TNotebook1_t3)
        self.TCombobox7.place(relx=0.13, rely=0.6, relheight=0.072
                , relwidth=0.175)
        self.value_list10 = ['Countplot', 'Barplot', 'Pieplot', 'Pareto', 'Time Series Plot', 'Boxplot', 'Violinplot', 'Stripplot', 'Swarmplot','Error Bar Plot' ,'Scatterplot','Regressionplot']
        self.TCombobox7.configure(values=self.value_list10)
        self.TCombobox7.configure(takefocus="")

        

        self.Button2 = tk.Button(self.TNotebook1_t3)
        self.Button2.place(relx=0.52, rely=0.6, height=33, width=113)
        self.Button2.configure(borderwidth="2")
        self.Button2.configure(compound='left')
        self.Button2.configure(command = plot_df)
        self.Button2.configure(text='''Plot''')

        
        self.Label52 = tk.Label(self.TNotebook1_t3)
        self.Label52.place(relx=0.333, rely=0.034, height=21, width=150)
        self.Label52.configure(anchor='w')
        self.Label52.configure(compound='left')
        self.Label52.configure(text='''3D Plots:''')

        
        self.Label9 = tk.Label(self.TNotebook1_t3)
        self.Label9.place(relx=0.333, rely=0.172, height=21, width=118)
        self.Label9.configure(anchor='w')
        self.Label9.configure(compound='left')
        self.Label9.configure(text='''z Value Column:''')

        self.TCombobox8 = ttk.Combobox(self.TNotebook1_t3)
        self.TCombobox8.place(relx=0.451, rely=0.172, relheight=0.072
                , relwidth=0.175)
        self.TCombobox8.configure(takefocus="")
        
        self.Label53 = tk.Label(self.TNotebook1_t3)
        self.Label53.place(relx=0.7, rely=0.034, height=21, width=150)
        self.Label53.configure(anchor='w')
        self.Label53.configure(compound='left')
        self.Label53.configure(text='''Tolerances:''')
        
        self.Label54 = tk.Label(self.TNotebook1_t3)
        self.Label54.place(relx=0.7, rely=0.172, height=21, width=118)
        self.Label54.configure(anchor='w')
        self.Label54.configure(compound='left')
        self.Label54.configure(text='''Upper Tolerance:''')

        self.Entry54 = tk.Entry(self.TNotebook1_t3)
        self.Entry54.place(relx=0.85, rely=0.172, height=23, relwidth=0.1)
        self.Entry54.configure(background="white")
        self.Entry54.configure(font="TkFixedFont")
        
        self.Label55 = tk.Label(self.TNotebook1_t3)
        self.Label55.place(relx=0.7, rely=0.3, height=21, width=118)
        self.Label55.configure(anchor='w')
        self.Label55.configure(compound='left')
        self.Label55.configure(text='''Lower Tolerance:''')

        self.Entry55 = tk.Entry(self.TNotebook1_t3)
        self.Entry55.place(relx=0.85, rely=0.3, height=23, relwidth=0.1)
        self.Entry55.configure(background="white")
        self.Entry55.configure(font="TkFixedFont")
        
        #############################################################
        #Tab4 join/append
        
        self.Label1909 = tk.Label(self.TNotebook1_t4)
        self.Label1909.place(relx=0.02, rely=0.03, height=21, width=125)
        self.Label1909.configure(anchor='w')
        self.Label1909.configure(compound='left')
        self.Label1909.configure(text='''Read second File:''')
        
        self.Entry2 = tk.Entry(self.TNotebook1_t4)
        self.Entry2.place(relx=0.133, rely=0.15, height=23, relwidth=0.182)
        self.Entry2.configure(background="white")
        self.Entry2.configure(font="TkFixedFont")

        self.Label19 = tk.Label(self.TNotebook1_t4)
        self.Label19.place(relx=0.02, rely=0.15, height=21, width=79)
        self.Label19.configure(anchor='w')
        self.Label19.configure(compound='left')
        self.Label19.configure(text='''Filename:''')

        self.Button8 = tk.Button(self.TNotebook1_t4)
        self.Button8.place(relx=0.333, rely=0.15, height=23, width=43)
        self.Button8.configure(borderwidth="2")
        self.Button8.configure(compound='left')
        self.Button8.configure(command=file2_open)
        self.Button8.configure(text='''...''')

        self.Button9 = tk.Button(self.TNotebook1_t4)
        self.Button9.place(relx=0.250, rely=0.75, height=23, width=130)
        self.Button9.configure(borderwidth="2")
        self.Button9.configure(compound='left')
        self.Button9.configure(command=read2_csv)
        self.Button9.configure(text='''read second CSV''')
        

        self.Label20 = tk.Label(self.TNotebook1_t4)
        self.Label20.place(relx=0.02, rely=0.3, height=21, width=89)
        self.Label20.configure(anchor='w')
        self.Label20.configure(compound='left')
        self.Label20.configure(text='''Delimeter:''')

        self.TCombobox16 = ttk.Combobox(self.TNotebook1_t4)
        self.TCombobox16.place(relx=0.137, rely=0.3, relheight=0.072
                , relwidth=0.06)
        self.value_list6 = [',',';','space','tab']
        self.TCombobox16.configure(values=self.value_list6)
        self.TCombobox16.configure(takefocus="")

        self.Label21 = tk.Label(self.TNotebook1_t4)
        self.Label21.place(relx=0.02, rely=0.45, height=21, width=63)
        self.Label21.configure(anchor='w')
        self.Label21.configure(compound='left')
        self.Label21.configure(text='''Coma:''')

        self.TCombobox17 = ttk.Combobox(self.TNotebook1_t4)
        self.TCombobox17.place(relx=0.137, rely=0.45, relheight=0.072
                , relwidth=0.06)
        #self.TCombobox2.configure(textvariable=self.combobox)
        self.value_list7 = ['.',',']
        self.TCombobox17.configure(values=self.value_list7)
        self.TCombobox17.configure(takefocus="")

        self.Label22 = tk.Label(self.TNotebook1_t4)
        self.Label22.place(relx=0.02, rely=0.6, height=21, width=70)
        self.Label22.configure(anchor='w')
        self.Label22.configure(compound='left')
        self.Label22.configure(text='''Header:''')

        self.TCombobox18 = ttk.Combobox(self.TNotebook1_t4)
        self.TCombobox18.place(relx=0.137, rely=0.6, relheight=0.072
                , relwidth=0.06)
        #self.TCombobox3.configure(textvariable=self.combobox)
        self.value_list8 = ['yes','no']
        self.TCombobox18.configure(values=self.value_list8)
        self.TCombobox18.configure(takefocus="")

        ## merge
        
        self.Label1919 = tk.Label(self.TNotebook1_t4)
        self.Label1919.place(relx=0.4, rely=0.03, height=21, width=125)
        self.Label1919.configure(anchor='w')
        self.Label1919.configure(compound='left')
        self.Label1919.configure(text='''Join File:''')
        
        self.Label24 = tk.Label(self.TNotebook1_t4)
        self.Label24.place(relx=0.4, rely=0.15, height=21, width=125)
        self.Label24.configure(anchor='w')
        self.Label24.configure(compound='left')
        self.Label24.configure(text='''Key Column:''')

        self.TCombobox20 = ttk.Combobox(self.TNotebook1_t4)
        self.TCombobox20.place(relx=0.53, rely=0.15, relheight=0.072
                , relwidth=0.17)
        #self.TCombobox3.configure(textvariable=self.combobox)
        self.TCombobox20.configure(takefocus="")

        self.Label25 = tk.Label(self.TNotebook1_t4)
        self.Label25.place(relx=0.4, rely=0.3, height=21, width=125)
        self.Label25.configure(anchor='w')
        self.Label25.configure(compound='left')
        self.Label25.configure(text='''How to join:''')

        self.TCombobox21 = ttk.Combobox(self.TNotebook1_t4)
        self.TCombobox21.place(relx=0.53, rely=0.3, relheight=0.072
                , relwidth=0.10)
        self.value_list9 = ['inner','left outer', 'right outer', 'full outer']
        self.TCombobox21.configure(values=self.value_list9)
        #self.TCombobox3.configure(textvariable=self.combobox)
        self.TCombobox21.configure(takefocus="")
        
        self.Button10 = tk.Button(self.TNotebook1_t4)
        self.Button10.place(relx=0.58, rely=0.85, height=23, width=130)
        self.Button10.configure(borderwidth="2")
        self.Button10.configure(compound='left')
        self.Button10.configure(command=join_table)
        self.Button10.configure(text='''join table''')
        
        self.Button11 = tk.Button(self.TNotebook1_t4)
        self.Button11.place(relx=0.8, rely=0.85, height=23, width=130)
        self.Button11.configure(borderwidth="2")
        self.Button11.configure(compound='left')
        self.Button11.configure(command=append_CSV)
        self.Button11.configure(text='''append table''')
        
        self.Label1929 = tk.Label(self.TNotebook1_t4)
        self.Label1929.place(relx=0.8, rely=0.03, height=21, width=125)
        self.Label1929.configure(anchor='w')
        self.Label1929.configure(compound='left')
        self.Label1929.configure(text='''Append File:''')
        
        
        self.Button12 = tk.Button(self.TNotebook1_t4)
        self.Button12.place(relx=0.25, rely=0.85, height=23, width=130)
        self.Button12.configure(borderwidth="2")
        self.Button12.configure(compound='left')
        self.Button12.configure(command=save_CSV)
        self.Button12.configure(text='''save file''')
        
        ####################################################################
        ##Tab6 - Statistics
        
        self.Button3 = tk.Button(self.TNotebook1_t6)
        self.Button3.place(relx=0.70, rely=0.15, height=33, width=200)
        self.Button3.configure(borderwidth="2")
        self.Button3.configure(compound='left')
        self.Button3.configure(command=table_statistics)
        self.Button3.configure(text='''Whoole Table Statitics''')
        
        self.Button300 = tk.Button(self.TNotebook1_t6)
        self.Button300.place(relx=0.70, rely=0.3, height=33, width=200)
        self.Button300.configure(borderwidth="2")
        self.Button300.configure(compound='left')
        self.Button300.configure(command=table_correlation)
        self.Button300.configure(text='''Whoole Table Correlation''')
        
        self.Label61 = tk.Label(self.TNotebook1_t6)
        self.Label61.place(relx=0.02, rely=0.034, height=21, width=200)
        self.Label61.configure(anchor='w')
        self.Label61.configure(compound='left')
        self.Label61.configure(text='''Statistic one Column:''')
        
        self.Label62 = tk.Label(self.TNotebook1_t6)
        self.Label62.place(relx=0.02, rely=0.172, height=21, width=112)
        self.Label62.configure(anchor='w')
        self.Label62.configure(compound='left')
        self.Label62.configure(text='''Value Column:''')

        self.TCombobox62 = ttk.Combobox(self.TNotebook1_t6)
        self.TCombobox62.place(relx=0.131, rely=0.172, relheight=0.072
                , relwidth=0.175)
        self.TCombobox62.configure(takefocus="")

        self.Label63 = tk.Label(self.TNotebook1_t6)
        self.Label63.place(relx=0.02, rely=0.3, height=21, width=100)
        self.Label63.configure(anchor='w')
        self.Label63.configure(compound='left')
        self.Label63.configure(text='''Easy Statistics:''')

        self.TCombobox63 = ttk.Combobox(self.TNotebook1_t6)
        self.TCombobox63.place(relx=0.131, rely=0.3, relheight=0.072
                , relwidth=0.175)
        self.value_list63 = ['Descriptive Statistics', 'Single Value Chart', 'Xbar/s-Chart', 'Capability Analysis', 'Histogram', 'QQ-Plot', 'Test of normal Distribution', 'Outlier-Test']
        self.TCombobox63.configure(values=self.value_list63)
        self.TCombobox63.configure(takefocus="")

        self.Label64 = tk.Label(self.TNotebook1_t6)
        self.Label64.place(relx=0.02, rely=0.45, height=21, width=110)
        self.Label64.configure(anchor='w')
        self.Label64.configure(compound='left')
        self.Label64.configure(text='''Tolerances:''')

        self.Label65 = tk.Label(self.TNotebook1_t6)
        self.Label65.place(relx=0.02, rely=0.60, height=21, width=70)
        self.Label65.configure(anchor='w')
        self.Label65.configure(compound='left')
        self.Label65.configure(text='''Lower Tol:''')
        
        self.Entry65 = tk.Entry(self.TNotebook1_t6)
        self.Entry65.place(relx=0.1, rely=0.6, height=23, relwidth=0.05)
        self.Entry65.configure(background="white")
        self.Entry65.configure(font="TkFixedFont")

        self.Label66 = tk.Label(self.TNotebook1_t6)
        self.Label66.place(relx=0.17, rely=0.60, height=21, width=70)
        self.Label66.configure(anchor='w')
        self.Label66.configure(compound='left')
        self.Label66.configure(text='''Upper Tol:''')
        
        self.Entry66 = tk.Entry(self.TNotebook1_t6)
        self.Entry66.place(relx=0.25, rely=0.6, height=23, relwidth=0.05)
        self.Entry66.configure(background="white")
        self.Entry66.configure(font="TkFixedFont")
        
        self.Label67 = tk.Label(self.TNotebook1_t6)
        self.Label67.place(relx=0.02, rely=0.75, height=21, width=100)
        self.Label67.configure(anchor='w')
        self.Label67.configure(compound='left')
        self.Label67.configure(text='''Sample Size:''')

        self.TCombobox67 = ttk.Combobox(self.TNotebook1_t6)
        self.TCombobox67.place(relx=0.131, rely=0.75, relheight=0.072
                , relwidth=0.1)
        self.value_list67 = ['2', '3','4', '5', '6', '7', '8', '9', '10']
        self.TCombobox67.configure(values=self.value_list67)
        self.TCombobox67.configure(takefocus="")
        

        self.Button66 = tk.Button(self.TNotebook1_t6)
        self.Button66.place(relx=0.2, rely=0.85, height=33, width=113)
        self.Button66.configure(borderwidth="2")
        self.Button66.configure(compound='left')
        self.Button66.configure(command = plot_stat)
        self.Button66.configure(text='''Plot''')
        
        #Linear Regression
        self.Label71 = tk.Label(self.TNotebook1_t6)
        self.Label71.place(relx=0.35, rely=0.034, height=21, width=200)
        self.Label71.configure(anchor='w')
        self.Label71.configure(compound='left')
        self.Label71.configure(text='''Linear Regression:''')
        
        self.Label72 = tk.Label(self.TNotebook1_t6)
        self.Label72.place(relx=0.35, rely=0.172, height=21, width=112)
        self.Label72.configure(anchor='w')
        self.Label72.configure(compound='left')
        self.Label72.configure(text='''y Value Column:''')

        self.TCombobox72 = ttk.Combobox(self.TNotebook1_t6)
        self.TCombobox72.place(relx=0.47, rely=0.172, relheight=0.072
                , relwidth=0.175)
        self.TCombobox72.configure(takefocus="")

        self.Label73 = tk.Label(self.TNotebook1_t6)
        self.Label73.place(relx=0.35, rely=0.3, height=21, width=100)
        self.Label73.configure(anchor='w')
        self.Label73.configure(compound='left')
        self.Label73.configure(text='''x Value Column:''')

        self.TCombobox73 = ttk.Combobox(self.TNotebook1_t6)
        self.TCombobox73.place(relx=0.47, rely=0.3, relheight=0.072
                , relwidth=0.175)
        self.TCombobox73.configure(takefocus="")
        
        self.Button74 = tk.Button(self.TNotebook1_t6)
        self.Button74.place(relx=0.53, rely=0.5, height=33, width=113)
        self.Button74.configure(borderwidth="2")
        self.Button74.configure(compound='left')
        self.Button74.configure(command = plot_L_Reg)
        self.Button74.configure(text='''Plot''')
        
        ####################################################################
        ##tab8 -Table Functions
        
        ##sequence nr
        self.Label81 = tk.Label(self.TNotebook1_t7)
        self.Label81.place(relx=0.02, rely=0.034, height=21, width=250)
        self.Label81.configure(anchor='w')
        self.Label81.configure(compound='left')
        self.Label81.configure(text='''create sequence number column:''')
        
        self.Label82 = tk.Label(self.TNotebook1_t7)
        self.Label82.place(relx=0.02, rely=0.15, height=21, width=200)
        self.Label82.configure(anchor='w')
        self.Label82.configure(compound='left')
        self.Label82.configure(text='''start number:''')
        
        self.Entry82 = tk.Entry(self.TNotebook1_t7)
        self.Entry82.place(relx=0.133, rely=0.150, height=23, relwidth=0.1)
        self.Entry82.configure(background="white")
        self.Entry82.configure(font="TkFixedFont")
        
        self.Label83 = tk.Label(self.TNotebook1_t7)
        self.Label83.place(relx=0.02, rely=0.3, height=21, width=200)
        self.Label83.configure(anchor='w')
        self.Label83.configure(compound='left')
        self.Label83.configure(text='''column name:''')
        
        self.Entry83 = tk.Entry(self.TNotebook1_t7)
        self.Entry83.place(relx=0.133, rely=0.3, height=23, relwidth=0.1)
        self.Entry83.configure(background="white")
        self.Entry83.configure(font="TkFixedFont")
        
        
        
        self.Button81 = tk.Button(self.TNotebook1_t7)
        self.Button81.place(relx=0.02, rely=0.45, height=33, width=113)
        self.Button81.configure(borderwidth="2")
        self.Button81.configure(compound='left')
        self.Button81.configure(command = seq_nr)
        self.Button81.configure(text='''Build # Column''')
        
        ##combine column
        self.Label84 = tk.Label(self.TNotebook1_t7)
        self.Label84.place(relx=0.30, rely=0.034, height=21, width=250)
        self.Label84.configure(anchor='w')
        self.Label84.configure(compound='left')
        self.Label84.configure(text='''combine column:''')
        
        self.Label85 = tk.Label(self.TNotebook1_t7)
        self.Label85.place(relx=0.30, rely=0.15, height=21, width=112)
        self.Label85.configure(anchor='w')
        self.Label85.configure(compound='left')
        self.Label85.configure(text='''first Column:''')

        self.TCombobox85= ttk.Combobox(self.TNotebook1_t7)
        self.TCombobox85.place(relx=0.42, rely=0.15, relheight=0.072
                , relwidth=0.175)
        self.TCombobox85.configure(takefocus="")

        self.Label86 = tk.Label(self.TNotebook1_t7)
        self.Label86.place(relx=0.30, rely=0.3, height=21, width=112)
        self.Label86.configure(anchor='w')
        self.Label86.configure(compound='left')
        self.Label86.configure(text='''second Column:''')

        self.TCombobox86= ttk.Combobox(self.TNotebook1_t7)
        self.TCombobox86.place(relx=0.42, rely=0.30, relheight=0.072
                , relwidth=0.175)
        self.TCombobox86.configure(takefocus="")        
        
        self.Label87 = tk.Label(self.TNotebook1_t7)
        self.Label87.place(relx=0.3, rely=0.45, height=21, width=200)
        self.Label87.configure(anchor='w')
        self.Label87.configure(compound='left')
        self.Label87.configure(text='''column name:''')
        
        self.Entry87 = tk.Entry(self.TNotebook1_t7)
        self.Entry87.place(relx=0.42, rely=0.45, height=23, relwidth=0.1)
        self.Entry87.configure(background="white")
        self.Entry87.configure(font="TkFixedFont")

        self.Button89 = tk.Button(self.TNotebook1_t7)
        self.Button89.place(relx=0.3, rely=0.6, height=33, width=113)
        self.Button89.configure(borderwidth="2")
        self.Button89.configure(compound='left')
        self.Button89.configure(command = combine_column)
        self.Button89.configure(text='''Build Column''')
        
        ## split column

        self.Label90 = tk.Label(self.TNotebook1_t7)
        self.Label90.place(relx=0.65, rely=0.034, height=21, width=250)
        self.Label90.configure(anchor='w')
        self.Label90.configure(compound='left')
        self.Label90.configure(text='''split column:''')
        
        self.Label91 = tk.Label(self.TNotebook1_t7)
        self.Label91.place(relx=0.65, rely=0.15, height=21, width=112)
        self.Label91.configure(anchor='w')
        self.Label91.configure(compound='left')
        self.Label91.configure(text='''Column:''')

        self.TCombobox91= ttk.Combobox(self.TNotebook1_t7)
        self.TCombobox91.place(relx=0.75, rely=0.15, relheight=0.072
                , relwidth=0.175)
        self.TCombobox91.configure(takefocus="")

        self.Label92 = tk.Label(self.TNotebook1_t7)
        self.Label92.place(relx=0.65, rely=0.3, height=21, width=200)
        self.Label92.configure(anchor='w')
        self.Label92.configure(compound='left')
        self.Label92.configure(text='''Sepeator:''')
        
        self.Entry92 = tk.Entry(self.TNotebook1_t7)
        self.Entry92.place(relx=0.75, rely=0.3, height=23, relwidth=0.1)
        self.Entry92.configure(background="white")
        self.Entry92.configure(font="TkFixedFont")

        self.Button92 = tk.Button(self.TNotebook1_t7)
        self.Button92.place(relx=0.65, rely=0.6, height=33, width=113)
        self.Button92.configure(borderwidth="2")
        self.Button92.configure(compound='left')
        self.Button92.configure(command = split_column)
        self.Button92.configure(text='''Split Column''')
        
        ###################################################################
        #tab 7 - Simple Math = Col Calculate + Crosstable + Contingency Table
 
        # column math with 2 columns
        self.Label801 = tk.Label(self.TNotebook1_t8)
        self.Label801.place(relx=0.03, rely=0.034, height=21, width=250)
        self.Label801.configure(anchor='w')
        self.Label801.configure(compound='left')
        self.Label801.configure(text='''Calculate 2 Columns:''')
        
        self.Label802 = tk.Label(self.TNotebook1_t8)
        self.Label802.place(relx=0.03, rely=0.15, height=21, width=112)
        self.Label802.configure(anchor='w')
        self.Label802.configure(compound='left')
        self.Label802.configure(text='''Column 1:''')

        self.TCombobox802= ttk.Combobox(self.TNotebook1_t8)
        self.TCombobox802.place(relx=0.12, rely=0.15, relheight=0.072
                , relwidth=0.175)
        self.TCombobox802.configure(takefocus="")
        
        self.Label803 = tk.Label(self.TNotebook1_t8)
        self.Label803.place(relx=0.03, rely=0.3, height=21, width=112)
        self.Label803.configure(anchor='w')
        self.Label803.configure(compound='left')
        self.Label803.configure(text='''Column 2:''')

        self.TCombobox803= ttk.Combobox(self.TNotebook1_t8)
        self.TCombobox803.place(relx=0.12, rely=0.3, relheight=0.072
                , relwidth=0.175)
        self.TCombobox803.configure(takefocus="")
        
        self.Label804 = tk.Label(self.TNotebook1_t8)
        self.Label804.place(relx=0.03, rely=0.45, height=21, width=112)
        self.Label804.configure(anchor='w')
        self.Label804.configure(compound='left')
        self.Label804.configure(text='''Math Function:''')

        self.TCombobox804= ttk.Combobox(self.TNotebook1_t8)
        self.TCombobox804.place(relx=0.14, rely=0.45, relheight=0.072
                , relwidth=0.05)
        self.value_list804 = ['+', '-','*', '/']
        self.TCombobox804.configure(values=self.value_list804)
        self.TCombobox804.configure(takefocus="")

        self.Label805 = tk.Label(self.TNotebook1_t8)
        self.Label805.place(relx=0.03, rely=0.60, height=21, width=150)
        self.Label805.configure(anchor='w')
        self.Label805.configure(compound='left')
        self.Label805.configure(text='''Column Name:''')



        self.Entry804 = tk.Entry(self.TNotebook1_t8)
        self.Entry804.place(relx=0.14, rely=0.60, height=23, relwidth=0.15)
        self.Entry804.configure(background="white")
        self.Entry804.configure(font="TkFixedFont")


        self.Button800 = tk.Button(self.TNotebook1_t8)
        self.Button800.place(relx=0.12, rely=0.75, height=33, width=113)
        self.Button800.configure(borderwidth="2")
        self.Button800.configure(compound='left')
        self.Button800.configure(command = calc2cols)
        self.Button800.configure(text='''Calculate''')
        
        
        #Calculate Column with value
        
        self.Label805 = tk.Label(self.TNotebook1_t8)
        self.Label805.place(relx=0.35, rely=0.034, height=21, width=250)
        self.Label805.configure(anchor='w')
        self.Label805.configure(compound='left')
        self.Label805.configure(text='''Simple Calculation:''')
        
        self.Label806 = tk.Label(self.TNotebook1_t8)
        self.Label806.place(relx=0.35, rely=0.15, height=21, width=112)
        self.Label806.configure(anchor='w')
        self.Label806.configure(compound='left')
        self.Label806.configure(text='''Column :''')

        self.TCombobox806= ttk.Combobox(self.TNotebook1_t8)
        self.TCombobox806.place(relx=0.47, rely=0.15, relheight=0.072
                , relwidth=0.175)
        self.TCombobox806.configure(takefocus="")
        
        self.Label807 = tk.Label(self.TNotebook1_t8)
        self.Label807.place(relx=0.35, rely=0.3, height=21, width=112)
        self.Label807.configure(anchor='w')
        self.Label807.configure(compound='left')
        self.Label807.configure(text='''Value:''')

        self.Entry807 = tk.Entry(self.TNotebook1_t8)
        self.Entry807.place(relx=0.47, rely=0.30, height=23, relwidth=0.10)
        self.Entry807.configure(background="white")
        self.Entry807.configure(font="TkFixedFont")        




        self.Label808 = tk.Label(self.TNotebook1_t8)
        self.Label808.place(relx=0.35, rely=0.45, height=21, width=112)
        self.Label808.configure(anchor='w')
        self.Label808.configure(compound='left')
        self.Label808.configure(text='''Math Function:''')

        self.TCombobox808= ttk.Combobox(self.TNotebook1_t8)
        self.TCombobox808.place(relx=0.47, rely=0.45, relheight=0.072
                , relwidth=0.05)
        self.value_list808 = ['+', '-','*', '/', '^', 'sqrt']
        self.TCombobox808.configure(values=self.value_list808)
        self.TCombobox808.configure(takefocus="")

        self.Label809 = tk.Label(self.TNotebook1_t8)
        self.Label809.place(relx=0.35, rely=0.60, height=21, width=150)
        self.Label809.configure(anchor='w')
        self.Label809.configure(compound='left')
        self.Label809.configure(text='''Column Name:''')



        self.Entry809 = tk.Entry(self.TNotebook1_t8)
        self.Entry809.place(relx=0.47, rely=0.60, height=23, relwidth=0.15)
        self.Entry809.configure(background="white")
        self.Entry809.configure(font="TkFixedFont")


        self.Button801 = tk.Button(self.TNotebook1_t8)
        self.Button801.place(relx=0.47, rely=0.75, height=33, width=113)
        self.Button801.configure(borderwidth="2")
        self.Button801.configure(compound='left')
        self.Button801.configure(command = calccolvalue)
        self.Button801.configure(text='''Calculate''')
        
        
        
        
        
        #Crosstable
        self.Label101 = tk.Label(self.TNotebook1_t8)
        self.Label101.place(relx=0.7, rely=0.034, height=21, width=250)
        self.Label101.configure(anchor='w')
        self.Label101.configure(compound='left')
        self.Label101.configure(text='''crosstable:''')
        
        self.Label102 = tk.Label(self.TNotebook1_t8)
        self.Label102.place(relx=0.7, rely=0.15, height=21, width=112)
        self.Label102.configure(anchor='w')
        self.Label102.configure(compound='left')
        self.Label102.configure(text='''Column 1:''')

        self.TCombobox102= ttk.Combobox(self.TNotebook1_t8)
        self.TCombobox102.place(relx=0.82, rely=0.15, relheight=0.072
                , relwidth=0.175)
        self.TCombobox102.configure(takefocus="")
        
        self.Label103 = tk.Label(self.TNotebook1_t8)
        self.Label103.place(relx=0.7, rely=0.3, height=21, width=112)
        self.Label103.configure(anchor='w')
        self.Label103.configure(compound='left')
        self.Label103.configure(text='''Column 2:''')

        self.TCombobox103= ttk.Combobox(self.TNotebook1_t8)
        self.TCombobox103.place(relx=0.82, rely=0.3, relheight=0.072
                , relwidth=0.175)
        self.TCombobox103.configure(takefocus="")
        
        self.Label104 = tk.Label(self.TNotebook1_t8)
        self.Label104.place(relx=0.7, rely=0.45, height=21, width=112)
        self.Label104.configure(anchor='w')
        self.Label104.configure(compound='left')
        self.Label104.configure(text='''Option:''')

        self.TCombobox104= ttk.Combobox(self.TNotebook1_t8)
        self.TCombobox104.place(relx=0.79, rely=0.45, relheight=0.072
                , relwidth=0.200)
        self.value_list104 = ['cross sum table', 'cross sum table with total','cross percent table', 'cross percent table with total', 'contingency table']
        self.TCombobox104.configure(values=self.value_list104)
        self.TCombobox104.configure(takefocus="")

        self.Button100 = tk.Button(self.TNotebook1_t8)
        self.Button100.place(relx=0.82, rely=0.6, height=33, width=113)
        self.Button100.configure(borderwidth="2")
        self.Button100.configure(compound='left')
        self.Button100.configure(command = crosstable)
        self.Button100.configure(text='''Build Crosstable''')
        
        ##################################################################
        ##tab 9 Modify DF (dataframe)
        
        #delete
        self.Label201 = tk.Label(self.TNotebook1_t9)
        self.Label201.place(relx=0.03, rely=0.034, height=21, width=250)
        self.Label201.configure(anchor='w')
        self.Label201.configure(compound='left')
        self.Label201.configure(text='''Delete:''')
        
        self.Label212 = tk.Label(self.TNotebook1_t9)
        self.Label212.place(relx=0.03, rely=0.15, height=21, width=150)
        self.Label212.configure(anchor='w')
        self.Label212.configure(compound='left')
        self.Label212.configure(text='''Delete Option:''')
        
        self.TCombobox212= ttk.Combobox(self.TNotebook1_t9)
        self.TCombobox212.place(relx=0.20, rely=0.15, relheight=0.072
                , relwidth=0.200)
        self.value_list212 = ['whole dataframe', 'into column']
        self.TCombobox212.configure(values=self.value_list212)
        self.TCombobox212.configure(takefocus="")
        
        self.Label202 = tk.Label(self.TNotebook1_t9)
        self.Label202.place(relx=0.03, rely=0.3, height=21, width=150)
        self.Label202.configure(anchor='w')
        self.Label202.configure(compound='left')
        self.Label202.configure(text='''Delete Option:''')
        
        self.TCombobox202= ttk.Combobox(self.TNotebook1_t9)
        self.TCombobox202.place(relx=0.20, rely=0.3, relheight=0.072
                , relwidth=0.200)
        self.value_list202 = ['nan rows', 'empty rows','NA rows', 'zero rows', 'rows with special characters']
        self.TCombobox202.configure(values=self.value_list202)
        self.TCombobox202.configure(takefocus="")
        
        self.Label222 = tk.Label(self.TNotebook1_t9)
        self.Label222.place(relx=0.03, rely=0.45, height=21, width=150)
        self.Label222.configure(anchor='w')
        self.Label222.configure(compound='left')
        self.Label222.configure(text='''Column:''')
        
        self.TCombobox222= ttk.Combobox(self.TNotebook1_t9)
        self.TCombobox222.place(relx=0.20, rely=0.45, relheight=0.072
                , relwidth=0.200)
        self.TCombobox222.configure(takefocus="")
        
        
        
        self.Label203 = tk.Label(self.TNotebook1_t9)
        self.Label203.place(relx=0.03, rely=0.6, height=21, width=150)
        self.Label203.configure(anchor='w')
        self.Label203.configure(compound='left')
        self.Label203.configure(text='''special characteristic:''')
        
        self.Entry203 = tk.Entry(self.TNotebook1_t9)
        self.Entry203.place(relx=0.20, rely=0.6, height=23, relwidth=0.1)
        self.Entry203.configure(background="white")
        self.Entry203.configure(font="TkFixedFont")
        
        
        
        self.Button204 = tk.Button(self.TNotebook1_t9)
        self.Button204.place(relx=0.20, rely=0.75, height=33, width=113)
        self.Button204.configure(borderwidth="2")
        self.Button204.configure(compound='left')
        self.Button204.configure(command = delete_rows)
        self.Button204.configure(text='''Delete''')
        
        #replace
        
        self.Label205 = tk.Label(self.TNotebook1_t9)
        self.Label205.place(relx=0.5, rely=0.034, height=21, width=250)
        self.Label205.configure(anchor='w')
        self.Label205.configure(compound='left')
        self.Label205.configure(text='''Replace into Column:''')
        
        self.Label206 = tk.Label(self.TNotebook1_t9)
        self.Label206.place(relx=0.5, rely=0.15, height=21, width=150)
        self.Label206.configure(anchor='w')
        self.Label206.configure(compound='left')
        self.Label206.configure(text='''Replace Option:''')
        
        self.TCombobox206= ttk.Combobox(self.TNotebook1_t9)
        self.TCombobox206.place(relx=0.7, rely=0.15, relheight=0.072
                , relwidth=0.200)
        self.value_list206 = ['value','character', 'float to point comma', 'point to float comma','Column Name']
        self.TCombobox206.configure(values=self.value_list206)
        self.TCombobox206.configure(takefocus="")
        
        self.Label207 = tk.Label(self.TNotebook1_t9)
        self.Label207.place(relx=0.5, rely=0.3, height=21, width=150)
        self.Label207.configure(anchor='w')
        self.Label207.configure(compound='left')
        self.Label207.configure(text='''replace:''')
        
        self.Entry207 = tk.Entry(self.TNotebook1_t9)
        self.Entry207.place(relx=0.70, rely=0.3, height=23, relwidth=0.1)
        self.Entry207.configure(background="white")
        self.Entry207.configure(font="TkFixedFont")
        
        self.Label217 = tk.Label(self.TNotebook1_t9)
        self.Label217.place(relx=0.5, rely=0.45, height=21, width=150)
        self.Label217.configure(anchor='w')
        self.Label217.configure(compound='left')
        self.Label217.configure(text='''with:''')
        
        self.Entry217 = tk.Entry(self.TNotebook1_t9)
        self.Entry217.place(relx=0.70, rely=0.45, height=23, relwidth=0.1)
        self.Entry217.configure(background="white")
        self.Entry217.configure(font="TkFixedFont")
        
        
        
        self.Label208 = tk.Label(self.TNotebook1_t9)
        self.Label208.place(relx=0.5, rely=0.6, height=21, width=150)
        self.Label208.configure(anchor='w')
        self.Label208.configure(compound='left')
        self.Label208.configure(text='''Column:''')
        
        self.TCombobox208= ttk.Combobox(self.TNotebook1_t9)
        self.TCombobox208.place(relx=0.7, rely=0.6, relheight=0.072
                , relwidth=0.200)
        self.TCombobox208.configure(takefocus="")
        
        
        self.Button209 = tk.Button(self.TNotebook1_t9)
        self.Button209.place(relx=0.70, rely=0.75, height=33, width=113)
        self.Button209.configure(borderwidth="2")
        self.Button209.configure(compound='left')
        self.Button209.configure(command = replace_into_column)
        self.Button209.configure(text='''Replace''')
        
        ###################################################################
        ##tab 10 - Modify date
        
        self.Label401 = tk.Label(self.TNotebook1_t12)
        self.Label401.place(relx=0.03, rely=0.034, height=21, width=250)
        self.Label401.configure(anchor='w')
        self.Label401.configure(compound='left')
        self.Label401.configure(text='''Convert datetime Column:''')
        
        self.Label412 = tk.Label(self.TNotebook1_t12)
        self.Label412.place(relx=0.03, rely=0.15, height=21, width=150)
        self.Label412.configure(anchor='w')
        self.Label412.configure(compound='left')
        self.Label412.configure(text='''Column:''')
        
        self.TCombobox412= ttk.Combobox(self.TNotebook1_t12)
        self.TCombobox412.place(relx=0.20, rely=0.15, relheight=0.072
                , relwidth=0.200)
        self.TCombobox412.configure(takefocus="")
        
        self.Label413 = tk.Label(self.TNotebook1_t12)
        self.Label413.place(relx=0.03, rely=0.3, height=21, width=150)
        self.Label413.configure(anchor='w')
        self.Label413.configure(compound='left')
        self.Label413.configure(text='''Format of Column:''')
        
        self.Label414 = tk.Label(self.TNotebook1_t12)
        self.Label414.place(relx=0.2, rely=0.3, height=21, width=150)
        self.Label414.configure(anchor='w')
        self.Label414.configure(compound='left')
        self.Label414.configure(text='''?''')
        
        self.Button404 = tk.Button(self.TNotebook1_t12)
        self.Button404.place(relx=0.40, rely=0.3, height=33, width=20)
        self.Button404.configure(borderwidth="2")
        self.Button404.configure(compound='left')
        self.Button404.configure(command = show_fr)
        self.Button404.configure(text='''...''')
        
        self.Label402 = tk.Label(self.TNotebook1_t12)
        self.Label402.place(relx=0.03, rely=0.45, height=21, width=150)
        self.Label402.configure(anchor='w')
        self.Label402.configure(compound='left')
        self.Label402.configure(text='''Current Date Fromat:''')
        
        self.TCombobox402= ttk.Combobox(self.TNotebook1_t12)
        self.TCombobox402.place(relx=0.20, rely=0.45, relheight=0.072
                , relwidth=0.200)
        self.value_list402 = ['yyyy-mm-dd hh:mm:ss', 'yyyy/mm/dd hh:mm:ss','dd-mm-yyyy hh:mm:ss', 'yyyy-mm-ddThh:mm:ss', 'dd.mm.yyyy hh:mm:ss', 'dd.mm.yyyy hh:mm', 'dd.mm.yyyy hh', 'dd.mm.yyyy', 'dd-mm-yyyy', 'yyyy-mm-dd']
        self.TCombobox402.configure(values=self.value_list402)
        self.TCombobox402.configure(takefocus="")
        
        self.Label403 = tk.Label(self.TNotebook1_t12)
        self.Label403.place(relx=0.03, rely=0.6, height=21, width=150)
        self.Label403.configure(anchor='w')
        self.Label403.configure(compound='left')
        self.Label403.configure(text='''New Column Name:''')
        
        self.Entry403 = tk.Entry(self.TNotebook1_t12)
        self.Entry403.place(relx=0.20, rely=0.6, height=23, relwidth=0.2)
        self.Entry403.configure(background="white")
        self.Entry403.configure(font="TkFixedFont")
        
        self.Button404 = tk.Button(self.TNotebook1_t12)
        self.Button404.place(relx=0.20, rely=0.75, height=33, width=200)
        self.Button404.configure(borderwidth="2")
        self.Button404.configure(compound='left')
        self.Button404.configure(command = convert_date)
        self.Button404.configure(text='''Build Date Column''')
        
        #get calendar info
        
        self.Label501 = tk.Label(self.TNotebook1_t12)
        self.Label501.place(relx=0.5, rely=0.034, height=21, width=250)
        self.Label501.configure(anchor='w')
        self.Label501.configure(compound='left')
        self.Label501.configure(text='''Get Calendar Info:''')
        
        self.Label512 = tk.Label(self.TNotebook1_t12)
        self.Label512.place(relx=0.5, rely=0.15, height=21, width=150)
        self.Label512.configure(anchor='w')
        self.Label512.configure(compound='left')
        self.Label512.configure(text='''Column:''')
        
        self.TCombobox512= ttk.Combobox(self.TNotebook1_t12)
        self.TCombobox512.place(relx=0.7, rely=0.15, relheight=0.072
                , relwidth=0.200)
        self.TCombobox512.configure(takefocus="")
        
        
        
        self.Label502 = tk.Label(self.TNotebook1_t12)
        self.Label502.place(relx=0.5, rely=0.45, height=21, width=150)
        self.Label502.configure(anchor='w')
        self.Label502.configure(compound='left')
        self.Label502.configure(text='''Needet Calendar Info:''')
        
        self.TCombobox502= ttk.Combobox(self.TNotebook1_t12)
        self.TCombobox502.place(relx=0.7, rely=0.45, relheight=0.072
                , relwidth=0.200)
        self.value_list502 = ['month', 'day','week', 'year', 'minutes', 'second', 'day name', 'month name', 'day of the year', 'day of the week']
        self.TCombobox502.configure(values=self.value_list502)
        self.TCombobox502.configure(takefocus="")
        
        self.Label503 = tk.Label(self.TNotebook1_t12)
        self.Label503.place(relx=0.5, rely=0.6, height=21, width=150)
        self.Label503.configure(anchor='w')
        self.Label503.configure(compound='left')
        self.Label503.configure(text='''New Column Name:''')
        
        self.Entry503 = tk.Entry(self.TNotebook1_t12)
        self.Entry503.place(relx=0.7, rely=0.6, height=23, relwidth=0.2)
        self.Entry503.configure(background="white")
        self.Entry503.configure(font="TkFixedFont")
        
        self.Button504 = tk.Button(self.TNotebook1_t12)
        self.Button504.place(relx=0.7, rely=0.75, height=33, width=200)
        self.Button504.configure(borderwidth="2")
        self.Button504.configure(compound='left')
        self.Button504.configure(command = create_cal_info)
        self.Button504.configure(text='''Build Calendar Info Column''')
        
        
        #####################################################################
        ##tab11 - Save CSV
        
        self.Label301 = tk.Label(self.TNotebook1_t10)
        self.Label301.place(relx=0.03, rely=0.034, height=21, width=600)
        self.Label301.configure(anchor='w')
        self.Label301.configure(compound='left')
        self.Label301.configure(text='''Save CSV Data File (With Header, Seperator =";" Delimeter =",") ''')
        
        self.Label302 = tk.Label(self.TNotebook1_t10)
        self.Label302.place(relx=0.03, rely=0.15, height=21, width=150)
        self.Label302.configure(anchor='w')
        self.Label302.configure(compound='left')
        self.Label302.configure(text='''Current File name:''')
        
        self.Label303 = tk.Label(self.TNotebook1_t10)
        self.Label303.place(relx=0.15, rely=0.15, height=21, width=600)
        self.Label303.configure(anchor='w')
        self.Label303.configure(compound='left')
        self.Label303.configure(text='''no file loaded''')

        self.Button303 = tk.Button(self.TNotebook1_t10)
        self.Button303.place(relx=0.03, rely=0.45, height=33, width=113)
        self.Button303.configure(borderwidth="2")
        self.Button303.configure(compound='left')
        self.Button303.configure(command = save_current_CSV_name)
        self.Button303.configure(text='''Save''')
        
        self.Button304 = tk.Button(self.TNotebook1_t10)
        self.Button304.place(relx=0.03, rely=0.60, height=33, width=113)
        self.Button304.configure(borderwidth="2")
        self.Button304.configure(compound='left')
        self.Button304.configure(command = save_CSV)
        self.Button304.configure(text='''Save as...''')
        
        var10 = tk.IntVar()
        self.Checkbutton305 = tk.Checkbutton(self.TNotebook1_t10)
        self.Checkbutton305.place(relx=0.03, rely=0.3, relheight=0.047
                , relwidth=0.165)
        self.Checkbutton305.configure(activebackground="#f9f9f9")
        self.Checkbutton305.configure(justify='left')
        self.Checkbutton305.configure(text='''Index Column needed''')
        self.Checkbutton305.configure(variable=var10, onvalue=1)
        
        
        ######################################################################
        ##Tab12 - Info
        
        self.Scrolledtext3 = ScrolledText(self.TNotebook1_t11)
        self.Scrolledtext3.place(relx=0.012, rely=0.034, relheight=0.934
                , relwidth=0.98)
        self.Scrolledtext3.configure(background="white")
        self.Scrolledtext3.configure(font="TkTextFont")
        self.Scrolledtext3.configure(insertborderwidth="3")
        self.Scrolledtext3.configure(selectbackground="blue")
        self.Scrolledtext3.configure(selectforeground="white")
        self.Scrolledtext3.configure(wrap="none")
        f = open('C:/Users/hieu/OneDrive/Desktop/CSVpySTAT-main/CSVpySTAT-main/Info.txt', "r", errors='ignore')
    
        self.Scrolledtext3.insert(END, f.read())
            
        
########################################################################
    

        #main tab with info text log informations

        self.Scrolledtext1 = ScrolledText(self.top)
        self.Scrolledtext1.place(relx=0.019, rely=0.494, relheight=0.467
                , relwidth=0.957)
        self.Scrolledtext1.configure(background="white")
        self.Scrolledtext1.configure(font="TkTextFont")
        self.Scrolledtext1.configure(insertborderwidth="3")
        self.Scrolledtext1.configure(selectbackground="blue")
        self.Scrolledtext1.configure(selectforeground="white")
        self.Scrolledtext1.configure(wrap="none")


##############################################################################


# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledText(AutoScroll, tk.Text):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')
def start_up():
    CSVpySTAT_support.main()

if __name__ == '__main__':
    CSVpySTAT_support.main()




