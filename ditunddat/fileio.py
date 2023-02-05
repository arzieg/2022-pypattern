# Manipulating Pathnames
import os
path = '/home/arne/m.sh'

#
print ("Path     : {}".format(path))
print ("Dateiname: {}".format(os.path.basename(path)))
print ("DirName  : {}".format(os.path.dirname(path)))
print ("Join tmp and data and m.sh: {}".format(os.path.join('tmp','data',os.path.basename(path))))
print ("----------------------------------")
path = '~/m.sh'
print ("~/m.sh wurde als path gesetzt")
print ("Expand home Directory")
print ("Home Path: {}".format(os.path.expanduser(path)))
print ("----------------------------------")
print ("Split the file extension")
print ("Fileextension: {}".format(os.path.splitext(path)))
print ("----------------------------------")

print ("/etc/passwd existiert: {}".format(os.path.exists('/etc/passwd')))
print ("/tmp/spam existiert  : {}".format(os.path.exists('/tmp/spam')))
print ("/etc/passwd ist ein file: {}".format(os.path.isfile('/etc/passwd')))
print ("/etc/passwd ist ein dir : {}".format(os.path.isdir('/etc/passwd')))
print ("python3 ist ein link:     {}".format(os.path.islink('/usr/bin/python3')))
print ("Realpath für python3:     {}".format(os.path.realpath('/usr/bin/python3')))
print ("Grösse von /etc/passwd:   {}".format(os.path.getsize('/etc/passwd')))
import time
print ("Timestamp von /etc/passwd: {}".format(time.ctime(os.path.getmtime('/etc/passwd'))))

print ("----------------------------------")
names = os.listdir('/home/arne')
import os.path
names = [name for name in os.listdir('/home/arne')
         if os.path.isfile(os.path.join('/home/arne',name))]
dirnames = [name for name in os.listdir('/home/arne')
            if os.path.isdir(os.path.join('/home/arne',name))]

print ("Names = {}".format(names))
print ("Dirnames = {}".format(dirnames))

print ("----------------------------------")
print ("Example of getting a directory listing")
import os
import os.path
import glob

pyfiles = glob.glob('*.py')

# get filesize and modification dates
file_metadata = [(name, os.stat(name)) for name in glob.glob('*')]

for name, meta in file_metadata:
    print (oct(os.stat(name).st_mode & 0o777000), oct(os.stat(name).st_mode & 0o777), name)  # print die drei oktalen Zahlen

# der Lower-Teil enthält die Permissions
# S_IRWXU 00700   mask for file owner permissions
# S_IRUSR 00400   owner has read permission
# S_IWUSR 00200   owner has write permission
# S_IXUSR 00100   owner has execute permission
# S_IRWXG 00070   mask for group permissions
# S_IRGRP 00040   group has read permission
# S_IWGRP 00020   group has write permission
# S_IXGRP 00010   group has execute permission
# S_IRWXO 00007   mask for permissions for others (not in group)
# S_IROTH 00004   others have read permission
# S_IWOTH 00002   others have write permission
# S_IXOTH 00001   others have execute permission

# Sidenote: the upper parts determine the filetype
# S_IFMT  0170000 bitmask for the file type bitfields
# S_IFSOCK    0140000 socket
# S_IFLNK 0120000 symbolic link
# S_IFREG 0100000 regular file
# S_IFBLK 0060000 block device
# S_IFDIR 0040000 directory
# S_IFCHR 0020000 character device
# S_IFIFO 0010000 FIFO
# S_ISUID 0004000 set UID bit
# S_ISGID 0002000 set-group-ID bit (see below)
# S_ISVTX 0001000 sticky bit (see below)


print ("------------------------------")
print ("Directory recursiv auslesen")
import glob

file_metadata = [(name, os.stat(name)) for name in glob.iglob('/home/arne/dev/python/ditunddat/tmp/'+'**/*', recursive=True)]

with open('/home/arne/dev/python/ditunddat/directory.txt', 'wt') as f:
    for name, meta in file_metadata:
        text = str(meta.st_mode) +";" + name + "\n"
        f.write(text)
        print (text)
        #f.write (os.stat(name).st_mode+";"+name)

