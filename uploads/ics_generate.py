# coding: utf-8
import datetime
import icalendar
import pytz
import uuid

lst_rcfc_time = [
    "202403021935;成都蓉城;青岛海牛;成都凤凰山体育公园专业足球场",
    "202403101530;沧州雄狮;成都蓉城;沧州体育场",
    "202403301900;成都蓉城;南通支云;成都凤凰山体育公园专业足球场",
    "202404061530;天津津门虎;成都蓉城;天津泰达足球场",
    "202404101935;成都蓉城;浙江俱乐部;成都凤凰山体育公园专业足球场",
    "202404141530;长春亚泰;成都蓉城;长春体育中心体育场",
    "202404201900;成都蓉城;深圳新鹏城;成都凤凰山体育公园专业足球场",
    "202404262000;成都蓉城;山东泰山;成都凤凰山体育公园专业足球场",
    "202405011935;成都蓉城;武汉三镇;成都凤凰山体育公园专业足球场",
    "202405051935;北京国安;成都蓉城;北京工人体育场",
    "202405101935;成都蓉城;河南俱乐部;成都凤凰山体育公园专业足球场",
    "202405171935;梅州客家;成都蓉城;五华奥体中心惠堂体育场",
    "202405222000;上海海港;成都蓉城;上汽浦东足球场",
    "202405261935;成都蓉城;青岛西海岸;成都凤凰山体育公园专业足球场",
    "202406161935;上海申花;成都蓉城;上海体育场",
    "202406261935;青岛海牛;成都蓉城;青岛青春足球场",
    "202406301935;成都蓉城;沧州雄狮;成都凤凰山体育公园专业足球场",
    "202407071900;南通支云;成都蓉城;如皋奥体中心体育场",
    "202407122000;成都蓉城;天津津门虎;成都凤凰山体育公园专业足球场",
    "202407281935;浙江俱乐部;成都蓉城;浙江省黄龙体育中心体育场",
    "202408032000;成都蓉城;长春亚泰;成都凤凰山体育公园专业足球场",
    "202408091935;深圳新鹏城;成都蓉城;深圳宝安体育中心体育场",
    "202408172000;山东泰山;成都蓉城;济南奥体中心体育场",
    "202408252000;武汉三镇;成都蓉城;武汉体育中心体育",
    "202409141935;成都蓉城;北京国安;成都凤凰山体育公园专业足球场",
    "202409211935;河南俱乐部;成都蓉城;郑州航海体育场",
    "202409291935;成都蓉城;梅州客家;成都凤凰山体育公园专业足球场",
    "202410182000;成都蓉城;上海海港;成都凤凰山体育公园专业足球场",
    "202410271530;青岛西海岸;成都蓉城;青岛西海岸大学城体育场",
    "202411021530;上海申花;成都蓉城;成都凤凰山体育公园专业足球场",
]

lst_cfa_time = [
    "202403262000;中国国家男子足球队;新加坡国家男子足球队;天津奥林匹克体育中心体育场",
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
    event["uid"] = str(uuid.uuid1()) + "/douyin:chuanzu"

    return event


if __name__ == "__main__":
    cal = icalendar.Calendar()
    cal.add("version", "2.0")
    cal.add("X-APPLE-CALENDAR-COLOR", "#FF0000")
    cal.add("X-WR-CALNAME", "四川球队赛程-抖音“看球去了”")
    cal.add("X-WR-TIMEZONE", "Asia/Shanghai")

    # 成都蓉城 2024
    for match in lst_rcfc_time:
        lst_match_info = match.split(";")
        summary = lst_match_info[1]
        if summary == "成都蓉城":
            summary = "⚽【主/中超】" + lst_match_info[1] + "vs" + lst_match_info[2]
        else:
            summary = "【客/中超】" + lst_match_info[1] + "vs" + lst_match_info[2]
        description = "抖音【看球去了】和你一起“雄起”！"
        location = lst_match_info[3]
        dtstart = pytz.timezone("Asia/Shanghai").localize(
            datetime.datetime.strptime(lst_match_info[0], "%Y%m%d%H%M")
        )
        dtend = dtstart + datetime.timedelta(hours=2)
        cal.add_component(create_event(summary, location, description, dtstart, dtend))
    
    # 国家队 from 2024
    for match in lst_cfa_time:
        lst_match_info = match.split(";")
        summary = lst_match_info[1]
        if summary.startswith("中国"):
            summary = "⚽【主】" + lst_match_info[1] + "vs" + lst_match_info[2]
        else:
            summary = "【客】" + lst_match_info[1] + "vs" + lst_match_info[2]
        description = "抖音【看球去了】和你一起“雄起”！"
        location = lst_match_info[3]
        dtstart = pytz.timezone("Asia/Shanghai").localize(
            datetime.datetime.strptime(lst_match_info[0], "%Y%m%d%H%M")
        )
        dtend = dtstart + datetime.timedelta(hours=2)
        cal.add_component(create_event(summary, location, description, dtstart, dtend))

    with open("/home/xldu/repos/repos_xlindo/blog/kewenlu/source/uploads/chuanzu.ics", "wb") as f:
        f.write(cal.to_ical())
