#遇到的bugs
>Q:下载`openCV`库的时候报 `ReadTimeoutError`<br>
>A1:下载的时候指定`timeout`时间稍微长一些，我这里设置了一个很大的值：<br>
>ACT:pip --default-timeout=100000 install opencv-python
>A2:可以在本地配置下载时使用清华源，（不过我刚刚配置完了以后并没有成功）<br>
>ACT:在Windows下：在`Users`文件夹下的`Administrator`中新建一个文件夹pip，并将以下信息保存<br>
> [global]
> index-url = https://pypi.tuna.tsinghua.edu.cn/simple