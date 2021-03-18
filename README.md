## 项目介绍

霍格沃兹测试学院 测开17期实战演示

## 霍格沃兹

- [测试人论坛] https://ceshiren.com/

## 参考链接

pytest: https://docs.pytest.org/en/stable/getting-started.html

## Google开源项目 Python风格规范

https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/

## 作业地址

## 课程内容

1. git环境搭建 代码->本地仓库->远程的git仓库 git命令：https://ceshiren.com/t/topic/7405

2. 搭建环境的参考步骤： （1）本地安装git，并在github上注册账号 （2）在github上面创建repository （3）在pycharm里面打开要执行的文件执行commit，点右边的√，加注释 (在pycharm
   terminal中执行git init，在本地初始化git本地仓库)
   （4）选择要忽略的文件加入到.ignore里 （5）push代码到repository中

3. 安装pytest （1）File->Settings->搜索框输入'pytest', 在Testing Default test runner切换到pytest，点OK （2）在project中的 Python
   interpreter，右边窗口下面点+，输入pytest，install package

4. 命令行运行报错： 在test_calculator.py的test_add方法报错：ModuleNotFoundError:No module named 'pythoncode'
   解决方法：因为导入的包pythoncode在HogwartsSDET17总目录下，所以在导入包之前，把HogwartsSDET17的路径append进去

5. pytest常用参数 pytest --collect-only 只收集用例

pytest -k "add" 匹配所有用例中，名称包含add的用例

方法前加上@pytest.mark.标签名 pytest -m mark 标签名查找 需要将自定义的标签名添加到pytest.ini文件，才不会有PytestUnknownMarkWarning

6. setup_module: 模块级别，模块前使用 teardown_module: 模块级别，模块后使用 setup_class: 类级别，类前使用 teardown_class: 类级别，类后使用 setup_function:
   函数级别，只对测试用例生效，函数前使用，在类外 teardown_function: 函数级别，只对测试用例生效，函数后使用，在类外 setup: 方法级别，在类中，方法前使用 teardown: 方法级别，在类中，方法后使用

7. 装饰器
   (1)在方法前加上: @pytest.mark.parameterize()
   (2)方法中加上相对应的参数个数

8. yaml菜鸟教程 https://www.runoob.com/w3cnote/yaml-intro.html
   YAML 的配置文件后缀为 .yml

基本语法:
大小写敏感 使用缩进表示层级关系 缩进不允许使用tab，只允许空格 缩进的空格数不重要，只要相同层级的元素左对齐即可
'#'表示注释

数据类型:
-字典类型 key:{key1: value1, key2: value2} key:
child-key: value child-key2: value2

数组类型 以 - 开头的行表示构成一个数组

- A
- B
- C

yaml.safeload(): 将yaml的数据流转换为python的对象 yaml.safedump(): 将ptyhon的对象转换成yaml格式

定义类变量:
:后面接list表示定义一个list类型的变量(类型提示)
例如: datas:list=get_datas()

浮点数相加:
0.1+0.2=0.30000004 通过round方法来控制位数 pi=3.1415926 例: round(pi,2)=3.14 或者导入Decimal方法来控制精度 from decimal import Decimal
Decimal('0.1')+Decimal('0.2')
得到Decimal('0.3')

捕获异常的方法:
with pytest.raises(exception):
若exception为相匹配的异常，则case将pass