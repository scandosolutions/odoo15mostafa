# -*- coding: utf-8 -*-

from odoo import models, fields, api


class test1(models.Model):
    _name = 'test.info'

    userName = fields.Char(string="User Name", required=True, )
    password = fields.Char(string="Password", required=True, )
