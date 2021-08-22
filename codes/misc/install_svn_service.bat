REM Install as Windows Services
sc create svn binpath= "\"C:\svn-win32-1.5.1\bin\svnserve.exe\" --service -r C:\svn-win32-1.5.1\my_repos" displayname= "Local SVN Server" depend= Tcpip start= auto
net start svn


REM link http://sites.google.com/site/freizl/Home/subversion
