#!/usr/bin/env python
# encoding: utf-8

from gnr.web.gnrbaseclasses import TableScriptToHtml


class Main(TableScriptToHtml):
    doc_header_height = 32
    doc_footer_height = 12
    grid_header_height = 5

    def docHeader(self, header):
        layout = header.layout(name='doc_header', margin='5mm', border_width=0)

        row = layout.row()
        left_cell = row.cell(width=80)
        center_cell = row.cell()
        right_cell = row.cell(width=80)
      
        self.invoiceData(left_cell)
        self.customerData(right_cell)

    def invoiceData(self, c):
        l = c.layout(lbl_class='cell_label', border_width=0.3)   
        r = l.row(height=8)
        r.cell(self.field('invoicedate'), lbl='Date')
        r = l.row(height=8)
        r.cell(self.field('invoiceid'), lbl='Invoice Nr.')
 
    def customerData(self, c):
        l = c.layout(lbl_class='cell_label', border_width=0.3)
        customerData = self.record['@customerid']
        fullname = '{firstname} {lastname}'.format(**customerData)
        l.row(height=5).cell(fullname, lbl='Customer')
        l.row(height=5).cell(customerData['company'], lbl='Company')
        fulladdress = "{address} {city} {state} {postalcode} {country}".format(**customerData)
        l.row(height=5).cell(fulladdress, lbl='Address')
        contacts_row = l.row(height=5)
        contacts_row.cell(customerData['email'],lbl='Email')
        contacts_row.cell(customerData['phome'],lbl='Phone')

    def defineCustomStyles(self):
        self.body.style(""".cell_label{
                            font-size:8pt;
                            text-align:left;
                            color:gray;
                            text-indent:1mm;}

                            .footer_content{
                            text-align:right;
                            margin:2mm;
                            }
                            """)


    def gridStruct(self,struct):
        r = struct.view().rows()
        info = r.columnset('info', name='Track informations')

        info.fieldcell('trackid',mm_width=0, name='Track')
        info.fieldcell('@trackid.@genreid.name',mm_width=18, name='Genre')
        info.fieldcell('@trackid.@albumid.title',mm_width=0, name='Album')
        info.fieldcell('@trackid.@albumid.@artistid.name',mm_width=20, name='Artist')
        info.fieldcell('unitprice',mm_width=12, name='Price')
        r.fieldcell('quantity',mm_width=12, name='Qt')
        r.fieldcell('totprice',mm_width=12, name='Tot')

    def gridQueryParameters(self):
        return dict(relation='@items')

    def docFooter(self, footer, lastPage=None):
        l = footer.layout(top=1,lbl_class='cell_label', content_class = 'footer_content')
        r = l.row(height=12)
        r.cell('Thanks for your purchase!')
        r.cell()
        r.cell(self.field('total'),lbl='Total',  width=20)