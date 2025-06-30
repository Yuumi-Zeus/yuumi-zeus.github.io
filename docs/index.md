---
hide:
  - navigation
comments: true
---
# README

## 简介

`Odin Toolkits For Unity` 是一个依赖 Unity 著名插件 `Odin Inspector and Serializer`（以下简称为 `Odin Inspector` ）的扩展工具集，开源项目，模块化设计，积累对整个项目低侵入性，尽量无侵入性的解决方案，尽量做到不使用则无感。

`GitHub` 项目链接: [OdinToolkits-For-Unity](https://github.com/Yuumi-Zeus/OdinToolkits-For-Unity)

`Unity AssetStore` 网站链接：[AssetStore Odin Inspector](https://assetstore.unity.com/packages/tools/utilities/odin-inspector-and-serializer-89041)

`Odin Inspector` 官网链接：[Sirenix Odin Inspector](https://odininspector.com/)

## 项目愿景

- 成为使用 `Odin Inspector` 的开发者的首推工具包。
- 能够帮助开发者快速学习使用 `Odin Inspector`，发挥其更多的价值，而不是仅了解官方提供的 `Attribute`。
- 能够提供更多优雅的，效率高的解决方案。

## 项目适合的人群

- 拥有 `Odin Inspector` 的开发人员，可以提供更多的解决方案。
- 想尝试使用 `Odin Inspector` 的开发人员，可以提前了解 `Odin Inspector` 插件，查看它能实现的效果。
- 准备进行开发 `Unity 编辑器扩展` 的人员，可以有更多的案例参考。
- 认同 `ScriptableObject` 模块化设计的开发人员，项目内部编辑器阶段大量使用 `ScriptableObject`。
- 只想使用官方提供的 `Attribute`，但是对 `Odin Inspector` 提供的特性使用方法不熟悉的 **使用中文的开发者**，内部包含 `Attribute` 中文解析窗口。
- 想进行插件开发的人员，提供了部分工具和参考，包括 API 文档，网页方案（此项目）。
- 使用 `Rider` 的 `Unity` 开发人员，`Odin Inspector` 和 `Rider` 达成了初步合作。

## 项目结构

``` title="项目树形结构图"
Plugins/
├─ Yuumix/
│  ├─ OdinToolkits/
│  │  ├─ Architecture/
│  │  ├─ Common/
│  │  ├─ Examples/
│  │  ├─ Modules/
│  │  ├─ ThirdParty/
│  │  ├─ CHANGELOG.md
```

项目结构目前可以划分为三个模块：

- `核心模块 [Core Modules]`：除了 `WorkInProgress/` 和 `Community/` 之外的所有文件，通常由我个人 `[Yuumi Zeus]` 编写以及维护，支持其他开发者贡献 `[Contribute]` ，但是需要遵守 `Odin Toolkits` 的代码规范，我将会审查贡献代码，维持 `Core Modules` 的代码规范统一。在持续迭代 `Core Modules` 过程中，我会不断吸收合并 `WorkInProgress` 模块中的代码，以及认真学习`Community` 模块中的解决方案。
- `工作进行中模块 [WorkInProgress/]`：`WorkInProgress/` 文件夹的所有内容，类似于 `Unity` 的 `Experimental`, 仅由我个人提交代码，**此模块不接受贡献 `[Contribute]`**，并提交给 `Core Modules` 模块进行合并，并持续迭代，同时会与 `Core Modules` 模块进行代码合并，并持续迭代。
- `社区模块 [Community]`：`Community/` 文件夹的所有内容，类似于 `Odin Inspector` 的 `Community`, 非常欢迎其他开发者提交代码，此模块贡献 **只有一个要求**：进行 `Build` 空包测试，在只包含 `Odin Inspector` 和 `Odin Toolkits` 的项目工程中，构建没有出现错误。

!!! tip 

    感谢你看到这里，如果 Odin Toolkits 在你的 Unity 开发中切实提供了帮助，恳请为项目点亮一颗 ★ Star！
    
    你的每一份支持都是我在业余时间持续维护、迭代项目的最强动力。

    如果 Odin Toolkits 打包出现错误，或者代码规范不符合要求，请提 issue。或者留言给我，我会及时处理。
   
