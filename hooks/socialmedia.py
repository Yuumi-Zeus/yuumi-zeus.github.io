# 导入 textwrap 模块中的 dedent 函数，用于处理多行字符串的缩进
from textwrap import dedent
# 导入 urllib.parse 模块，用于 URL 编码/解码
import urllib.parse

# 定义 Twitter（X）的分享链接基础 URL
x_intent = "https://x.com/intent/tweet"
# 定义 Facebook 的分享链接基础 URL
fb_sharer = "https://www.facebook.com/sharer/sharer.php"

# 定义 MkDocs 的 markdown 处理钩子函数
def on_page_markdown(markdown, **kwargs):
    """
    处理页面 markdown 内容，添加社交分享按钮
    
    Args:
        markdown (str): 原始 markdown 内容
        **kwargs: 包含页面和配置信息的字典
        
    Returns:
        str: 处理后的 markdown 内容
    """
    
    # 从 kwargs 中获取当前页面对象
    page = kwargs['page']
    # 从 kwargs 中获取 MkDocs 配置对象
    config = kwargs['config']
    
    # 检查页面元数据中的 template 字段，如果不是博客文章模板则直接返回原始内容
    if page.meta.get('template') != 'blog-post.html': # Only apply the social media tags to blog posts
        return markdown

    # 构建完整的页面 URL（站点基础 URL + 页面相对 URL）
    page_url = config.site_url + page.url
    # 对页面标题进行 URL 编码，并添加换行符
    page_title = urllib.parse.quote(page.title + '\n')

    # 返回原始 markdown 内容加上新增的社交分享按钮部分
    return markdown + dedent(f"""
    <!-- 社交分享按钮容器，居中显示 -->
    <div style="text-align: center;" markdown="1">
    <!-- 分享标题 -->
    <h2 style="font-weight: bold; text-decoration: underline; padding: 10px; border-radius: 5px;">
    Share on Socials
    </h2>
    [Share on :simple-x:]({x_intent}?text={page_title}&url={page_url}){{ .md-button }}
    [Share on :simple-facebook:]({fb_sharer}?u={page_url}){{ .md-button }}
    </div>
    """)
