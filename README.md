# hexo_hook
VPS接受WebHooks人Python脚本


## 前提
1. 成功安装hexo环境，手动可以发布博客
2. 成功安装git，并且已经`git pull origin master`
具体操作方法可以参考[hexo多电脑同步 ](http://blog.learso.com/2016/07/08/hexo-syn-in-pcs/)

## 步骤
1. 把build.sh他hook.py放到你的hexo工作目录
2. 在WebHook看设置URL为http://your_domain/deploy:8989，端口可以在hook.py中修改
3. 写文章，并且提交到git仓库
4. 完成
