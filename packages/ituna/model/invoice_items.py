# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('invoice_items',legacy_name='main.invoice_items',legacy_db='chinook',pkey='invoicelineid',caption_field='invoicelineid',name_long='Invoice item',name_plural='Invoice items')
        tbl.column('invoicelineid',dtype='I',name_long='Id',legacy_name='InvoiceLineId')
        tbl.column('invoiceid',dtype='I',name_long='Invoice',legacy_name='Invoice',indexed=True,unique=False).relation('invoices.invoiceid',
                                                                                                                    relation_name='items',
                                                                                                                    onDelete='raise', 
                                                                                                                    meta_thmode='dialog')
        tbl.column('trackid',dtype='I',name_long='Track',legacy_name='Track',indexed=True,unique=False).relation('tracks.trackid',
                                                                                                                    onDelete='raise',
                                                                                                                    relation_name='invoice_items', 
                                                                                                                    meta_thmode='dialog')
        tbl.column('unitprice',dtype='N',size='10,2',name_long='Unit Price',legacy_name='UnitPrice')
        tbl.column('quantity',dtype='I',name_long='Quantity',legacy_name='Quantity')
