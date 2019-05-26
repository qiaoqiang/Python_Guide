# Python的C-API接口

- Python 的应用编程接口（API）使得C 和C++ 程序员可以在多个层级上访问Python 解释器。该API 在C++ 中同样可用，但为简化描述，通常将其称为Python/C API。使用Python/C API 有两个基本的理由。
  - 第一个理由是为了特定目的而编写扩展模块；它们是扩展Python 解释器功能的C 模块。这可能是最常见的使用场景。extending Python.
  - 第二个理由是将Python 用作更大规模应用的组件；这种技巧通常被称为在一个应用中embedding Python。
- 编写扩展模块的过程相对来说更易于理解，可以通过“菜谱”的形式分步骤介绍。使用某些工具可在一定程度上自动化这一过程。虽然人们在其他应用中嵌入Python 的做法早已有之，但嵌入Python 的过程没有编写扩展模块那样方便直观。
- 许多API 函数在你嵌入或是扩展Python 这两种场景下都能发挥作用；此外，大多数嵌入Python 的应用程序也需要提供自定义扩展，因此在尝试在实际应用中嵌入Python 之前先熟悉编写扩展应该会是个好主意。


# Python的C扩展与嵌入



1. 如何使用C 或C++ 编写模块以使用新模块来扩展Python 解释器的功能。这些模块不仅可以定义新的函数，还可以定义新的对象类型及其方法；(python-ethtool)

2. 描述了如何将Python 解释器嵌入到另一个应用程序中，以用作扩展语言；(collected)
3. Cython的Python代码加速方法   (pyzmq)





## extending Python（扩展）





## embedding Python（嵌入）

