"""
北京安贞医院 肾内科
"""
from sanjia.utils.common import *


def parse_detail(link):
    doc = pq(link, encoding='utf-8')
    file = os.path.basename(__file__)
    hospital = '北京安贞医院'
    name = doc('div.doctor_message > div > dl > dt > h1').text()
    title = doc('div.doctor_message > div > dl > dd:nth-child(4)').text().split(':')[1]
    department = doc('div.doctor_message > div > dl > dd:nth-child(2) > a').text()
    special = doc('div.doctor_message > div > dl > dd:nth-child(7)').text().strip('专业特长:')
    resume = doc('#Descri > p').text()
    outpatient_info = parse_outpatient(doc)
    yield {
        'file': file,
        'hospital': hospital,
        'grade': '三甲',
        'name': name,
        'title': title,
        'department': department,
        'special': special,
        'resume': resume,
        'outpatient_info': outpatient_info,
        'url': link
    }


# 解析出诊信息
def parse_outpatient(doc):
    week = {1: '周一', 2: '周二', 3: '周三', 4: '周四', 5: '周五', 6: '周六', 7: '周日'}
    outpatient_info = []
    morning = doc('#scheduling > table tr:nth-child(3) td').items()
    for a, b in enumerate(morning):
        if b('span'):
            outpatient_info.append(week[a] + '上午 ' + b('span').text())

    afternoon = doc('#scheduling > table tr:nth-child(4) th').items()
    for a, b in enumerate(afternoon):
        if b('span'):
            outpatient_info.append(week[a] + '下午 ' + b('span').text())

    return outpatient_info


def main(url):
    doc = pq(url)
    links = doc('#doctor img').parent().items()
    for url in links:
        link = 'http://www.anzhen.org' + url('a').attr('href')
        results = parse_detail(link)
        for result in results:
            print(result)
            # save_to_mongo(result)


if __name__ == '__main__':
    url = 'http://www.anzhen.org/Html/Departments/Main/SearchIndex_225.html'
    main(url)