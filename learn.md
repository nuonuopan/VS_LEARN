- 【ctrl+,】打开设置👉搜索zoom👉打勾
实现✔按住ctrl+滚轮对字体大小进行缩放

# github传输工作
- 下载git并安装，安装的时候仅有一步选择编辑器的时候注意选择vscode即可 *[下载地址](https://git-scm.com/download/win)
- 第一次进入是需要设定user.name和user.email 
    *[参考](https://crycrycry.blog.csdn.net/article/details/109131441?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1-109131441-blog-113933630.pc_relevant_aa&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1-109131441-blog-113933630.pc_relevant_aa&utm_relevant_index=1)
    设置全局用户名
    `git config --global user.name "Cry"`
    设置全局邮箱地址
    `git config --global user.email "Cry111@163.com"`
    查看git配置
    `git config --list`


- 进入项目vscode👉源代码管理👉初始化储存库(项目下的东西即保存了)👉有个√，是推；填入master，默认是村早master里【这里是存在本地仓库】,当左下角master没有*号时，点击上传。。。但我这里不管有没有开v都无法更新上去

#TODO
- 网页上传github    √
- 本地git代码上传
- 有一个bilibili提供的软件，试试能不能上传


- 网页上穿github
先创建仓库，右上+号，new repository，填写仓库名、是否要read.md、license文件，确定即可
【下载】创建好后，绿色的code，download zip可以下载整个repository
【上传】Add file👉Create new file（当前目录创建全新的文件） 或者 Upload files👉选择上传的文件👉填写更新描述👉commit即可
【上传-新建文件夹】路径写：code/test.md github不允许增空文件夹，写一个文件放着，之后进入这个文件【上传】即可  [参考](https://www.csdn.net/tags/Mtzacg1sNTk0Mi1ibG9n.html)


git是一个语言，只要在cmd上使用即可，在项目的当前文件夹下右键 get bash here打开cmd
- 本地git代码上传 [参考：非常详尽](https://blog.csdn.net/weixin_35805266/article/details/113073974?utm_term=desktop%20github%20%E7%99%BB%E5%BD%95%E4%B8%8D%E4%B8%8A&utm_medium=distribute.pc_aggpage_search_result.none-task-blog-2~all~sobaiduweb~default-1-113073974-null-null&spm=3001.4430)
- 最常用的几个命令+git代码上传步骤：
    - git 初始化的指令 
         `git init`   
         等于源代码管理的  初始化git库
    - 把东西放到暂存区
         `git add .`  
         等于源代码管理的   √ 提交   
    - 把暂存区的内容放到历史区
         `git commit -m "comment"` 等于源代码管理的   
         把我们暂存区里面的文件变成一个历史版本,历史版本要写一下comment，简洁明了告诉自己更新、修改了什么
    - 第一次传入先新建库+手动添加仓库地址
        第一次传入要在网页端新建一个库，建库好了以后会有一个.git地址，第一次同步需要先添加仓库地址
        `git remote add origin https://github.com/guoxiang910223/ceshi1913.git`
    - 第一次上传
        `git push -u origin master ` 
        第一次上传表示把内容上传到 origin 这个地址,master 是上传到远程的 master 分支
    - 第二次上传
        直接`git push`
以上的命令可以在项目的vscode里输入，也可以在项目文件夹里打开get bash here输入

真神奇，要不行的时候都不行，要可以的时候什么方法都可以了


- vscode上传整理一份 
- git代码上传整理一份  ＜（＾－＾）＞

