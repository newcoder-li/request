# -*- coding: utf-8 -*-

from contract.base import Base


class Contract(Base):

    def get_member_info(self, userid):
        get_member_url = 'https://qyapi.weixin.qq.com/cgi-bin/user/get'
        params = {"userid": userid}
        r = self.send("GET", get_member_url, params=params)
        return r.json()

    def update_member(self, userid, name, mobile):
        update_member_url = 'https://qyapi.weixin.qq.com/cgi-bin/user/update'
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
        }
        r = self.send("POST", update_member_url, json=data)
        return r.json()

    def create_member(self, userid, name, mobile, department):
        create_member_url = 'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            'department': department
        }
        r = self.send("POST", create_member_url, json=data)
        return r.json()

    def delete_member(self, userid):
        delete_url = 'https://qyapi.weixin.qq.com/cgi-bin/user/delete'
        params = {"userid": userid}
        r = self.send("GET", delete_url, params=params)
        return r.json()
