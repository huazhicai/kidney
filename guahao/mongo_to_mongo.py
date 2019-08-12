"""
提取114gh数据，存入到114yygh 表中
"""
import time

import pymongo


class Extract(object):
    def __init__(self):
        self.client = pymongo.MongoClient('localhost')
        self.db = self.client['114gh']
        self.collection_114gh = self.db['114gh']
        self.collection_114yygh = self.db['114yygh_copy']

    def extract_data(self):
        """
        提取不重复姓名
        :return:
        """
        for i in self.collection_114gh.find({}):
            if i['outpatient']:
                for j in i['outpatient']:
                    for m, n in j.items():
                        # print(m, n)
                        # l = []
                        for k in n:
                            k['dutyCodeName'] = m[:13] + k['dutyCodeName']
                            # print("'" + k['doctorName'] + "'", end=',')
                            # yield {
                            #     'hospital': i['hospital'],
                            #     'department': i['department'],
                            #     'name': k['doctorName'],
                            #     'title': k['doctorTitleName'],
                            #     'special': k['skill'],
                            #     'link': i['link'],
                            #     'website': i.get('website', None),
                            #     'phone': i['phone'],
                            #     'city': '北京',
                            #     # 'outpatient_info': i.outpatient,
                            # }
                            yield {
                                'date': k['dutyCodeName'],
                                'name': k['doctorName'],
                                'totalFee': k['totalFee'],
                                'remainAvailableNumber': k['remainAvailableNumber']
                            }

    def save_to_mongo(self, result):
        # self.collection_114yygh.update_one({'name': result['name']}, {'$set': result}, True)
        self.collection_114yygh.update_one({'name': result['name']}, {'$set': result['outpatient_info'].append()}, True)
        print(result)


if __name__ == '__main__':
    extract = Extract()
    names = ['左力', '杨宏宇', '张宜苗', '王鑫', '苏涛', '王鑫', '王鑫', '张宏', '陈育青', '吕继成', '刘立军', '刘刚', '许戎', '喻小娟', '刘立军', '赵明辉',
             '陈育青', '王玉', '张宏', '苏涛', '金其庄', '陈旻', '陈育青', '董捷', '喻小娟', '张宜苗', '王鑫', '刘立军', '刘刚', '张宜苗', '韩庆烽', '韩庆烽',
             '许慧莹', '王炜', '庄震', '许慧莹', '李月红', '许慧莹', '庄震', '蔡士铭', '王炜', '王冲', '李月红', '李敏侠', '王炜', '王炜', '庄震', '吕佳璇',
             '许慧莹', '李月红', '王炜', '庄震', '韩庆烽', '汪涛', '汪涛', '汪涛', '韩庆烽', '王悦', '孙继永', '冯桂兰', '冯桂兰', '孙继永', '冯桂兰', '周国民',
             '刘秀萍', '李建民', '周国民', '任文英', '刘秀萍', '李建民', '周国民', '刘秀萍', '李建民', '周国民', '任文英', '刘秀萍', '李建民', '周国民', '刘秀萍',
             '李建民', '周国民', '任文英', '刘秀萍', '李建民', '周国民', '刘秀萍', '李建民', '周国民', '任文英', '刘秀萍', '李建民', '李普庆', '张壹言', '陈凤锟',
             '李冀军', '李冀军', '宋岩', '宋岩', '殷培', '齐跃', '副主任号', '副主任号', '副主任号', '副主任号', '余仁欢', '权正洪', '郝建荣', '郝建荣', '郝建荣',
             '郝建荣', '郝建荣', '郝建荣', '郝建荣', '郝建荣', '邱模炎', '耿艳秋', '张艳霞', '张承英', '张承英', '陈君', '陈君', '黄晓晔', '黄晓晔', '黄晓晔',
             '黄晓晔', '陈君', '陈君', '陈君', '陈君', '黄晓晔', '黄晓晔', '黄晓晔', '黄晓晔', '陈君', '陈君', '陈君', '陈君', '黄晓晔', '黄晓晔', '黄晓晔',
             '黄晓晔', '陈君', '陈君', '陈君', '陈君', '黄晓晔', '黄晓晔', '黄晓晔', '黄晓晔', '陈君', '陈君', '陈君', '陈君', '黄晓晔', '黄晓晔', '黄晓晔',
             '黄晓晔', '陈君', '陈君', '陈君', '陈君', '黄晓晔', '黄晓晔', '黄晓晔', '黄晓晔', '陈君', '陈君', '陈君', '陈君', '黄晓晔', '黄晓晔', '陈君',
             '陈君', '黄晓晔', '黄晓晔', '黄晓晔', '黄晓晔', '陈君', '陈君', '陈君', '陈君', '黄晓晔', '黄晓晔', '黄晓晔', '黄晓晔', '陈君', '陈君', '陈君',
             '陈君', '黄晓晔', '黄晓晔', '黄晓晔', '黄晓晔', '陈君', '陈君', '叶明', '刘文军', '孙建实', '王丽', '孙建实', '周静媛', '李深', '刘文军', '韩东彦',
             '缪洁萍', '缪洁萍', '缪洁萍', '缪洁萍', '缪洁萍', '缪洁萍', '缪洁萍', '王暴魁', '秦建国', '任可', '秦建国', '任可', '王暴魁', '王暴魁', '安海燕',
             '王暴魁', '秦建国', '任可', '秦建国', '任可', '王暴魁', '王暴魁', '安海燕', '任可', '王暴魁', '王暴魁', '安海燕', '张雪光', '肖跃飞', '王艺萍',
             '杨松涛', '张雪光', '肖跃飞', '杨松涛', '王艺萍', '张雪光', '肖跃飞', '王艺萍', '杨松涛', '张雪光', '肖跃飞', '杨松涛', '王艺萍', '张雪光', '肖跃飞',
             '王艺萍', '杨松涛', '张雪光', '肖跃飞', '杨松涛', '王艺萍', '张雪光', '肖跃飞', '王艺萍', '杨松涛', '张雪光', '肖跃飞', '杨松涛', '王艺萍', '胡瑞海',
             '朱晓明', '朱晓明', '伦立德', '初  梅', '李清刚遗传性肾病', '赵佳慧', '王涌', '张利', '肾内科',
             '冯哲', '谢院生罕见肾脏病', '蔡广研', '朱晗玉', '林淑芃', '吴镝', '魏日胞', '孙雪峰', '曹雪莹', '张利', '魏日胞',
             '程庆砾', '李清刚', '周建辉', '朱晗玉', '林淑芃', '曹雪莹', '吴杰', '张冬', '张晓英', '王涌', '冯哲', '张利',
             '李清刚遗传性肾病', '赵佳慧', '王涌', '李清刚', '冯哲', '谢院生罕见肾脏病', '蔡广研',
             '朱晗玉', '林淑芃', '吴镝', '魏日胞', '孙雪峰', '曹雪莹', '张利', '魏日胞', '程庆砾', '李清刚', '周建辉',
             '朱晗玉', '林淑芃', '曹雪莹', '吴杰', '张冬', '张晓英', '王涌', '冯哲', '张利', '李清刚遗传性肾病', '赵佳慧',
             '王涌', '冯哲', '谢院生罕见肾脏病', '蔡广研', '朱晗玉', '林淑芃', '吴镝', '魏日胞',
             '孙雪峰', '曹雪莹', '张利', '魏日胞', '程庆砾', '李清刚', '周建辉', '朱晗玉', '林淑芃', '曹雪莹', '吴杰',
             '张冬', '张利', '张晓英', '王涌', '冯哲', '李清刚遗传性肾病', '赵佳慧', '王涌', '王涌', '肾内科',
             '冯哲', '谢院生罕见肾脏病', '蔡广研', '朱晗玉', '林淑芃', '吴镝', '魏日胞', '孙雪峰', '曹雪莹',
             '张利', '魏日胞', '程庆砾', '李清刚', '朱晗玉', '林淑芃', '曹雪莹', '吴杰', '张冬', '张利', '张晓英', '王涌',
             '冯哲', '于晓初', '于阳']

    for i in set(names):
        l = []
        results = extract.extract_data()
        for result in results:
            if result['name'] == i:
                l.append(result)
        extract.collection_114yygh.update_one({'name': l[0].get('name')}, {'$set': {'outpatient_info': l}}, True)
        print(l)
        # extract.save_to_mongo(result)