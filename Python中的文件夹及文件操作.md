#python 的文件夹及文件操作

## os.path模块

| 函数           | 功能                       |
| ------------ | ------------------------ |
| abspath      | 获取文件绝对路径                 |
| basename     | 获取文件的路径                  |
| commonprefix | 入参为路径名称的列表，返回最长的公共路径前缀组合 |
| dirname      | 获取文件夹名称                  |
| exists       | 判断文件是否存在                 |
| expanduser   | 将~扩展成真实路径                |
| expandvars   | 用环境变量中的$HOME扩展成真实路径      |
| getatime     | 获取文件的acces时间             |
| getmtime     | 获取文件的修改时间                |
| getsize      | 获取文件的size                |
| isabs        | 是否是绝对路径                  |
| isdir        | 是否是文件夹                   |
| isfile       | 是否是文件                    |
| islink       |                          |
| ismount      |                          |
| join         |                          |
| lexists      |                          |
| normcase     |                          |
| normpath     |                          |
| realpath     |                          |
| relpath      |                          |
| samefile     |                          |
| sameopenfile |                          |
|              |                          |
|              |                          |
|              |                          |

python 中os.path模块用于操作文件或文件夹

### 判断文件路径是否存在

os.path.exists(path) 判断文件路径是否存在

dir = "c:\windows"
if os.path.exists(dir) :
　　print "dir exists"
else :
　　print "no exists"

### 判断path是否是文件 

os.path.isfile(path) 判断path是否是文件

dir = "c:\windows\system32\cmd.exe"
if os.path.isfile(dir) :
　　print "file exists"
else :
　　print "no exists"

### 获取path文件的大小

os.path.getsize(path) 获取path文件的大小

size = os.path.getsize(dir)
print size/1024

 

## os中的处理函数

可参考http://www.runoob.com/python/os-file-methods.html



| 函数                    | 功能                                       |
| --------------------- | ---------------------------------------- |
| os.abort              | 不返回。立即中断                                 |
| os.access(path, mode) | 可以返回True，不然返回False                       |
| os.chdir              | 改变运行目录到指定路径                              |
| os.chmod              | 改变路径的owner和group id权限                    |
| os.chroot             | 改变root文件夹                                |
| os.close              | 关闭文件描述符                                  |
| os.closerange         | 关闭一个范围的文件描述符，忽略错误                        |
| os.fchdir             | 切到文件描述符所指向的路径，必须是一文件夹                    |
| os.fchmod             | 改变指定文件描述符的权限                             |
| os.fchown             | 改变描述符的owner和group id。                    |
| os.fdatasync          | 强制写入，不强制更新元数据                            |
| os.fdopen             | 返回一个连接了文件描述符的打开的文件对象                     |
| os.fsync              | 强制文件描述符对应文件写入到磁盘                         |
| os.getcwd             | 返回当前工作路径的字符串                             |
| os.getcwdu            | 返回当前工作路径的unicode字符串                      |
| os.lchown             | 改变路径的owner和group id，此函数不追踪链接             |
| os.link               | 创建一个文件的硬链接                               |
| os.listdir            | 列出目录下文件                                  |
| os.lseek              | 设置文件描述符的当前位置                             |
| os.lstat              | 路径当前的stat信息，不追踪链接                        |
| os.makedirs           | super-mkdir; 用于递归创建目录。像 mkdir(), 但创建的所有intermediate-level文件夹需要包含子目录。 |
| os.mkdir              | 创建文件夹                                    |
| os.walk               | 遍历功能                                     |
| os                    |                                          |
|                       |                                          |
|                       |                                          |
| os.chdir              | 切换到某个目录                                  |
| os.remove             | 删除文件                                     |
|                       |                                          |
|                       |                                          |
|                       |                                          |
|                       |                                          |
|                       |                                          |
|                       |                                          |
|                       |                                          |
|                       |                                          |
|                       |                                          |
|                       |                                          |
|                       |                                          |
| os.walk               |                                          |
| write                 | 写文件内容                                    |



| a                                    | b    |
| ------------------------------------ | ---- |
| os 模块提供了非常丰富的方法用来处理文件和目录。常用的方法如下表所示： |      |





os 模块提供了非常丰富的方法用来处理文件和目录。常用的方法如下表所示：

序号	方法及描述
1	
os.access(path, mode)


检验权限模式
2	
os.chdir(path)


改变当前工作目录
3	
os.chflags(path, flags)


设置路径的标记为数字标记。
4	
os.chmod(path, mode)


更改权限
5	
os.chown(path, uid, gid)


更改文件所有者
6	
os.chroot(path)


改变当前进程的根目录
7	
os.close(fd)


关闭文件描述符 fd
8	
os.closerange(fd_low, fd_high)


关闭所有文件描述符，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略
9	
os.dup(fd)


复制文件描述符 fd
10	
os.dup2(fd, fd2)


将一个文件描述符 fd 复制到另一个 fd2
11	
os.fchdir(fd)


通过文件描述符改变当前工作目录
12	
os.fchmod(fd, mode)


改变一个文件的访问权限，该文件由参数fd指定，参数mode是Unix下的文件访问权限。
13	
os.fchown(fd, uid, gid)


修改一个文件的所有权，这个函数修改一个文件的用户ID和用户组ID，该文件由文件描述符fd指定。
14	
os.fdatasync(fd)


强制将文件写入磁盘，该文件由文件描述符fd指定，但是不强制更新文件的状态信息。
15	
os.fdopen(fd[, mode[, bufsize]])


通过文件描述符 fd 创建一个文件对象，并返回这个文件对象
16	
os.fpathconf(fd, name)


返回一个打开的文件的系统配置信息。name为检索的系统配置的值，它也许是一个定义系统值的字符串，这些名字在很多标准中指定（POSIX.1, Unix 95, Unix 98, 和其它）。
17	
os.fstat(fd)


返回文件描述符fd的状态，像stat()。
18	
os.fstatvfs(fd)


返回包含文件描述符fd的文件的文件系统的信息，像 statvfs()
19	
os.fsync(fd)


强制将文件描述符为fd的文件写入硬盘。
20	
os.ftruncate(fd, length)


裁剪文件描述符fd对应的文件, 所以它最大不能超过文件大小。
21	
os.getcwd()


返回当前工作目录
22	
os.getcwdu()


返回一个当前工作目录的Unicode对象
23	
os.isatty(fd)


如果文件描述符fd是打开的，同时与tty(-like)设备相连，则返回true, 否则False。
24	
os.lchflags(path, flags)


设置路径的标记为数字标记，类似 chflags()，但是没有软链接
25	
os.lchmod(path, mode)


修改连接文件权限
26	
os.lchown(path, uid, gid)


更改文件所有者，类似 chown，但是不追踪链接。
27	
os.link(src, dst)


创建硬链接，名为参数 dst，指向参数 src
28	
os.listdir(path)


返回path指定的文件夹包含的文件或文件夹的名字的列表。
29	
os.lseek(fd, pos, how)


设置文件描述符 fd当前位置为pos, how方式修改: SEEK_SET 或者 0 设置从文件开始的计算的pos; SEEK_CUR或者 1 则从当前位置计算; os.SEEK_END或者2则从文件尾部开始. 在unix，Windows中有效
30	
os.lstat(path)


像stat(),但是没有软链接
31	
os.major(device)


从原始的设备号中提取设备major号码 (使用stat中的st_dev或者st_rdev field)。
32	
os.makedev(major, minor)


以major和minor设备号组成一个原始设备号
33	
os.makedirs(path[, mode])


递归文件夹创建函数。像mkdir(), 但创建的所有intermediate-level文件夹需要包含子文件夹。
34	
os.minor(device)


从原始的设备号中提取设备minor号码 (使用stat中的st_dev或者st_rdev field )。
35	
os.mkdir(path[, mode])


以数字mode的mode创建一个名为path的文件夹.默认的 mode 是 0777 (八进制)。
36	
os.mkfifo(path[, mode])


创建命名管道，mode 为数字，默认为 0666 (八进制)
37	
os.mknod(filename[, mode=0600, device])
创建一个名为filename文件系统节点（文件，设备特别文件或者命名pipe）。

38	
os.open(file, flags[, mode])


打开一个文件，并且设置需要的打开选项，mode参数是可选的
39	
os.openpty()


打开一个新的伪终端对。返回 pty 和 tty的文件描述符。
40	
os.pathconf(path, name)


返回相关文件的系统配置信息。
41	
os.pipe()


创建一个管道. 返回一对文件描述符(r, w) 分别为读和写
42	
os.popen(command[, mode[, bufsize]])


从一个 command 打开一个管道
43	
os.read(fd, n)


从文件描述符 fd 中读取最多 n 个字节，返回包含读取字节的字符串，文件描述符 fd对应文件已达到结尾, 返回一个空字符串。
44	
os.readlink(path)


返回软链接所指向的文件
45	
os.remove(path)


删除路径为path的文件。如果path 是一个文件夹，将抛出OSError; 查看下面的rmdir()删除一个 directory。
46	
os.removedirs(path)


递归删除目录。
47	
os.rename(src, dst)


重命名文件或目录，从 src 到 dst
48	
os.renames(old, new)


递归地对目录进行更名，也可以对文件进行更名。
49	
os.rmdir(path)


删除path指定的空目录，如果目录非空，则抛出一个OSError异常。
50	
os.stat(path)


获取path指定的路径的信息，功能等同于C API中的stat()系统调用。
51	
os.stat_float_times([newvalue])
决定stat_result是否以float对象显示时间戳

52	
os.statvfs(path)


获取指定路径的文件系统统计信息
53	
os.symlink(src, dst)


创建一个软链接
54	
os.tcgetpgrp(fd)


返回与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组
55	
os.tcsetpgrp(fd, pg)


设置与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组为pg。
56	
os.tempnam([dir[, prefix]])


返回唯一的路径名用于创建临时文件。
57	
os.tmpfile()


返回一个打开的模式为(w+b)的文件对象 .这文件对象没有文件夹入口，没有文件描述符，将会自动删除。
58	
os.tmpnam()


为创建一个临时文件返回一个唯一的路径
59	
os.ttyname(fd)


返回一个字符串，它表示与文件描述符fd 关联的终端设备。如果fd 没有与终端设备关联，则引发一个异常。
60	
os.unlink(path)


删除文件路径
61	
os.utime(path, times)


返回指定的path文件的访问和修改的时间。
62	
os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])


输出在文件夹中的文件名通过在树中游走，向上或者向下。
63	
os.write(fd, str)


写入字符串到文件描述符 fd中. 返回实际写入的字符串长度





### 遍历path的walk

os.walk(path) 遍历path，返回一个三元组（dirpath, dirnames, filenames). dirpath表示遍历到的路径, dirnames表示该路径下的子目录名，是一个列表, filesnames表示该路径下的文件名，也是一个列表. 

例如: 当遍历到c:\windows时，dirpath="c:\windows", dirnames是这个路径下所有子目录名的列表，filenames是这个路径下所有文件名的列表

列出windows目录下的所有文件和文件名

for (root, dirs, files) in os.walk("C:\windows"): 
　　for filename in files:
　　　　print os.path.join(root,filename)

　　for dirc in dirs:

　　　　print os.path.join(root,dirc)

 

问题 1 获取给定文件夹的大小?

　　要遍历文件的大小，只需要遍历文件内的所有文件，然后将所有文件夹的大小加起来

def getDirSzie(dir) :
for (root,dirs,files) in os.walk(dir,False) :
　　Size = 0
　　for filename in files :
　　　　Size += os.path.getsize(os.path.join(root,filename))
　　print root,Size/1024

 

问题 2 遍历一个文件夹的子目录，不遍历子目录的字目录？

os.listdir(path) 函数列出指定目录下的文件和文件夹

dir = 'c:/windows'
if os.path.exists(dir):
　　dirs = os.listdir(dir)
　　for dirc in dirs:
　　　　print dirc
else :
　　print "dir not exists"

 

问题3　删除指定目录下空的目录

for (root, dirs, files) in os.walk(path) :
　　for item in dirs :
　　　　dir = os.path.join(root, item)
　　　　try :
　　　　　　print dir
　　　　　　os.rmdir(dir)
　　　　except :
　　　　　　pass

问题4  修改指定目录下所有文件的文件后缀

for (root,dirs,files) in os.walk(path) :
　　for item in files :
　　　　d = os.path.join(root, item)
　　　　name = d + ".eml"
　　　　os.rename(d, name)

### os.chmod

os.chmod(path,mode) 这个方法应该很简单，只需要2个参数，一个是路径，一个是说明路径的模式，下面列出了这个用法中可以使用的一些常用的模式：

- **stat.S_ISUID:** Set user ID on execution. 不常用
- **stat.S_ISGID:** Set group ID on execution. 不常用
- **stat.S_ENFMT:** Record locking enforced. 不常用
- **stat.S_ISVTX:** Save text image after execution. 在执行之后保存文字和图片
- **stat.S_IREAD:** Read by owner. 对于拥有者读的权限
- **stat.S_IWRITE:** Write by owner. 对于拥有者写的权限
- **stat.S_IEXEC:** Execute by owner. 对于拥有者执行的权限
- **stat.S_IRWXU:** Read, write, and execute by owner. 对于拥有者读写执行的权限
- **stat.S_IRUSR:** Read by owner. 对于拥有者读的权限
- **stat.S_IWUSR:** Write by owner. 对于拥有者写的权限
- **stat.S_IXUSR:** Execute by owner. 对于拥有者执行的权限
- **stat.S_IRWXG:** Read, write, and execute by group. 对于同组的人读写执行的权限
- **stat.S_IRGRP:** Read by group. 对于同组读的权限
- **stat.S_IWGRP:** Write by group. 对于同组写的权限
- **stat.S_IXGRP:** Execute by group. 对于同组执行的权限
- **stat.S_IRWXO:** Read, write, and execute by others. 对于其他组读写执行的权限
- **stat.S_IROTH:** Read by others. 对于其他组读的权限
- **stat.S_IWOTH:** Write by others. 对于其他组写的权限
- **stat.S_IXOTH:** Execute by others. 对于其他组执行的权限



## 文件操作

| 函数   | 功能   | 备注   |
| ---- | ---- | ---- |
|      |      |      |





### 文件创建



### 文件删除

```
file = "/root/1.txt"
os.remove(file)
```



### 文件修改



### 文件读取

```
file1 = "/root/1.txt"
open(file1, 'r')

file(file1, 'r')

```



### 文件属性





### 文件锁





## 文件夹及文件的压缩



## 压缩文件的内容提取





