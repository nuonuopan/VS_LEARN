
####使用
#####【运行】
- [编辑器单步运行]python 编辑器单步运行按`F8`,或者右键 👉 在终端中运行指定的行
- [运行完整文件]运行整个文件,可以在终端直接输入 `python 文件名.py` 或右键👉在终端中运行python文件；当文件所在位置指定不明的时候，要填写绝对路径`python f:/vs_learn/demo2/test_2.py`
- [运行完整文件]当不设置断点的时候直接`F5`进入调试也等于直接运行文件进行输出


#####【调用上一级目录文件】
- `.\` 代表上一级目录  `python .\hello_word.py`
- 步骤
   ```
   # 导入库
   import sys
   # 把当前.py文件存在的文件夹的上一级文件夹添加到路径搜索系统里去
    sys.path.append("./")
   # 然后才能把上一级.py文件当成模块，导入模块里的函数
   from demo1 import test_1 #导入模块中的文件
   test_1.print_hello() #导入文件中的函数
  ```
- 可能出现的问题：导入模块在导入库前 
    - 一般是autoppep8设置保存自动格式化后，会将下面的import放入页面底部的问题（我用的black，目前无问题）
    - 解决方案*[参考](https://blog.csdn.net/qq_16829085/article/details/107214948?utm_medium=distribute.pc_aggpage_search_result.none-task-blog-2~aggregatepage~first_rank_ecpm_v1~rank_v31_ecpm-1-107214948-null-null.pc_agg_new_rank&utm_term=pep8%E8%AE%BE%E7%BD%AEimport%E9%A1%BA%E5%BA%8F+vscode&spm=1000.2123.3001.4430)：
    1. 打开 VSCode的设置，添加下面的语句，让 autopep8 忽略 E402，也就是 “模块级别导入不在文件顶部”错误。
      `"python.formatting.autopep8Args": ["--ignore", "E402"]`
    2. 在需要固定位置的 import 语句后面加上 `# NOQA: E402` 注释
      ```
      import os
      from bluelog import create_app  # NOQA: E402
      ```


#####【debug】
- `Ctrl+Shift+D` 打开 debug 窗口
- `F5`进入调式界面，
- `F9`设置断点
- `F10`单步运行
- `F11`进入函数来调试


#####【vscode 每个项目安装虚拟环境设置】
- 利用 anaconda 来设置，和平时用 anaconda 建立虚拟环境一样,此时是一整个环境，用conda管理环境包
    - 【创建一个名字为 p350,版本为 python3.5.0的虚拟环境】`conda create --name p350 python=3.5.0`
- 单独一个文件一个包，用pip管理环境包
    - 环境要先安装两个包 `pip install virtualenv` `pip install virtualenvwrapper-win`
    - 建立虚拟环境，`python -m venv .venv`       .venv是虚拟环境名字
    - 进入虚拟环境：把.venv的Script的activate.bat拉到cmd编辑框，前头显示出(.venv)即为进入到虚拟环境
     - 如果是把activate.bat拉到powershell编辑框会报错，[参考](https://zhuanlan.zhihu.com/p/403713319)
      1. 以管理员身份运行powershell
      2. 输入 `set-executionpolicy remotesigned` 然后 `y`
      (我已经设定好了可以直接使用)
    - 在当前虚拟环境里下载包  `pip install pandas` 不能用conda，否则会直接安装到anaconda的base；在cmd或者powershell都可以
      - 下载包，设置防止超时报错+使用镜像
      `pip --default-timeout=100 install flask_script -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com`
      上面--default-timeout=100是防止那个timeout报错的，后面用的镜像源。
- 两种方法的区别是：①anaconda利用conda管理包，选择解释器的时候选择新建的环境即可，而后者利用pip管理包，在选择解释器时选择当前建立的虚拟环境后要把activate.bat拉入终端，进入虚拟环境以后前面会有(.venv)显示，前者没有；


#####【使用 jupyter】
- 建立.ipynb 文件
- 打开右侧有个[选择内核]
- 选择好后每个框框左侧有个三角形，点击运行即可


#####【设置】
- `Ctrl+,`快捷打开
- 用户设置是全局；当前工作空间是局部
- 如果用户和工作空间设置了同样的项目，局部的会覆盖全局的设置


####美化
#####【自动化排版】
- black 库 pip install black
- 命令行中使用：black 文件名.py
- 自动集成排版：设置 👉 搜 format on save👉 ✔
  👉 搜 python format provider👉 选 black
  【自动化排版不排版 markdown】#todo
- 设置中加入局部过滤：
    <details><summary>代码段</summary>
    <p>

    ```
    "[markdown]": {
        "editor.wordWrap": "on",
        "editor.quickSuggestions": false,
        "editor.formatOnSave": false
      },
    ```
    </details> </p>


#####【python 设置代码自动补充冒号和()】  
  ```
  "python.analysis.completeFunctionParens": true,
  "python.autoComplete.addBrackets": true,
  ```


####插件
#####【Material Icon Theme】
  - 图标主题；设置 👉 文件图标主题


#####【autoDocstring】
  - 注释；用三个"""调出，按 tab 去填写


#####【Todo Tree】
  - 要用`#`开头
  - 按照别人的方法设置了一下更新；采用下面这段代码，直接打开设置的 json 加进去 \*[参考](https://blog.csdn.net/cc1998414/article/details/115408584)
    <details><summary>代码段</summary>
    <p>

    ```
      "todo-tree.tree.showScanModeButton": false,
      "todo-tree.filtering.excludeGlobs": ["**/node_modules", "*.xml", "*.XML"],
      "todo-tree.filtering.ignoreGitSubmodules": true,
      "todohighlight.keywords": [
      ],
      "todo-tree.tree.showCountsInTree": true,
      "todohighlight.keywordsPattern": "TODO:|FIXME:|NOTE:|\\(([^)]+)\\)",
      "todohighlight.defaultStyle": {

      },
      "todohighlight.isEnable": false,
      "todo-tree.highlights.customHighlight": {
        "BUG": {
          "icon": "bug",
          "foreground": "#F56C6C",
          "type": "line"
        },
        "FIXME": {
          "icon": "flame",
          "foreground": "#FF9800",
          "type":"line"
        },
        "TODO":{
          "foreground": "#FFEB38",
          "type":"line"
        },
        "NOTE":{
          "icon": "note",
          "foreground": "#67C23A",
          "type":"line"
        },
        "INFO":{
          "icon": "info",
          "foreground": "#909399",
          "type":"line"
        },
        "TAG":{
          "icon": "tag",
          "foreground": "#409EFF",
          "type":"line"
        },
        "HACK":{
          "icon": "versions",
          "foreground": "#E040FB",
          "type":"line"
        },
        "XXX":{
          "icon": "unverified",
          "foreground": "#E91E63",
          "type":"line"
        }
      },
      "todo-tree.general.tags": [
        "BUG",
        "HACK",
        "FIXME",
        "TODO",
        "INFO",
        "NOTE",
        "TAG",
        "XXX"
      ],
      "todo-tree.general.statusBar": "total",
    ```
    </details> </p>

#####【Markdown Preview Enhanced】
  - 一个 markdown 来画流程图、时序图

    ```sequence
    title:简单示例
    A->B:HELLO
    B-->A:WORLD
    ```

#####【Git Graph】
  - 源代码管理 👉 右侧出现一个 View Git Graph 点击 👉 可以看到每次存的版本 👉 点击可以看到更改文件更改的对比,且可以回溯版本

#####【IntelliCode】
  - 语法代码提示

#####【indent-rainbow】
  - 彩虹缩进
  - 正确语法会报错，改一个配置，打开设置，输入下面语法~~
    <details><summary>代码段</summary>
    <p>

    ```
        "todo-tree.general.statusBar": "total",
        "indentRainbow.ignoreErrorLanguages": [
            "python"
        ],
    ```
  </details> </p>


#####【local history】
  - 这个软件是保存更改的不同处，但需要自己“保存”了才能保存更改处（因只保存更改处，所以不会占用太大内存）
  - 所以配合使用vscode的自动保存才能无缝衔接保存更改处，自动保存设置如下
  - 在设置里搜索save
    - 把`File:Auto Save`改为`afterDelay`
    - `Code-runner:Save File Before Run`改为 `true`
    - `Files: Auto Save Delay` 是更改自动保存的间隔时间，可以设置的久一点，减小拖垮时间；我设置为10分钟自动保存一次

#TODO: 同步 vscode 设置（bilibili 视频）

####学习文档：
##### - 【markdown学习文档】
  - *[参考](https://docs.github.com/cn/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

####记录：
1. JSON检测错误，让把`"terminal.integrated.shell.windows": "C:\\Windows\\System32\\cmd.exe",`改成`"terminal.integrated.defaultProfiles.windows": "C:\\Windows\\System32\\cmd.exe"；`我简单记录一下