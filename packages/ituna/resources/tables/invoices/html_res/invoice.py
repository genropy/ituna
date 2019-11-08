#!/usr/bin/env python
# encoding: utf-8

from gnr.web.gnrbaseclasses import TableScriptToHtml


class Main(TableScriptToHtml):
    doc_header_height = 40
    doc_footer_height = 12
    grid_header_height = 5

    def docHeader(self, header):
        layout = header.layout(name='doc_header', border_width=0,
                                lbl_class='cell_label', 
                                content_class = 'footer_content', margin=5)

        row = layout.row()
        left_cell = row.cell(width=50)
        row.cell()
        right_cell = row.cell(width=100)
        layout.row()
        self.invoiceData(left_cell)
        self.customerData(right_cell)

        
    def defineCustomStyles(self):
        self.body.style(""".cell_label{
                            font-size:8pt;
                            text-align:left;
                            color:gray;}

                            .footer_content{
                            text-align:right;
                            margin:2mm;
                            }
                            """)



    def invoiceData(self, c):
        l = c.layout(lbl_class='cell_label', border_width=0)   
        r = l.row(height=0)
        r.cell(self.field('invoicedate'), lbl='Date')
        r = l.row(height=0)
        r.cell(self.field('invoiceid'), lbl='Invoice Nr.')
 
    def customerData(self, c):
        l = c.layout(lbl_class='cell_label', border_width=0)
        customerData = self.record['@customerid']
        fullname = '{firstname} {lastname}'.format(**customerData)
        r = l.row(height=10)
        r.cell(fullname, lbl='Customer')
        r.cell(customerData['company'], lbl='Company')
        fulladdress = "{billingaddress} {billingcity} {billingpostalcode} {billingcountry}".format(**self.record)
        l.row(height=10).cell(fulladdress, lbl='Address')
        contacts_row = l.row(height=10)
        contacts_row.cell(self.field('@customerid.email'),lbl='Email')
        contacts_row.cell(self.field('@customerid.phone'),lbl='Phone')


    def gridStruct(self,struct):
        r = struct.view().rows()
        r.fieldcell('trackid',mm_width=0, name='Track')
        r.fieldcell('@trackid.@genreid.name',mm_width=25, name='Genre')
        r.fieldcell('@trackid.@albumid.title',mm_width=0, name='Album')
        r.fieldcell('@trackid.@albumid.@artistid.name',mm_width=34, name='Artist')
        r.fieldcell('unitprice',mm_width=10, name='Price')
        r.fieldcell('quantity',mm_width=10, name='Qt')
        r.fieldcell('totprice',mm_width=10, name='Tot')

    def gridQueryParameters(self):
        return dict(relation='@items')

    def docFooter(self, footer, lastPage=None):
        l = footer.layout(top=1,lbl_class='cell_label', content_class = 'footer_content')
        r = l.row(height=12)
        r.cell('Thanks for your purchase from iTuna!')
        r.cell()
        r.cell(self.field('total'),lbl='Total',  width=20)