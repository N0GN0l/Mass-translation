@echo off
set /P row= please choose a row: 
set /P column= please choose a column: 
set /P input= please choose a language: 
set /p country= please input country of origin: 
set /P languageModule= please input the language as a usable module for google translate
set /P number= please input the language number: 
echo def %input%():
echo    languages.append(%number%)
echo    print(languages)
echo    %input%Choose['state'] = DISABLED
echo %input%Choose = Button(root, text="%input%?", padx=20, command=%input%, bg="grey",)
echo %input%Choose.grid(row=%row%, column=%column%)
echo        if i == %number%:
echo            %country% = Toplevel()
echo            %country%.title("%language% email")
echo            %country%.geometry("1000x100")
echo            def focusText(event):
echo                %language%Output.config(state='normal')
echo                %language%Output.focus()
echo                %language%Output.config(state='disabled')
echo            %language%Output = Text(china, borderwidth=0)
echo            %language%Output.insert(1.0, translater.translate(email.get(), src="en", dest="%languageModule%").text)
echo            %language%Output.pack()
echo            %language%Output.configure(state="disabled")
echo            %language%Output.bind('<Button-1>', focusText)
pause