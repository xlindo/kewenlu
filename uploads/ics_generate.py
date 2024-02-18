# coding: utf-8
import datetime
import icalendar
import pytz
import uuid

lst_rcfc_time = [
    "20240302193500;成都蓉城;青岛海牛;凤凰山体育公园专业足球场",
    "20240310153000;沧州雄狮;成都蓉城;沧州体育场",
    "20240330190000;成都蓉城;南通支云;凤凰山体育公园专业足球场",
    "20240406153000;天津津门虎;成都蓉城;天津泰达足球场",
    "20240410193500;成都蓉城;浙江俱乐部;凤凰山体育公园专业足球场",
    "20240414153000;长春亚泰;成都蓉城;长春体育中心体育场",
    "20240420190000;成都蓉城;深圳新鹏城;凤凰山体育公园专业足球场",
    "20240426200000;成都蓉城;山东泰山;凤凰山体育公园专业足球场",
    "20240501193500;成都蓉城;武汉三镇;凤凰山体育公园专业足球场",
    "20240505193500;北京国安;成都蓉城;北京工人体育场",
    "20240510193500;成都蓉城;河南俱乐部;凤凰山体育公园专业足球场",
    "20240517193500;梅州客家;成都蓉城;五华奥体中心惠堂体育场",
    "20240522200000;上海海港;成都蓉城;上汽浦东足球场",
    "20240526193500;成都蓉城;青岛西海岸;凤凰山体育公园专业足球场",
    "20240616193500;上海申花;成都蓉城;上海体育场",
    "20240626193500;青岛海牛;成都蓉城;青岛青春足球场",
    "20240630193500;成都蓉城;沧州雄狮;凤凰山体育公园专业足球场",
    "20240707190000;南通支云;成都蓉城;如皋奥体中心体育场",
    "20240712200000;成都蓉城;天津津门虎;凤凰山体育公园专业足球场",
    "20240728193500;浙江俱乐部;成都蓉城;浙江省黄龙体育中心体育场",
    "20240803200000;成都蓉城;长春亚泰;凤凰山体育公园专业足球场",
    "20240809193500;深圳新鹏城;成都蓉城;深圳宝安体育中心体育场",
    "20240817200000;山东泰山;成都蓉城;济南奥体中心体育场",
    "20240825200000;武汉三镇;成都蓉城;武汉体育中心体育",
    "20240914193500;成都蓉城;北京国安;凤凰山体育公园专业足球场",
    "20240921193500;河南俱乐部;成都蓉城;郑州航海体育场",
    "20240429193500;成都蓉城;梅州客家;凤凰山体育公园专业足球场",
    "20241018200000;成都蓉城;上海海港;凤凰山体育公园专业足球场",
    "20241027153000;青岛西海岸;成都蓉城;青岛西海岸大学城体育场",
    "20241102153000;上海申花;成都蓉城;凤凰山体育公园专业足球场",
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
            datetime.datetime.strptime(lst_match_info[0], "%Y%m%d%H%M%S")
        )
        dtend = dtstart + datetime.timedelta(hours=2)
        cal.add_component(create_event(summary, location, description, dtstart, dtend))

    with open("chuanzu.ics", "wb") as f:
        f.write(cal.to_ical())
