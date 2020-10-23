#!/usr/bin/python

class FilterModule(object):
    def filters(self):
        return {
            'get_member_index': self.get_member_index}

    def get_member_index(self, members_list, member_id):
        return {item: index for index, item in enumerate(members_list, 1)}[member_id]
