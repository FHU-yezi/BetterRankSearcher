# 项目简介

一个更好的简书上榜查询工具。

灵感源自：https://js.zhangxiaocai.cn/

# 部署

推荐使用 Docker 部署。

您需要在 `27017` 端口启动一个 MongoDB 数据库服务，并将其加入名为 `mongodb` 的 Docker 网络中。

将项目下载至本地：

```bash
https://github.com/FHU-yezi/BetterRankSearcher.git
```

进入项目目录：

```bash
cd BetterRankSearcher/
```

启动：

```bash
docker compose up -d
```