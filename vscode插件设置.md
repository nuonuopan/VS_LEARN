【运行】
- python 单步运行按`F8`,或者右键 👉 在终端中运行指定的行
- 运行整个文件,可以在终端直接输入 `python 文件名.py`

【debug】
- `Ctrl+Shift+D` 打开 debug 窗口
- `F5`进入调式界面，
- `F9`设置断点
- `F10`单步运行
- `F11`进入函数来调试

【自动化排版】
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

【python 设置代码自动补充冒号和()】
  <details><summary>代码段</summary>
  <p>
  
  ```
  "python.analysis.completeFunctionParens": true,
  "python.autoComplete.addBrackets": true,
  ```
  </details> </p>

【vscode 每个项目安装虚拟环境设置】
- 利用 anaconda 来设置，和平时用 anaconda 建立虚拟环境一样,此时是一整个环境，用conda管理环境包
- 单独一个文件一个包，用pip管理环境包
    - 环境要先安装两个包 `pip install virtualenv` `pip install virtualenvwrapper-win`
    - `python -m venv .venv`       .venv是虚拟环境名字
    - 进入虚拟环境：把.venv的Script的activate.bat拉到cmd编辑框，前头显示出((.venv)即为进入到虚拟环境
    - 在当前虚拟环境里下载包  `pip install pandas` 不能用conda，否则会直接安装到anaconda的base


#TODO：【调用上一级目录文件】





【使用 jupyter】
- 建立.ipynb 文件
- 打开右侧有个[选择内核]
- 选择好后每个框框左侧有个三角形，点击运行即可

【设置】
- `Ctrl+,`快捷打开
- 用户设置是全局；当前工作空间是局部
- 如果用户和工作空间设置了同样的项目，局部的会覆盖全局的设置

【插件】
- Material Icon Theme
  图标主题；设置 👉 文件图标主题

- autoDocstring
  注释；用三个"""调出，按 tab 去填写

- Todo Tree
  要用`#`开头
  按照别人的方法设置了一下更新；采用下面这段代码，直接打开设置的 json 加进去 \*[参考](https://blog.csdn.net/cc1998414/article/details/115408584)

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

- Markdown Preview Enhanced
  一个 markdown 来画流程图、时序图

```sequence
title:简单示例
A->B:HELLO
B-->A:WORLD
```

- Git Graph
  源代码管理 👉 右侧出现一个 View Git Graph 点击 👉 可以看到每次存的版本 👉 点击可以看到更改文件更改的对比,且可以回溯版本

- IntelliCode
  语法代码提示

- indent-rainbow
  彩虹缩进
  正确语法会报错，改一个配置，打开设置，输入下面语法~~
    <details><summary>代码段</summary>
    <p>

    ```
        "todo-tree.general.statusBar": "total",
        "indentRainbow.ignoreErrorLanguages": [
            "python"
        ],
    ```
    </details> </p>

#TODO: b站up--向量cwl的视频，有调用上一级目录的方法
#TODO：回溯历史版本
#TODO: 同步 vscode 设置（bilibili 视频）
【markdown学习文档】
  - *[参考](https://docs.github.com/cn/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
