# coding: utf-8
import datetime
import icalendar
import pytz
import uuid6

lst_rcfc_time = [
    "202403021935;中超;成都蓉城;青岛海牛;成都凤凰山体育公园专业足球场",
    "202403101530;中超;沧州雄狮;成都蓉城;沧州体育场",
    "202403301900;中超;成都蓉城;南通支云;成都凤凰山体育公园专业足球场",
    "202404061530;中超;天津津门虎;成都蓉城;天津泰达足球场",
    "202404101935;中超;成都蓉城;浙江俱乐部;成都凤凰山体育公园专业足球场",
    "202404141530;中超;长春亚泰;成都蓉城;长春体育中心体育场",
    "202404201900;中超;成都蓉城;深圳新鹏城;成都凤凰山体育公园专业足球场",
    "202404262000;中超;成都蓉城;山东泰山;成都凤凰山体育公园专业足球场",
    "202405011935;中超;成都蓉城;武汉三镇;成都凤凰山体育公园专业足球场",
    "202405051935;中超;北京国安;成都蓉城;北京工人体育场",
    "202405101935;中超;成都蓉城;河南俱乐部;成都凤凰山体育公园专业足球场",
    "202405171935;中超;梅州客家;成都蓉城;五华奥体中心惠堂体育场",
    "202405222000;中超;上海海港;成都蓉城;上汽浦东足球场",
    "202405261935;中超;成都蓉城;青岛西海岸;成都凤凰山体育公园专业足球场",
    "202406161935;中超;上海申花;成都蓉城;上海体育场",
    "202406211600;足协杯;上海三菱重工;成都蓉城;上海体育场",
    "202406261935;中超;青岛海牛;成都蓉城;青岛青春足球场",
    "202406301935;中超;成都蓉城;沧州雄狮;成都凤凰山体育公园专业足球场",
    "202407071900;中超;南通支云;成都蓉城;如皋奥体中心体育场",
    "202407122000;中超;成都蓉城;天津津门虎;成都凤凰山体育公园专业足球场",
    "202407281935;中超;浙江俱乐部;成都蓉城;浙江省黄龙体育中心体育场",
    "202408032000;中超;成都蓉城;长春亚泰;成都凤凰山体育公园专业足球场",
    "202408091935;中超;深圳新鹏城;成都蓉城;深圳宝安体育中心体育场",
    "202408172000;中超;山东泰山;成都蓉城;济南奥体中心体育场",
    "202408252000;中超;武汉三镇;成都蓉城;武汉体育中心体育",
    "202409141935;中超;成都蓉城;北京国安;成都凤凰山体育公园专业足球场",
    "202409211935;中超;河南俱乐部;成都蓉城;郑州航海体育场",
    "202409291935;中超;成都蓉城;梅州客家;成都凤凰山体育公园专业足球场",
    "202410182000;中超;成都蓉城;上海海港;成都凤凰山体育公园专业足球场",
    "202410271530;中超;青岛西海岸;成都蓉城;青岛西海岸大学城体育场",
    "202411021530;中超;上海申花;成都蓉城;成都凤凰山体育公园专业足球场",
]

lst_cba_time = [
    "202402221930;2025男篮亚预赛;中国男篮;蒙古国男篮;西安",
    "202402251300;2025男篮亚预赛;日本男篮;中国男篮;东京",
    "202404221930;2023-2024WCBA总决赛第5场(5局3胜);内蒙古农信(2);四川远达美乐(2);呼和浩特内蒙古体育馆",
]

lst_cfa_time = [
    "202403212030;世预;新加坡国家男子足球队;中国国家男子足球队;新加坡国家体育场",
    "202403262000;世预;中国国家男子足球队;新加坡国家男子足球队;天津奥林匹克体育中心体育场",
    "202406062000;世预;中国国家男子足球队;泰国国家男子足球队;沈阳奥林匹克体育中心场",
    "202406111900;世预;韩国国家男子足球队;中国国家男子足球队;韩国",
]

lst_key_time = [
    "202402201600;亚冠1/8决赛;川崎前锋;山东泰山;川崎等等力陆上竞技场",
    "202403061800;亚冠1/4决赛;山东泰山;横滨水手;济南奥体中心体育场",
    "202403131800;亚冠1/4决赛;横滨水手;山东泰山;横滨国际综合竞技场",
    "202406150300;欧洲杯A组;德国;英格兰;德国",
    "202406152100;欧洲杯A组;匈牙利;瑞士;德国",
    "202406160000;欧洲杯B组;西班牙;克罗地亚;德国",
    "202406160300;欧洲杯B组;意大利;阿尔巴尼亚;德国",
    "202406162100;欧洲杯D组;波兰;荷兰;德国",
    "202406170000;欧洲杯C组;斯洛文尼亚;丹麦;德国",
    "202406170300;欧洲杯C组;塞尔维亚;英格兰;德国",
    "202406172100;欧洲杯E组;罗马尼亚;乌克兰;德国",
    "202406180000;欧洲杯E组;比利时;斯洛伐克;德国",
    "202406180300;欧洲杯D组;奥地利;法国;德国",
    "202406190000;欧洲杯F组;土耳其;格鲁吉亚;德国",
    "202406190300;欧洲杯F组;葡萄牙;捷克;德国",
    "202406192100;欧洲杯B组;克罗地亚;阿尔巴尼亚;德国",
    "202406200000;欧洲杯A组;德国;匈牙利;德国",
    "202406200300;欧洲杯A组;苏格兰;瑞士;德国",
    "202406202100;欧洲杯C组;斯洛文尼亚;塞尔维亚;德国",
    "202406210000;欧洲杯C组;丹麦;苏格兰;德国",
    "202406210300;欧洲杯B组;西班牙;意大利;德国",
    "202406212100;欧洲杯E组;斯洛伐克;乌克兰;德国",
    "202406220000;欧洲杯D组;波兰;奥地利;德国",
    "202406220300;欧洲杯D组;荷兰;法国;德国",
    "202406222100;欧洲杯F组;格鲁吉亚;捷克;德国",
    "202406230000;欧洲杯F组;土耳其;葡萄牙;德国",
    "202406230300;欧洲杯E组;比利时;罗马尼亚;德国",
    "202406240300;欧洲杯A组;苏格兰;匈牙利;德国",
    "202406240300;欧洲杯A组;瑞士;德国;德国",
    "202406250300;欧洲杯B组;克罗地亚;意大利;德国",
    "202406250300;欧洲杯B组;阿尔巴尼亚;西班牙;德国",
    "202406260000;欧洲杯D组;法国;波兰;德国",
    "202406260000;欧洲杯D组;荷兰;奥地利;德国",
    "202406260300;欧洲杯C组;丹麦;塞尔维亚;德国",
    "202406260300;欧洲杯C组;英格兰;斯洛文尼亚;德国",
    "202406270000;欧洲杯E组;乌克兰;比利时;德国",
    "202406270000;欧洲杯E组;斯洛伐克;罗马尼亚;德国",
    "202406270300;欧洲杯F组;捷克;土耳其;德国",
    "202406270300;欧洲杯F组;格鲁吉亚;葡萄牙;德国",
    "202406300000;欧洲杯1/8决赛;瑞士;意大利;德国",
    "202406300300;欧洲杯1/8决赛;德国;丹麦;德国",
    "202407010000;欧洲杯1/8决赛;英格兰;斯洛伐克;德国",
    "202407010300;欧洲杯1/8决赛;西班牙;格鲁吉亚;德国",
    "202407020000;欧洲杯1/8决赛;法国;比利时;德国",
    "202407020300;欧洲杯1/8决赛;葡萄牙;斯洛文尼亚;德国",
    "202407030000;欧洲杯1/8决赛;罗马尼亚;荷兰;德国",
    "202407030300;欧洲杯1/8决赛;奥地利;土耳其;德国",
    "202407060000;欧洲杯1/4决赛;待定;待定;德国",
    "202407060300;欧洲杯1/4决赛;待定;待定;德国",
    "202407070000;欧洲杯1/4决赛;待定;待定;德国",
    "202407070300;欧洲杯1/4决赛;待定;待定;德国",
    "202407100300;欧洲杯半决赛;待定;待定;德国",
    "202407110300;欧洲杯半决赛;待定;待定;德国",
    "202407150300;欧洲杯决赛;待定;待定;德国",
]


def create_event(summary, location, description, dtstart, dtend):
    event = icalendar.Event()
    event.add("summary", summary)

    event.add("dtstart", dtstart)
    event.add("dtend", dtend)
    # 创建时间
    # event.add('dtstamp', dt_now)
    event.add("location", location)
    event.add("description", description)

    # uid保证唯一
    event["uid"] = str(uuid6.uuid6()) + "/douyin:chuanzu"

    return event


if __name__ == "__main__":
    cal = icalendar.Calendar()
    cal.add("version", "2.0")
    cal.add("X-APPLE-CALENDAR-COLOR", "#FF0000")
    cal.add("X-WR-CALNAME", "一起看球赛历-抖音“看球去了”")
    cal.add("X-WR-TIMEZONE", "Asia/Shanghai")

    description = "一起雄起！\n该订阅日历由抖音【看球去了】更新、维护。"

    # 成都蓉城 from 2024
    for match in lst_rcfc_time:
        lst_match_info = match.split(";")
        if lst_match_info[2].startswith("成都"):
            summary = (
                f"⚽【主/{lst_match_info[1]}】{lst_match_info[2]}vs{lst_match_info[3]}"
            )
        else:
            summary = (
                f"【客/{lst_match_info[1]}】{lst_match_info[2]}vs{lst_match_info[3]}"
            )
        location = lst_match_info[4]
        dtstart = pytz.timezone("Asia/Shanghai").localize(
            datetime.datetime.strptime(lst_match_info[0], "%Y%m%d%H%M")
        )
        dtend = dtstart + datetime.timedelta(hours=2)
        cal.add_component(create_event(summary, location, description, dtstart, dtend))

    # 男篮国家队 from 2024
    for match in lst_cba_time:
        lst_match_info = match.split(";")
        if lst_match_info[2].startswith("中国"):
            summary = (
                f"🏀【主/{lst_match_info[1]}】{lst_match_info[2]}vs{lst_match_info[3]}"
            )
        else:
            summary = (
                f"【客/{lst_match_info[1]}】{lst_match_info[2]}vs{lst_match_info[3]}"
            )
        location = lst_match_info[4]
        dtstart = pytz.timezone("Asia/Shanghai").localize(
            datetime.datetime.strptime(lst_match_info[0], "%Y%m%d%H%M")
        )
        dtend = dtstart + datetime.timedelta(hours=2)
        cal.add_component(create_event(summary, location, description, dtstart, dtend))

    # 男足国家队 from 2024
    for match in lst_cfa_time:
        lst_match_info = match.split(";")
        if lst_match_info[2].startswith("中国"):
            summary = (
                f"⚽【主/{lst_match_info[1]}】{lst_match_info[2]}vs{lst_match_info[3]}"
            )
        else:
            summary = (
                f"【客/{lst_match_info[1]}】{lst_match_info[2]}vs{lst_match_info[3]}"
            )
        location = lst_match_info[4]
        dtstart = pytz.timezone("Asia/Shanghai").localize(
            datetime.datetime.strptime(lst_match_info[0], "%Y%m%d%H%M")
        )
        dtend = dtstart + datetime.timedelta(hours=2)
        cal.add_component(create_event(summary, location, description, dtstart, dtend))

    # 关键比赛 from 2024
    for match in lst_key_time:
        lst_match_info = match.split(";")
        summary = f"【{lst_match_info[1]}】{lst_match_info[2]}vs{lst_match_info[3]}"
        location = lst_match_info[4]
        dtstart = pytz.timezone("Asia/Shanghai").localize(
            datetime.datetime.strptime(lst_match_info[0], "%Y%m%d%H%M")
        )
        dtend = dtstart + datetime.timedelta(hours=2)
        cal.add_component(create_event(summary, location, description, dtstart, dtend))
    with open(
        "/home/xldu/repos/repos_xlindo/blog/kewenlu/source/uploads/chuanzu.ics", "wb"
    ) as f:
        f.write(cal.to_ical())
