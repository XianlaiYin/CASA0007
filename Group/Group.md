---
title: Proposal of CASA0007 Group Work
author: Xianlai Yin
date: 02/12/2022
---

### Theme
**Title 15s**
如何在西雅图拥有一个受欢迎的Airbnb房源？

**Content 25s** 
1. 判断您的房源是否拥有受欢迎的潜力——受欢迎的Airbnb房源有着什么样的特征？
2. 您的房源如何定价——如何定价使得Airbnb房源更加受到欢迎？
   
**Area 10s**
Seattle

**Data Source 10s**
[InsideAirbnb](http://insideairbnb.com/)

### Progress
**Step1: 数据清理 ZL 2.5mins**
`将原始数据（Inside Airbnb）进行整理，清理不相关列，重点添加“热门程度指数”，“周边2公里房源均价”，“与周边房源的相对价格”`
1. 数据整理与清理不相关列
2. 热门程度指数[需要理论支撑]：将月均评论数进行标准化作为过去热门程度，将未来一年已预定天数进行标准化作为预期热门程度，二者相加得到。
3. 周边2公里房源均价：由于本研究不涉及空间分析，为了排除区位因素带来的干扰，采取相对价格作为价格指标，以周边2公里为广义社区范围[需要理论支撑]，计算其平均价格
4. 与周边房源的相对价格：房源价格-周边2公里房源均价
- [可补充具体内容]

**Step2: 聚类分析 YYK 2mins**
`通过聚类分析，将房源划分为不同价位段，并得出不同价位段中最受欢迎的一批房源`
1. 价格聚类分析: 将“价格”，“与周边房源的相对价格”划分为3~5档[需要理论支撑]，作为价格分类的标准
2. 热门程度聚类分析：将“热门程度指数”划分为3~5档[需要理论支撑]，作为热门程度分类的标准
3. 将二者进行叠加，得到每一个价格分类中最受欢迎的一批房源
- [可补充具体内容]

**Step3: 相关与回归分析（热门程度的影响因素） YXL 1.5mins**
`通过相关分析，判断在不同价位段，显著影响热门程度的因素，得出多元回归模型`
1. 数据二次处理，创建虚拟变量（get dummy）
2. VIF检验多重共线性，判断与热门程度显著相关的因子
- [需要补充具体内容]

**Step4: 描述性统计分析 CDM 2.5mins**
`通过描述性统计分析，分析不同价位段受欢迎的Airbnb房源有着什么样的特征`
- [需要补充具体内容]

**Step5: 相关与回归分析（价格的影响因素） YXL 1.5mins**
`通过回归分析，判断在受到欢迎的程度情况下，各种因素如何影响定价，得出多元线性回归，再基于周边价格基础得到最终模型（输入各项因素的值即可以得到预期定价）。题外：利润分析，利润指数=销量的回归模型（基于价格）*价格，在有其他变量的基础上进行案例计算`
- [需要补充具体内容]

### References
[需要补充]

### Data
**删除列**
['name','description','neighborhood_overview','host_thumbnail_url','host_picture_url','picture_url','calendar_last_scraped','host_url','host_name','host_about', 'scrape_id', 'last_scraped', 'source', 'listing_url', 'host_neighbourhood', 'neighbourhood', 'neighbourhood_cleansed', 'neighbourhood_group_cleansed', 'bathrooms_text', 'minimum_nights', 'maximum_nights', 'minimum_minimum_nights', 'maximum_minimum_nights', 'minimum_maximum_nights', 'maximum_maximum_nights', 'calendar_updated', 'has_availability', 'availability_30', 'availability_60', 'availability_90', 'number_of_reviews', 'number_of_reviews_ltm', 'number_of_reviews_l30d', 'first_review', 'last_review','calculated_host_listings_count_entire_homes', 'calculated_host_listings_count_private_rooms', 'calculated_host_listings_count_shared_rooms', 'host_listings_count', 'host_total_listings_count']

**整理与删除后现有列**
['id', 'host_id', 'host_since', 'host_location', 'host_response_time', 'host_response_rate', 'host_acceptance_rate', 'host_is_superhost', 'host_verifications', 'host_has_profile_pic', 'host_identity_verified', 'latitude', 'longitude', 'property_type', 'room_type', 'accommodates', 'bathrooms', 'bedrooms', 'beds', 'amenities', 'price', 'minimum_nights_avg_ntm', 'maximum_nights_avg_ntm', 'availability_365',  'review_scores_rating', 'review_scores_accuracy', 'review_scores_cleanliness', 'review_scores_checkin', 'review_scores_communication', 'review_scores_location', 'review_scores_value', 'license', 'instant_bookable', 'calculated_host_listings_count', 'reviews_per_month']

**进一步整理**
1. 'host_location' -> 'host_location_num' 添加列：是否为本地（tf）
2. 'host_response_time' -> 'response_time_num' 将文字更改为1~5级
3. 'host_verifications' -> 'host_verifications_num' 添加列：验证种类数量
4. 'amenities' -> 'amenities_num' 添加列：设施种类数量
5. 'license' -> 'license_num' 添加列：是否有license（tf）
6. 'availability_365' -> 'booked_365' 未来一年被预定天数：365-'availability_365'
7. '热门程度指数' （见前文）、
8. '周边2公里房源均价' （见前文）
9.  '与周边房源的相对价格' （见前文）
[可补充具体内容]

**整理成果**