# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Borrowing(models.Model):
    _name = 'kiakoi.borrowing'

    borrower_id = fields.Many2one('kiakoi.borrower', required=True, ondelete='set null', string="Borrower", index=True,
                                  domain=[('trusted', '=', True)])

    object_id = fields.Many2one('kiakoi.object', required=True, ondelete='set null', string="Object", index=True)

    borrow_date = fields.Date(required=True)
    return_date = fields.Date(required=False)

    color = fields.Integer()

    _sql_constraints = [
        ('borrow_before_return',
         'CHECK (return_date >= borrow_date)',
         "The return date cannot be anterior to the borrow date"),
    ]

    @api.constrains('object_id')
    def object_borrow_unique(self):
        """Check if there is another one active borrowing (no return_date) for the same object

        Note : An SQL constraint would be better, but I didn't found the way to create it,
        because in this case a partial index was required :
        CREATE UNIQUE INDEX object_borrow_unique ON kiakoi_borrowing (object_id) WHERE return_date IS NULL;
        """
        for record in self:
            print "record.object_id : "+str(record.object_id)
            if len(self.search([('object_id', '=', record.object_id.id), ('return_date', '=', False)])) > 1 :
                raise ValidationError("The object can be loaned to one person at a time")

    #FIXME: missing constraint : avoid to save a borrowing with a return date empty and a not trusted borrower






