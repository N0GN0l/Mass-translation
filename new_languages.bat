@echo off
set /P row= please choose a row: 
set /P column= please choose a column: 
set /P input= please choose a language: 
set /P number= please input the language number: 
echo def %input%():
echo    languages.append(%number%)
echo    print(languages)
echo    %input%Choose['state'] = DISABLED

echo %input%Choose = Button(root, text="%input%?", padx=20, command=%input%, bg="grey",)
echo
echo
echo
echo
echo
echo
echo %input%Choose.grid(row=%row%, column=%column%)



pause