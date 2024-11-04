---
draft: false
title: "路由安防实践为何推广如此缓慢？"
date: 2024-11-03T19:38:00+08:00
---


[原文](https://pulse.internetsociety.org/blog/why-is-routing-security-adoption-moving-so-slowly)所有权利归原作者（Josephine Wolff）所有。本译文仅供个人学习研究和交流使用。

All rights of the [original work](https://pulse.internetsociety.org/blog/why-is-routing-security-adoption-moving-so-slowly) belong to the original author(s) (Josephine Wolff). This translation work is for personal study and research and communication purposes only.

---

原文发表时间：2024 年 10 月 15 日。

梗概
* 在网络内采用路由安防的最佳实践，可以降低客户流量被劫持的风险。
* 地理位置、网络规模、业务类型和地址空间的复杂度，都会影响路由安防措施的采纳程度。
* 最新发现能帮助政策制定者了解当前的挑战，并帮助推广路由安防实践。

路由安全并不是一个新问题。几十年来，人们一直知道，为实现域间路由而设计的、广泛使用的协议，即边界网关协议（[BGP](https://pulse.internetsociety.org/glossary#bgp)），存在关键性的漏洞：它缺乏一种内置机制来验证路由信息，这些信息在网络间共享，用来为数据流量选择全局路由。

这意味着，当网络在决定流量转发目的地时，往往无法验证目的地网络是否真正能够将其传送到预定地址。因此，[流量](https://arstechnica.com/information-technology/2022/09/how-3-hours-of-inaction-from-amazon-cost-cryptocurrency-holders-235000/)[经常](https://securityboulevard.com/2024/01/orange-spain-outage-bgp-traffic-hijacked-by-threat-actor/)[会被](https://www.zdnet.com/article/russian-telco-hijacks-internet-traffic-for-google-aws-cloudflare-and-others/)[路由](https://www.bleepingcomputer.com/news/security/cloudflare-blames-recent-outage-on-bgp-hijacking-incident/)到错误的网络，无论是出于意外还是恶意。人们常把这种问题称为 BGP 劫持。

由于 BGP 劫持由来已久，研究人员和技术专家设计了各种方法来阻止它的发生。最常用的解决方案之一，是一个名为 “资源公钥基础设施”（[RPKI](https://pulse.internetsociety.org/glossary#rpki)）的框架，于 2012 年由互联网工程任务组标准化。

在 RPKI 框架下，网络能够发布加密记录，其他网络可以用它们来验证通过 BGP 传播的信息，有效确保网络流量不被劫持。不过，要充分受益于 RPKI 的保护，网络需要为它们使用的整个 IP 地址空间发布 RPKI 记录。

在[这里](https://pulse.internetsociety.org/reports)，您能够查看所处国家的 IP 地址空间内 RPKI 记录的覆盖率。

令人沮丧的是，尽管 RPKI 已经存在了十多年，但推广一直很慢。在 2024 年的今天，全球通过 BGP 发布的 IP 地址中，只有大约一半有 RPKI 记录。

{{< figure src="https://pulse.internetsociety.org/wp-content/uploads/2024/10/Internet-address-space-covered-by-ROA_Oct2024.png" link="https://pulse.internetsociety.org/wp-content/uploads/2024/10/Internet-address-space-covered-by-ROA_Oct2024.png" caption="图 1 - 使用 RPKI 加强互联网路由安全有两个要素。第一个要素是网络运营商要发布路由起源认证（Route Origin Authorization，ROA）。ROA 是一种经过加密签名的对象，说明了对于一段或者一组 IP 地址前缀，哪个自治系统（[AS](https://pulse.internetsociety.org/glossary#as)/网络）拥有使用它们作为源地址的授权。资料来源：[Pulse](https://pulse.internetsociety.org/en/technologies/#metric-roa-coverage)；数据来自 [APNIC](https://pulse.internetsociety.org/glossary#apnic) 实验室。" >}}

我们希望通过研究了解 RPKI 的部署为何如此缓慢，哪怕它能解决的安全风险已经众所周知，以及哪些组织在 RPKI 的部署方面处于滞后状态。我们希望这些发现能为政策制定者提供参考，以推进 RPKI 的部署，从而增强 BGP 的安全保障。在美国政府[再次发力](https://www.fcc.gov/document/fcc-proposes-internet-routing-security-reporting-requirements-0)推动解决路由安全问题的近期背景下，这项工作的意义就更为突出了。

# 地域和网络规模是影响 RPKI 部署的关键因素

在分析中，我们发现了影响各个组织部署 RPKI 的四个关键特征：地理位置、网络规模、业务类型和地址空间的复杂度。

我们认为，RPKI 部署率的地域差异源于各个地区互联网注册管理机构 (RIR) 各自独立的 RPKI 记录发布流程和要求。最终它们导致每个 [RIR](https://pulse.internetsociety.org/glossary#rir) 管理的地理区域的 RPKI 部署情况各不相同。

{{< figure src="https://pulse.internetsociety.org/wp-content/uploads/2024/10/RPKI-adoption_Fig1.png" link="https://pulse.internetsociety.org/wp-content/uploads/2024/10/RPKI-adoption_Fig1.png" caption="图 2 - 资源公钥基础设施 (RPKI) 在各地区互联网注册管理机构辖区的覆盖率（AFRINIC = 非洲，APNIC = 亚太地区，[ARIN](https://pulse.internetsociety.org/glossary#arin) = 北美和加勒比地区，[LACNIC](https://pulse.internetsociety.org/glossary#lacnic) = 南美和中美洲，RIPENCC = 欧洲和中东）。" >}}

而且，网络的规模也是一个重要因素，因为 RPKI 要求额外的管理和操作，而在日常运维中增加这些工作对规模较小的网络更具挑战性。

此外，相比于那些与在线服务关系密切的组织，与互联网服务无关的组织比如教育和政府网络，对 RPKI 的认知和部署动力要更少。

{{< figure src="https://pulse.internetsociety.org/wp-content/uploads/2024/10/RPKI-adoption_Fig2.png" link="https://pulse.internetsociety.org/wp-content/uploads/2024/10/RPKI-adoption_Fig2.png" caption="图 3 - 使用 RPKI 签名和加密的 [IPv4](https://pulse.internetsociety.org/glossary#ipv4) 地址占比，对比头部10%的大网络和尾部10%的小网络（按源地址空间总量排序）。" >}}

最后，即使是在大型网络内，针对不同 IP 地址发布 RPKI 记录所需的工作量也不尽相同。地址空间的授权和再分配所涉及的法务和运维挑战，可能会使一部分地址空间更难部署 RPKI。

您可以阅读我们的[论文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4948317)来了解有关此研究和结果的更多详情。

我们计划以这些结果作为更广泛研究的起点，探寻那些落后于 RPKI 部署的组织所面临的障碍，并最终提出可能的政策方案，帮助人们在未来应对这些挑战。

其它贡献者：Cecilia Testart、Deepak Gouda 和 Romain Fontugne。

[Josephine Wolff](https://www.linkedin.com/in/josephine-wolff-1baa414b/) 是塔夫茨大学弗莱彻学院网络安全政策副教授。

本博客作者的观点仅属于作者本人，不代表互联网协会的观点。

---

译文作者：王文鑫

转载需注明“本译文仅供个人学习研究和交流使用”，注明原作者、译文作者和引用出处。

在保证原作者所有权益的情况下，本译文使用 Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International 授权，详情见 https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en。超出此授权范围之外的使用需获得“计算机史料随译”项目的许可，详情见 https://random-cs-hans.github.io。

On the precondition of keeping all rights of the original authors, this translation work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike License (International/4.0), see https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en for details. Permissions beyond the scope of this license are administered by the "RandomCSHans" Project，see https://random-cs-hans.github.io.

{{< figure src="http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-nc-sa.svg" alt="CC BY-NC-SA License" >}}
