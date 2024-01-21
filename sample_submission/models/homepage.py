from odoo import api, fields, models


class homepage(models.Model):
    _name = "home.page"
    _description = "page record"


    name_of_sample = fields.Char(string='Name', required=True, tracking=True)
    customer_id = fields.Many2one('res.partner', string="Customer", tracking=True)
    date_of_submission = fields.Date(string="Date of Submission", tracking=True)
    description = fields.Text(string="Description", tracking=True)
    price = fields.Integer(string="Price", tracking=True)
    discount = fields.Integer(string="Discount", store=True)
    vat = fields.Integer(string="Vat")
    slno = fields.Char(string='SL.NO', default=lambda self: ('New'))
    stages = fields.Selection([('pending', 'Pending'), ('doing', 'Doing'), ('completed', 'Completed')],
                              default="pending", string="Stages")

    view_ids = fields.One2many('field', "treeview_id")

    def generate_invoice(self):
        invoice_data = {
            'partner_id': self.customer_id.id,
            'display_name': self.name_of_sample,
            'amount_total': self.price,
            'discount': self.discount,
            'vat': self.vat,
        }
        invoice = self.env['account.move'].create(invoice_data)
        self.write({'invoice_reference': invoice.name})

    @api.model_create_multi
    def create(self, vals_list):
        for v in vals_list:
            v['slno'] = self.env['ir.sequence'].next_by_code('Customer')
        return super(homepage, self).create(vals_list)


class field(models.Model):
    _name = "field"

    treeview_id = fields.Many2one('home.page', string="Treeview")
    material_id = fields.Char(string="Materials", required=True)
    number = fields.Integer(string="SLNO", required=True)
    quantity = fields.Integer(string="Quantity", required=True)
    remark = fields.Char(string="Remark")
