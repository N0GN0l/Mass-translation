@echo off
Rem inputs
set /P column= please choose a column: 
set /P input= please choose a language: 
set /p country= please input country of origin: 
Rem use language_list.py ti check for languages
set /P languageModule= please input the language as a usable module for google translate: 
set /P number= please input the language number: 
Rem button creation
echo def %input%():
echo    languages.append(%number%)
echo    print(languages)
echo    %input%Choose['state'] = DISABLED
echo %input%Choose = Button(root, text="%input%?", padx=20, command=%input%, bg="grey", fg="red")
Rem storing button on the grid
Rem check the row and column needed
echo %input%Choose.grid(row=15, column=%column%)
Rem Creating new page after button press
echo        if i == %number%:
echo            %country% = Toplevel()
echo            %country%.title("%input% email")
echo            %country%.geometry("1000x100")
echo            def focusText(event):
echo                %input%Output.config(state='normal')
echo                %input%Output.focus()
echo                %input%Output.config(state='disabled')
echo            %input%Output = Text(%country%, borderwidth=0)
echo            %input%Output.insert(1.0, translater.translate(email.get(), src="en", dest="%languageModule%").text)
echo            %input%Output.pack()
echo            %input%Output.configure(state="disabled")
echo            %input%Output.bind('<Button-1>', focusText)
pause