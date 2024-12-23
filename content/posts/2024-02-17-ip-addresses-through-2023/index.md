---
draft: false
title: "IP 地址这些年 - 2023年回顾"
date: 2024-02-17T00:00:00+08:00
---


[原文](https://blog.apnic.net/2024/01/17/ip-addresses-through-2023/)所有权利归原作者（Geoff Huston）所有。本译文在获得原作者同意后发布，译文版权声明见结尾。

All rights of the [original work](https://blog.apnic.net/2024/01/17/ip-addresses-through-2023/) belong to the original author(s) (Geoff Huston). This translation work is published with the approval of the original author(s) and includes its own copyright disclaimer at the end.

---

又到了一年一度的 IP 地址回顾时间。让我们看看在过去 12 个月中互联网内有哪些寻址相关的变化，以及 IP 地址分配信息是如何向我们揭示互联网不断变化的特性。

早在 1992 年左右，互联网工程任务组（IETF）就曾在 "下一代 IP"研究项目中凝视他们的预言水晶球，试图了解互联网将如何发展，以及这将对寻址系统提出怎样的要求。我们今天所看到的联网设备的惊人数量确实落在了这项研究的预测范围之内，而且无疑将继续增长。

人类在不断提高硅芯片的产量并持续改进生产工艺。不仅如此，我们还曾预言，要想让互联网在如此庞大的联网设备群中正常运行，唯一的办法就是部署一个地址空间远远更大的新 IP 协议。IPv6 正是基于这一推理而设计的，它主要要解决的就是海量硅处理器的世界所带来的问题。IPv6 所包含的巨大地址空间，就是为了让我们能够为每一个这样的设备分配一个唯一的公共 IPv6 地址，无论这些设备有多小，也无论它们的部署规模有多大。

然而，当互联网以惊人的速度发展时，IPv6 的部署进度却相对缓慢而谨慎。目前人们对协议部署的紧迫程度没有展现出任何共识，也仍没有一致认为依赖 IPv4 会拖我们的后腿。

IPv4 互联网目前的设备数量远远大于它设计时理论能支持的用户数量，这其中明显存在矛盾，其背后的主要原因是互联网已经从“点对点”架构迅速地转变为“客户端/服务器”模式。客户端可以向服务器主动发起通信，但无法向其他客户端主动发起通信。

网络地址转换器（NAT）非常适合这种客户端/服务器模式，在这种模式下，客户端共享一个较小的公共地址池，并且只在与远程服务器进行会话期间占用一个地址。因为有了 NAT，300 多亿台联网设备才能挤在约 30 亿个公开 IPv4 地址中。无法通过 NAT 通信的应用程序不再有用，也就不再有人使用了。

然而，互联网设备数量的增长势不可挡，即使是 NAT 也无法永远承受这样的压力。NAT 将有效寻址空间扩展了“额外” 32 比特，并实现了分时地址共享。这两项技术确实有效地拉伸了 IPv4 地址空间以涵盖更多的客户端设备，但它们并不能将地址空间转化为有无限弹性的资源。

这一过程如果继续发展，最终会无可避免地将 IPv4 互联网分割成许多互不相连的部分，每个部分的基底很可能是由各个内容分发服务节点延伸出的服务 "锥筒"。这样一来，“构建于单独统一的数据包传输域之上、全球唯一且一致的地址分配池”这一整个概念将不复存在。

或者，这些增长压力也许会推动 IPv6 的进一步部署，然后随着互联网试图维系它作为一个凝聚联通的整体，网络中会出现纯 IPv6 的成员。这两个方向上都有商业活动在发力，因此现在完全无法分辨互联网在未来几年会走什么样的道路，但我个人犬儒且厌世观点是，网络的未来是高度的分裂。

地址分配数据能否帮助我们了解广阔的互联网正在发生什么？让我们看看 2023 年的情况。

# 2023 年 IPv4 地址数量分析

到 2021 年底，随着各地区互联网注册管理机构（RIR）剩余的未分配地址池耗尽，旧的注册管理机构分配模式实际上已经走到尽头。尽管如此，事实表明，剩余未分配 IPv4 地址池的消耗过程与 IPv6 的过渡一样旷日持久。

在当今的互联网中，“分配”是个难以说明的话题。目前仍有从 RIR 管理的可用地址空间剩余池中提取并分配或指派给网络运营商的地址分派过程，同时也有一些网络之间的地址买卖过程。这两类交易必然涉及注册信息的变更，因此注册机构以类似分配或指派的方式记录转让或出售的结果。

如果我们想更全面地了解互联网网络运营商所使用或可用的 IPv4 地址数量，那么最好的衡量标准应该是已分配和已指派地址的总数，以及对应的各类地址数量的年度变化情况。

> **地址的“分配”和“指派”有什么区别？**
> 网络运营商或子注册中心收到地址 *分配* 后，可以继续将 IP 地址空间指派给其客户，用于客户自己的内部基础设施。网络运营商获得 *指派* 的地址后，只能用于自己的内部基础设施。
> 我个人认为这两个术语之间的区别如今有些无关紧要且令人费解，因此从现在起，我将使用“分配”一词来统一代指分配和指派。

2023 年，IPv4 已分配地址池的总地址数有史以来第一次缩减，约减少了 40 万个地址，变为年底的 36.85 亿个。这意味着已分配的 IPv4 公共地址池总量缩减了约 0.01%（表 1）。

| |2010 |2011 |2012 |2013 |2014 |2015 |2016 |2017 |2018 |2019 |2020 |2021 |2022 |2023|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|地址段（亿万）|3.227 |3.395 |3.483 |3.537 |3.593 |3.624 |3.643 |3.657 |3.657 |3.682 |3.684 |3.685 |3.687 |3.686|
|年度同比变化（百万）|241.7 |168.0 |88.4 |53.9 |55.9 |30.6 |19.4 |13.2 |0.6 |24.9 |2.2 |1.1 |1.6 |-0.4|
|年度相对变化|8.1% |5.2% |2.6% |1.5% |1.6% |0.85% |0.53% |0.36% |0.02% |0.68% |0.06% |0.03% |0.04% |0.01% |

表 1 - 按年份分列的 IPv4 已分配地址数量

我们是否已用尽 IPv4 地址的所有可用来源？现有地址管理的模式是，未分配的地址由互联网号码分配机构 (IANA) 保存在一个单一的地址池中，地址块分配给区域互联网注册管理机构，后者再将地址分配给不同的终端实体，供其使用或进一步分配。但是，IANA 早在几年前就已经用完了最后一个可用地址池，目前[只拥有三个 /24 地址前缀](https://www.iana.org/assignments/ipv4-recovered-address-space/ipv4-recovered-address-space.xhtml)。由于将这个小地址池分成 5 个相等的 153.6 个地址块的方案不可行，这些地址很可能会在 IANA 的回收地址注册表中继续待上一段时间。

> 或者说，直到一个或多个区域互联网注册管理机构将更多曾经从旧“遗留”地址池中分配出的前缀归还给 IANA，那时 IANA 就可以将地址池平均分配给五个区域互联网注册管理机构。这种情况不太可能发生。

IANA 将一部分地址标记为了保留地址，包括用于组播的地址段。而在 IPv4 地址段注册表的最顶端，有一组地址被不恰当地标记为保留供未来使用。这是一个由 268,435,456 个地址组成的相对较大的地址池（以前的 "E 类 "空间），如果说 IPv4 还有 "未来 "的话，那么这个“未来”早就已经切切实实地成为过去了。但是，如何释放这些空间并将其归还给通用地址池，这个问题迄今为止还没有找到一个普遍可行的解决方案，尽管业界时不时会有人试图解决它。

> 在过去 15 年左右的时间里，关于将 E 类空间作为全局可路由单播地址空间在公共互联网中释放使用的话题不时被提出。有些互联网草案已经是发布供 IETF 审议的状态，其中有的直接建议释放该空间，有的概述了 2008 年制定这些草案时观察到的各种主机和路由器实现对这些提案的阻碍。
> 这些建议之所以被搁置，可能是因为当时考虑到解决这些问题的可用时间和资源有限，而且费力“调整”这些 IPv4 空间使之能被公开使用，只能略微延长剩余 IPv4 地址池的预计耗尽时间，而将同样的努力用于推进 IPv6 部署则会产生更大的效益。
> 这个话题时不时会在不同的邮件列表中再次出现，但往往会激发对同一组话题的辩论，然后就偃旗息鼓了。

由于 IANA 不再是地址的来源，因此我们只需要研究 RIR 的做法，从注册机构的角度了解地址的生命周期。当 IP 地址段根据 RIR 的政策返回或被回收时，通常会在 RIR 所有的地址池中放置一段时间，并标记为保留。将返回或回收的地址保留一段时间后再进行后续分配，能够给各种地址前缀声誉和其它服务（包括路由记录）一些时间，来记录这段前缀已经从之前的状态变为停止使用。经过几个月到几年不等的隔离期后，这些保留地址段会被释放以供重新使用。

表 2 显示了和表 1 相同的 13 年间，每个 RIR 的地址分配地址的年度同比变化。在某些年份，某些 RIR 的已分配地址池规模有所缩小,通常是由于地址在 RIR 之间的移动，有时是由于行政变动，有时是由于 RIR 自发进行地址转让。

| |2010 |2011 |2012 |2013 |2014 |2015 |2016 |2017 |2018 |2019 |2020 |2021 |2022 |2023|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|APNIC |119.5 |101.0 |0.6 |1.2 |4.6 |7.4 |6.7 |3.2 |0.4 |10.5 |1.7 |1.5 |0.8 |-1.1|
|RIPE NCC |52.3 |40.5 |37.8 |1.0 |33.8 |4.7 |4.1 |3.7 |0.3 |12.0 |0.4 |2.5 |4.7 |6.2|
|ARIN |27.2 |53.8 |24.3 |19.0 |-14.1 |2.3 |-4.8 |-2.3 |-0.3 |-10.1 |-0.9 |-1.7 |-3.8 |-5.5|
|LACNIC |17.1 |13.6 |17.3 |26.3 |18.7 |1.2 |1.5 |1.4 |0.1 |2.4 |1.2 |-0.2 |-0.3 |-0.1|
|AFRINIC  |8.8 |9.4 |8.5 |6.3 |12.8 |15.0 |11.9 |7.1 |0.2 |10.1 |-0.2 |-0.9 |0.2 |0.1|
|总数 |224.9 |218.3 |88.5 |53.8 |55.8 |30.6 |19.4 |13.1 |0.7 |24.9 |2.2 |1.2 |1.6 |-0.4|

表 2 - 已分配 IPv4 地址的年度变化（百万），按 RIR 区分

每个 RIR 都在使用它们最后的 IPv4 地址池了。到 2023 年底，所有 RIR 的可用地址池加起来约有 360 万个地址，主要由 APNIC（250 万）和 AFRINIC（120 万）持有。约有 1250 万个地址被标记为保留地址，其中 ARIN 拥有 520 万个地址，AFRINIC 拥有 400 万个地址。从表 3 中可以看出，ARIN 的保留池（98K）和 RIPE NCC 的保留池（26K）略有净减少，而 APNIC 的保留池增加了 68.7 万个地址，LACNIC 和 AFRINIC 的保留池有小幅增长。

| |可用地址数| | |保留地址数| | |
|---|---|---|---|---|---|---|
|RIR |2021 |2022 |2023 |2021 |2022 |2023|
|APNIC |3,533,056 |2,503,424 |2,469,120 |1,787,904 |1,514,752 |2,202,624|
|RIPE NCC |-   |- |1,024 |762,104 |737,496 |708,872|
|ARIN |4,608 |8,448 |8,960 |5,244,160 |5,311,488 |5,213,184|
|LACNIC |7,168 |1,024 |256 |224,768 |148,480 |151,296|
|AFRINIC |1,652,480 |1,403,136 |1,201,664 |4,065,024 |4,104,960 |4,186,112|
|总数 |5,197,312 |3,916,032 |3,681,024 |12,083,960 |11,817,176 |12,462,088 |

表 3 - 可用和保留的 IPv4 池大小，截至 2023 年 12 月 [^译注1]

[^译注1]: 译者注：原文为“2022 年”，应为笔误。

图 1 显示了按年份分列的 RIR IPv4 地址分配数量，但要准确比较各 RIR 的分配情况却很困难，因为各 RIR 之间存在一些微妙但重要的差异，特别是在 IPv4 地址转让的处理上。

就 ARIN 而言，受 ARIN 服务的两个实体之间的转让在概念上被视为两项不同的交易——一个将地址退还给 ARIN 注册机构，另一个对应 ARIN 进行新的分配，转让的日期记录为 RIR 的新分配的日期。其他 RIR 将地址转让看作更改已分配地址的指定持有者，在处理转让时，RIR 保留了这些地址的原始分配日期。当我们查看 RIR 公布的各个交易记录数据并按年份统计时，ARIN 的记录额外包含了当年处理的地址转让量，而其他 RIR 的记录只包括当年进行的分配。

为了提供整体视角，我们分析时必须要能区分 RIR 记录地址交易方式的差异。在本研究中，我们定义“分配”为注册记录中从“保留”或“可用”状态到“已分配”状态的转换。这是为了能区分出处理地址转让的各种操作，因为地址转让一般不涉及明显的状态变化，因为被转让的地址块在整个转让过程中仍处于“已分配”状态。分析 RIR 公布的数据，比较每年年底的地址池状态与该年年初的状态，就得到了 图 1 的数据。如果一段地址在年初未登记为“已分配”，年底却变为“已分配”，则可确定分配是在该年内发生。

{{< figure src="https://blog.apnic.net/wp-content/uploads/2024/01/addressing23-fig1.png" link="https://blog.apnic.net/wp-content/uploads/2024/01/addressing23-fig1.png" caption="图 1 - 各 RIR 的 IPv4 被分配地址总数（百万），按年份分列" >}}

图 2 显示了按年份分列的 RIR IPv4 分配次数，这些数据也是通过使用与图 1 相同的数据分析技术生成的。

{{< figure src="https://blog.apnic.net/wp-content/uploads/2024/01/addrfig2-1.png" link="https://blog.apnic.net/wp-content/uploads/2024/01/addrfig2-1.png" caption="图 2 - 各 RIR 的 IPv4 分配次数，按年份分列" >}}

从这两张图可以明显看出，近年来 IPv4 地址分配的平均规模已大幅缩减，与每个 RIR 的各种 IPv4 地址耗尽政策相呼应。

# IPv4 地址转让分析

近年来，RIR 允许登记地址持有者之间的 IPv4 地址转让，以在向 RIR 除退回闲置地址的方式之外，开放另一种地址的再分配方式。这是为了应对 IPv4 地址枯竭带来的各种问题，其根本动机是通过 IPv4 地址的市场激励，促进对原本闲置或低效使用的地址块的再利用，并确保这种转让在注册系统中有公开记录。

表 4 列出了过去十一年中登记的转让数量。数量既包括 RIR 间的转让，也包括 RIR 内的转让。它还包括基于合并和收购以及以其他理由进行的地址转让。每次转让都被视为一次单独交易，如果是 RIR 之间的转让，则计入接收 RIR 的转让总数。

|接收 RIR |2012 |2013 |2014 |2015 |2016 |2017 |2018 |2019 |2020 |2021 |2022 |2023|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|APNIC |158 |180 |307 |451 |840 |845 |491 |533 |820 |785 |745 |796|
|RIPE NCC |10 |171 |1,054 |2,836 |2,373 |2,451 |3,775 |4,221 |4,696 |5,742 |4,640 |4,937|
|ARIN |  |  |  |3 |22 |26 |26 |68 |94 |150 |141 |97|
|LACNIC |  |  |  |  |  |  |2 |  |3 |9 |17 |20|
|AFRINIC |  |  |  |  |  |  |17 |27 |26 |80 |58 |14|
|总数 |168 |351 |1,361 |3,290 |3,235 |3,322 |4,311 |4,849 |5,639 |6,766 |5,601 |5,864 |

表 4 - 每年的 IPv4 地址转让次数

不同 RIR 报告的数字之间的差异很有意思。在 AFRINIC 和 LACNIC 服务区域，地址持有者似乎并没有明显接纳与地址转让的相关政策，而在 RIPE NCC 服务区域，采用这些政策的热情似乎很高！

从每年转让的地址数量来看，情况略有不同（表 5）。

|接收 RIR |2012 |2013 |2014 |2015 |2016 |2017 |2018 |2019 |2020 |2021 |2022 |2023|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|APNIC |        1.6 |    2.3 |4.1 |      6.6 |      8.2 |      4.9 |      10.0 |        4.3 |      16.6 |        6.5 |        3.7 |2.7|
|RIPE NCC |        0.1 |    2.0 |      9.6 |    11.6 |      9.2 |    24.6 |      19.5 |      26.9 |      18.2 |      16.2 |      36.9 |20.8|
|ARIN ||||      0.1 |      0.3 |      0.2 ||        0.3 |        0.2 |        0.2 |        3.1 |1.6|
|LACNIC |||||||||||||
|AFRINIC |||||||        0.2 |        0.5 |        1.2 |        3.4 |        0.5 |0.1|
|总数 |        1.7 |    4.3 |    13.7 |    18.2 |    17.6 |    29.7 |      29.7 |      31.9 |      36.2 |      26.4 |      44.3 |25.3 |

表 5 - 每年转让的 IPv4 地址数量（百万）。

图 3 和图 4 显示了这些数字的分布情况。

{{< figure src="https://blog.apnic.net/wp-content/uploads/2024/01/addressing23-fig3.png" link="https://blog.apnic.net/wp-content/uploads/2024/01/addressing23-fig3.png" caption="图 3 - IPv4 地址转让次数，2012-2023" >}}

{{< figure src="https://blog.apnic.net/wp-content/uploads/2024/01/addressing23-fig4.png" link="https://blog.apnic.net/wp-content/uploads/2024/01/addressing23-fig4.png" caption="图 4 - IPv4 地址转让数量，2012-2023" >}}

地址转让量在 2022 年达到峰值，2023 年有所下降。就 APNIC 而言，峰值出现在 2020 年，而 APNIC 2023 年的传输量与 2012 年的传输量相当。如果地址转让的目的是地址分配后的再分配，那么 2023 年内，对这一功能的需求似乎正在减弱。

# 地址转让真的在回收闲置地址吗？

这些数据提出了一些有关转让性质的问题。第一个问题是，地址转让是否有效地打捞了已分配但未公开的公共 IPv4 地址段，并将这些地址重新投入使用。

人们认为，如果能够从这些闲置地址的转让中牟利，就可能促使它们的持有者将自己的网络转而使用私有地址，再并转售它们持有这些的公共地址。换句话说，地址市场的开放将促使原本无收益的地址资产进入市场。有地址需求的网络供应商将与其他有类似需求的供应商竞争，竞价购买这些地址。按照传统的市场理论，最有效率（指使用地址产生最大收益的能力）的地址用户将能够确定市场价格。反之，那这些闲置的地址就会投入生产使用。只要供不应求，市场行为就会促进地址的最有效利用。至少理论如此。

地址转让的实际过程就不像理论分析那样明晰了。与地址回收有关的数据并不确定，2011 年至 2017 年末，未宣告（已分配但没有公布到互联网路由表）的地址量在 38 至 40 个 /8 之间。从 2018 年开始，这个未公开的地址库有所上升，到 2020 年初，在公共互联网上未公开的 /8 地址略低于 50 个。未公开地址池这为期两年的增长应该对应 IPv4 地址的囤积时期。不过，仅从这个顶层聚类得到的日期就得出这样的结论，有很多推测的成分，结论很可能不合理。

2021 年初，这个未公开的地址池规模大幅缩减。2021 年的主要变化是互联网路由系统把 ARPANET 早期分配给美国国防部的地址空间中的约 7 个 /8 重新宣告了出来。到 2021 年底，AS749 宣告出的 IPv4 地址比其他任何网络都多，达到 211,581,184 个，相当于 /4.34 的前缀长度，占 IPv4 地址池总数的 5%。

在 2022 年和 2023 年期间，未宣告地址段的数量恢复了之前的上升趋势。

{{< figure src="https://blog.apnic.net/wp-content/uploads/2024/01/addressing23-fig5.png" link="https://blog.apnic.net/wp-content/uploads/2024/01/addressing23-fig5.png" caption="图 5 - IPv4 未宣告的地址数量" >}}

图 6a 显示了 2000 年以来三种 IPv4 地址池，已分配、已宣告和未宣告地址池的总体变化。收紧的地址政策开始实施的时间能与 2011 年初 IANA 中央未分配地址池耗尽对应上。

{{< figure src="https://blog.apnic.net/wp-content/uploads/2024/01/addressing23-fig6a.png" link="https://blog.apnic.net/wp-content/uploads/2024/01/addressing23-fig6a.png" caption="图 6a - IPv4 地址池大小，2000-2024" >}}

我们还可以看看 2023 年，这些地址池自年初以来的变化情况，如图 6b 所示。已宣告地址的总数在这一年中减少了约 2200 万个地址。RIR 的记录也显示了全年净减少 23.6 万个已分配地址。全年未宣告地址库增加了 2100 万个地址。

{{< figure src="https://blog.apnic.net/wp-content/uploads/2024/01/addressing23-fig6b.png" link="https://blog.apnic.net/wp-content/uploads/2024/01/addressing23-fig6b.png" caption="图 6b - IPv4 地址池大小在 2023 年内的变化" >}}

从相对值的角度，表示为在整体已分配 IP 地址池中的占比，未宣告的地址数量从 2011 年占已分配地址池总量的 25% 降至 2016 年初的 22%，随后在 2020 年底升至 24%。2021 年，这一数字下降到 16%，主要原因是美国国防部遗留地址空间的宣告，而不是激活了其它从前未宣告的地址空间。由此可以得出结论，在过去 12 个月中，地址转让活动并未对地址利用效率的总体情况产生任何积极的净变化（图 7）。

{{< figure src="https://blog.apnic.net/wp-content/uploads/2024/01/addressing23-fig7.png" link="https://blog.apnic.net/wp-content/uploads/2024/01/addressing23-fig7.png" caption="图 7 - 未宣告地址在整体已分配地址池中的占比" >}}

该数据还显示出，转让市场有些疲软。大多数 RIR 的地址转让交易数量都在上升，但除 RIPE NCC（表 4 和表 5）地区外，地址转让总量却在下降。地址市场似乎未能有效地带出闲置地址并将它们重新部署到路由网络中。

不过，与所有其他商品市场一样，商品的市场价格反映了供需平衡以及对未来供需的预期。从过去八年的 IPv4 地址交易价格中又可以看出什么呢？

地址中间商之一 Hilco Streambank 公布了交易的历史价格信息（如果所有中间商都这样做就好了，因为交易价格信息公开的市场比价格信息闭塞的市场运行得更有效、更公平）。图 8 使用 Hilco Streambank 交易数据生成了地址价格的时序图。

这些数据显示了几种截然不同的行为模式。2016 年之前的初始数据显示当时的交易量相对较低且价格稳定，略低于每个地址 10 美元。在随后的四年里，直到 2019 年初，价格翻了一番，其中小地址段（/24 和/23）吸引了最高溢价。在接下来的 18 个月里，价格稳定在每个地址 20 美元到 25 美元之间，大地址段和小地址段的交易单价相近。

到 2022 年开始的 18 个月内，价格呈指数上升，出现了新的动态，到 2021 年底，价格上升到每个地址 45 美元到 60 美元之间。2022 年，全年平均市场价格下降，但价格差异增大，年底的交易价格在每个地址 40 美元至 60 美元之间。这种价格下降的趋势持续到 2023 年，到 2023 年底，IPv4 地址的交易单价在 30 美元到 40 美元之间。两个地址的价值没有任何区别，对于这样一个无差别的商品市场来说，这种 30% 的价格变化超乎意料，有些不寻常。

如果价格能反映供求关系，那么需求的增幅似乎远远大于供应，2021 年的价格上涨反映了近来对地址稀缺造成的溢价（图 8）。

{{< figure src="https://blog.apnic.net/wp-content/uploads/2024/01/addressing23-fig8.png" link="https://blog.apnic.net/wp-content/uploads/2024/01/addressing23-fig8.png" caption="图 8 - IPv4 地址价格时序（数据来自 Hilco Streambank）" >}}

可交易 IPv4 地址的供应量是否在下降？要回答这个问题，可以通过观察已转让地址的注册年限来了解一些情况。这些地址主要是最近分配的地址，还是持有时间较长的地址，持有者希望实现未使用资产的内在价值？最根本的问题与转让地址的年龄分布有关，这个年龄对应了地址首次由 RIR 系统分配或指派之后的时间。

图 9 和图 10 逐年显示了转让地址的累积年龄分布。如图 9 （每个地址单独计数）所示，在 2023 年的所有转让地址中，约 15% 来自遗留地址的持有者。由此看来，回收遗留地址库的努力已接近尾声，转让的遗留地址数量已急剧下降。

在 2019 年至 2021 年期间，有一部分地址持有者在获取最近分配的地址之后，似乎会先按政策要求在两年的最短期限内保留这些地址，然后就在市场上转让。前几年，有 8% 的被转让地址是在转让前五年内分配的。2022 年，这一数字下降到 4%，这可能是因为 2022 年地址分配数量较少，地址持有者的行为模式应该没有变化。到了 2023 年，这一现象几乎消失，原因是 RIR 分配的地址数量非常之少，同样也不是因为地址持有者的行为模式有所改变。

{{< figure src="https://blog.apnic.net/wp-content/uploads/2024/01/addressing23-fig9.png" link="https://blog.apnic.net/wp-content/uploads/2024/01/addressing23-fig9.png" caption="图 9 - 转让地址的年龄分布（按地址数目）" >}}

图 10 显示了转让交易的累积年限分布（每笔转让单独计数）。2023 年上面两个分布之间的差异表明，最近的单笔地址分配规模要小得多，但仍在进行买卖。2023 年记录的转让交易笔数中有 20% 是过去五年内分配的地址前缀，但这些交易的地址数目只占 2023 年转让地址总量的不到 2%。同年记录中，转让地址数量的约 30% 是在 20 年或更早之前分配的，但对应的交易笔数仅占 12%。[^译注2]

[^译注2]: 译者注：整段中的“2023 年”，在原文中均为“2022 年”，应为笔误。

{{< figure src="https://blog.apnic.net/wp-content/uploads/2024/01/addressing23-fig10.png" link="https://blog.apnic.net/wp-content/uploads/2024/01/addressing23-fig10.png" caption="图 10 - 转让地址的年龄分布（按交易笔数）" >}}

地址转让过程的驱动力有如下几个。其一是供不应求，不可避免地导致价格上涨。这会促使一些网络运营商提前购买地址，因为它们会预测到再晚买入会遇到更高价格。这个因素还可能促使一些地址持有者继续等待，等到价格上涨之后再出售地址。综合来看，这些动机可能会损害市场流动性，并形成一个导致价格进一步上涨的正反馈循环。2021 年的情况似乎就是如此。

第二个驱动力是 IPv6 的部署。在条件允许的情况下，许多应用程序倾向使用 IPv6 而不是 IPv4（即所谓的协议选择协议“Happy Eyeballs”）。对于接入双协议栈的网络来说，双协议栈提供的服务越多，IPv4 的流量就越少。这就减少了 IPv4 CG-NAT 的地址消耗压力，降低了对 IPv4 地址空间的持续需求。对 IPv4 地址的进一步需求减少后，市场价格会收到影响。市场价格下降会促使卖方尽快将其闲置地址库存推向市场，因为进一步拖延只会让它们卖得更低。

地址市场的最大特点是 IPv6 过渡状况的不确定性，以及网络进一步发展的不确定性。这种高度不确定性可能导致了图 8 中转让交易之间价格的巨大差异。

不过，这种不确定性在 2023 年得到了一定程度缓解，在过去 12 个月中需求水平似乎已经下降了。是不是我们终于成功部署了足够多的双栈网络基础设施，跑赢了需求压力？也许我们终于，可能是有史以来第一次，看到市场中的地址数量和相关服务平台设施达到饱和。

# 地址转让会导致地址空间的碎片化吗？

下一个问题是，转让过程是否会将较大的地址块分割成连续较小的地址块，从而进一步分裂地址空间。从 2012 年初到 2024 年初，RIR 转让登记记录了 44,757 项交易。其中，11,184 笔交易包含了比原始分配区块更小的已转让地址区块。换句话说，约 25% 的转让隐含了对已分配地址段的碎片化。

这 11,184 笔分割了已分配地址段的转让交易对应 7014 比原始地址分配。平均意义上，每个原始分配的地址被分成了两个较小的地址块。通过这些数据回答上面的问题，地址转让过程确实加剧了碎片化，但从整体角度看这并不是大问题。截至 2023 年底，RIR 注册表中有 240,220 笔 IPv4 地址分配记录，这 11,184 笔交易虽然将原始分配地址块切分得更细，但只占已分配地址前缀总数的 4.7%。

# 地址的进出口

下一个议题是转让地址的国际流动。让我们来看看发起转让地址数量最多的十个经济体（表 6），不论目的地（包括同一经济体内部的“国内 ”转让），然后再看看接收转让地址数量最多的十个经济体（表 7），以及转让量最大的二十笔国际交易（表 8）。这些表格是从 RIR 在 2023 年发布的地址转让记录中总结出的。

| 排名 |国家代号 |发起转让地址数量 |经济体名|
|---|---|---|---|
|1 |US |7,942,912 |美国        |
|2 |GB |2,858,240 |英国         |
|3 |NL |1,927,680 |荷兰|
|4 |JP |1,495,296 |日本      |
|5 |GR |1,032,192 |希腊     |
|6 |RU |904,704 |俄罗斯       |
|7 |DE |821,504 |德国      |
|8 |IT |727,808 |意大利        |
|9 |SE |626,432 |瑞典       |
|10 |BE |528,384 |比利时     |

表 6 - 2023 年发起最多地址转让的前十个经济体

| 排名 |国家代号 |接收转让地址数量 |经济体名|
|---|---|---|---|
|1 |GB |8,518,400 |英国|
|2 |US |3,424,000 |美国|
|3 |NL |1,830,400 |荷兰|
|4 |GR |1,044,224 |希腊|
|5 |JP |938,496 |日本|
|6 |DE |880,640 |德国|
|7 |RU |697,088 |俄罗斯|
|8 |SE |685,056 |瑞典|
|9 |SG |558,336 |新加坡|
|10 |BE |540,928 |比利时|

表 7 - 2023 年 [^译注4] 发起最多地址转让的前十个经济体

[^译注4]: 译者注：原文为“2021 年”，应为笔误。

一些 RIR 记录地址转让的国家代号的原则是，使用地址持有者实体总部的实际位置，而不是地址在互联网上的实际使用地。另一些 RIR 允许持有者更新转让记录的地理位置，改为此地址的预期使用地点。一般情况下我们无法确信持有人对使用地点的声明，因此我们没法确知这些自发的记录能反映地址的实际使用地点，还是只是它们为了方便而填入的地址。

当我们研究各种地理定位服务时，比如其中常用的 Maxmind，也会遇到类似的定位挑战。这些服务一般都是为了定位地址的物理位置。有时这并不容易确定，例如 VPN 中的隧道。“正确”的位置是隧道入口的位置还是隧道出口的位置？地理定位服务的许多细微差别，就是源于 VPN 的挑战以及定位服务的应对方法。此外还有云服务带来的问题。

云服务使用任播时，它的 IP 地址会同时处于多个位置。即便云服务使用传统单播，它所使用的地址也可能随着云服务按需调整各地的地址数目，而在它的接入点间流动。总之，这些位置信息只是一个“模糊”的近似值，而不是精确的定位。

考虑了这些后，我们在来看看 2023 年，来源地和目的地不同的地址转让进出口情况。

| |来源 |目的 |转让地址数量（百万） |来源经济体名 | 目的经济体名|
|---|---|---|---|---|---|
|1 |US |GB |5,389,568 |美国 |英国|
|2 |IT |US |344,064 |意大利 |美国|
|3 |JP |GB |329,728 |日本 |英国|
|4 |GB |US |238,336 |英国 |美国|
|5 |DE |GB |141,568 |德国 |英国|
|6 |CA |GB |136,192 |加拿大 |英国|
|7 |GB |SE |131,328 |英国 |瑞典|
|8 |FR |SE |131,072 |法国 |瑞典|
|9 |IR |DE |131,072 |伊朗 |德国|
|10 |SE |US |131,072 |瑞典 |美国|
|11 |AU |US |110,848 |澳大利亚 |美国|
|12 |JP |PH |106,496 |日本 |菲律宾|
|13 |US |DE |105,728 |美国 |德国|
|14 |DE |FR |99,584 |德国 |法国|
|15 |JP |SG |98,304 |日本 |新加坡|
|16 |NL |US |98,048 |荷兰 |美国|
|17 |GB |ES |77,824 |英国 |西班牙|
|18 |CA |US |74,752 |加拿大 |美国|
|19 |GB |DE |74,496 |英国 |德国|
|20 |UA |US |70,400 |乌克兰 |美国 |

表 8 - 2023 年地址数量最多的前二十笔跨经济体转让

2023 年的转移记录包含了 3,674 次国内地址转移，共涉及 14,314,400 个地址，按地址量计算，英国、美国、荷兰、希腊和日本的国内转移活动最多。有 2,190 次转移似乎导致了地址在不同经济体之间的流动，共涉及 11,001,600 个地址。

关于这些转让数据，一个悬而未决的问题是，是否所有地址转让都已正式记录在登记系统中。之所以提出这个问题，是因为转让登记需要遵守各种登记政策，导致可能只有一部分转让被记录在登记处中。要检测这种情况可能有些困难，特别是如果这种转让是租赁或其他临时形式，加上当事各方可能同意对转让细节保密。

通过观察互联网的路由系统，或许可以给出任意时间段内地址转让量的上限。要进一步了解地址转让量的上限是多少，一种方法是对路由系统进行简单的检查，通过比较 2023 年年初和年末的路由稳定状态，查看 2023 年宣告的地址数量（表 9）。

||2023年1月 |2024年1月 |增量|无变动|重新归属|移除|新增|
|---|---|---|---|---|---|---|---|
|宣告数 |941,707 |944,714 |3,007 |810,902 |25,154 |105,561 |108,658|
|地址段数 (/8) |249.25 |246.94 |-2.32 |232.95 |4.31 |11.99 |9.68|
||
|顶层前缀数 |444,678 |456,574 |11,896 |396,935 |17,375 |32,054 |42,237|
|地址段数 (/8s) |182.81 |181.51 |-1.30 |174.00 |3.35 |5.99 |4.16|
||
|细分前缀数 |497,029 |488,167 |-8,862 |413,967 |7,779 |73,597 |66,421|
|地址段数 (/8s) |50.69 |50.48 |-0.21 |58.95 |0.96 |6.01 |5.52|

表 9 - 2023 年 [^译注3] IPv4 BGP 变化

[^译注3]: 译者注：原文为“2022 年”，应为笔误。

虽然路由表在这一年中净增加了 3,007 个条目，但变化涵盖了不少细节。年初宣告的前缀中，有 105,561 个在年内从路由系统中删除了，而年底宣告前缀中，有 108,658 个在年初时不存在。当然，还有更多短命的前缀可能在全年中增加和撤销（见下段），但这里我们比较的是两个快照，而不是每一条更新信息。还有 25,154 个前缀改变了发布它的自治系统编号 (ASN），这表明该前缀的网络位置以某种方式发生了变化。

如果我们在某个 BGP 节点（AS131072），查看 2023 年全年看到的 BGP 更新的完整集合，我们会看到很多短命的地址前缀。2023 年共能观察到 1,161,367 个不同的前缀，这意味着和年初的初始前缀集相比，在这一年内的不同时间点，又出现了约 219,660 个额外的前缀。

我们可以将这些在 2023 年发生变化的前缀与 2022 和 2023 这两年间的 BGP 变动记录进行比较。表 10 显示了这些路由表项数量与这两年间记录的 BGP 变动条目数量的比较。

|变动类型 |2023 年发生变化的前缀对应的 BGP 变动 |其它前缀对应的 BGP 变动|占比|
|---|---|---|---|
|重新归属 |
|   全部前缀数|2,562 |22,592 |10.2%|
|   顶层前缀数|2,291 |14,690 |13.5%|
||
|移除 ||
|   全部前缀数|4,556 |101,095 |4.3%|
|   顶层前缀数|2,791 |29,263 |8.7%|
||
|新增 ||
|   全部前缀数|5,390 |103,268 |5.0%|
|   顶层前缀数|3,840 |38,397 |9.1% |

表 10 - 2023 年 IPv4 路由表项变化数与 2022-2023 之间 BGP 变动条目数量的比较

这些数字表明，从年初到年末，4% 到 13% 的宣告地址数量对应了 RIR 记录的地址转让。我们不能说，其余的前缀宣告对应了未记录的地址转让。造成地址前缀宣告变化的原因有很多，地址管理者的变更只是其中潜在的一个。不过，这确实为 2023 年 [^译注5] 的地址变动数量设定了一个概念上的上限，其中有些变动与未记录的地址转让有关。

[^译注5]: 译者注：原文为“2022 年”，应为笔误。

现在，我们终于可以对 2023 年期间新增、移除和重新归属的地址进行年龄剖析，并将其与路由表中 IPv4 地址的整体年龄剖析进行比较，如图 11 所示。就 2023 年新增的地址而言，由于人们偏向于“较老”的地址，它们与平均年龄分布图有所不同，所有宣告的地址中有 40% 是在 25 年前分配或指派的。

{{< figure src="https://blog.apnic.net/wp-content/uploads/2024/01/addressing23-fig11-1320x912.png" link="https://blog.apnic.net/wp-content/uploads/2024/01/addressing23-fig11-1320x912.png" caption="图 11 - 不同 BGP 路由表项变动类型对应的地址年龄分布" >}}

此外，随着 IPv4 进入最后阶段，我们现在或许可以对 IPv4 地址的总体分布情况进行评估，并看看这些地址的去向。表 11 显示了分配 IPv4 地址最多的十个经济体。不过，我必须指出，地址注册表中国家代号的指配反映的是地址持有者所在的经济体（公司所在地），而不一定是地址所部署到的经济体。

|排名 |国家代号 |IPv4 地址池大小 |总体占比|人均地址数 |经济体|
|---|---|---|---|---|---|
|1 |US |1,613,416,288 |43.80% |4.73 |美国|
|2 |CN |343,128,576 |9.30% |0.24 |中国|
|4 |GB |125,666,696 |3.40% |1.85 |英国|
|5 |DE |124,023,296 |3.40% |1.49 |德国|
|6 |KR |112,502,528 |3.10% |2.17 |韩国|
|7 |BR |87,131,648 |2.40% |0.4 |巴西|
|8 |FR |82,154,096 |2.20% |1.27 |法国|
|9 |CA |68,649,984 |1.90% |1.76 |加拿大|
|10 |IT |53,993,792 |1.50% |0.92 |意大利|
|总数 |XA |3,686,113,784 |100.00% |0.46 |全球|

表 11 - 各国家经济体 IPv4 分配地址池大小

如果我们将地址池除以每个国家的现有人口数，就可以得出人均地址排名。全球已分配地址总数为 36.9 亿，而全球人口估计为 80 亿，因此人均 IPv4 地址数量为 0.46。

|排名 |国家代号 |IPv4 地址池大小 |总体占比|人均地址数 |经济体|
|---|---|---|---|---|---|
|1 |SC |7,284,480 |0.20% |67.46 |塞舌尔|
|2 |VA |10,752 |0.00% |20.6 |教廷|
|3 |GI |239,104 |0.00% |7.31 |直布罗陀|
|4 |US |1,613,416,288 |43.80% |4.73 |美国|
|5 |SG |26,087,936 |0.70% |4.32 |新加坡|
|6 |MU |4,779,008 |0.10% |3.67 |毛里求斯|
|7 |CH |25,955,896 |0.70% |2.94 |瑞士|
|8 |VG |92,160 |0.00% |2.91 |英属维尔京群岛|
|9 |NO |15,537,680 |0.40% |2.83 |挪威|
|10 |NL |49,889,568 |1.40% |2.83 |荷兰|
|总数 |XA |3,686,113,784 |100.00% |0.46 |全球|

表 12 - 各国家经济体 IPv4 分配地址池大小，按人均地址数排名


[这里](https://resources.potaroo.net/iso3166/v4cc.html)可以查看每个国家经济体 IPv4 分配情况的完整表格。

# IPv4 地址租赁情况

值得注意的是，地址市场还包括租赁和销售。如果一个实体需要使用 IPv4 地址，它进入市场后，是应该从现有地址持有者那里直接购买地址，还是应该有限期地租赁，只在一定期限内使用这些地址，期满归还？租赁还是购买的问题在市场经济学中是一个非常传统的问题，有各种现成的答案，一般取决于市场信息和具体情景分析。

如果买方认为导致当下市场状况的因素还会持续很长时间，而且市场上交易的商品供应有限，对这些商品的需求水平却在不断提高，那么市场就会在交易商品的价格上增加一个不断攀升的稀缺性溢价。供求关系的平衡就成了交易商品稀缺性溢价的函数。随着时间的推移，供不应求的商品往往会变得更加昂贵。商品的持有者能享受到所持商品的升值，而承租人则不能。

如果买方认为市场只有很短的生命周期，而且对商品的需求会在生命周期结束时迅速消散，那么租赁商品就是合理的，因为当市场崩溃时，承租人不会只剩下无价值的资产。

稀缺性还有其它额外的影响，比如替代品的定价。当原有商品的价格涨到一定地步，替代品就会具有经济吸引力，哪怕替代品的生产或使用成本更高。事实是，替代品的价格本质上为原来的稀缺商品设定了一个价格上限。

一些评论认为，IPv4 价格上涨会刺激 IPv6 的经济驱动力，事实也许确实如此。不过，也有人使用了其他可能的替代品，其中最著名的是 NAT。虽然 NAT 并不能消除 IPv4 的需求压力，但它们可以大大提高 IPv4 地址的利用效率。NAT 允许多个客户端在不同时间使用同一个地址。共享 NAT 地址池的客户数量越多，可实现的复用能力就越强。

要估计 IPv4 地址市场还能将持续多久，实际上就是判断 IPv4 和 NAT 还能持续多久，以及 IPv6 需要多长时间才能得到充分部署，使纯 IPv6 服务具有可行性。那时很可能会出现一个临界点，所有主机和网络都不再有任何要支持通过 IPv4 访问它们服务的压力。到那时，纯 IPv6 的先行者可以将它们所有剩余的 IPv4 资源抛向市场，因为他们不再需要这些资源，很可能会引发一定程度的市场恐慌，因为现有的持有者面临着资产变得毫无价值的前景，被迫需要在市场上仍有买家时出售其 IPv4 资产。

虽然先存的大量纯 IPv4 主机和网络会阻碍这一过渡，并增加稀缺性压力，但如果稀缺压力过大，采用纯 IPv6 的动力就会增加，导致 IPv6 基础设施达到支配市场的程度。一旦达到这一条件，IPv4 地址市场将迅速崩溃。

# 2023 年 IPv6 地址数量分析

IPv4 地址分配显然只是故事的一半，要想完整的图景，就必须要看 IPv6 在 2023 年 [^译注6] 的表现。

[^译注6]: 译者注：原文为“2022 年”，应为笔误。

IPv6 使用的地址分配模式与 IPv4 有些不同，服务提供商可自行决定为每个客户分配多大的 IPv6 地址前缀。最初，互联网架构委员会（IAB）和互联网工程指导小组（IESG）于 2001 年在 RFC 3177 中发布的建议预想到，未来我们需要普遍使用 /48 前缀作为适用于一般终端站点的前缀。在后续对长期地址保存的考虑中，人们采用了更为灵活的方法，由服务提供商选择终端站点的前缀长度。

在当今的 IPv6 环境中，一些提供商以 /60 为单位分配地址给终端站点，另一些提供商使用 /56，还有许多提供商使用 /48。这种差异容易误导我们对已分配 IPv6 地址数量的比较，因为为了容纳相同规模的客户群，与使用 /56 前缀的提供商相比，使用 /48 作为终端站点的互联网服务提供商（ISP）需要 256 倍的地址空间，而使用 /60 的互联网服务提供商需要 4096 倍的地址空间！

因此对于 IPv6，让我们同时使用 IPv6 分配次数和分配的空间总量，看看 IPv6 在 2023 年的表现如何。

与 2022 年相比，2023 年IPv6 地址空间的分配次数下降了 5%，而 IPv4 分配次数下降了 21%（表 13）。

|分配次数 |2011 |2012 |2013 |2014 |2015 |2016 |2017 |2018 |2019 |2020 |2021 |2022 |2023|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|IPv6 |3,582 |3,291 |3,529 |4,502 |4,644 |5,567 |5,740 |6,176 |6,799 |5,376 |5,350 |4,066 |3,874|
|IPv4 |8,234 |7,435 |6,429 |10,435 |11,352 |9,648 |8,185 |8,769 |12,560 |5,874 |6,939 |4,395 |3,462 |

表 13 - 2011-2023 地址分配次数比较

2023 年分配的 IPv6 地址空间比 2022 年增长了 170%[^译注7]，而相应的 IPv4 地址空间则减少了 24%（表 14）。

[^译注7]: 译者注：原文此处数据对应的是 2022 年相对 2021 年的变化，应为笔误，已经修正为 2023 年相对 2022 年的变化。

|分配地址数 |2011 |2012 |2013 |2014 |2015 |2016 |2017 |2018 |2019 |2020 |2021 |2022 |2023|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|IPv6 （/32）|14,986 |17,710 |23,642 |17,847 |15,765 |25,260 |19,975 |38,699 |35,924 |21,620 |28,131 |27,497 |74,159|
|IPv4 （/32，百万）|191.7 |88.8 |57.7 |58.8 |32.3 |20.8 |15.1 |14.1 |13.9 |4.2 |3.1 |2.1 |1.6 |

表 14 - 2011-2023 地址分配地址数比较

按地区来看，每个 RIR 在 2023 年的 IPv6 分配活动与 2022 年相当，但远低于 2018 年至 2019 年的 IPv6 分配活动高峰期（表 15）。

|分配次数 |2011 |2012 |2013 |2014 |2015 |2016 |2017 |2018 |2019 |2020 |2021 |2022 |2023|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Allocations |2011 |2012 |2013 |2014 |2015 |2016 |2017 |2018 |2019 |2020 |2021 |2022 |2023|
|AFRINIC |129 |82 |72 |59 |81 |111 |110 |108 |111 |108 |135 |151 |115|
|APNIC |641 |599 |540 |528 |777 |1,680 |1,369 |1,460 |1,484 |1,498 |1,392 |1,317 |1,381|
|ARIN |1,035 |603 |543 |489 |604 |645 |684 |648 |601 |644 |668 |680 |712|
|LACNIC |130 |251 |223 |1,199 |1,053 |1,007 |1,547 |1,439 |1,614 |1,801 |725 |635 |612|
|RIPENCC |1,647 |1,756 |2,151 |2,227 |2,129 |2,124 |2,030 |2,521 |2,989 |1,325 |2,430 |1,283 |1,054|
|Total |3,582 |3,291 |3,529 |4,502 |4,644 |5,567 |5,740 |6,176 |6,799 |5,376 |5,350 |4,066 |3,874|

表 15 - 各 RIR 的地址分配次数

地址分配数则略有不同。表 16 显示了每年分配的 IPv6 /32 数量。2023 年，APNIC 分配的 IPv6 地址数量明显低于 2022 年，LACNIC 和 RIPE NCC 地区的分配数量也略低于 2022 年。ARIN 向 Capital One Financial Cooperation 分配了一个 /16 地址块，Capital One Financial Cooperation 是美国大银行之一，在零售领域拥有大量信用卡用户。

|分配地址数（/32）|2011 |2012 |2013 |2014 |2015 |2016 |2017 |2018 |2019 |2020 |2021 |2022 |2023|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|AFRINIC |155 |4,201 |66 |48 |308 |76 |112 |71 |360 |88 |141 |387 |400|
|APNIC |9,506 |3,807 |4,462 |2,663 |2,108 |1,235 |4,228 |19,681 |7,945 |7,365 |10,185 |4,856 |599|
|ARIN |2,280 |1,672 |12,571 |5,214 |642 |1,087 |1,372 |844 |5,520 |4,975 |373 |13,695 |66,340|
|LACNIC |620 |4,301 |158 |1,314 |953 |1,173 |1,427 |1,327 |1,496 |1,669 |658 |563 |467|
|RIPENCC |2,425 |3,729 |6,385 |8,608 |11,754 |21,689 |12,836 |16,776 |20,603 |7,523 |16,774 |7,996 |6,353|
|Total |14,986 |17,710 |23,642 |17,847 |15,765 |25,260 |19,975 |38,699 |35,924 |21,620 |28,131 |27,497 |74,159 |

表 16 - 各 RIR 的地址分配数量

将地址除以分配次数，就得出了各地区的平均 IPv6 分配规模（表 17）。总体而言，平均 IPv6 分配规模为 /28，RIPE NCC 和 ARIN 的平均分配规模大于其他 RIR。

||2011 |2012 |2013 |2014 |2015 |2016 |2017 |2018 |2019 |2020 |2021 |2022 |2023|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|AFRINIC |/31.7 |/26.3 |/32.1 |/32.3 |/30.1 |/32.5 |/32.0 |/32.6 |/30.3 |/32.3 |/31.9 |/30.6 |/30.2|
|APNIC |/28.1 |/29.3 |/29.0 |/29.7 |/30.6 |/32.4 |/30.4 |/28.2 |/29.6 |/29.7 |/29.1 |/30.1 |/33.2|
|ARIN |/30.9 |/30.5 |/27.5 |/28.6 |/31.9 |/31.2 |/31.0 |/31.6 |/28.8 |/29.1 |/32.8 |/27.7 |/25.5|
|LACNIC |/29.7 |/27.9 |/32.5 |/31.9 |/32.1 |/31.8 |/32.1 |/32.1 |/32.1 |/32.1 |/32.1 |/32.2 |/32.4|
|RIPENCC |/31.4 |/30.9 |/30.4 |/30.0 |/29.5 |/28.6 |/29.3 |/29.3 |/29.2 |/29.5 |/29.2 |/29.4 |/29.4|
|Average |/29.9 |/29.6 |/29.3 |/30.0 |/30.2 |/29.8 |/30.2 |/29.4 |/29.6 |/30.0 |/29.6 |/29.2 |/27.7 |

表 17 - 各 RIR 的单次平均地址分配数量

图 12 和图 13 显示了每个区域互联网注册管理机构每年 IPv6 分配的次数和地址量。

{{< figure src="https://blog.apnic.net/wp-content/uploads/2024/01/addressing23-fig12.png" link="https://blog.apnic.net/wp-content/uploads/2024/01/addressing23-fig12.png" caption="图 12 - 每年 IPv6 地址分配次数" >}}

{{< figure src="https://blog.apnic.net/wp-content/uploads/2024/01/addressing23-fig13.png" link="https://blog.apnic.net/wp-content/uploads/2024/01/addressing23-fig13.png" caption="图 13 - 每年 IPv6 地址分配数量" >}}

或许我们可以将 RIPE NCC 2020 年 IPv6 分配量的下降归因于当年许多欧洲经济体受 COVID-19 措施的严重打击。与之相反的观点是，世界各地的经济体都受到了类似的影响，但 2020 年 IPv6 分配活动的下降却只出现在 RIPE NCC 的数据中。不过，为什么欧洲经济体的 IPv6 地址分配活动会下滑（表 18 和表 19），确实是一个有趣的问题。

|Rank |2019 |2020 |2021 |2022 |2023|
|---|---|---|---|---|---|
|1 |巴西 |1,112 |巴西 |1,394 |美国 |619 |美国 |638 |美国 |691|
|2 |美国 |538 |美国 |588 |俄罗斯 |576 |印度 |377 |印度 |424|
|3 |俄罗斯 |502 |印度尼西亚 |389 |巴西 |508 |巴西 |339 |巴西 |267|
|4 |德国 |407 |印度 |226 |荷兰 |448 |孟加拉国 |239 |印度尼西亚 |198|
|5 |印度尼西亚 |366 |荷兰 |199 |印度 |390 |德国 |158 |孟加拉国 |159|
|6 |荷兰 |342 |德国 |192 |英国 |304 |俄罗斯 |138 |越南 |143|
|7 |英国 |223 |孟加拉国 |182 |孟加拉国 |213 |英国 |125 |德国 |126|
|8 |孟加拉国 |202 |俄罗斯 |128 |德国 |196 |印度尼西亚 |113 |哥伦比亚 |99|
|9 |法国 |179 |澳大利亚 |118 |印度尼西亚 |110 |澳大利亚 |100 |墨西哥 |96|
|10 |中国 |165 |中国 |115 |香港 |108 |越南 |91 |英国 |85 |

表 18 - 各经济体每年的 IPv6 地址分配次数

这两个表格是过去五年按经济体的划分，表 18 显示了获得 IPv6 分配次数最多的经济体，而表 19 则显示了每个经济体获得分配的 IPv6 地址空间数量（使用 /32 为单位）。

|Rank |2019 |2020 |2021 |2022 |2023|
|---|---|---|---|---|---|
|1 |中国 |6,787 |中国 |6,765 |中国 |5,424 |美国 |13,919 |美国 |66,579|
|2 |美国 |5,510 |美国 |5,051 |俄罗斯 |4,409 |中国 |4,354 |立陶宛 |522|
|3 |俄罗斯 |3,716 |巴西 |1,358 |印度 |4,281 |俄罗斯 |925 |英国 |513|
|4 |德国 |2,522 |荷兰 |1,331 |荷兰 |3,390 |英国 |734 |德国 |478|
|5 |荷兰 |2,516 |德国 |716 |英国 |2,249 |德国 |706 |俄罗斯 |371|
|6 |英国 |1,355 |俄罗斯 |715 |德国 |896 |摩尔多瓦共和国 |456 |乌克兰 |369|
|7 |法国 |1,182 |英国 |552 |乌克兰 |651 |法国 |404 |伊朗 |314|
|8 |意大利 |1,052 |意大利 |391 |立陶宛 |633 |荷兰 |397 |法国 |276|
|9 |巴西 |1,049 |法国 |390 |巴西 |502 |意大利 |363 |塞舌尔 |258|
|10 |西班牙 |854 |土耳其 |290 |美国 |491 |巴西 |328 |卢旺达 |256 |

表 19 - 各经济体每年的 IPv6 地址分配数量

我们还可以查看前 25 个获得最多 IPv6 分配的地址数量的经济体（表 20）。

|排名 |国家代号 |地址分配数（/48）|总体占比|人均地址数量（/48）|宣告前缀数量（/48）|实际部署比例 |经济体名|
|---|---|---|---|---|---|---|---|
|1 |US |9,126,192,440 |31.30% |26.8 |1,399,113,308 |13.80% |美国|
|2 |CN |4,220,731,486 |14.50% |3 |1,665,240,127 |16.40% |中国|
|3 |DE |1,567,556,343 |5.40% |18.8 |1,067,282,327 |10.50% |德国|
|4 |GB |1,508,704,744 |5.20% |22.2 |468,594,870 |4.60% |英国|
|5 |FR |983,511,453 |3.40% |15.2 |181,849,911 |1.80% |法国|
|6 |RU |896,401,723 |3.10% |6.2 |196,222,375 |1.90% |俄罗斯|
|7 |NL |774,635,835 |2.70% |43.9 |328,258,068 |3.20% |荷兰|
|8 |IT |689,770,536 |2.40% |11.7 |426,414,680 |4.20% |意大利|
|9 |JP |665,723,093 |2.30% |5.4 |510,861,733 |5.00% |日本|
|10 |AU |622,396,680 |2.10% |23.4 |309,895,455 |3.10% |澳大利亚|
|11 |BR |543,392,965 |1.90% |2.5 |413,190,587 |4.10% |巴西|
|12 |SE |456,720,739 |1.60% |42.9 |90,319,074 |0.90% |瑞典|
|13 |IN |436,733,275 |1.50% |0.3 |370,137,769 |3.60% |印度|
|14 |PL |405,405,950 |1.40% |10 |235,541,715 |2.30% |波兰|
|15 |ES |402,784,297 |1.40% |8.5 |111,136,126 |1.10% |西班牙|
|16 |KR |345,767,946 |1.20% |6.7 |2,427,826 |0.00% |韩国|
|17 |AR |344,328,294 |1.20% |7.5 |284,954,258 |2.80% |阿根廷|
|18 |ZA |325,325,998 |1.10% |5.4 |293,199,836 |2.90% |南非|
|19 |EG |270,336,004 |0.90% |2.4 |270,008,322 |2.70% |埃及|
|20 |CH |256,115,135 |0.90% |29 |119,093,658 |1.20% |瑞士|
|21 |AE |248,643,595 |0.90% |26 |15,532,070 |0.20% |阿联酋|
|22 |TR |241,631,262 |0.80% |2.8 |43,376,879 |0.40% |土耳其|
|23 |IR |208,338,953 |0.70% |2.3 |49,976,209 |0.50% |伊朗|
|24 |CZ |196,673,655 |0.70% |18.7 |116,790,955 |1.20% |捷克|
|25 |UA |179,634,359 |0.60% |4.8 |55,948,379 |0.60% |乌克兰|

表 20 - 各经济体所持有的 IPv6 地址分配数量，截至 2023 年 12 月

虽然美国在已分配 IPv6 地址总数中名列榜首，占已分配 IPv6 地址总数的 14%，但人均数量却低于榜单中的其他国家（荷兰、瑞典、瑞士）。一些互联网服务提供商拥有大量 IPv6 地址，这可能是由于早期的 IPv6 分配政策与现在的分配政策有些不同。

二十年前，人们经常讨论 IPv4 地址部署状况的不公平状态。当时，美国一些大学掌握的 IPv4 地址比一些人口稠密的发展中经济体还要多，这种差距也是当时地址管理方法受到批评的原因之一。

RIR 系统的目的就是要解决导致分配不均的设计问题。该系统背后的理念是，在地区范围内，每个社区都可以自行决定“公平”和“公正”等术语的含义，据此制定自己的地址分配政策，然后指导其 RIR 执行这些政策。

IPv4 最初基于地址类别的分配计划明显会对前期采用者有更大奖励，可以称得上奢侈，与此相比，IPv6 的想法是从一开始就通过各地自下而上的政策框架来制定地址分配机制，从而避免不公平的结果，或者说至少希望如此。

按之前的设想，128 位地址空间允许我们进行庞大的地址规划，很大程度上会让稀缺性和不公平的概念将变得无关紧要。 2 的 128 次方是一个庞大的数字，在两个庞大的地址池之间进行比较在某种程度上是没有意义的。因此，当我们看人均地址数量的指标时，不要忘记 /48 前缀实际上是 80 比特的地址空间，比整个 IPv4 地址空间大得多。即使印度的人均只有 0.1 个 /48 前缀，这个地址数量仍然非常庞大！

不过我们不要沿着这条思路走太远，要知道 IPv6 中的 128 位地址空间在很大程度上已是过去的神话。我们在地址计划中砍掉了 64 比特，事后看来这样做并没有什么特别好的理由。然后，我们又削减了 16 位，同样也没有什么好理由。分配给终端站点地址的这 16 位允许每个站点内有大约 65,000 个不同的子网，哪怕考虑到所有可能，这都有些离谱。结果是，IPv6 中 128 比特所代表的庞大地址空间，实际上并没有那么庞大了。

在两个协议的可用地址前缀空间中，一个 /32 的 IPv4 终端地址大致相当于一个 IPv6 中的 /48 前缀。从这点出发，按 /48 前缀去比较人均地址数量也许并不完全是凭空想象，而且目前IPv6 地址分配不公平的说法也有一定的道理。不过与 IPv4 不同的是，IPv6 地址空间的耗尽尚需时日，而且我们仍然相信有足够的 IPv6 地址来支持整个芯片世界长期采用统一的地址使用模式。

比这更大的问题是当今公共网络的基本联网模式。IPv6 试图恢复 20 世纪 80 年代的点对点网络范式，每个联网设备都可以向任何其他联网设备发送数据包。然而，当今的网络环境将这种无限制的连接能力视为一种负担。人们认为暴露终端客户设备是不必要的愚蠢行为，当今的网络范式已经主要依赖客户端发起连接过程。

新的范式非常适合基于 NAT 的 IPv4 连接，但为了 IPv6 互联网的长远未来，人们需要决定是否要承担终端唯一寻址方案的维护成本，以及 NAT 是否也能在 IPv6 客户机/服务器网络中成为客户端侧最具性价比的服务平台。

那么在互联网路由表中，有多少已分配的 IPv6 地址是宣告出来的呢？

图 14 显示了自 2010 年以来 IPv6 已宣告、未宣告和已分配的地址总量，图 15 对应未宣告地址数占已分配 IPv6 地址总数的百分比。

{{< figure src="https://blog.apnic.net/wp-content/uploads/2024/01/addressing23-fig14.png" link="https://blog.apnic.net/wp-content/uploads/2024/01/addressing23-fig14.png" caption="图 14 - 已宣告、未宣告和已分配的 IPv6 地址总量" >}}

{{< figure src="https://blog.apnic.net/wp-content/uploads/2024/01/addressing23-fig15.png" link="https://blog.apnic.net/wp-content/uploads/2024/01/addressing23-fig15.png" caption="图 15 - 未宣告地址与已分配地址的比例" >}}

2013 年分配地址数量下降的原因是 LACNIC 发生了变化，将向巴西的一大段分配改为向互联网服务提供商和类似终端实体的细化分配和指派。

IPv4 地址分配一贯谨慎，有 77% 的已分配地址在 BGP 路由表中宣告，与此相比，IPv6 的 35% 看起来并不那么令人印象深刻。这其实并不关键。IPv6 的 128 位地址大小就是为了能在无需过于顾虑地址存量的前提下使用地址，我们有权低效地使用地址。

2024 年初，已宣告的 IPv6 地址总数相当于 152,000 个 /32 前缀，或约 99 亿个终端站点的 /48 前缀。这仅占 IPv6 /48 前缀总数的 0.004%。

# 互联网的前景展望

我们再一次发现，围绕互联网近期前景的一系列不确定因素比我们可以合理进行的预测要多得多。

2017 年，IPv6 部署急剧上升，这在很大程度上受到印度 IPv6 服务部署的影响，尤其来自 Reliance Jio 公司。接下来的 2018 年则较为平静，不过下半年有所上升，这是由于中国主要的服务提供商在进行大规模部署 IPv6 的初步努力。同样的努力在 2019 年加速，IPv6 部署水平整体移动了约 5%，这与中国 IPv6 部署的极速崛起有很大关系。中国的 IPv6 部署水平一直在持续上升，实测 IPv6 已从占用户群的 28% 上升到 2023 年的 32%，说明中国在这一年新增了 3600 万 IPv6 终端客户。

{{< figure src="https://blog.apnic.net/wp-content/uploads/2024/01/addressing23-fig16.png" link="https://blog.apnic.net/wp-content/uploads/2024/01/addressing23-fig16.png" caption="图 16 - IPv6 部署水平，2010 - 2023" >}}

如图 17 所示，2023 年全球 IPv6 的增长更加分散，总体增长率为 2.5%，但蒙古（27%）、不丹（20%）、尼泊尔（17%）、挪威（17%）和瑞典（11%）的 IPv6 部署稳步增长。

{{< figure src="https://blog.apnic.net/wp-content/uploads/2024/01/addressing23-fig17.png" link="https://blog.apnic.net/wp-content/uploads/2024/01/addressing23-fig17.png" caption="图 17 - IPv6 部署水平，2023 年 12 月" >}}

虽然已经有几家服务运营商认定，未来部署 NAT 的预期成本对于他们的服务平台来说不可持续，但仍有相当一部分人认为，NAT 将高性价比地吸收未来几年的互联网人口增长。或者说，这是我所能为大量服务提供商找到的唯一理由，他们现在看上去并没有任何部署双协议栈服务的行动。鉴于这一过渡的最终目标不是在所有地区启用双协议栈，而是关闭 IPv4，因此这还需要一些时间，其不确定性就在于如何估计这段时间。

过去十年间，移动互联网服务的大规模营销占据了主导地位，2014 年至 2016 年的互联网增长率或许是迄今为止最高的。如果不是因为 IPv4 地址池的枯竭，这一点在 IP 地址部署数据中就会显现出来。

就地址而言，IPv4 互联网的这种增长几乎完全被移动服务提供商所使用的运营商级 NAT 所掩盖，导致它们对 IPv4 公共地址的需求相当低，网络内部的增长也就因为这些 NAT 而不可见。而在 IPv6 这边的大部分需求量则是被超大的地址空间所掩盖。如果一个互联网服务提供商获得了一个 /20 的 IPv6 前缀，它就能分配 2.68 亿个 /48 前缀或 680 亿个 /56 前缀，因此 IPv6 网络中的大部分增长都被 IPv6 底层的庞大寻址方案所隐藏。

人们还认为，未来大规模传感器网络部署和其他形式的物联网部署会产生对 IPv6 地址的需求。尽管这种可能性始终存在，但我们不能只认为这些部署预期只是当红行业的过度炒作。更有可能的情况是，到目前为止，这类部署都使用了私有 IPv4 地址，依靠 NAT 和应用级网关与公共网络连接。我们一次又一次地被教育，NAT 不能作为合适的安全设备，但在实际操作中，NAT 确实又能相对合理地在前线防御恶意软件的网络扫描。因此，大规模设备网络使用 NAT 可能不仅仅是出于继续使用 IPv4 的简单保守思想，背后可能还有更远大的考虑。

更广泛地说，我们的行业不再以技术创新、开放和多样化作为主要的推动手段。IPv4 中广泛使用的 NAT 将互联网的技术基础限制在一个非常有限的模型中，只能使用 TCP 和 UDP 进行简单的客户端/服务器交互。NAT 迫使网络通信变成了由客户发起的过程，能非常灵活地自由通信的开放联网模式在当今的网络中已难以为继。在 IPv4/IPv6 的漫长过渡中，既得利益者正在巩固自己的地位，而创新和创业精神则退居其次。

现在的情况是，当今的互联网运输服务由少数几个非常大的参与者提供的，每个参与者看上去都在各自所属的市场中占据着非常强势的地位。这些大型企业的驱动力往往是规避风险、保守主义和加强对它们经营领域内的控制。内容提供领域也在出现同样的市场聚合趋势，少数内容提供商在整个互联网上完全占据了主导地位。

互联网行业不断演变的构成相当深远地影响了网络中立性、传输和服务提供功能的分离、投资概况和基础设施投资的预期风险回报，以及互联网本身的开放性。

由于互联网行业巨大的经济规模，要维持一个高效、完全开放且有竞争力的行业总是充满挑战，但当底层平台耗尽作为基本货币的 IP 地址时，这些议程所面临的挑战程度就会成倍增加。随着有能力参与竞争的新鲜力量逐渐枯竭，现存的巨头就会面临更大的压力来利用现行地位巩固它们对行业的全面控制。要解决这种情况，通常需要某种形式的公共部门干预，目的是恢复有效竞争，重新让市场有动力提供更高效、更有效的产品。

随着互联网的不断发展，它已不再是技术创新的挑战者，与电话、印刷报纸、电视娱乐和社交互动等传统行业同台经济。现在，互联网自己才是常态。能将互联网标榜为宽松管制下的颠覆者的时代早已一去不复返，如今的互联网正在越来越多地寻求监管和治理框架，以挑战对新建立的常态秩序的惰性满足。

这种求索能取得怎样的成就，目前还不清楚，我们只能拭目以待。

---

译文作者：王文鑫

本译文最初发表于 [《中国教育网络》](https://www.edu.cn/xxh/zt/tj/202405/t20240515_2609767.shtml)，转载请按此下述授权要求，注明译文作者、使用同一授权，并注明原作者和引用出处。

感谢作者 Geoff Huston 的亲切支持！

Thanks to Geoff Huston (the original author) for your kind support!

在保证原作者所有权益的情况下，本译文使用 Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International 授权，详情见 https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en
  超出此授权范围之外的使用需获得“计算机史料随译”项目的许可，详情见 https://random-cs-hans.github.io。

On the precondition of keeping all rights of the original authors, this translation work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike License (International/4.0), see https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en for details. Permissions beyond the scope of this license are administered by the "RandomCSHans" Project，see https://random-cs-hans.github.io.

{{< figure src="http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-nc-sa.svg" alt="CC BY-NC-SA License" >}}
