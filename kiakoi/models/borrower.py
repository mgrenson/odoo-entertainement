# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Borrower(models.Model):
    _inherits = {'res.partner': 'partner_id'}
    _name = 'kiakoi.borrower'

    trusted = fields.Boolean(string="Trusted", required=True)
    partner_id = fields.Many2one('res.partner', required=True, ondelete='cascade', string="Partner", index=True)

    borrowing_ids = fields.One2many('kiakoi.borrowing', 'borrower_id', string="Borrowing's history")

    # The current borrowings if the ones that have an empty return_date
    current_borrowings_id = fields.One2many('kiakoi.borrowing', 'borrower_id', string="Current borrowings",
                                           domain=[('return_date', '=', False)])

    currently_borrowing = fields.Boolean(compute='_compute_currently_borrowing', string="Currently borrowing some stuff")

    @api.multi
    def _compute_currently_borrowing(self):
        """Determine if the borrower is currently borrowing some stuff"""
        for record in self:
            print record.name+" : "+str(record.current_borrowings_id)
            if record.current_borrowings_id.exists():
                record.currently_borrowing = True
            else:
                record.currently_borrowing = False

    # FIXME: An unique constraint on name should be applicated to the name field of the inherit model : sql or python ?



