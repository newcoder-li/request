# -*- coding: utf-8 -*-
import pytest
import yaml

from contract.contract_memeber import Contract


class TestContract():
    def setup(self):
        self.contract = Contract()
        self.userid = 'zhangsanhaha'
        self.name = "laosan"
        self.mobile = "+86 13812309876"
        self.department = [1]

    path = "../testcase/data/contract_data.yaml"
    with open(path, encoding="utf-8") as f:
        datas: list = yaml.safe_load(f)['datas']
        for data in datas:
            user_id = data[0]
            mobile = data[1]

    @pytest.mark.parametrize("user_id, mobile", datas)
    def test_create_member(self, user_id, mobile):
        # 测试创建成员前需删除已有数据
        self.contract.delete_member(self.userid)
        # 调用创建成员方法
        r = self.contract.create_member(user_id, self.name, mobile, self.department)
        # 判断是否创建成功
        assert r.get('errmsg', 'network error') == "created"
        # 获取成员信息
        r = self.contract.get_member_info(user_id)
        # 删除测试数据后在断言，否则断言失败无法删除数据
        self.contract.delete_member(self.userid)
        # 判断是否为添加成员
        assert r.get("name") == self.name

    def test_get_member_info(self):
        # 测试获取成员信息时先创建成员
        self.contract.create_member(self.userid, self.name, self.mobile, self.department)
        # 调用获取成员信息方法
        r = self.contract.get_member_info(self.userid)
        # 删除测试数据
        self.contract.delete_member(self.userid)
        # 断言获取信息是否成功
        assert r.get('errmsg') == "ok"
        assert r.get("name") == self.name

    def test_delete_member(self):
        # 测试删除成员前需先创建成员
        self.contract.create_member(self.userid)
        # 调用删除成员方法
        r = self.contract.delete_member(self.userid)
        # 断言删除是否成功
        assert r.get('errmsg') == "deleted"
        # 获取已删除成员信息
        r = self.contract.get_member_info(self.userid)
        # 判断是否返回指定错误码
        assert r.get("errcode") == 60111

    def test_update_member(self):
        # 测试更新成员前需删除并创建成员
        self.contract.delete_member(self.userid)
        self.contract.create_member(self.userid, self.name, self.mobile, self.department)
        new_name = self.name + "tmp"
        # 调用更新成员方法
        r = self.contract.update_member(self.userid, new_name, self.mobile)
        # 删除测试数据
        self.contract.delete_member(self.userid)
        # 断言更新是否成功
        assert r.get("errmsg") == "updated"
        # 调用获取成员方法
        r = self.contract.get_member_info(self.userid)
        assert r.get("name") == new_name
