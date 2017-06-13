目的首先，我们要mock 这个pdf 里的内容，使之呈现出一个网页

1、这个网页必须是responsive的
2、我们可以将这个网页分成若干个box，见pdf。
   a.header是一个box  宽度100%（黑色边框）
   b.body 是一个box  宽度100% (黑色边框)
   c.body中又可以分为左右两部分，left-body  right-body  分别用红色圈起来
   d.left-body中只需要直接从上到下，竖排三张图片就行
   e.right-body（不妨将main-content）同理又可以分为 theme-header-picture 和 content 两部分（蓝色内容）
   f.theme-header-picture elements 占 parents elemet的100%
   g.content分为3列排列
   
3、准备一个简单网页，实现上述draft

4、准备图片进行填充

5、添加medie query 适应多屏幕