#python 的文件夹及文件操作

## os.path模块

| 函数           | 功能       |
| ------------ | -------- |
| abspath      | 获取文件绝对路径 |
| basename     | 获取文件的路径  |
| commonprefix |          |
| dirname      | 获取文件夹名称  |
| exists       | 判断文件是否存在 |
| expanduser   |          |
| expandvars   |          |
| geatime      |          |
| getmtime     |          |
| getsize      |          |
| isabs        |          |
| isdir        |          |
| isfile       |          |
|              |          |
|              |          |
|              |          |

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

| 函数      | 功能   |
| ------- | ---- |
| os.walk | 遍历功能 |



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





## 文件操作

| 函数   | 功能   | 备注   |
| ---- | ---- | ---- |
|      |      |      |





### 文件创建



### 文件删除



### 文件修改



### 文件读取



### 文件属性



