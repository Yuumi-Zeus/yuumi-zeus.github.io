﻿# `YuumixLogger static class`
## Introduction
- NameSpace: `Yuumix.OdinToolkits.Common.Logger`
- Assembly: `Assembly-CSharp-firstpass`

``` csharp
[MultiLanguageComment]
public static class YuumixLogger : System.Object
```
### Description
- Yuumix Odin Toolkits 的日志工具，提供多种封装的 Log 方法
- The logging tool of Yuumix Odin Toolkits offers a variety of encapsulated Log methods.

## Methods
| 方法 | 注释 | Comment |
| :--- | :--- | :--- |
| `public static void CompleteLog(string message, LogType logType, Type logTagType, Object sender, bool showTimeStamp, string prefix, Color prefixColor, bool useCallerSuffix, string suffix, Color suffixColor, bool writeToFile, string filePath, int lineNumber, string memberName)` | 无 | No Comment |
| `public static void EditorLog(string message, Type logTagType, string prefix, Object sender, bool showTimeStamp, bool writeToFile, string filePath, int lineNumber, string memberName)` | 无 | No Comment |
| `public static void EditorLogError(string message, Type logTagType, string prefix, Object sender, bool showTimeStamp, bool writeToFile, string filePath, int lineNumber, string memberName)` | 无 | No Comment |
| `public static void EditorLogWarning(string message, Type logTagType, string prefix, Object sender, bool showTimeStamp, bool writeToFile, string filePath, int lineNumber, string memberName)` | 无 | No Comment |
| `public static void Log(string message, Type logTagType, string prefix, Object sender, bool showTimeStamp, bool writeToFile, string filePath, int lineNumber, string memberName)` | 无 | No Comment |
| `public static void LogError(string message, Type logTagType, string prefix, Object sender, bool showTimeStamp, bool writeToFile, string filePath, int lineNumber, string memberName)` | 无 | No Comment |
| `public static void LogWarning(string message, Type logTagType, string prefix, Object sender, bool showTimeStamp, bool writeToFile, string filePath, int lineNumber, string memberName)` | 无 | No Comment |



## Inherited Members
| 成员 | 注释 | 声明此方法的类 |
| :--- | :--- | :--- |
| `public virtual bool Equals(Object obj)` | 无 | `System.Object` |
| `public virtual int GetHashCode()` | 无 | `System.Object` |
| `public Type GetType()` | 无 | `System.Object` |
| `public virtual string ToString()` | 无 | `System.Object` |
| `protected virtual void Finalize()` | 无 | `System.Object` |
| `protected Object MemberwiseClone()` | 无 | `System.Object` |

## Addition Description
- 不要修改标题级别和内容，## Addition Description 是标识符
- Addition Description 之后的内容不会被新生成的文档覆盖，可以对特定的方法进行额外说明
