ECHO
"C:\Program Files (x86)\BlueZone\6.1\bzmd.exe" /F C:\Users\E668872\Documents\BlueZone\Config\transfer_file.zmd
echo hello world

C:\Software\anaconda3\python.exe c:\files\transform_datetime.py

set today=%date:~6,4%%date:~0,2%%date:~3,2%
copy /y C:\files\\transfertest_filtered.txt C:\Users\E668872\Documents\BlueZone\Transfer\quote-%today%.txt
