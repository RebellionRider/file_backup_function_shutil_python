# file_backup_function_shutil_python
In This Project We Created A Function That Will Perform A Backup of A File. This Function is highly customizable and created by taking the perspective of reusability in mind.

## Video Tutorial

Like Always I have done a video explaningt this code which you can watch here [YouTube Video](https://youtu.be/uU_iuYv53-U "YouTube Video")
I would Highly Suggest You To Watch This Video For Any Doubts

## Function Brief
The name of the function is take_bkp created inside python script whose name is file_bkp. You can find this script inside “File_Ops” Directory.
This function takes 4 parameters.
1.	Source File Name
2.	Backup File Name
3.	Source File location 
4.	Backup File Location

*With Last Two Parameters You Need To Take Care of Theree things, which are –

- Just Specify The Path of The Directory

- All The Slashes In That Path Must Always Be “Forward Slashes”

- Both The Paths Must End With a “Forward Slash”

### All The Parameters Except The first One Are Optional
Optional Values For 2nd, 3rd and 4th parameter –
- In case you don’t want to specify The Name For The Backup File (2nd parameter) Then You Can Write “None” (Without The Quote) or empty string(""). On doing so the function will use the name of the source file and append it with the date.

- In case you don't want to specify paths for the last two parametere then you can give empty string ("") while calling the function

