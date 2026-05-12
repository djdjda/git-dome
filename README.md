## 欢迎来到 Cloud Studio ##

当前模板包含最简单的Hello World以及运行指令的Python示例代码仓库

##  “运行”按钮怎么使用 ##

点击运行按钮会自动运行，是因为有 `.vscode/preview.yml` 文件存在。

该文件的格式说明如下：

```yml
# .vscode/preview.yml
autoOpen: false
apps:
  - port: 5000
    run: 'pip install -i https://mirrors.tencent.com/pypi/simple/ -r ./requirements.txt && python ./app.py'
    root: ./web
    name: Python Cloud Studio Demo
    description: Python Cloud Studio Demo Project
    autoOpen: true

```


## 帮助和支持
### 1. Cloud Studio 相关支持
- [Cloud Studio 帮助文档](https://cloudstudio.net/docs/)
- [本模板已内置 腾讯云智能编码工具CodeBuddy Code, 点击查看使用文档](https://cloudstudio.net/docs/guide/code_editing/productivity_plugin/codebuddycode/)
- [nosleep 空间不休眠脚本使用方法](nosleep.md)

### 2. 用户反馈群
扫码加入 Cloud Studio 用户反馈群，获取实时技术支持：
- 腾讯云工程师群内答疑，解决环境与训练问题；
- 优先体验产品上新功能，获取专属活动通知；
- 与其他开发者交流 LoRA 训练经验与技巧。

<img title="" src="img/image.png" alt="Cloud Studio 用户反馈群" width="200">