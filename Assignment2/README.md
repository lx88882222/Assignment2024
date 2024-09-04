# 前端作业

## 作业要求

请根据自己的掌握程度、空闲时间和兴趣爱好，在[讲义](https://cloud.tsinghua.edu.cn/d/79c394f05d4b425bb34c/files/?p=%2F%E8%AF%BE%E7%A8%8B%E5%86%85%E5%AE%B9%2F%E5%89%8D%E7%AB%AF%2F%E6%9A%91%E5%9F%B9%E8%AE%B2%E4%B9%89-%E5%89%8D%E7%AB%AF.pdf)末尾给出的项目中选择一个完成。为了鼓励大家多做尝试，作业并没有给出具体的页面细节，也不限定页面结构和数量，具体的样式和交互效果由同学们自己决定。如果你有其他想法，也可以自己设计一个页面并完成。

## 提交方式

本次作业有如下三种提交方式：

1. 将自己的页面部署在 GitHub 的静态页面托管服务上，将项目地址添加到文档中。具体流程见[附录](#GitHub静态页面托管服务)。（推荐）
2. 将自己的页面部署在 Vercel 或者 Heroku 等云服务上，将项目地址添加到文档中。具体流程请参考官方文档。
3. 将自己的页面文件夹按照`网站名称-部门-姓名`的格式提交到`Assignment2`文件夹下。

## Tips

1. 可以在项目根目录下创建一个名为`README.md`的文件，文件中包含项目名称、项目描述、项目地址等信息，可以帮助他人更好地了解你的项目。
2. 请确保你的项目文件夹中包含一个名为`index.html`的文件，这个文件将作为你的网站的首页。
3. 关于AI：本次作业不限制是否使用AI，但是如果你使用了AI，请确保你知道AI完成的部分大致是如何工作的。
4. 课程中仅涉及到了HTML元素中很少的一部分，HTML元素和CSS样式浩如烟海，如果你想制作一个精美的网站，讲义的最后给出了一些参考资料，好好利用他们会对你的作业有所帮助。

## 附录

### GitHub静态页面托管服务

1. 在GitHub上创建一个名为`<username>.github.io`的**Public**仓库，其中`<username>`为你的GitHub用户名。例如，我的GitHub用户名是`zhangsan`，那么我创建的仓库名就是`zhangsan.github.io`。
2. 将你的项目文件夹上传到这个仓库中。注意，你的项目文件夹中必须包含一个名为`index.html`的文件，这个文件将作为你的网站的首页。仓库中的文件结构应该如下所示：
   ```
   zhangsan.github.io
   ├── index.html
   ├── style.css
   ├── script.js
   ├── image.png
   └── ...
   ```
   **注意**：
   1. `<username>`是一个整体，代表应该将这一部分替换为你自己的内容，你的仓库名和最终网址**不应该**带有尖括号：✅`zhangsan.github.io`, ❌`<zhangsan>.github.io`。
   1. index.html应该在这个仓库的**根目录**下，而不是在一个文件夹中。换句话说，当你在GitHub上打开这个仓库时，你应该能够直接看到`index.html`文件，而不是一个名为`<username>.github.io`或者其他什么的文件夹。
   2. 只有index.html文件是必须的，其他文件可以根据你的需要添加。
   3. 请确保只将最终的项目文件夹上传到仓库中，如果你是通过`create-react-app`等工具创建的项目，请只提交生成的`build`文件夹中的内容。（如果你就是想用git管理**所有的**项目文件，那么可以将`build`文件夹重命名为`docs`后提交所有文件，并在`仓库` - `设置` - `Pages`中将部署文件夹修改为`/docs`）
4. 在仓库的设置页面中，找到`Pages`选项，将`Source`设置为`Deploy from a branch`，`branch`设置为你的项目文件所在的分支（一般为`master`或`main`），`folder`选择`/(root)`，然后点击`Save`。这样你的网站就会被部署在`https://<username>.github.io/`这个地址上了。
5. 等待一段时间，然后访问`https://<username>.github.io/`，确认你的网站可以正常访问之后，在`AssignmentList.md`的末尾添加一行，内容为`- [项目名称-部门-姓名](https://<username>.github.io/)`，注意链接中的`<username>`应该替换为你的GitHub用户名。
6. 如果你已经有了一个`<username>.github.io`的仓库，或者因为其他原因无法采用这种方式提交，可以采用其余的提交方式。
7. 示例：<https://github.com/Yelp/yelp.github.io>

### Vercel 或其他云服务

1. 由于各家云服务厂商操作流程不一，因此具体流程请参考官方文档。
2. 确保你的网站可以正常访问之后，在`AssignmentList.md`的末尾添加一行，内容为`- [项目名称-部门-姓名](https://your-website-url/)`，注意链接中的`https://your-website-url/`应该替换为你的网站地址。

### 提交文件夹

如果你选择将项目文件夹提交到此文件夹（`Assignment2`）下，请确保你的文件夹名称符合`网站名称-部门-姓名`的格式。例如，如果你的项目名称是`弹弹球`，部门是`软件部`，姓名是`张三`，那么你的文件夹名称应该是`弹弹球-软件部-张三`。你的文件夹结构应该类似于下面这样：
```
弹弹球-软件部-张三
├── index.html
├── style.css
├── script.js
├── image.png
└── ...
```

## 参考资料

1. [GitHub Pages](https://pages.github.com/)
2. [Vercel](https://vercel.com/)
3. [Netlify](https://www.netlify.com/)
4. [Heroku](https://www.heroku.com/)
5. [Google](https://www.google.com/)
