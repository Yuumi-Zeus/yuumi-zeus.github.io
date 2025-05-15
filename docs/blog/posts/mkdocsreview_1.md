---
date: 
  - created: 2025-05-15
  - updated: 2025-05-15
categories:
  - 复盘
tags:
  - MkDocs
authors:
  - Yuumi-Zeus
slug: mkdocsreview_1
comments: true
---

# MkDocs 复盘 - 1

这是有关于 MkDocs-Materia 的部分使用记录。

<!-- more -->

## 自定义域名

### 步骤

    1. 购买一个域名，可以在阿里云，腾讯云，华为云，以及国外的 namecheap 等等。
    2. 进行 DNS 解析，添加解析记录。
    3. 在 GitHub 上添加 CNAME 文件，可以是 www.<yourdomain.com> 也可以是 <yourdomain.com>。这个内容取决于添加的解析记录。
    4. 然后在仓库的 Pages 页面设置自定义域名，点击 Save。

!!! tip "DNS 提示"

    1. 购买域名和 DNS 解析，不是同一个东西，你购买域名后，要使用 DNS 解析，才能生效。对于 github pages 来说，最好选可以免费 4 条以上的负载均衡的 DNS 解析。虽然只使用 www | CNAME | <username>.github.io 也可以运行，但是稳定（安全），要开启 HTTPS，需要针对github 的四个 ip 提交记录：185.199.108.153、185.199.109.153、185.199.110.153、185.199.111.153。所以建议使用负载均衡可以 4 条及以上的 DNS 解析。
    2. 如果你不幸选择了腾讯云（DNS 免费只有 2 条负载均衡，不知道为什么，不知道它有什么优势，第一次使用），那么你可以首先添加一条 www | CNAME | <username>.github.io，然后继续添加 a1 | A | 185.199.108.153、a1 | A | 185.199.109.153、a2 | A | 185.199.110.153、a2 | A | 185.199.111.153。最后再添加 @ ｜ CNAME ｜ a1.<yourdomain.com>、@ | CNAME | a2.<yourdomain.com>。可以以上方式曲线救国，但是根据 AI 的建议，可能会不稳定（不懂）。
    3. 如果可以四条负载均衡，那么可以直接添加 @ | A | 185.199.108.153、@ | A | 185.199.109.153、@ | A | 185.199.110.153、@ | A | 185.199.111.153、www ｜ CNAME ｜ www.<yourdomain.com>。一共五条。
