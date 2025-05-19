# GenerateTemplateCode

## 用法

1. 选择脚本模板文件
2. 设置命名空间
3. 设置类名
4. 选择脚本文件生成路径
5. 点击生成

## 扩展脚本模板

1. 找到 `Assets/Plugins/Yuumix/OdinToolkits/Modules/Tools/GenerateTemplateCode/Editor/Template` 文件夹
2. 新建脚本模板文件，文件名必须以 `.txt` 结尾
3. 模板文件中的命名空间使用 `#NAMESPACE#` 占位，类名使用 `#CLASSNAME#` 占位

!!! tip "提示"

    模板文件需要注意引入的命名空间，如果有修改，需要及时修改模板。
