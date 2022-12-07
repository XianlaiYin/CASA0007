---
title: Proposal of CASA0007 Group Work
author: Xianlai Yin
date: 02/12/2022
---

### Theme
**Title 15s**
如何在西雅图拥有一个受欢迎的Airbnb房源？

**Content 25s** 
1. 受欢迎的Airbnb房源有着什么样的特征？
2. 如何定价使得Airbnb房源更加受到欢迎？
   
**Area 10s**
Seattle

**Data Source 10s**
[InsideAirbnb](http://insideairbnb.com/)

### Progress
**Step1: 数据清理 ZL 2.5mins**
`将原始数据（Inside Airbnb）进行整理，清理不相关列，重点添加“热门程度指数”，“周边2公里房源均价”，“与周边房源的相对价格”`
1. 数据整理与清理不相关列（'host_location' -> 'host_location_num' 添加列：是否为本地（tf）；'host_response_time' -> 'response_time_num' 将文字更改为1~5级 ；'host_verifications' -> 'host_verifications_num' 添加列：验证种类数量；'amenities' -> 'amenities_num' 添加列：设施种类数量；'license' -> 'license_num' 添加列：是否有license（tf）；'availability_365' -> 'booked_365' 未来一年被预定天数：365-'availability_365'
2. 热门程度指数：将月均评论数进行标准化作为过去热门程度，将未来一年已预定天数进行标准化作为预期热门程度，二者相加得到。
[没有明确的“热门的定义”]（Li et al., 2017）。根据Huang et al. (2017) and Li et al. (2020)对于热门指数的计算，以及具备的数据，我们采用月均评价数量和未来一月已预定的天数计算热门程度指数。
Huang, D., C. Leung and C. Tse (2018) What Accounts for the Differences in Rent-Price Ratio and Turnover Rate? A Search-and-Matching Approach. The journal of real estate finance and economics. [Online] 57 (3), 431–475.
Li, Y., S. Wang, Y. Ma, Q. Pan and E. Cambria (2020) Popularity prediction on vacation rental websites. Neurocomputing (Amsterdam). [Online] 412372–380.
1. 周边0.5公里房源均价：由于本研究不涉及空间分析，为了排除区位因素带来的干扰，采取相对价格作为价格指标，以周边0.5公里为广义社区范围，计算其平均价格
[选择0.5km作为计算房源相对均价的原因]：“Seattle, WA, has a median lot size of almost 5,300 square feet”，西雅图每幢房子的平均占地面积约为0.00049平方千米（Gatea, 2021），0.5km为半径的范围内基本能够形成一个community，具有相似的基础设施、环境，用作计算相对平均房租较为合适。
Gatea, M. (2021) 'The American Backyard In The Last 100 Years: Lot Sizes In San Diego Get Bigger While Seattle Loses Yard Space BY MARIA GATEA  JULY 29, 2021  26 MINS READ', Storagecafe (www.storagecafe.com/blog/lot-size-home-size-in-top-20-biggest-us-cities/; 3 December 2022)

**Step2: 聚类分析 YYK 2mins**
`通过聚类分析，将房源划分为不同价位段，并得出不同价位段中最受欢迎的一批房源`
1. 价格聚类分析: 将“价格”，“与周边房源的相对价格”划分为3~5档[需要理论支撑]，作为价格分类的标准
2. 热门程度聚类分析：将“热门程度指数”划分为3~5档[需要理论支撑]，作为热门程度分类的标准
3. 将二者进行叠加，得到每一个价格分类中最受欢迎的一批房源
- [可补充具体内容]

**Step3: 相关与回归分析（热门程度的影响因素） YXL 1.5mins**
`通过相关分析，判断在不同价位段，显著影响热门程度的因素，得出多元回归模型`
1. 数据二次处理，创建虚拟变量（get dummy）
2. 相关性检验
3. VIF检验多重共线性，删除高线性因素
4. OLS回归

**Step4: 描述性统计分析 CDM 2.5mins**
`通过描述性统计分析，分析不同价位段受欢迎的Airbnb房源有着什么样的特征`
1. 对整体房源价格进行分析:绘制价格的概率密度直方图，发现价格区间为[0,1000],但大部分房源的价格集中在[0-250]之间，进一步缩小价格区间，可以得到价格集中在[50,l250]
2. 绘制价格与最低预定天数的散点图:可以看到，大部分最低预定天数都在100天以下，有较少的房子被定了700天，用于长住。
3. 经纬度定位：查看不同房源在西雅图的分布，点状图
4. 房间类型分析(room_type):1. 统计出三种房间类型以及每种房间类型占全部房型的百分比：Entire home/apt, Private room, Shared room  2.room_type的可视化pie chart
5. 房间类型和价格关系: 价格和房间类型的散点图

**Step5: 相关与回归分析（价格的影响因素） YXL 1.5mins**
`通过回归分析，判断在受到欢迎的程度情况下，各种因素如何影响定价，得出多元线性回归，再基于周边价格基础得到最终模型（输入各项因素的值即可以得到预期定价）。题外：利润分析，利润指数=销量的回归模型（基于价格）*价格，在有其他变量的基础上进行案例计算`
1. 数据二次处理，创建虚拟变量（get dummy）
2. 相关性检验
3. VIF检验多重共线性，删除高线性因素
4. OLS回归

### References
[需要补充]

**Step4: 描述性统计分析 CDM 2.5mins**
`通过描述性统计分析，分析不同价位段受欢迎的Airbnb房源有着什么样的特征`

1. 对整体房源价格进行分析:绘制价格的概率密度直方图，发现价格区间为[0,1000],但大部分房源的价格集中在[0-250]之间，进一步缩小价格区间，可以得到价格集中在[50,l250]
