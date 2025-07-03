---
date: 2025-07-03
categories:
  - Odin Toolkits
tags:
  - Odin Editor Analysis
authors:
  - Yuumi-Zeus
slug: multilanguagebuttonattributequestion
comments: true
---

# MultiLanguageButtonAttribute 问题

已经解决 MultiLanguageButtonAttribute 的实时切换问题，但是过程中发现了无法理解的疑点 `[已解决]`，遂记录。

<!-- more -->

## 最终解决方案

多语言的按钮特性的实现一共使用了三个脚本文件，分别是 `MultiLanguageButtonAttribute.cs`,`MultiLanguageButtonAttributeDrawer`,`MultiLanguageAttributeProcessor`。

实现思路是通过 `MultiLanguageButtonAttribute`，在 `Proccessor` 中动态添加 `ButtonAttribute`，然后在 `Drawer` 中动态修改 `ButtonAttribute` 的字段。

`MultiLanguageButtonAttribute` 提供和 `ButtonAttribute` 基本一致的参数，构造函数中的前两位设计为 `ChineseName` 和 `EnglishName`，代替 `ButtonAttribute` 的 `name` 参数。

``` csharp title="MultiLanguageButtonAttribute.cs"
[AttributeUsage(AttributeTargets.All, Inherited = false)]
[Conditional("UNITY_EDITOR")]
public class MultiLanguageButtonAttribute : ShowInInspectorAttribute
{
    public readonly string ChineseName;
    public readonly string EnglishName;
    public readonly ButtonSizes ButtonSize;
    public readonly int ButtonHeight;
    public readonly ButtonStyle Style;
    public readonly SdfIconType Icon;
    public readonly IconAlignment ButtonIconAlignment;

    // 省略 ... 
}
```

其他参数和 `ButtonAttribute` 一致，主要是添加了 `ChineseName` 和 `EnglishName` 两个参数，用于设置按钮的显示名称。

在 `Processor` 中动态添加 `ButtonAttribute`。

``` csharp title="MultiLanguageAttributeProcessor.cs"
public class MultiLanguageAttributeProcessor<T> : OdinAttributeProcessor<T> where T : class
{
    public override void ProcessChildMemberAttributes(InspectorProperty parentProperty, MemberInfo member,
            List<Attribute> attributes)
    {
        if (member.MemberType == MemberTypes.Method &&
            member.GetCustomAttribute<MultiLanguageButtonAttribute>() != null)
        {
            var button = member.GetCustomAttribute<MultiLanguageButtonAttribute>();
            // 静态工厂方法，创建 ButtonAttribute 实例
            var chineseButton = button.CreateChineseButton();
            attributes.Add(chineseButton);
        }
    }
}
```

在 `Drawer` 类中，修改 `Name`

``` csharp title="MultiLanguageButtonAttributeDrawer.cs"
namespace Yuumix.OdinToolkits.Common.InspectorMultiLanguage.Editor
{
    [DrawerPriority(DrawerPriorityLevel.WrapperPriority)]
    public class MultiLanguageButtonAttributeDrawer : OdinAttributeDrawer<MultiLanguageButtonAttribute>
    {
        ButtonAttribute _buttonAttribute;
        ValueResolver<string> _chineseGetter;
        ValueResolver<string> _englishGetter;

        protected override void Initialize()
        {
            _buttonAttribute = Property.GetAttribute<ButtonAttribute>();
            _chineseGetter = ValueResolver.GetForString(Property, Attribute.ChineseName);
            _englishGetter = ValueResolver.GetForString(Property, Attribute.EnglishName);
            _buttonAttribute.Name =
                $"@InspectorMultiLanguageManagerSO.IsChinese ? \"{_chineseGetter.GetValue()}\" : \"{_englishGetter.GetValue()}\"";
        }

        protected override void DrawPropertyLayout(GUIContent label)
        {
            CallNextDrawer(label);
        }
    }
}
```

`Drawer` 的优先级要大于原本的 `ButtonAttribute` 的优先级，因此设置为 `[DrawerPriority(DrawerPriorityLevel.WrapperPriority)]`，要在 `Button` 实际绘制之前修改它的 `Name` 值。

!!! Warning "特别注意"

    ***必须*** 在 `Initialize()` 中修改 `Name` 值，而且 ***必须使用解析字符串*** ，使用 `if-else` 语句判断当前语言进行 `Button.Name` 的赋值无法实时切换。

``` csharp title="如下代码无法实时切换"
if (InspectorMultiLanguageManagerSO.IsChinese)
{
    _buttonAttribute.Name = "测试";
}
else
{
    _buttonAttribute.Name = "Test";
}
```

!!! Success "结果分析"

    因为 `Button` 的 `Name` 值会在它的 `Initialze()` 中用与生成 `ValueResolver<string>`，在 DrawPropertyLayout 中不会再次刷新，所以必须在 `MultiLanguageButtonAttributeDrawer.Initialize()` 中赋值，并使用解析字符串。
    
    实际这样的操作就等于给 `ButtonAttribute` 添加解析字符串，这么做是为了在编码过程中省略了一个返回值为 string 的函数。

