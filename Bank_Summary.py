# author    :   Sanket Khedekar sakh3719@colorado.edu
# name      :   Bank Summary.py
# purpose   :   Program to generate Bank details Summary
# date      :   2018.06.23
# Run the following command on Pycharm terminal
# pip install --upgrade google-api-python-client
# pip install oauth2client

from __future__ import print_function

import sys
import os
import tkinter as tk
import datetime
from apiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from httplib2 import Http
from oauth2client import file, client, tools


try:
    class GUI(tk.Tk):
        def __init__(self, *args, **kwargs):
            tk.Tk.__init__(self, *args, **kwargs)
            container = tk.Frame(self)

            container.pack(side="top", fill="both", expand=True)
            container.grid_rowconfigure(0, weight=1)
            container.grid_columnconfigure(0, weight=1)

            self.frames = {}

            for F in (StartPage, PageOne):
                frame = F(container, self)
                self.frames[F] = frame
                frame.grid(row=0, column=0, sticky="nsew")

            self.show_frame(StartPage)

        def show_frame(self, cont):
            frame = self.frames[cont]
            frame.tkraise()


    class StartPage(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            self.lblSignIn = tk.Label(self, text="Sign In")

            self.lblUsername = tk.Label(self, text="Username")
            self.entUsername = tk.Entry(self)

            self.lblPassword = tk.Label(self, text="Password")
            self.entPassword = tk.Entry(self, show="*")

            self.btnSignIn = tk.Button(self, text="Sign In", command=self.sign_in, width=10)
            self.btnReset = tk.Button(self, text="Reset", command=self.reset, width=10)
            self.btnGoogleSignIn = tk.Button(self, text="Google Sign In", width=10)

            self.lblMessage = tk.Label(self, text="")

            self.lblSignIn.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

            self.lblUsername.grid(row=2, column=1, padx=10, pady=10)
            self.entUsername.grid(row=2, column=2, padx=10, pady=10)

            self.lblPassword.grid(row=3, column=1, padx=10, pady=10)
            self.entPassword.grid(row=3, column=2, padx=10, pady=10)

            self.btnSignIn.grid(row=4, column=1, padx=10, pady=10)
            self.btnReset.grid(row=4, column=2, padx=10, pady=10)

            self.btnGoogleSignIn.grid(row=5, column=1, columnspan=2, padx=10, pady=10)

            self.lblMessage.grid(row=6, column=1, columnspan=2, padx=10, pady=10)

        # For SignIn
        def sign_in(self):
            Cred = "Test"
            valUsername = self.entUsername.get()
            valPassword = self.entPassword.get()

            if valUsername == Cred and valPassword == Cred:
                self.entUsername.delete(0, 100)
                self.entPassword.delete(0, 100)
                self.controller.show_frame(PageOne)
            else:
                self.lblMessage['text'] = "Please enter valid credentials."

        def google_sign_in(self):
            scopes = 'https://www.googleapis.com/auth/drive'
            store = file.Storage('token.json')
            print("Store")
            print(store)
            credentials = store.get()
            print("Credentials")
            print(credentials)
            if not credentials or credentials.invalid:
                flow = client.flow_from_clientsecrets('credentials.json', scopes)
                credentials = tools.run_flow(flow, store)
            service = build('drive', 'v3', http=credentials.authorize(Http()))
            print("Service")
            print(service)

            '''
            if valUsername == Cred and valPassword == Cred:
                self.entUsername.delete(0, 100)
                self.entPassword.delete(0, 100)
                self.controller.show_frame(PageOne)
            else:
                self.lblMessage['text'] = "Please enter valid credentials."
            '''

        def reset(self):
            self.entUsername.delete(0, 100)
            self.entPassword.delete(0, 100)
            self.lblMessage['text'] = ""


    class PageOne(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)

            # All widgets in root
            self.lblWelcome = tk.Label(self, text="Bank Summary")

            self.lblWFCheck = tk.Label(self, text="Wells Fargo Checking")
            self.entWFCheck = tk.Entry(self)

            self.lblWFSave = tk.Label(self, text="Wells Fargo Saving")
            self.entWFSave = tk.Entry(self)

            # self.lblCHCheck = tk.Label(self, text="Chase Checking")
            # self.entCHCheck = tk.Entry(self)

            self.lblFBCheck = tk.Label(self, text="First Bank Checking")
            self.entFBCheck = tk.Entry(self)

            self.lblFBSave = tk.Label(self, text="First Bank Saving")
            self.entFBSave = tk.Entry(self)

            # self.lblELCheck = tk.Label(self, text="Elevation Checking")
            # self.entELCheck = tk.Entry(self)
            #
            # self.lblELSave = tk.Label(self, text="Elevation Saving")
            # self.entELSave = tk.Entry(self)

            self.lblCash = tk.Label(self, text="Cash")
            self.entCash = tk.Entry(self)

            self.lblBankTotal = tk.Label(self, text="Total Amount")
            self.lblBankTotalValue = tk.Label(self, text="")

            self.lblDiscover = tk.Label(self, text="Discover")
            self.entDiscover = tk.Entry(self)

            self.lblAmex = tk.Label(self, text="American Express")
            self.entAmex = tk.Entry(self)

            self.lblFinal = tk.Label(self, text="Final Amount")
            self.lblFinalValue = tk.Label(self, text="")

            self.btnTotal = tk.Button(self, text="Total", command=self.total, width=10)
            self.btnClose = tk.Button(self, text="Close", command=lambda: [self.clear(), controller.show_frame(StartPage)], width=10)

            self.lblText = tk.Label(self, text="")

            # Positions of widgets
            self.lblWelcome.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

            self.lblWFCheck.grid(row=2, column=1, padx=10, pady=10)
            self.entWFCheck.grid(row=2, column=2, padx=10, pady=10)

            self.lblWFSave.grid(row=3, column=1, padx=10, pady=10)
            self.entWFSave.grid(row=3, column=2, padx=10, pady=10)

            # self.lblCHCheck.grid(row=4, column=1, padx=10, pady=10)
            # self.entCHCheck.grid(row=4, column=2, padx=10, pady=10)

            self.lblFBCheck.grid(row=4, column=1, padx=10, pady=10)
            self.entFBCheck.grid(row=4, column=2, padx=10, pady=10)

            self.lblFBSave.grid(row=5, column=1, padx=10, pady=10)
            self.entFBSave.grid(row=5, column=2, padx=10, pady=10)

            # self.lblELCheck.grid(row=7, column=1, padx=10, pady=10)
            # self.entELCheck.grid(row=7, column=2, padx=10, pady=10)

            # self.lblELSave.grid(row=8, column=1, padx=10, pady=10)
            # self.entELSave.grid(row=8, column=2, padx=10, pady=10)

            self.lblCash.grid(row=6, column=1, padx=10, pady=10)
            self.entCash.grid(row=6, column=2, padx=10, pady=10)

            self.lblBankTotal.grid(row=7, column=1, padx=10, pady=10)
            self.lblBankTotalValue.grid(row=7, column=2, padx=10, pady=10)

            self.lblDiscover.grid(row=8, column=1, padx=10, pady=10)
            self.entDiscover.grid(row=8, column=2, padx=10, pady=10)

            self.lblAmex.grid(row=9, column=1, padx=10, pady=10)
            self.entAmex.grid(row=9, column=2, padx=10, pady=10)

            self.lblFinal.grid(row=10, column=1, padx=10, pady=10)
            self.lblFinalValue.grid(row=10, column=2, padx=10, pady=10)

            self.btnTotal.grid(row=11, column=1, padx=10, pady=10)
            self.btnClose.grid(row=11, column=2, padx=10, pady=10)

            self.lblText.grid(row=12, column=1, columnspan=2, padx=10, pady=10)
            self.lblText.configure(font=("Times New Roman", 10, "bold"))

        # For Final total
        def total(self):
            file_name, file_path = self.file_write()
            print("File Name")
            print(file_name)
            service = self.setup_drive()
            folder_id = self.folder(service)
            self.upload(service, file_name, file_path, folder_id)

        # For Clearing all text:
        def clear(self):
            self.entWFCheck.delete(0, 'end')
            self.entWFSave.delete(0, 'end')
            self.entFBCheck.delete(0, 'end')
            self.entFBSave.delete(0, 'end')
            self.entCash.delete(0, 'end')
            self.lblBankTotalValue['text'] = ""
            self.entDiscover.delete(0, 'end')
            self.entAmex.delete(0, 'end')
            self.lblFinalValue['text'] = ""
            self.lblText['text'] = ""

        # Final write
        def file_write(self):
            if self.entWFCheck.get() != "":
                valWFCheck = round(float(self.entWFCheck.get()), 2)
            else:
                self.entWFCheck.insert(0, "0")
                valWFCheck = 0
            if self.entWFSave.get() != "":
                valWFSave = round(float(self.entWFSave.get()), 2)
            else:
                self.entWFSave.insert(0, "0")
                valWFSave = 0
            # if self.entCHCheck.get() != "":
            #     valCHCheck = round(float(self.entCHCheck.get()), 2)
            # else:
            #     self.entCHCheck.insert(0, "0")
            #     valCHCheck = 0
            if self.entFBCheck.get() != "":
                valFBCheck = round(float(self.entFBCheck.get()), 2)
            else:
                self.entFBCheck.insert(0, "0")
                valFBCheck = 0
            if self.entFBSave.get() != "":
                valFBSave = round(float(self.entFBSave.get()), 2)
            else:
                self.entFBSave.insert(0, "0")
                valFBSave = 0
            # if self.entELCheck.get() != "":
            #     valELCheck = round(float(self.entELCheck.get()), 2)
            # else:
            #     self.entELCheck.insert(0, "0")
            #     valELCheck = 0
            # if self.entELSave.get() != "":
            #     valELSave = round(float(self.entELSave.get()), 2)
            # else:
            #     self.entELSave.insert(0, "0")
            #     valELSave = 0
            if self.entCash.get() != "":
                valCash = round(float(self.entCash.get()), 2)
            else:
                self.entCash.insert(0, "0")
                valCash = 0
            if self.entDiscover.get() != "":
                valDiscover = round(float(self.entDiscover.get()), 2)
            else:
                self.entDiscover.insert(0, "0")
                valDiscover = 0

            if self.entAmex.get() != "":
                valAmex = round(float(self.entAmex.get()), 2)
            else:
                self.entAmex.insert(0, "0")
                valAmex = 0

            # banktotal = valWFCheck + valWFSave + valCHCheck + valFBCheck + valFBSave + valELCheck + valELSave + valCash
            banktotal = valWFCheck + valWFSave + valFBCheck + valFBSave + valCash
            self.lblBankTotalValue['text'] = str(round(banktotal, 2))

            finalamount = banktotal - valDiscover - valAmex
            self.lblFinalValue['text'] = str(round(finalamount, 2))

            # Write into file
            now = datetime.datetime.now()
            file_name = "Bank_Summary-" + str(now.strftime("%Y%m%d")) + ".txt"
            file_dir = "D:\Google Drive\Jobs\Balance\\"
            if os.path.isdir(file_dir):
                file_path = file_dir + file_name
            else:
                file_path = file_name

            file = open(file_path, 'w')

            file.write('|==================================\n')
            file.write('|Bank Summary ' + str(now.strftime("%Y%m%d") + '\n'))
            file.write('|==================================\n')
            file.write('|Wells Fargo Checking:---' + str(valWFCheck) + '\n')
            file.write('|Wells Fargo Saving:-----' + str(valWFSave) + '\n')
            # file.write('|Chase Checking:---------' + str(valCHCheck) + '\n')
            file.write('|First Bank Checking:----' + str(valFBCheck) + '\n')
            file.write('|First Bank Saving:------' + str(valFBSave) + '\n')
            # file.write('|Elevation Checking:-----' + str(valELCheck) + '\n')
            # file.write('|Elevation Saving:-------' + str(valELSave) + '\n')
            file.write('|==================================\n')
            file.write('|Cash:-------------------' + str(valCash) + '\n')
            file.write('|==================================\n')
            file.write('|Total Amount:-----------' + str(round(banktotal, 2)) + '\n')
            file.write('|==================================\n')
            file.write('|Discover:---------------' + str(valDiscover) + '\n')
            file.write('|American Express:-------' + str(valAmex) + '\n')
            file.write('|==================================\n')
            file.write('|Final Amount:-----------' + str(round(finalamount, 2)) + '\n')
            file.write('|==================================\n')
            file.close()

            return file_name, file_path

        # For setting up Drive v3 API
        def setup_drive(self):
            scopes = 'https://www.googleapis.com/auth/drive'
            store = file.Storage('token.json')
            credentials = store.get()
            if not credentials or credentials.invalid:
                flow = client.flow_from_clientsecrets('credentials.json', scopes)
                credentials = tools.run_flow(flow, store)
            service = build('drive', 'v3', http=credentials.authorize(Http()))
            return service

        # For getting Folder 'Balance' ID
        def folder(self, service):
            # ID of My Drive - 0AIGysAUDz8feUk9PVA
            folder_id = ""
            query = "'0AIGysAUDz8feUk9PVA' in parents and mimeType='application/vnd.google-apps.folder' and name='Balance'"
            folder_list = service.files().list(q=query, spaces='drive', fields='files(id, name, parents)').execute()
            print("Folder List")
            print(folder_list)
            for folder in folder_list.get('files', []):
                if folder.get('name') == "Balance":
                    folder_id = folder.get('id')
                    break

            if folder_id == "":
                file_metadata = {
                    'name': 'Balance',
                    'mimeType': 'application/vnd.google-apps.folder'
                }
                folder = service.files().create(body=file_metadata, fields="id").execute()
                folder_id = folder.get('id')

            print(folder_id)
            return folder_id

        # For Uploading file on Drive v3 API
        def upload(self, service, file_name, file_path, folder_id):
            file_metadata = {
                'name': file_name,
                'parents': [folder_id]
            }
            media = MediaFileUpload(file_path, mimetype='text/plain')

            upload_file = service.files().create(body=file_metadata, media_body=media, fields='id, name').execute()
            message = "File '" + str(upload_file.get('name')) + "'\nuploaded on Google Drive"
            print(message)
            self.lblText['text'] = message


    if __name__ == '__main__':
        root = GUI()
        root.title("U.S. Bank Summary")
        root.mainloop()


except Exception as e:
    print("Error while executing." + str(e))
    sys.exit()
