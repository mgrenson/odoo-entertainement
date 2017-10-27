# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Object(models.Model):
    _name = 'kiakoi.object'

    name = fields.Char(string="Name", required=True)
    type = fields.Char(string="Type")

    borrowing_ids = fields.One2many('kiakoi.borrowing', 'object_id', string="Borrowing's history")

    current_borrowing_id = fields.One2many('kiakoi.borrowing', 'object_id', string="Current borrowing",
                                         domain=[('return_date', '=', False)])

    currently_borrowed = fields.Boolean(compute='_compute_currently_borrowed', string="Currently borrowed")

    _sql_constraints = [
        ('name_unique',
         'UNIQUE(name)',
         "The name must be unique"),
    ]

    @api.multi
    def _compute_currently_borrowed(self):
        """Determine if the object is currently borrowed by someone"""
        for record in self:
            if record.current_borrowing_id.exists():
                record.currently_borrowed = True
            else:
                record.currently_borrowed = False
